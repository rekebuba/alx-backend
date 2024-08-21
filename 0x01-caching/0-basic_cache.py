#!/usr/bin/env python3
"""BasicCache module"""

from typing import Any, Optional
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """caching system"""

    def __init__(self) -> None:
        """Initialize the base class"""
        super().__init__()

    def put(self, key: Optional[Any], item: Optional[Any]) -> None:
        """Must assign to the dictionary the item value for the key.

        Args:
            key (Optional[Any])
            item (Optional[Any])
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key: Optional[Any]) -> Optional[Any]:
        """Must return the value linked to key.

        Args:
            key (Optional[Any])

        Returns:
            Optional[Any]: return item in dictionary
        """
        return self.cache_data.get(key, None)
