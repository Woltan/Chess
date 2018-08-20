import random

from pieces import Pawn, Rook


class Board(object):
	Pieces = property(lambda self: self._pieces)

	def __init__(self, pieces, turn):
		self._pieces = pieces
		self._turn = turn

	@classmethod
	def CreateNewBoard(cls):
		pieces = [Pawn((i, 1), "white") for i in range(8)] + [Pawn((i, 6), "black") for i in range(8)]
		pieces.extend([Rook((0, 0), "white"), Rook((7, 0), "white"), Rook((0, 7), "black"), Rook((7, 7), "black")])

		return cls(pieces, "white")

	def Move(self):
		possibleMoves = [(piece, newPos) for piece in self._pieces if piece.Color == self._turn for newPos in piece.GetPossibleMoves(self, None)]

		piece, newPos = random.choice(possibleMoves)

		removePiece = self.GetPiece(newPos)
		if removePiece:
			self._pieces.remove(removePiece)

		prevPos = piece.HumanPos

		piece.Move(newPos)

		print("{}: {} -> {} (Pieces: {}, {})".format(piece.Abbreviation, prevPos, piece.HumanPos, len(self.GetPieces("white")), len(self.GetPieces("black"))))

		self._turn = "white" if self._turn == "black" else "black"

	def GetPiece(self, position):
		for piece in self._pieces:
			if piece.Pos == position:
				return piece
		else:
			return None

	def GetPieces(self, colors=None, positions=None):
		pieces = self._pieces

		if colors is not None:
			pieces = [p for p in pieces if p.Color in colors]

		if positions is not None:
			pieces = [p for p in pieces if p.Pos in positions]

		return pieces

	def Print(self):
		board = "_" * 8 + "\n"
		for i in range(7, -1, -1):
			for j in range(8):
				piece = self.GetPiece((j, i))
				if piece:
					board += piece.Abbreviation if piece.Color == "white" else piece.Abbreviation.lower()
				else:
					board += " "

			board += "\n"

		board += "-" * 8 + "\n"

		print(board)

