class _Piece(object):
	Abbreviation = None

	Pos = property(lambda self: self._pos)
	HumanPos = property(lambda self: "abcdefgh"[self._pos[0]] + str(self._pos[1] + 1))
	Color = property(lambda self: self._color)

	def __init__(self, pos, color):
		self._pos = pos
		self._color = color

		self._moved = False

	def Move(self, newPos):
		self._pos = newPos

		self._moved = True

	def GetPossibleMoves(self, board, prevMove):
		raise NotImplementedError()


class Pawn(_Piece):
	Abbreviation = "P"

	def GetPossibleMoves(self, board, prevMove):
		# TODO: Implement En-Passant
		possibleMoves = list()

		if self._color == "white":
			if self._pos[1] == 7:
				return []

			if not board.GetPiece((self._pos[0], self._pos[1] + 1)):
				possibleMoves.append((self._pos[0], self._pos[1] + 1))
			if self._pos[1] == 1 and not board.GetPiece((self._pos[0], self._pos[1] + 2)):
				possibleMoves.append((self._pos[0], self._pos[1] + 2))

			possibleMoves.extend([p.Pos for p in board.GetPieces("black", [(self._pos[0] + 1, self._pos[1] + 1), (self._pos[0] - 1, self._pos[1] + 1)])])

		else:
			if self._pos[1] == 0:
				return []

			if not board.GetPiece((self._pos[0], self._pos[1] - 1)):
				possibleMoves.append((self._pos[0], self._pos[1] - 1))
			if self._pos[1] == 6 and not board.GetPiece((self._pos[0], self._pos[1] - 2)):
				possibleMoves.append((self._pos[0], self._pos[1] - 2))

			possibleMoves.extend([p.Pos for p in board.GetPieces("white", [(self._pos[0] + 1, self._pos[1] - 1), (self._pos[0] - 1, self._pos[1] - 1)])])

		return possibleMoves


class Rook(_Piece):
	Abbreviation = "R"

	def GetPossibleMoves(self, board, prevMove):
		possibleMoves = list()

		# Right
		for i in range(self._pos[0] + 1, 8):
			newPos = (i, self._pos[1])
			piece = board.GetPiece(newPos)
			if piece:
				if piece.Color != self._color:
					possibleMoves.append(newPos)
					break
				else:
					break
			else:
				possibleMoves.append(newPos)

		# Left
		for i in range(self._pos[0] - 1, -1, -1):
			newPos = (i, self._pos[1])
			piece = board.GetPiece(newPos)
			if piece:
				if piece.Color != self._color:
					possibleMoves.append(newPos)
					break
				else:
					break
			else:
				possibleMoves.append(newPos)

		# Top
		for i in range(self._pos[1] + 1, 8):
			newPos = (self._pos[0], i)
			piece = board.GetPiece(newPos)
			if piece:
				if piece.Color != self._color:
					possibleMoves.append(newPos)
					break
				else:
					break
			else:
				possibleMoves.append(newPos)

		# Bottom
		for i in range(self._pos[1] - 1, -1, -1):
			newPos = (self._pos[0], i)
			piece = board.GetPiece(newPos)
			if piece:
				if piece.Color != self._color:
					possibleMoves.append(newPos)
					break
				else:
					break
			else:
				possibleMoves.append(newPos)

		return possibleMoves
