'''

sum(1) = 1
sum(2) = 1 + 2 = 3
sum(3) = 1 + 2 + 3 = 6
sum(4) = 1 + 2 + 3 + 4 = 10

sum(n) = 1 + 2 + 3 + ... + n     n
sum(n) = sum(n-1) + n    
'''

def sum(n):
    if (n == 1):
        return 1
    else:
        return sum(n - 1) + n

print(sum(5))