#!/usr/bin/env python3
"""class FIFOCaching that inherits from BaseCaching"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCaching defines:
      - put and get method to retrieve data
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed_key, _ = self.cache_data.popitem(last=True)
                print(f'DISCARD: {removed_key}')
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        return None
