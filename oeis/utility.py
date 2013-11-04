def choose(a, b):
	if a < b:
		return 0
	r = 1
	for i in range(0, b):
		r *= a - i
		r /= i + 1
	return r

def factorial(a):
        r = 1
        for i in range(0, a):
                r *= i + 1
        return r

def fibonacci():
        a, b = 0, 1
        while 1:
                yield a
                a, b = b, a+b

def firstn(g, n):
        for i in range(0, n):
                yield g.next()

def partitions(n):
        if n == 0:
                return
        a = []
        if n == 1:
                a.append(1)
                yield a
                return
        a = [0 for i in range(n)]
        k = 1
        a[1] = n
        while k != 0:
                x = a[k-1] + 1
                y = a[k] - 1
                k -= 1
                while x <= y:
                        a[k] = x
                        y -= x
                        k += 1
                a[k] = x + y
                yield a[:k+1:]

def multiples(partition):
        idx = 0
        n = len(partition)
        while idx < n:
                s = idx
                num = partition[s]
                while idx < n and partition[idx] == num:
                        idx += 1
                yield [idx-s, partition[s]]

