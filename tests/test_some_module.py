from package_name.some_module import fib,reverse_string

def test_fib():
	fib10 = 55
	assert fib(10) == fib10

def test_reverse_string():
	assert reverse_string('foobar!') == '!raboof'
	assert reverse_string('stressed') == 'desserts'