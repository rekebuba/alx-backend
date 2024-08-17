#!/usr/bin/env python3
"""Hypermedia pagination"""
import csv
import math
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Creating Hypermedia pagination

        Args:
            page (int, optional): Defaults to 1.
            page_size (int, optional): Defaults to 10.

        Returns:
            dict: returns a dictionary containing key-value
        """
        data = self.get_page(page, page_size)
        total_page = math.ceil(len(self.__dataset) / page_size)
        def next_page(page): return page + 1 if page + 1 < total_page else None
        def prev_page(page): return page - 1 if page - 1 > 0 else None
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page(page),
            "prev_page": prev_page(page),
            "total_pages": total_page
        }
