from time import perf_counter
from functools import wraps

class Tools():
    def cash(size = -1):
        def cash(func):
            bild = {}
            @wraps(func)
            def wrappers(*args,**kwargs):
                key = args+tuple((x,kwargs[x]) for x in kwargs)
                if key not in bild:
                    bild[key] = func(*args,**kwargs)
                    if len(bild) > size > 0:
                        del bild[next(iter(bild))]
                    return bild[key]
                else:
                    return bild[key]
            return wrappers
        return cash

    

    def log(donep = True):
        def log(func):
            @wraps(func)
            def wrapper(*args,**kwargs):
                    try:
                        start = perf_counter()
                        red = func(*args,**kwargs)
                        end = perf_counter()
                        if donep:
                            print(f"[{func.__name__}] [module: {func.__module__}] {1/round(end-start,5)} done...")
                        return red
                    except Exception as errorsx:
                        print(f"errors: [{func.__name__}] [module: {func.__module__}]  {errorsx}")
                        print(args+tuple((x,kwargs[x]) for x in kwargs))
            return wrapper
        return log
    


import multiprocessing
import time
import math
import numpy as np
import numba
import sys
import struct

def sieve(n):
    flags = np.ones(n, dtype=bool)
    flags[0] = flags[1] = False
    for i in range(2, int(math.sqrt(n))+1):
        # We could use a lower upper bound for this loop, but I don't want to bother with
        # getting the rounding right on the sqrt handling.
        if flags[i]:
            flags[i*i::i] = False
    return np.flatnonzero(flags)



if __name__ == "__main__":
    start = perf_counter()
    t = sieve(1_000_000_000)
    end = perf_counter()
    print(end-start)
    with open("textprime.txt","a") as f:
        for x in t:
            f.write(str(x))

