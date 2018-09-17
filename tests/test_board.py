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

		# e4
		board.Move(((4, 1), (4, 3)))
		self.assertEqual("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1", board.ExportFEN())

		# Nf6
		board.Move(((6, 7), (5, 5)))
		self.assertEqual("rnbqkb1r/pppppppp/5n2/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 1 1", board.ExportFEN())

		# a3
		board.Move(((0, 1), (0, 2)))
		self.assertEqual("rnbqkb1r/pppppppp/5n2/8/4P3/P7/1PPP1PPP/RNBQKBNR b KQkq - 0 2", board.ExportFEN())

		# Nxe4
		board.Move(((5, 5), (4, 3)))
		self.assertEqual("rnbqkb1r/pppppppp/8/8/4n3/P7/1PPP1PPP/RNBQKBNR w KQkq - 0 2", board.ExportFEN())

		# Ke2
		board.Move(((4, 0), (4, 1)))
		self.assertEqual("rnbqkb1r/pppppppp/8/8/4n3/P7/1PPPKPPP/RNBQ1BNR b kq - 1 3", board.ExportFEN())

		# Rg8
		board.Move(((7, 7), (6, 7)))
		self.assertEqual("rnbqkbr1/pppppppp/8/8/4n3/P7/1PPPKPPP/RNBQ1BNR w q - 2 3", board.ExportFEN())


if __name__ == '__main__':
	unittest.main()
