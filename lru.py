# pass in the cache dictionary
# if the address is within cache, its a hit
# otherwise, lru will determine which entry in cache to use

#               # # of sets
#               # cache size
CL_SIZE = 64    # cache line will be 64 bytes
#               # replacement policy

# def access(rw, address)
# determine hit or miss
#   check if in cache
#   cut the bits to find the set id and offset in cache
#   search in set: tag comparison
# do hit or miss process
#   ***if hit, update access/age/timestamp/at/access_time of Hit_CL
#   queue uses time_stamp, can use tag or id
#   ***if miss, find slot.
#   use an empty way, if there is one, or use an lru
#   update the slot
#       set valid bit to 1
#       update tag
#       update timestamp
# keep track of misses to report miss rate


def cache_find(cache, cache_valid, va, pf, at):
    if cache.get(va, "NF") == "NF":
        pf += 1
        cache[va] = at
    else:
        pf = pf

    return pf
