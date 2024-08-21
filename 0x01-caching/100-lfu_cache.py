#!/usr/bin/env python3
"""LFU caching Algorithm"""
from typing import Any, Optional, List, Dict
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """base class"""

    def __init__(self) -> None:
        super().__init__()
        self.cache_data = OrderedDict()
        self.recently_used: Dict[Any, int] = OrderedDict()

    def put(self, key: Optional[Any], item: Optional[Any]) -> None:
        """Must assign to the dictionary the item value for the key.
        If the number of items in is higher that BaseCaching.MAX_ITEMS
        implement LFU Algorithm

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
                least_frequently_used = min(
                    self.recently_used, key=self.recently_used.get
                )
                del self.recently_used[least_frequently_used]
                del self.cache_data[least_frequently_used]
                print("DISCARD:", least_frequently_used)

            if key in self.recently_used:
                self.recently_used[key] += 1
            else:
                self.recently_used[key] = 0

            self.cache_data[key] = item

    def get(self, key: Optional[Any]) -> Optional[Any]:
        """Must return the value linked to key.

        Args:
            key (Optional[Any])

        Returns:
            Optional[Any]: return item in dictionary
        """
        if key in self.cache_data:
            self.recently_used[key] += 1

            return self.cache_data.get(key)

        return None
