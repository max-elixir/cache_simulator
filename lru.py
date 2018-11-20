# pass in the cache dictionary
# if the address is within cache, its a hit
# otherwise, lru will determine which entry in cache to use


def cache_find(cache, cache_valid, va, pf, at):
    if cache.get(va, "NF") == "NF":
        pf += 1
        cache[va] = at

    return pf
