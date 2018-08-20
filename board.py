import random

from pieces import Pawn, Rook, Knight, King, Bishop, Queen


class Board(object):
	Pieces = property(lambda self: self._pieces)

	def __init__(self, pieces, turn):
		self._pieces = pieces
		self._turn = turn

	@classmethod
	def CreateNewBoard(cls):
		pieces = [Pawn((i, 1), "white") for i in range(8)] + [Pawn((i, 6), "black") for i in range(8)]
		pieces.extend([Rook((0, 0), "white"), Rook((7, 0), "white"), Rook((0, 7), "black"), Rook((7, 7), "black")])
		pieces.extend([Knight((1, 0), "white"), Knight((6, 0), "white"), Knight((1, 7), "black"), Knight((6, 7), "black")])
		pieces.extend([Bishop((2, 0), "white"), Bishop((5, 0), "white"), Bishop((2, 7), "black"), Bishop((5, 7), "black")])
		pieces.extend([King((4, 0), "white"), King((4, 7), "black")])
		pieces.extend([Queen((3, 0), "white"), Queen((3, 7), "black")])

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

	def printBoard(self):
		print()
		print('    ________ ________ ________ ________ ________ ________ ________ ________')
		for a in range(7, -1, -1):
			if (a) % 2 == 0:
				print('   |        |  ----  |        |  ----  |        |  ----  |        |  ----  |')
			else :
				print('   |  ----  |        |  ----  |        |  ----  |        |  ----  |        |')
			print( a, ' ', end = '')
			for b in range (8):
				piece = self.GetPiece((b, a))
				if (a + b) % 2 == 0:
					if not piece : print ('|        ', end = '')
					elif piece.Color == "white":print (piece.AbbreviationLong, end = '')
					else:print (piece.AbbreviationLong.lower, end = '')

				else :
					if not piece: print('|  ----  ', end='')
					elif piece.Color == "white": print (piece.AbbreviationLongColored, end = '')
					else:	print (piece.AbbreviationLongColored.lower, end = '')


			print('|')
			if (a) % 2 == 0:
				print('   |________|__----__|________|__----__|________|__----__|________|__----__|')
			else :
				print('   |__----__|________|__----__|________|__----__|________|__----__|________|')
		print()
		print('       a        b        c        d        e        f        g        h    ')
		print()