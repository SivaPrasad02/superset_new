'import pytest from superset.utils.core import choicify
def test_choicify_basic(): """Test basic string list functionality""" assert choicify(["a", "b"]) == [("a", "a"), ("b", "b")]
def test_choicify_empty(): """Test empty list handling""" assert choicify([]) == []
def test_choicify_numbers(): """Test numeric values""" assert choicify([1, 2, 3]) == [(1, 1), (2, 2), (3, 3)] '