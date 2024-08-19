#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """Retrieves info about page from a given index with a specified size.
        Handles gaps in indexing due to deleted rows.
        """
        data = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(data.keys())

        current_index = index
        page_data = []
        data_keys = sorted(data.keys())

        while len(page_data) < page_size and current_index < len(data_keys):
            if current_index in data:
                page_data.append(data[current_index])
            current_index += 1

        next_index = current_index if current_index < len(data_keys) else None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }
