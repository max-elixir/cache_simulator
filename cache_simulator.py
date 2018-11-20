import sys
from lru import cache_find

access_time = 1                                                 # time counter for access
page_fault = 0                                                  # counter for number of times address isn't in cache
cache = {}                                                      # 16-way cache
cache_valid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 16-way cache's valid entries
counter = 0                                                     # index for cache_valid

# open the first parameter as a file, reach each line and find its virtual address
# simulating using the address by seeing if it is already a valid entry in the cache
# keep count of the number of times it isn't within the cache (cache miss)
# if it isn't in the cache, which will have a limited size of 16 ways
#   then give it an entry
with open(sys.argv[1], 'r') as cache_file:
    for line in cache_file:
        x = line.split()
        pc = x[0][:-1]      # program counter (PC)
        rw = x[1]           # read/write instruction
        va = x[2]           # virtual address

        page_fault = cache_find(cache, cache_valid, va, page_fault, access_time)

        access_time += 1

print("Cache miss rate:", page_fault/(access_time-1) * 100, "%")
