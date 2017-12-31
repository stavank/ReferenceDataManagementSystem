import os

from common.utils.files.file_util import get_file_name


def valid_file_path(file_path):
    valid_file_name(file_path)
    if not os.path.isfile(file_path):
        raise ValueError("'{file_name}' is not a valid file path.".format(file_name=file_path))


def valid_file_name(file_name):
    if (file_name.strip() == "") or (len(file_name.strip()) != len(file_name)) or ("." not in file_name):
        raise ValueError("'{file_name}' is not a valid file name.".format(file_name=file_name))


def valid_csv_file_path(file_path):
    file_name = get_file_name(file_path)
    valid_file_name(file_name)
    valid_file_path(file_path)
    file_name_split = file_name.split(".")
    if file_name_split[len(file_name_split) - 1] != "csv":
        raise ValueError("'{file_name}' is not a valid csv file name.".format(file_name=file_name))


def valid_directory(directory_path):
    if not os.path.isdir(directory_path):
        raise ValueError("'{directory}' is not a valid directory path.".format(directory=directory_path))
