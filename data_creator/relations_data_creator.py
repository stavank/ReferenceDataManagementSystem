import csv
import os
import common.utils.utils as utils
import common.utils.validations.file_validations as file_validations
import common.utils.validations.data_type_validations as data_type_validations

from datetime import datetime
from common.exceptions.primary_key_exception import PrimaryKeyCollisionException
from common.utils.files.file_util import get_file_header, create_col_name_to_idx_dict
from common.exceptions.file_exception import InputFileDataException
from common.internal_structures import DataTypes, TimeComponent


class CreateRelationsData:
    """
    This class is responsible to create relation data that can be processed by the neo4j-import tool to create relations
    of one particular type (label). These relations are between the nodes of two types. This data will store the
    properties of these relations.

    """
    def __init__(self, file_path, delimiter, destination_file_path, relation_from, relation_to, relation_name,
                 relation_time_component):
        self.__relation_file_path = file_path
        self.__delimiter = delimiter
        self.__destination_file_path = destination_file_path
        self.__relation_from = relation_from
        self.__relation_to = relation_to
        self.__relation_name = relation_name
        self.__relation_time_component = relation_time_component

    def create(self, relation_from_primary_key_dict, relation_to_primary_key_dict, data_type_preference):
        """
        This method creates a new file '__destination_file_path'. This file is compatible the neo4j-import
        tool to create relations of a particular label/type between two node types.

        :param relation_from_primary_key_dict: The relation_from_primary_key_dict is a dictionary that contains the
                                               mapping of column name and column index for the columns that belong to
                                               the primary key of the node from which the relationship stems.
                                               Example:
                                               {'Col_A': 1, 'Col_B': 2, 'Col_C': 3}
        :param relation_to_primary_key_dict: The relation_to_primary_key_dict is a dictionary that contains the
                                             mapping of column name and column index for the columns that belong to the
                                             primary key of the node at which the relationship ends.
                                             Example:
                                             {'Col_D': 4, 'Col_B': 5, 'Col_C': 6}
        :param data_type_preference: This is the dictionary of all the preferred data_types for the columns in the
                                     source file.
                                     Example:
                                     {'Col_A': 1, 'Col_B': 2, 'Col_C': 3}
        """
        # Parameter validations.
        data_type_validations.valid_param_type_for_string(self.__relation_file_path, "file_path")
        data_type_validations.valid_param_type_for_string(self.__delimiter, "delimiter")
        data_type_validations.valid_param_type_for_string(self.__destination_file_path, "destination_file_path")
        data_type_validations.valid_param_type_for_create_node_data(self.__relation_from, "relation_from")
        data_type_validations.valid_param_type_for_create_node_data(self.__relation_to, "relation_to")
        data_type_validations.valid_param_type_for_string(self.__relation_name, "relation_name")
        data_type_validations.valid_param_type_for_dict(relation_from_primary_key_dict,
                                                        "relation_from_primary_key_dict")
        data_type_validations.valid_param_type_for_time_component(self.__relation_time_component,
                                                                  "relation_time_component")
        data_type_validations.valid_param_type_for_dict(relation_to_primary_key_dict, "relation_to_primary_key_dict")
        data_type_validations.valid_param_type_for_dict(data_type_preference, "data_type_preference")
        file_validations.valid_file_path(self.__relation_file_path)
        file_validations.valid_csv_file_path(self.__destination_file_path)

        source_file_header = get_file_header(self.__relation_file_path, self.__delimiter)
        number_of_columns = len(source_file_header)
        self.__col_to_idx_dict = create_col_name_to_idx_dict(source_file_header)

        # Parameter validations - Business logic
        if not self.__relation_from.__data_created:
            raise ValueError(("Data not created for node: '{node_label}'. Please create data and then try to create "
                             "relation between nodes.").format(node_label=self.__relation_from.__node_label))
        if not self.__relation_to.__data_created:
            raise ValueError(("Data not created for node: '{node_label}'. Please create data and then try to create "
                             "relation between nodes.").format(node_label=self.__relation_to.__node_label))
        if sorted(list(relation_from_primary_key_dict.keys())) != sorted(self.__relation_from.primary_key_ids):
            raise ValueError(("There is a mismatch in primary key ids with which node data was generated : "
                              "'{node_key_ids}' and the primary key ids supplied in '{param_name}' : "
                              "'{relation_key_ids}'.").format(node_key_ids=self.__relation_from.primary_key_ids,
                                                              param_name="relation_from_primary_key_dict",
                                                              relation_key_ids=relation_from_primary_key_dict))
        if sorted(list(relation_to_primary_key_dict.keys())) != sorted(self.__relation_to.primary_key_ids):
            raise ValueError(("There is a mismatch in primary key ids with which node data was generated : "
                              "'{node_key_ids}' and the primary key ids supplied in '{param_name}' : "
                              "'{relation_key_ids}'.").format(node_key_ids=self.__relation_to.primary_key_ids,
                                                              param_name="relation_to_primary_key_dict",
                                                              relation_key_ids=relation_to_primary_key_dict))
        if len(utils.difference_in_lists(list(relation_from_primary_key_dict.keys()), source_file_header)) > 0:
            raise ValueError("Columns: '{missing_cols}' in '{param_name}' are not found in relation file header.".
                             format(missing_cols=utils.difference_in_lists(relation_from_primary_key_dict.keys(),
                                                                           source_file_header),
                                    param_name='relation_from_primary_key_dict'))
        if len(utils.difference_in_lists(list(relation_to_primary_key_dict.keys()), source_file_header)) > 0:
            raise ValueError("Columns: '{missing_cols}' in '{param_name}' are not found in relation file header.".
                             format(missing_cols=utils.difference_in_lists(relation_to_primary_key_dict.keys(),
                                                                           source_file_header),
                                    param_name='relation_to_primary_key_dict'))
        if len(utils.difference_in_lists(list(data_type_preference.keys()), source_file_header)) > 0:
            raise ValueError("Columns: '{missing_cols}' in '{param_name}' are not found in relation file header.".
                             format(missing_cols=utils.difference_in_lists(data_type_preference.keys(),
                                                                           source_file_header),
                                    param_name='data_type_preference'))

        if self.__relation_time_component == TimeComponent.STATIC:
            self.__create_static_relation()
        elif self.__relation_time_component == TimeComponent.TIMESERIES:
            self.__create_timeseries_relation()
        elif self.__relation_time_component == TimeComponent.BITEMPORAL:
            self.__create_bitemporal_relation()

    def __create_static_relation(self):
        pass

    def __create_timeseries_relation(self):
        pass

    def __create_bitemporal_relation(self):
        pass
