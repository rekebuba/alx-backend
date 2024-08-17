#!/usr/bin/env python3
"""Simple Pagination"""
import csv
from typing import List


index_range = __import__('0-simple_helper_function').index_range


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
            with open(self.DATA_FILE, 'r') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get the appropriate page of the dataset

        Args:
            page (int, optional): 1-indexed. Defaults to 1.
            page_size (int, optional): page size. Defaults to 10.

        Returns:
            List[List]: a list of datasets
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        index = index_range(page, page_size)
        self.dataset()
        return self.__dataset[index[0]: index[1]]
