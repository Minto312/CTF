import time
import string

def measeure_time(flag):
    start = time.time()
    exec('./chall')
    print
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time: {end - start}")
        return result
    return wrapper