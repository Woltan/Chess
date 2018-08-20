import unittest

from board import Board


class TestBoard(unittest.TestCase):
	def testMove(self):
		board = Board.CreateNewBoard()
		for i in range(80):
			board.printBoard()
			print("-" * 20)
			board.Move()

	def testExportFEN(self):
		board = Board.CreateNewBoard()
		self.assertEqual("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", board.ExportFEN())


if __name__ == '__main__':
	unittest.main()
