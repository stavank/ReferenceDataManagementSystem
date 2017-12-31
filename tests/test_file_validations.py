import tempfile
import common.utils.validations.file_validations as file_validations

from nose.tools import *


# Test valid file name
def test_valid_file_name_with_valid_name():
    file_validations.valid_file_name("ABC.txt")


@raises(ValueError)
def test_valid_file_name_with_empty_file_name():
    file_validations.valid_file_name("")


@raises(ValueError)
def test_valid_file_name_with_spaces_as_name():
    file_validations.valid_file_name("    ")


@raises(ValueError)
def test_valid_file_name_with_dotless_name():
    file_validations.valid_file_name("ABC")


@raises(ValueError)
def test_valid_file_name_with_dotless_name():
    file_validations.valid_file_name("ABC")


@raises(ValueError)
def test_valid_file_name_with_trailing_spaces_and_dotless():
    file_validations.valid_file_name("ABC   ")


@raises(ValueError)
def test_valid_file_name_with_leading_spaces_and_dotless():
    file_validations.valid_file_name("   ABC")


@raises(ValueError)
def test_valid_file_name_with_leading_and_trailing_spaces_and_dotless():
    file_validations.valid_file_name("   ABC  ")


@raises(ValueError)
def test_valid_file_name_with_leading_spaces():
    file_validations.valid_file_name("   ABC.txt")


@raises(ValueError)
def test_valid_file_name_with_trailing_spaces():
    file_validations.valid_file_name("ABC.txt   ")


@raises(ValueError)
def test_valid_file_name_with_trailing_and_leading_spaces():
    file_validations.valid_file_name("   ABC.txt   ")


# Test valid file path
def test_valid_file_path_with_valid_path():
    temp_file = tempfile.NamedTemporaryFile(suffix='.txt')
    file_validations.valid_file_path(temp_file.name)
    temp_file.close()


@raises(ValueError)
def test_valid_file_path_with_invalid_path():
    temp_file = tempfile.NamedTemporaryFile(suffix='.txt')
    temp_file.close()
    file_validations.valid_file_path(temp_file.name)


# Test valid csv file path
def test_valid_csv_file_path_with_valid_path():
    temp_file = tempfile.NamedTemporaryFile(suffix='.csv')
    file_validations.valid_csv_file_path(temp_file.name)
    temp_file.close()


@raises(ValueError)
def test_valid_csv_file_path_with_invalid_path():
    temp_file = tempfile.NamedTemporaryFile(suffix='.txt')
    temp_file.close()
    file_validations.valid_csv_file_path(temp_file.name)
