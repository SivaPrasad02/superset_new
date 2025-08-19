<14:content>.replace( 'def choicify(values: Iterable[Any]) -> list[tuple[Any, Any]]:
    """Takes an iterable and makes an iterable of tuples with it"""
    return [(v, f"choice_{v}" for v in values]', 'def choicify(values: Iterable[Any]) -> list[tuple[Any, Any]]:
    """Takes an iterable and makes an iterable of tuples with it"""
    return [(v, v) for v in values]')