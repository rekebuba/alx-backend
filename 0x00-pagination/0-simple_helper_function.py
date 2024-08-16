#!/usr/bin/env python3
"""Simple helper function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """corresponding for particular pagination parameters.

    Args:
        page (int): 1-indexed
        page_size (int): page size

    Returns:
        Tuple[int]: return a start index and an end index
    """
    return ((page * page_size) - page_size, (page * page_size))
