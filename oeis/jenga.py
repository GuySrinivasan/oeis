from utility import *
from numpy import prod

def A200544(n):
    if n == 0:
        return 1
    p = [[y for y in multiples(x)] for x in partitions(n)]
    return sum([prod([choose(fib(x[i][1]+1)+x[i][0]-1,x[i][0]) for i in range(0,len(x))]) for x in p])

fib_memo = [0, 1]
def fib(n):
    s = len(fib_memo)
    if n < s:
        return fib_memo[n]
    for i in range(s, n+1):
        fib_memo.append(fib_memo[i-2] + fib_memo[i-1])
    return fib_memo[n]
