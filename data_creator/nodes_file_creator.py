import csv
import os
import common.utils.utils as utils
import common.utils.validations.file_validations as file_validations
import common.utils.validations.data_type_validations as data_type_validations

from datetime import datetime
from common.exceptions.primary_key_exception import PrimaryKeyCollisionException
from common.utils.files.file_util import get_file_header, create_col_name_to_idx_dict
from common.exceptions.file_exception import InputFileDataException
from common.data_types import DataTypes


class CreateNodeFile:
    """
    This class is responsible to create node file that can be processed by the neo4j-import tool to create nodes of
    one particular type (label). This node file will store the properties of these nodes and will create a unique id
    for each node.
    """

    __col_to_idx_dict = {}  # This is a dictionary of column names to their indices in source file.

    def __init__(self, file_path, delimiter, primary_key_ids, destination_file_path, node_label):
        self.__node_file_path = file_path
        self.__delimiter = delimiter
        self.__node_label = node_label
        self.__primary_key_ids = primary_key_ids
        self.__destination_file_path = destination_file_path

    def create(self, data_type_preference=None):
        """
        This method creates a new file '__destination_file_path'. This file is compatible the neo4j-import
        tool to create nodes of a particular label/type. It also creates UUID for each node using the columns
        chosen in '__primary_key_ids'.

        :param data_type_preference: This is the list of all the preferred data_types for the columns in the source
                                     file.

        """
        # Parameter Validations.
        data_type_validations.valid_param_type_for_string(self.__node_file_path, "file_path")
        data_type_validations.valid_param_type_for_list(self.__primary_key_ids, "primary_key_columns")
        data_type_validations.valid_param_type_for_string(self.__destination_file_path, "destination_file_path")
        file_validations.valid_file_path(self.__node_file_path)
        file_validations.valid_csv_file_path(self.__destination_file_path)

        source_file_header = get_file_header(self.__node_file_path, self.__delimiter)
        number_of_columns = len(source_file_header)
        self.__col_to_idx_dict = create_col_name_to_idx_dict(source_file_header)

        # Parameter validations - Business logic.
        if (len(self.__primary_key_ids) > number_of_columns) or \
                (len(utils.difference_in_lists(self.__primary_key_ids, source_file_header)) > 0):
            raise ValueError(("Column(s): {missing_cols}, in the parameter 'primary_key_ids' do not exist in file:"
                              "'{file_name}'.").format(missing_cols=utils.difference_in_lists(self.__primary_key_ids,
                                                                                              source_file_header),
                                                       file_name=self.__node_file_path))
        if data_type_preference:
            if len(data_type_preference) != number_of_columns:
                raise ValueError("Number of data type preferences does not match the number of header columns.")
            if any(not isinstance(preference, DataTypes) for preference in data_type_preference):
                raise ValueError(("'data_type_preference' has data types that are not recognized. Please check the "
                                  "enum 'DataTypes' for available data types."))

        # Create new node file compatible with neo4j-import tool
        node_id_set = set()
        temp_file = self.__destination_file_path + datetime.now().strftime('%Y%m%d_%H%M%S') + ".tmp"
        try:
            with open(temp_file, "w") as fw:
                file_writer = csv.writer(fw) 
                node_file_header = self.__create_node_file_header(source_file_header, data_type_preference)
                file_writer.writerow(node_file_header)
                with open(self.__node_file_path, "r") as fr:
                    file_reader = csv.reader(fr, delimiter=self.__delimiter)
                    next(file_reader)
                    for row in file_reader:
                        if len(row) != number_of_columns:
                            raise InputFileDataException(("The input file: '{file}' has incorrect number of columns at "
                                                          "line '{line_num}'.").format(file=self.__node_file_path,
                                                                                       line_num=file_reader.line_num))
                        node_id = self.__create_node_id(row)
                        if node_id in node_id_set:
                            error_dict = {col: row[self.__col_to_idx_dict[col]] for col in self.__primary_key_ids}
                            raise PrimaryKeyCollisionException(("Unique Nodes can't be created. Node with the primary "
                                                                "key columns candidate '{error_dict}' already "
                                                                "exists.").format(error_dict=str(error_dict)))
                        node_id_set.add(node_id)
                        row.insert(0, node_id)
                        file_writer.writerow(row)
            os.rename(temp_file, self.__destination_file_path)
        except (PrimaryKeyCollisionException, InputFileDataException):
            os.remove(temp_file)
            raise
    
    def __create_node_id(self, arr):
        """
        This method creates a unique node id across the global name space using the __primary_key_ids and __node_label.

        :param arr: This is the list of values to be used for __primary_key_ids.
        :return: Unique id created for a node.
        """
        node_id = self.__node_label
        for col in self.__primary_key_ids:
            node_id += '_' + arr[self.__col_to_idx_dict[col]]
        return node_id

    def __create_node_file_header(self, source_file_header, data_type_preference):
        """
        This method creates the new header for the file to be used for importing nodes.

        :param source_file_header: The header column names retrieved from the source file.
        :param data_type_preference: This is the list of all the preferred data_types for the columns in the source
                                     file
        :return: The header for the new node file.
        """
        node_file_header = []
        if data_type_preference:
            node_file_header = [source_file_header[x] + ":" + data_type_preference[x].value
                                for x in range(0, len(data_type_preference))]
        node_file_header.insert(0, ":ID")
        return node_file_header
