from enum import Enum


class DataTypes(Enum):
    """
    This class gives access to the various data types that neo4j permits.

    """
    BOOL = "Boolean"
    BYTE = "byte"
    SHORT = "short"
    INT = "int"
    LONG = "long"
    FLOAT = "float"
    DOUBLE = "double"
    CHAR = "char"
    STRING = "String"
