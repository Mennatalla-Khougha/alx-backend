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
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                min_freq = min(self.cache_map, key=self.cache_map.get)
                self.cache_data.pop(min_freq)
                # removed_key = self.removed_lfu()
                print(f'DISCARD: {min_freq}')
                self.cache_map.pop(min_freq)
            if key not in self.cache_map:
                self.cache_map[key] = 0
            self.cache_data[key] = item

    # def removed_lfu(self):
    #     """return the LFU key to be removed"""
    #     min_freq = min(self.cache_map.values())
    #     min_freq_keys = [key for key, freq in
    #                      self.cache_map.items() if freq == min_freq]

    #     if len(min_freq_keys) > 1:
    #         removed_key = self.removed_lru()
    #     else:
    #         removed_key = min_freq_keys[0]
    #         self.cache_data.pop(removed_key)
    #         self.cache_map.pop(removed_key)

    #     return removed_key

    # def removed_lru(self):
    #     """return the LRU key to be removed"""
    #     removed_key, _ = self.cache_map.popitem(last=False)
    #     self.cache_data.pop(removed_key)
    #     return removed_key

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            self.cache_map[key] += 1
            return self.cache_data[key]
        return None
