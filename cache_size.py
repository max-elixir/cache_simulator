import sys
# Determines the size of the cache by hard-coded
# sizes from project doc
# might be better to put this in the wrapper
# BASH script instead of its own class
# It should inspect the file name and use
# it to hard-code the cache size
# driver script will start reading the file,
# unaffected by this wrapper

file = open(sys.argv[1])
filename = file.name
file.close()


def getsize():
    global filename
    print("Filename: " + filename)
    # 1 KB cache
    if filename == "memory_traces/1KB_64":
        cs = 1024
    # 4 MB cache = 4096 KB cache
    elif filename == "memory_traces/4MB_4":
        cs = 4194304
    elif filename == "memory_traces/32MB_4B":
        cs = 4194304
    elif filename == "memory_traces/bw_dgemm.traces.txt":
        cs = 4194304
    # 256 KB cache
    elif filename == "memory_traces/full_dgemm.traces.txt":
        cs = 262144
    # 32 KB cache
    elif filename == "memory_traces/gcc.trace.txt":
        cs = 32768
    elif filename == "memory_traces/ls.trace.txt":
        cs = 32768
    # 256 KB cache
    elif filename == "memory_traces/naive_dgemm.trace.txt":
        cs = 262144
    elif filename == "memory_traces/naive_dgemm_full.trace.txt":
        cs = 262144
    elif filename == "memory_traces/openblas_dgemm.trace.txt":
        cs = 262144
    # default to 1 KB cache
    else:
        cs = 1024
    return cs
