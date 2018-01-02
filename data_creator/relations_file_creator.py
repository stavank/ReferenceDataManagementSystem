class CreateRelationsData:
    """
    This class is responsible to create relation data that can be processed by the neo4j-import tool to create relations
    of one particular type (label). These relations are between the nodes of two types. This data will store the
    properties of these relations.

    """
    def __init__(self, file_path, delimiter, destination_file_path, relation_from, relation_to, relation_name):
        self.__relation_file_path = file_path
        self.__delimiter = delimiter
        self.__destination_file_path = destination_file_path
        self.__relation_from = relation_from
        self.__relation_to = relation_to
        self.__relation_name = relation_name

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
        :param data_type_preference: This is the list of all the preferred data_types for the columns in the source
                                     file.
        """
        pass
