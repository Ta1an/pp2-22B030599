import time
import math
def root(n, ms):
    print(time.time())
    time.sleep(ms/1000)
    print(f'Square root of {n} after {ms} milliseconds is {math.sqrt(n)}')
    print(time.time())
