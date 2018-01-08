from nose.tools import *
from common.utils.validations.data_type_validations import *


# Test valid param type for string
def test_valid_param_type_for_string_when_param_is_string():
    valid_param_type_for_string("some_string", "param_name")


@raises(ValueError)
def test_valid_param_type_for_string_when_param_is_list():
    valid_param_type_for_string(list(), "param_name")


@raises(ValueError)
def test_valid_param_type_for_string_when_param_is_dict():
    valid_param_type_for_string(dict(), "param_name")


@raises(ValueError)
def test_valid_param_type_for_string_when_param_is_number():
    valid_param_type_for_string(3, "param_name")


# Test valid param type for list
def test_valid_param_type_for_list_when_param_is_list():
    valid_param_type_for_list(list(), "param_name")


@raises(ValueError)
def test_valid_param_type_for_list_when_param_is_dict():
    valid_param_type_for_list(dict(), "param_name")


@raises(ValueError)
def test_valid_param_type_for_list_when_param_is_number():
    valid_param_type_for_list(5, "param_name")


@raises(ValueError)
def test_valid_param_type_for_list_when_param_is_string():
    valid_param_type_for_list("some_string", "param_name")


# Test valid param type for dict
def test_valid_param_type_for_dict_when_param_is_dict():
    valid_param_type_for_dict(dict(), "param_name")


@raises(ValueError)
def test_valid_param_type_for_dict_when_param_is_number():
    valid_param_type_for_dict(5, "param_name")


@raises(ValueError)
def test_valid_param_type_for_dict_when_param_is_string():
    valid_param_type_for_dict("some_string", "param_name")


@raises(ValueError)
def test_valid_param_type_for_dict_when_param_is_list():
    valid_param_type_for_dict(list(), "param_name")


# Test valid param type for TimeComponent
def test_valid_param_type_for_time_component_when_param_is_bitemporal():
    valid_param_type_for_time_component(TimeComponent.BITEMPORAL, "param_name")


def test_valid_param_type_for_time_component_when_param_is_timeseries():
    valid_param_type_for_time_component(TimeComponent.TIMESERIES, "param_name")


def test_valid_param_type_for_time_component_when_param_is_static():
    valid_param_type_for_time_component(TimeComponent.STATIC, "param_name")


@raises(ValueError)
def test_valid_param_type_for_time_component_when_param_is_list():
    valid_param_type_for_time_component(list(), "param_name")


@raises(ValueError)
def test_valid_param_type_for_time_component_when_param_is_string():
    valid_param_type_for_time_component("", "param_name")


@raises(ValueError)
def test_valid_param_type_for_time_component_when_param_is_dict():
    valid_param_type_for_time_component(dict(), "param_name")


@raises(ValueError)
def test_valid_param_type_for_time_component_when_param_is_number():
    valid_param_type_for_time_component(7, "param_name")
