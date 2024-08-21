#!/usr/bin/env python3
"""FIFO caching Algorithm"""
from typing import Any, Optional
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """base class"""

    def __init__(self) -> None:
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key: Optional[Any], item: Optional[Any]) -> None:
        """Must assign to the dictionary the item value for the key.
        If the number of items in is higher that BaseCaching.MAX_ITEMS
        implement FIFO Algorithm

        Args:
            key (Optional[Any])
            item (Optional[Any])
        """
        if key is not None and item is not None:
            valid = (
                len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                key not in self.cache_data
            )
            if valid:
                first_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", first_key)

            self.cache_data[key] = item

    def get(self, key: Optional[Any]) -> Optional[Any]:
        """Must return the value linked to key.

        Args:
            key (Optional[Any])

        Returns:
            Optional[Any]: return item in dictionary
        """
        return self.cache_data.get(key, None)
