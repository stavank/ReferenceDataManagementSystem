import os

from utils.files.file_util import create_newline, get_file_header, create_col_name_to_idx_dict


class CreateNodeFile:
    """
    This class is responsible to create node file that can be processed by the neo4j-import tool to create nodes of
    one particular type (label). This node file will store the properties of these nodes and will create a unique id
    for each node.
    """

    # TO DO :
    # 1. Add validations for parameters, their data types and values.
    def __init__(self, file_path, delimiter):
        self.__node_file_path = file_path
        self.__delimiter = delimiter

    # TO DO :
    # 1. Add validations for parameters, their data types and values.
    def create(self, primary_key_cols, destination_folder, destination_file_name):
        """
        This method creates a new file at 'destination_folder' with the name 'destination_name'. This file is
        compatible the neo4j-import tool to create noes of a particular label/type. It also creates UUID for each node
        using the columns chosen in 'primary_key_cols'.

        :param primary_key_cols:
        :param destination_folder:
        :param destination_file_name:
        :return:
        """

        destination_file = os.path.join(destination_folder, destination_file_name)

        file_header = get_file_header(self.__node_file_path, self.__delimiter)

        if len(primary_key_cols) > len(file_header):
            # TO DO:
            # Identify missing columns
            # Throw missing columns in file exception.
            pass

        col_to_idx_dict = create_col_name_to_idx_dict(file_header)

        node_id_set = set()

        with open(destination_file, 'w') as file_writer:
            file_writer.write(create_newline(self.delimiter.join(file_header.insert(0, "NODE_UUID"))))
            with open(self.__node_file_path, 'r') as file_reader:
                for line in file_reader:
                    line_arr = line.split(self.__delimiter)
                    self.__create_node_id(line_arr)

        pass

    def __create_node_id(self, arr):
        node_id = ''
        for col in self.__primary_key_cols:
            node_id += arr[self.__col_to_idx_dict[col]] + '_'
        pass


