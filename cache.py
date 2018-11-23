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
print("~~"*11, "Data", "~~"*11)
ways = 16               # number of entries in LRU
CL_SIZE = 64            # cache line will be 64 bytes, always
offset_bits = 5         # 64 Byte for CL_Size -> 2^6 for CL_Size -> 6 bits for offset
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

print("Ways: ", ways, "- Cache Line Size (B): ", CL_SIZE)
print("Cache size (B):", cache_size)
print("Total Sets: ", sets)
cache = []      # 16-way set associative cache
queue = []
page_fault = 0
access_time = 0


def access(rw, va, at):
    global access_time      # static, global storage of access time
    global page_fault       # static, global storage of page fault counter
    at = at + 1             # increment access time passed
    access_time = at        # assign to global access-time
    counter = 0             # counter for looping through set
    found = 0               # boolean for finding value in set

    dc = str(int(va, 16))   # decimal value of virtual address, USEFUL SOMEHOW?
    binary_val = bin(int(va, 16))
    set_num = bin(int(binary_val, 2) >> offset_bits)[-set_bits:]
    set_num_val = int(set_num, 2)

    # va is string, converted to a hex, converted to binary,
    # removed of its binary indicator at the fron,
    # filling a full line of 64 characters with 0s
    #tag = bin(int(va, 16) >> 6)
    #print(tag, bin(int(va, 16)))
          #int(bin(int(va, 16))[2:]) & 63)
    # print(va.rjust(12), dc.rjust(12), binary_val.rjust(12), set_num, set_num_val)
    # print("va:", va.rjust(5), "val:", dc.rjust(5), "offset:", offset.rjust(5))

    for entry in cache:
        if counter >= ways:
            break
        counter += 1
        if entry.tag == va:
            entry.timestamp = access_time
            found = 1
            break

    if found == 0:
        page_fault += 1
        cache.append(CacheEntry(va, 1, access_time))

    return page_fault, at
