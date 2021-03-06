from nose.tools import *
from data_creator.nodes_data_creator import CreateNodeData
from common.internal_structures import DataTypes
from common.utils.files.file_util import create_temp_file


# Test Primary Key Ids
def test_with_correct_primary_key_id():
    data_file = create_temp_test_file()
    dest_file = create_temp_file(suffix=".csv")
    nodes = CreateNodeData(data_file.name, "|", ["ISIN"], dest_file.name, "ISIN")
    data_types = {"ISIN": DataTypes.STRING, "CompName": DataTypes.STRING, "IssuerId": DataTypes.INT,
                  "PX_LAST": DataTypes.FLOAT}
    nodes.create(data_type_preference=data_types)
    data_file.close()
    dest_file.close()


@raises(ValueError)
def test_with_1_invalid_primary_key_id():
    data_file = create_temp_test_file()
    dest_file = create_temp_file(suffix=".csv")
    nodes = CreateNodeData(data_file.name, "|", ["ITIN"], dest_file.name,"ISIN")
    data_types = {"ISIN": DataTypes.STRING, "CompName": DataTypes.STRING, "IssuerId": DataTypes.INT,
                  "PX_LAST": DataTypes.FLOAT}
    nodes.create(data_type_preference=data_types)
    data_file.close()
    dest_file.close()


@raises(ValueError)
def test_with_2_invalid_primary_key_ids():
    data_file = create_temp_test_file()
    dest_file = create_temp_file(suffix=".csv")
    nodes = CreateNodeData(data_file.name, "|", ["IN", "PT"], dest_file.name, "ISIN")
    data_types = {"ISIN": DataTypes.STRING, "CompName": DataTypes.STRING, "IssuerId": DataTypes.INT,
                  "PX_LAST": DataTypes.FLOAT}
    nodes.create(data_type_preference=data_types)
    data_file.close()
    dest_file.close()


@raises(ValueError)
def test_with_valid_and_1_invalid_primary_key_id():
    data_file = create_temp_test_file()
    dest_file = create_temp_file(suffix=".csv")
    nodes = CreateNodeData(data_file.name, "|", ["ISIN", "PN"], dest_file.name, "ISIN")
    data_types = {"ISIN": DataTypes.STRING, "CompName": DataTypes.STRING, "IssuerId": DataTypes.INT,
                  "PX_LAST": DataTypes.FLOAT}
    nodes.create(data_type_preference=data_types)
    data_file.close()
    dest_file.close()


# Test data type preferences
def test_with_correct_data_type_preference():
    data_file = create_temp_test_file()
    dest_file = create_temp_file(suffix=".csv")
    nodes = CreateNodeData(data_file.name, "|", ["ISIN"], dest_file.name, "ISIN")
    data_types = {"ISIN": DataTypes.STRING, "CompName": DataTypes.STRING, "IssuerId": DataTypes.INT,
                  "PX_LAST": DataTypes.FLOAT}
    nodes.create(data_type_preference=data_types)
    data_file.close()
    dest_file.close()


def test_with_no_data_type_preference():
    data_file = create_temp_test_file()
    dest_file = create_temp_file(suffix=".csv")
    nodes = CreateNodeData(data_file.name, "|", ["ISIN"], dest_file.name, "ISIN")
    nodes.create()
    data_file.close()
    dest_file.close()


@raises(ValueError)
def test_with_extra_correct_data_type_preference():
    data_file = create_temp_test_file()
    dest_file = create_temp_file(suffix=".csv")
    nodes = CreateNodeData(data_file.name, "|", ["ISIN"], dest_file.name, "ISIN")
    data_types = {"ISIN": DataTypes.STRING, "CompName": DataTypes.STRING, "IssuerId": DataTypes.INT,
                  "PX_LAST": DataTypes.FLOAT, "NewCol": DataTypes.DOUBLE}
    nodes.create(data_type_preference=data_types)
    data_file.close()
    dest_file.close()


@raises(ValueError)
def test_with_fewer_correct_data_type_preference():
    data_file = create_temp_test_file()
    dest_file = create_temp_file(suffix=".csv")
    nodes = CreateNodeData(data_file.name, "|", ["ISIN"], dest_file.name, "ISIN")
    data_types = {"ISIN": DataTypes.STRING, "CompName": DataTypes.STRING, "IssuerId": DataTypes.INT}
    nodes.create(data_type_preference=data_types)
    data_file.close()
    dest_file.close()


# Test source file path
def test_with_correct_source_file_path():
    data_file = create_temp_test_file()
    dest_file = create_temp_file(suffix=".csv")
    nodes = CreateNodeData(data_file.name, "|", ["ISIN"], dest_file.name, "ISIN")
    data_types = {"ISIN": DataTypes.STRING, "CompName": DataTypes.STRING, "IssuerId": DataTypes.INT,
                  "PX_LAST": DataTypes.FLOAT}
    nodes.create(data_type_preference=data_types)
    data_file.close()
    dest_file.close()


@raises(ValueError)
def test_with_invalid_source_file_path():
    data_file = create_temp_test_file()
    dest_file = create_temp_file(suffix=".csv")
    data_file.close()
    nodes = CreateNodeData(data_file.name, "|", ["ISIN"], dest_file.name, "ISIN")
    data_types = {"ISIN": DataTypes.STRING, "CompName": DataTypes.STRING, "IssuerId": DataTypes.INT,
                  "PX_LAST": DataTypes.FLOAT}
    nodes.create(data_type_preference=data_types)
    dest_file.close()


@raises(ValueError)
def test_with_empty_source_file_path():
    dest_file = create_temp_file(suffix=".csv")
    nodes = CreateNodeData("", "|", ["ISIN"], dest_file.name, "ISIN")
    data_types = {"ISIN": DataTypes.STRING, "CompName": DataTypes.STRING, "IssuerId": DataTypes.INT,
                  "PX_LAST": DataTypes.FLOAT}
    nodes.create(data_type_preference=data_types)
    dest_file.close()


@raises(ValueError)
def test_with_source_file_path_as_spaces():
    dest_file = create_temp_file(suffix=".csv")
    nodes = CreateNodeData("   ", "|", ["ISIN"], dest_file.name, "ISIN")
    data_types = {"ISIN": DataTypes.STRING, "CompName": DataTypes.STRING, "IssuerId": DataTypes.INT,
                  "PX_LAST": DataTypes.FLOAT}
    nodes.create(data_type_preference=data_types)
    dest_file.close()


# supporting function for tests
def create_temp_test_file():
    content = ("ISIN|CompName|IssuerId|PX_LAST\n"
               "US123|Apple Inc.|123456|123.567\n"
               "US24567|Toys “r” us. Inc|234567|45.21\n"
               "US0987|Helium~ Inc.|7654|165.098\n"
               "US1234|Argon&*% Inc,.|10982|9.123\n")
    temp_file = create_temp_file(suffix=".txt")
    with open(temp_file.name, "w") as file_writer:
        file_writer.write(content)
    return temp_file
