def valid_param_type_for_string(input_param, param_name):
    """
    This method verifies if the given input is of type 'string' or not.

    :param input_param: This is the input parameter which needs to be verified for data type.
    :param param_name: Name of the parameter. It is needed only when exception is to be raised.
    :return: Raises exception if given input_param is not of type 'string'.
    """
    if not isinstance(input_param, str):
        raise ValueError("Invalid data type for parameter: '{param_name}'. The expected data type is "
                         "'str'.".format(param_name=param_name))


def valid_param_type_for_list(input_param, param_name):
    """
    This method verifies if the given input is of type 'list' or not.

    :param input_param: This is the input parameter which needs to be verified for data type.
    :param param_name: Name of the parameter. It is needed only when exception is to be raised.
    :return: Raises exception if given input_param is not of type 'list'.
    """
    if not isinstance(input_param, list):
        raise ValueError("Invalid data type for parameter: '{param_name}'. The expected data type is "
                         "'list'.".format(param_name=param_name))


def valid_param_type_for_dict(input_param, param_name):
    """
    This method verifies if the given input is of type 'dict' or not.

    :param input_param: This is the input parameter which needs to be verified for data type.
    :param param_name: Name of the parameter. It is needed only when exception is to be raised.
    :return: Raises exception if given input_param is not of type 'dict'.
    """
    if not isinstance(input_param, dict):
        raise ValueError("Invalid data type for parameter: '{param_name}'. The expected data type is "
                         "'dict'.".format(param_name=param_name))
