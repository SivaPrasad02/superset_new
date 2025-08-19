def test_choicify():
    """
    Test the choicify function returns proper value pairs
    """
    values = ["a", "b", "c"]
    expected = [("a", "a"), ("b", "b"), ("c", "c")]
    assert choicify(values) == expected
      
    empty = []
    assert choicify(empty) == []
      
