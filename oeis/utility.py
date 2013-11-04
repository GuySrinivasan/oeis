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

def another():
        return 3
