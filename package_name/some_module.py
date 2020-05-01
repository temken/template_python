
def reverse_string(s):
	"""
	Reverses order or characters in string s.
	"""
	return s[::-1]
	
def fib(n):
	"""
	Returns the nth Fibonacci number.
	"""
	if n < 2:
		return n
	else:
		return fib(n-2) + fib(n-1)