import os
import tempfile


def create_newline(line):
    """
    This method adds a new line character to the given input string.

    :param line: Given input string.
    :return: String that ends with a new line character.
    """
    return line + "\n"


def get_file_header(file_path, delimiter):
    """
    This file finds header for a given file.

    :param file_path: This is the file for which we need to find the header.
    :param delimiter: This is the delimiter by which the file content is separated.
    :return: Returns the header as a list.
    """
    with open(file_path, "r") as file_reader:
        file_header_line = file_reader.readline().rstrip()
        file_header = file_header_line.split(str(delimiter))
        if file_header_line == "" or len(file_header) == 0:
            raise ValueError("{file_path} is empty.".format(file_path=file_path))

    return file_header


def create_col_name_to_idx_dict(file_header):
    """
    This method creates a dictionary with column names as keys and index of their occurrence as values.

    :param file_header: Given input header as a list.
    :return: Returns a dictionary
    """
    return {file_header[x]: x for x in range(0, len(file_header))}


def get_file_name(file_path):
    """
    This method finds the name of the file for a given file path.

    :param file_path: The file path for which the file name is to be found.
    :return: Returns the name of the file.
    """
    return os.path.basename(file_path)


def create_temp_file(suffix):
    """
    This method creates a temporary file with a given suffix.

    :param suffix: This is the suffix to be used for file creation.
    :return: Returns the file handler of a temporary file.
    """
    return tempfile.NamedTemporaryFile(suffix=suffix)
