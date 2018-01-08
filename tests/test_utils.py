import common.utils.utils as utils


# Test difference in lists
def test_difference_in_lists_when_same_lists():
    res = sorted(utils.difference_in_lists([1, 2, 3, 4], [1, 2, 3, 4]))
    assert res == []


def test_difference_in_lists_when_disjoint_lists():
    res = sorted(utils.difference_in_lists([1, 2, 3, 4], [5, 6, 7, 8]))
    assert res == [1, 2, 3, 4]


def test_difference_in_lists_when_partially_intersecting_lists():
    res = sorted(utils.difference_in_lists([1, 2, 3, 4], [3, 4, 5, 6, 7]))
    assert res == [1, 2]
