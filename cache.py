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


# each entry of a cache or lru queue
class CacheEntry:
    def __init__(self, tag, valid, timestamp):
        self.tag = tag
        self.valid = valid
        self.timestamp = timestamp

    def __lt__(self, other):
        return self.timestamp < other.timestamp


# test prints for variables - remove later
# print("~~"*11, "Data", "~~"*11)
ways = 16               # number of entries in LRU
CL_SIZE = 64            # cache line will be 64 bytes, always
offset_bits = 6         # 64 Byte for CL_Size -> 2^6 for CL_Size -> 6 bits for offset
cache_size = getsize()
sets = int(cache_size / (CL_SIZE*ways))
if sets == 1:
    set_bits = 1
elif sets == 32:
    set_bits = 5
elif sets == 256:
    set_bits = 8
elif sets == 4096:
    set_bits = 12

# print("Ways: ", ways, "- Cache Line Size (B): ", CL_SIZE)
# print("Cache size (B):", cache_size)
# print("Total Sets: ", sets)
cache = []      # 16-way set associative cache
page_fault = 0
access_time = 0
for i in range((sets * 16)):
    cache.append(CacheEntry(-1, 0, 0))
# print("Cache now has this many entries:", len(cache))


def access(rw, va, at):
    global access_time      # static, global storage of access time
    global page_fault       # static, global storage of page fault counter
    at = at + 1             # increment access time passed
    access_time = at        # assign to global access-time

    # tag_here = str(int(va, 16))           # decimal value of virtual address, USEFUL SOMEHOW?
    binary_val = bin(int(va, 16))
    set_num = bin(int(binary_val, 2) >> offset_bits)[-set_bits:]
    set_num_val = int(set_num, 2)   # Convert virtual address to binary, pull set number out
    start = (set_num_val * 16)
    end = start + 16
    found = 0

    tag_new = bin(int(binary_val, 2) >> (offset_bits + set_bits))
    # print(int(tag_new, 2))
    # starting at the beginning of a set, look at the 16-ways
    # if tag matches, and is valid,
    # Hit - update access time
    # print("rw:", rw, "va:", va, "Time:", access_time, "set:", set_num_val)
    for counter in range(start, end):
        if cache[counter].tag == tag_new:
            if cache[counter].valid == 1:
                cache[counter].timestamp = access_time
                found = 1
                break

    # Miss - found = 0, so find a spot to put it in
    if found == 0:
        page_fault += 1
        # default timestamp checker is current time, which is the oldest age possible
        timestamp_check = access_time
        counter_hold = start     # default spot is first way in set
        # Look through set again to find a spot
        for counter in range(start, end):
            if cache[counter].timestamp < timestamp_check:
                timestamp_check = cache[counter].timestamp
                counter_hold = counter
        cache[counter_hold].timestamp = access_time
        cache[counter_hold].valid = 1
        cache[counter_hold].tag = tag_new

    # OLD FOR LOOP
    # print(va.rjust(12), dc.rjust(12), binary_val.rjust(12), set_num, set_num_val)
    # print("va:", va.rjust(5), "val:", dc.rjust(5), "offset:", offset.rjust(5))
    # for entry in cache:
    #    if counter >= ways:
    #        break
    #    counter += 1
    #    if entry.tag == va:
    #        entry.timestamp = access_time
    #        found = 1
    #       break
    # if found == 0:          # not in set, page fault occurs
    #    page_fault += 1
    #    cache.append(CacheEntry(va, 1, access_time))

    return page_fault, at

# def print22():
#    for entry in cache:
#        print(str(entry.tag).rjust(25), str(entry.valid).rjust(2), str(entry.timestamp).rjust(7))
