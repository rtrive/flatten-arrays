from src.run import flatten_array


def test_one_array():
    res = flatten_array(array=[1, 2, 3])
    assert res == [1, 2, 3]


def test_multiple_arrays():
    res = flatten_array(array=[1, [2, 5], 3])
    assert res == [1, 2, 5, 3]


def test_all_arrays():
    res = flatten_array(array=[[1], [2], [5], [3]])
    assert res == [1, 2, 5, 3]


def test_array_with_array():
    res = flatten_array(array=[[1, 2, 5, 3]])
    assert res == [1, 2, 5, 3]


def test_example():
    res = flatten_array(array=[[1, 2, [3]], 4])
    assert res == [1, 2, 3, 4]


def test_empty_array():
    res = flatten_array(array=[])
    assert res == []


def test_empty_arrays():
    res = flatten_array(array=[[], []])
    assert res == []


def test_another_array_inside_array():
    res = flatten_array(array=[1, [1, 2], 3])
    assert res == [1, 1, 2, 3]
