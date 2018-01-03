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


class TimeComponent(Enum):
    """
    This class determines the type of data model to be built on top of neo4j.
    TO DO:
    1. Can a data model have multiple kinds of time components ? Imagine some relations to be bi-temporal whereas
       some relations to be static ?

    """
    TIMESERIES = "TimeSeries"
    BITEMPORAL = "BiTemporal"
    STATIC = "Static"
