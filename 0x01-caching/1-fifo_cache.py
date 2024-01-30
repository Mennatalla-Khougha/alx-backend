#!/usr/bin/env python3
"""class FIFOCaching that inherits from BaseCaching"""
# BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCaching defines:
      - put and get method to retrieve data
    """
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.cache_data = OrderedDict()
        # self.queue = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # removed_key = self.queue.pop(0)
                removed_key, _ = self.cache_data.popitem(last=False)
                print(f'DISCARD: {removed_key}')
                # self.cache_data.pop(removed_key)
            self.cache_data[key] = item
            # self.queue.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
