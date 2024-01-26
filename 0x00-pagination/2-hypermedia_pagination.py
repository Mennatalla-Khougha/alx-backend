#!/usr/bin/env python3
"""Define the index_range function"""
import csv
import math
from typing import Tuple, List, Dict, Any


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Use index_range to find the correct indexes to paginate the dataset
        correctly and return the appropriate page of the dataset

        Args:
            page (int, optional): the start page number. Defaults to 1.
            page_size (int, optional): the size of the page. Defaults to 10.

        Returns:
            List[List]: The dataset from the page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        if self.__dataset is None:
            self.dataset()

        start, end = index_range(page, page_size)

        try:
            result = self.__dataset[start: end]
        except IndexError:
            result = []

        return result

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """method that takes the same arguments (and defaults) as get_page and
        returns a dictionary

        Args:
            page (int, optional): Defaults to 1.
            page_size (int, optional): Defaults to 10.

        Returns:
            Dict[str, int] 
        """
        data = self.get_page(page, page_size)
        total = math.ceil(len(self.__dataset) / page_size)
        next_page = page + 1 if page < total else None
        prev_page = page - 1 if page > 1 else None

        result = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total
        }

        return result