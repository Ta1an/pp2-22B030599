from functools import reduce
import math
def multiply():
    list = map(int, input().split())
    result = reduce(lambda a, b: a * b, list)
    print(result)