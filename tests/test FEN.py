import unittest

from board import Board


class TestFEN(unittest.TestCase):
	def testFEN(self):
		board = Board.CreateNewBoard()
		print(board.ExportFEN())
		for i in range(10):
			board.printBoard()
			print("-" * 20)
			board.Move()
			print(board.ExportFEN())


if __name__ == '__main__':
	unittest.main()
