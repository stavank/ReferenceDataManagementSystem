def validate_file_path(file_path):
    pass


def validate_file_name(file_name):

    if file_name == "" or ("." not in file_name):
        return False

    return True
