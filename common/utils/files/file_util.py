import os
import tempfile


def create_newline(line):
    return line + "\n"


def get_file_header(file_path, delimiter):
    with open(file_path, "r") as file_reader:
        file_header_line = file_reader.readline().rstrip()
        file_header = file_header_line.split(str(delimiter))
        if file_header_line == "" or len(file_header) == 0:
            raise ValueError("{file_path} is empty.".format(file_path=file_path))

    return file_header


def create_col_name_to_idx_dict(file_header):
    return {file_header[x]: x for x in range(0, len(file_header))}


def get_file_name(file_path):
    return os.path.basename(file_path)


def create_temp_file(suffix):
    return tempfile.NamedTemporaryFile(suffix=suffix)