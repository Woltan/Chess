import unittest

from board import Board
from pieces import Pawn


class TestPawn(unittest.TestCase):
	def setUp(self):
		self._board = Board.CreateNewBoard()

	def testGetPossibleMoves(self):
		pawn = self._board.GetPiece((4, 1))
		self.assertListEqual(pawn.GetPossibleMoves(self._board, None), [(4, 2), (4, 3)])

		self._board.Pieces.append(Pawn((4, 3), "black"))
		self.assertListEqual(pawn.GetPossibleMoves(self._board, None), [(4, 2)])

		self._board.Pieces.append(Pawn((4, 2), "black"))
		self.assertListEqual(pawn.GetPossibleMoves(self._board, None), [])

		self._board.Pieces.append(Pawn((5, 2), "black"))
		self._board.Pieces.append(Pawn((3, 2), "white"))
		self.assertListEqual(pawn.GetPossibleMoves(self._board, None), [(5, 2)])


class TestRook(unittest.TestCase):
	def setUp(self):
		self._board = Board.CreateNewBoard()

	def testGetPossibleMoves(self):
		rook = self._board.GetPiece((7, 0))
		self.assertListEqual(rook.GetPossibleMoves(self._board, None), [])


class TestKnight(unittest.TestCase):
	def setUp(self):
		self._board = Board.CreateNewBoard()

	def testGetPossibleMoves(self):
		knight = self._board.GetPiece((1, 7))
		self.assertListEqual(knight.GetPossibleMoves(self._board, None), [(0, 5), (2, 5)])


if __name__ == '__main__':
	unittest.main()
