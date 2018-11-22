from cache_size import getsize
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

ways = 16
CL_SIZE = 64    # cache line will be 64 bytes, always
cache_size = 0


# each entry of a cache or lru queue
class CacheEntry:
    def __init__(self, tag, valid, data, timestamp):
        self.tag = tag
        self.valid = valid
        self.data = data
        self.timestamp = timestamp


cache = []      # 16-way cache
queue = []
page_fault = 0
access_time = 0


def access(rw, va):
    global access_time
    global page_fault
    access_time += 1
    counter = 0
    found = 0

    for entry in cache:
        if counter >= 16:
            break
        counter += 1
        if entry.tag == va:
            entry.timestamp = access_time
            found = 1
            break

    if found == 0:
        page_fault += 1
        cache.append(CacheEntry(va, 1, "x", access_time))

    return page_fault, access_time
