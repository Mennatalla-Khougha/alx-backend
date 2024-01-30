#!/usr/bin/env python3
"""class LFUCaching that inherits from BaseCaching"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCaching defines:
      - put and get method to retrieve data
    """
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.cache_map = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.cache_map, key=self.cache_map.get)
                self.cache_data.pop(min_freq)
                print(f'DISCARD: {min_freq}')
                self.cache_map.pop(min_freq)
            if key not in self.cache_map:
                self.cache_map[key] = 0
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            self.cache_map[key] += 1
            return self.cache_data[key]
        return None
