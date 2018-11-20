import sys

associtivity = 0
ways = 16 # size of page/frame table
size = 10 # number of offset bits
access_time = 1
cache = {}
pf = 0
ct = 0
    
with open(sys.argv[1], 'r') as cache_file:
    for line in cache_file:
        x = line.split()
        x[0] = x[0][:-1]
        if access_time > 16:
            access_time = 1
        if cache.get(access_time, "nope") == "nope":
            pf += 1
            print("oh shoot my DOOD")
        cache[access_time] = x[2]
        print(x[0], x[1], x[2], access_time)

        ct += 1
        access_time += 1

print(pf/ct * 100)

