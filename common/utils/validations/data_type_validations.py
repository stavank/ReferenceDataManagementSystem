def validate_param_type_for_string(input_param, param_name):
    if not isinstance(input_param, str):
        raise ValueError("Invalid data type for parameter: '{param_name}'. The expected data type is "
                         "'str'.".format(param_name=param_name))


def validate_param_type_for_list(input_param, param_name):
    if not isinstance(input_param, list):
        raise ValueError("Invalid data type for parameter: '{param_name}'. The expected data type is "
                         "'list'.".format(param_name=param_name))
