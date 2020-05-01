import sys
import argparse

from .some_module import fib, reverse_string

def main():
	args = parse_args(sys.argv[1:])
	print(fib(args.number))
	print(reverse_string(args.some_string))

def parse_args(args):
	parser = argparse.ArgumentParser(description="python project template")
	parser.add_argument("number", help = "Some integer. (Default: 10)",
						nargs='?', type = int, default = 10)
	parser.add_argument("some_string", help = "Some string. (Default: 'foo')",
						nargs='?', type = str, default = "foo")
	return parser.parse_args(args)