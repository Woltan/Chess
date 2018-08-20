import unittest

from board import Board


class TestBoard(unittest.TestCase):
	def testMove(self):
		board = Board.CreateNewBoard()
		for i in range(80):
			board.printBoard()
			print("-" * 20)
			board.Move()


if __name__ == '__main__':
	unittest.main()
