import sys
from cache import access

error = 0
access_time = 0
page_fault = 0                                                  # counter for number of times address isn't in cache
counter = 0                                                     # index for cache_valid

# open the first parameter as a file, reach each line and find its virtual address
# simulate using the address by seeing if it is already a valid entry in the cache
# keep count of the number of times it isn't within the cache (cache miss)
# if it isn't in the cache, which will have a limited size of 16 ways
#   then give it an entry
with open(sys.argv[1], 'r') as cache_file:
    for line in cache_file:
        try:
            x = line.split()
            pc = x[0][:-1]          # program counter (PC), USELESS
            rw = x[1]               # read/write instruction, USEFUL FOR A WRITE BACK-POLICY
            va = x[2]               # virtual address, CONVERT TO INTEGER
            dc = str(int(va, 16))   # decimal value of virtual address, USEFUL SOMEHOW?
            # address is assumed 64-bit, 6 is offset, # of bits = set index,
            # the rest is the tag
            page_fault, access_time = access(rw, va, access_time)
        except IndexError:
            error += 1
            print(access_time + error, x)
        except ValueError:
            error += 1
            print(access_time + error, x)
print("~~"*10, "Output", "~~"*10)
print("page fault:", page_fault, "- Total accesses:", access_time)
print("Cache miss rate:", page_fault/access_time * 100, "%")
cache_file.close()