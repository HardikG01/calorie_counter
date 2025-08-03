from cachetools import TTLCache

# Key: food_name, Value: calories per serving
cache = TTLCache(maxsize=100, ttl=3600)  # 1 hour cache
