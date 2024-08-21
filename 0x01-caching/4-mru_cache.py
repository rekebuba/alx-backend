#!/usr/bin/env python3
"""MRU caching Algorithm"""
from typing import Any, Optional, List
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """base class"""

    def __init__(self) -> None:
        super().__init__()
        self.cache_data = OrderedDict()
        self.recently_used: List[Any] = []

    def put(self, key: Optional[Any], item: Optional[Any]) -> None:
        """Must assign to the dictionary the item value for the key.
        If the number of items in is higher that BaseCaching.MAX_ITEMS
        implement MRU Algorithm

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
                most_recently_used = self.recently_used.pop()
                del self.cache_data[most_recently_used]
                print("DISCARD:", most_recently_used)

            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.recently_used.append(key)

            self.cache_data[key] = item

    def get(self, key: Optional[Any]) -> Optional[Any]:
        """Must return the value linked to key.

        Args:
            key (Optional[Any])

        Returns:
            Optional[Any]: return item in dictionary
        """
        if key in self.cache_data:
            self.recently_used.pop(self.recently_used.index(key))
            self.recently_used.append(key)

            return self.cache_data.get(key)

        return None
