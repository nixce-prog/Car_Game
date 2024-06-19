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
