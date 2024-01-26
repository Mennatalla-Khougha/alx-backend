#!/usr/bin/env python3
"""Define the index_range function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """The function return a tuple containing a start and an end indices
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters

    Args:
        page (int): the start page number
        page_size (int): the size of the page

    Returns:
        Tuple[int, int]: tuple containing a start and an end indices
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
