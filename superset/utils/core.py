from typing import Any
from collections.abc import Iterable
      
def choicify(values: Iterable[Any]) -> list[tuple[Any, Any]]:
    """Takes an iterable and makes an iterable of tuples with it"""
    return [(v, v) for v in values]
                    
