from functools import reduce
l = [1, 2, 111, 65, 344, 53, 643, 754, 45, 55]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))