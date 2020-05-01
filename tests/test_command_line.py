from unittest import TestCase

from package_name.command_line import main, parse_args

class TestCmd(TestCase):
	def test_parser(self):
		parser = parse_args(['11', 'word'])
		self.assertEqual(parser.number,11)
		self.assertEqual(parser.some_string,"word")