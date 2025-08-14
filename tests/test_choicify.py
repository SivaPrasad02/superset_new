import pytest
from superset.utils.core import choicify
      
def test_choicify_with_strings():
    values = ["a", "b", "c"]
    result = choicify(values)
    assert result == [("a", "a"), ("b", "b"), ("c", "c")]
      
def test_choicify_with_numbers():
    values = [1, 2, 3]
    result = choicify(values)
    assert result == [(1, 1), (2, 2), (3, 3)]
      
def test_choicify_with_mixed_types():
    values = [1, "b", 3.14]
    result = choicify(values)
    assert result == [(1, 1), ("b", "b"), (3.14, 3.14)]
      
def test_choicify_with_empty_list():
    values = []
    result = choicify(values)
    assert result == []
      
def test_choicify_with_none_values():
    values = [None, 1, None]
    result = choicify(values)
    assert result == [(None, None), (1, 1), (None, None)]
      
