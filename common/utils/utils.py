def difference_in_lists(list1, list2):
    """
    This method returns the elements in list1 not present in list2.

    :param list1: List of elements.
    :param list2: List of elements.
    :return: Returns a list of elements.
    """
    return list(set(list1).difference(set(list2)))

