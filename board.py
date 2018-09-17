import random

from pieces import Pawn, Rook, Knight, King, Bishop, Queen


class Board(object):
	Pieces = property(lambda self: self._pieces)

	def __init__(self, pieces, turn):
		self._pieces = pieces
		self._turn = turn
		self._lastMove = None
		self._moveNumber = 0
		self._moves = list()

	@classmethod
	def CreateNewBoard(cls, fen=None):
		if fen:
			raise NotImplementedError()
		else:
			pieces = [Pawn((i, 1), "white") for i in range(8)] + [Pawn((i, 6), "black") for i in range(8)]
			pieces.extend([Rook((0, 0), "white"), Rook((7, 0), "white"), Rook((0, 7), "black"), Rook((7, 7), "black")])
			pieces.extend([Knight((1, 0), "white"), Knight((6, 0), "white"), Knight((1, 7), "black"), Knight((6, 7), "black")])
			pieces.extend([Bishop((2, 0), "white"), Bishop((5, 0), "white"), Bishop((2, 7), "black"), Bishop((5, 7), "black")])
			pieces.extend([King((4, 0), "white"), King((4, 7), "black")])
			pieces.extend([Queen((3, 0), "white"), Queen((3, 7), "black")])

		return cls(pieces, "white")

	def Move(self, move=None):
		if move is None:
			possibleMoves = [(piece, newPos) for piece in self._pieces if piece.Color == self._turn for newPos in piece.GetPossibleMoves(self, None)]

			piece, newPos = random.choice(possibleMoves)

			removePiece = self.GetPiece(newPos)
			if removePiece:
				self._pieces.remove(removePiece)

			prevPos = piece.HumanPos

			piece.Move(newPos)
		else:
			prevPos, newPos = move
			piece = self.GetPiece(prevPos)
			if not piece:
				raise Exception("Cannot find piece on field '{}'.".format(prevPos))

			removePiece = self.GetPiece(newPos)
			if removePiece:
				self._pieces.remove(removePiece)

			piece.Move(newPos)

		self._moves.append((piece, prevPos, newPos, bool(removePiece)))

		print("{}: {} -> {} (Pieces: {}, {})".format(piece.Abbreviation, prevPos, piece.HumanPos, len(self.GetPieces("white")), len(self.GetPieces("black"))))

		if self._turn == "white":
			self._moveNumber += 1
			self._turn = "black"
		else:
			self._turn = "white"

	def GetPiece(self, position):
		for piece in self._pieces:
			if piece.Pos == position:
				return piece
		else:
			return None

	def GetPieces(self, colors=None, positions=None, pieces=None):
		filteredPieces = self._pieces

		if colors is not None:
			filteredPieces = [p for p in filteredPieces if p.Color in colors]

		if positions is not None:
			filteredPieces = [p for p in filteredPieces if p.Pos in positions]

		if pieces is not None:
			filteredPieces = [p for p in filteredPieces if p.__class__ in pieces]

		return filteredPieces

	def ExportFEN(self):
		fen = ""
		for i in range(7, -1, -1):
			z = 0
			for j in range(8):
				piece = self.GetPiece((j, i))
				if piece:
					if z != 0:
						fen += str(z)

					fen += piece.Abbreviation if piece.Color == "white" else piece.Abbreviation.lower()
					z = 0
				else:
					z += 1

			else:
				if z != 0:
					fen += str(z)

				if i > 0:
					fen += "/"

		fen += " {} ".format(self._turn[0])

		# Castling
		whiteCastlings = self._CheckCastling("white")
		blackCastlings = self._CheckCastling("black")

		if not whiteCastlings and not blackCastlings:
			fen += "- "
		else:
			if whiteCastlings is not None:
				fen += whiteCastlings
			if blackCastlings is not None:
				fen += blackCastlings

			fen += " "

		# Last pawn move
		if not self._moves:
			fen += "-" + " "
		else:
			piece, prevPos, newPos, _ = self._moves[-1]
			if not issubclass(type(piece), Pawn):
				fen += "-" + " "
			else:
				if prevPos[1] < newPos[1]:
					if prevPos[1] == 1 and newPos[1] == 3:
						fen += "abcdefgh"[prevPos[0]] + str(3) + " "
					else:
						fen += "- "
				elif newPos[1] < prevPos[1]:
					if prevPos[1] == 6 and newPos[1] == 4:
						fen += "abcdefgh"[prevPos[0]] + str(6) + " "
					else:
						fen += "- "
				else:
					fen += "- "

		for i, move in enumerate(self._moves[::-1]):
			piece, _, _, removed = move
			if issubclass(type(piece), Pawn) or removed:
				break

		fen += str(i) + " " + str(max(self._moveNumber, 1))

		return fen

	def _CheckCastling(self, color):
		if self.GetPieces([color], pieces=[King])[0].Moved:
			return None

		castles = ["", ""]
		for rook in self.GetPieces([color], pieces=[Rook]):
			if rook.Moved:
				continue
			else:
				if rook.Pos[0] == 7:
					castles[0] = "K" if color == "white" else "k"
				elif rook.Pos[0] == 0:
					castles[1] = "Q" if color == "white" else "q"

		castles = "".join(castles).strip()

		return castles

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
			print( a+1, ' ', end = '')
			for b in range (8):
				piece = self.GetPiece((b, a))
				if (a + b) % 2 == 0:
					if not piece : print ('|        ', end = '')
					elif piece.Color == "white":print (piece.AbbreviationLong, end = '')
					else:print (piece.AbbreviationLong.lower(), end = '')

				else :
					if not piece: print('|  ----  ', end='')
					elif piece.Color == "white": print (piece.AbbreviationLongColored, end = '')
					else:	print (piece.AbbreviationLongColored.lower(), end = '')


			print('|')
			if (a) % 2 == 0:
				print('   |________|__----__|________|__----__|________|__----__|________|__----__|')
			else :
				print('   |__----__|________|__----__|________|__----__|________|__----__|________|')
		print()
		print('       a        b        c        d        e        f        g        h    ')
		print()