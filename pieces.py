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
	AbbreviationLong = "|  PAWN  "
	AbbreviationLongColored = "|--PAWN--"

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
	AbbreviationLong = "|  ROOK  "
	AbbreviationLongColored = "|--ROOK--"

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


class Bishop(_Piece):
	Abbreviation = "B"
	AbbreviationLong = "|  BSHP  "
	AbbreviationLongColored = "|--BSHP--"

	def GetPossibleMoves(self, board, prevMove):
		possibleMoves = list()

		# Up right
		j = self._pos[1]
		for i in range(self._pos[0] + 1, 8):
			j = j + 1
			if j > 7: break
			newPos = (i, j)
			piece = board.GetPiece(newPos)
			if piece:
				if piece.Color != self._color:
					possibleMoves.append(newPos)
					break
				else:
					break
			else:
				possibleMoves.append(newPos)

		# Up Left
		j = self._pos[1]
		for i in range(self._pos[0] - 1, -1):
			j = j + 1
			if j > 7: break
			newPos = (i, j)
			piece = board.GetPiece(newPos)
			if piece:
				if piece.Color != self._color:
					possibleMoves.append(newPos)
					break
				else:
					break
			else:
				possibleMoves.append(newPos)

		# Down Right
		j = self._pos[1]
		for i in range(self._pos[0] + 1, 8):
			j = j - 1
			if j < 0: break
			newPos = (i,j)
			piece = board.GetPiece(newPos)
			if piece:
				if piece.Color != self._color:
					possibleMoves.append(newPos)
					break
				else:
					break
			else:
				possibleMoves.append(newPos)

		# Down Left
		j = self._pos[1]
		for i in range(self._pos[0] - 1, -1, -1):
			j = j - 1
			if j < 0: break
			newPos = (i , j)
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


class King(_Piece):
	Abbreviation = "K"
	AbbreviationLong = "|  KING  "
	AbbreviationLongColored = "|--KING--"

	def GetPossibleMoves(self, board, prevMove):
		possibleMoves = list()

		# Up left
		newPos = (self._pos[0] - 1, self._pos[1] + 1)
		piece = board.GetPiece(newPos)
		if piece:
			if piece.Color != self._color:
				possibleMoves.append(newPos)
		else:
			if newPos[0] > -1 and newPos[0] < 8 and newPos[1] > -1 and newPos[1]< 8:
				possibleMoves.append(newPos)

		# Up right
		newPos = (self._pos[0] + 1, self._pos[1] + 1)
		piece = board.GetPiece(newPos)
		if piece:
			if piece.Color != self._color:
				possibleMoves.append(newPos)
		else:
			if newPos[0] > -1 and newPos[0] < 8 and newPos[1] > -1 and newPos[1] < 8:
				possibleMoves.append(newPos)

		# Down left
		newPos = (self._pos[0] - 1, self._pos[1] - 1)
		piece = board.GetPiece(newPos)
		if piece:
			if piece.Color != self._color:
				possibleMoves.append(newPos)
		else:
			if newPos[0] > -1 and newPos[0] < 8 and newPos[1] > -1 and newPos[1] < 8:
				possibleMoves.append(newPos)

		# Down right
		newPos = (self._pos[0] + 1, self._pos[1] - 1)
		piece = board.GetPiece(newPos)
		if piece:
			if piece.Color != self._color:
				possibleMoves.append(newPos)
		else:
			if newPos[0] > -1 and newPos[0] < 8 and newPos[1] > -1 and newPos[1] < 8:
				possibleMoves.append(newPos)

		# Left
		newPos = (self._pos[0]-1, self._pos[1])
		piece = board.GetPiece(newPos)
		if piece:
			if piece.Color != self._color:
				possibleMoves.append(newPos)
		else:
			if newPos[0] > -1 and newPos[0] < 8 and newPos[1] > -1 and newPos[1]< 8 :
				possibleMoves.append(newPos)

		# Down
		newPos = (self._pos[0], self._pos[1] - 1)
		piece = board.GetPiece(newPos)
		if piece:
			if piece.Color != self._color:
				possibleMoves.append(newPos)
		else:
			if newPos[0] > -1 and newPos[0] < 8 and newPos[1] > -1 and newPos[1] < 8:
				possibleMoves.append(newPos)

		# Up
		newPos = (self._pos[0], self._pos[1] + 1)
		piece = board.GetPiece(newPos)
		if piece:
			if piece.Color != self._color:
				possibleMoves.append(newPos)
		else:
			if newPos[0] > -1 and newPos[0] < 8 and newPos[1] > -1 and newPos[1] < 8:
				possibleMoves.append(newPos)

		# Right
		newPos = (self._pos[0] + 1, self._pos[1])
		piece = board.GetPiece(newPos)
		if piece:
			if piece.Color != self._color:
				possibleMoves.append(newPos)
		else:
			if newPos[0] > -1 and newPos[0] < 8 and newPos[1] > -1 and newPos[1] < 8:
				possibleMoves.append(newPos)

		return possibleMoves


class Knight(_Piece):
	Abbreviation = "N"
	AbbreviationLong = "|  KNGT  "
	AbbreviationLongColored = "|--KNGT--"

	def GetPossibleMoves(self, board, prevMove):
		possibleMoves = list()

		# Up left
		newPos = (self._pos[0] - 1, self._pos[1] + 2)
		piece = board.GetPiece(newPos)
		if piece:
			if piece.Color != self._color:
				possibleMoves.append(newPos)
		else:
			if newPos[0] > -1 and newPos[0] < 8 and newPos[1] > -1 and newPos[1] < 8:
				possibleMoves.append(newPos)

		# Up right
		newPos = (self._pos[0] + 1, self._pos[1] + 2)
		piece = board.GetPiece(newPos)
		if piece:
			if piece.Color != self._color:
				possibleMoves.append(newPos)
		else:
			if newPos[0] > -1 and newPos[0] < 8 and newPos[1] > -1 and newPos[1] < 8:
				possibleMoves.append(newPos)

		return possibleMoves


class Queen(_Piece):
	Abbreviation = "Q"
	AbbreviationLong = "|  QUEN  "
	AbbreviationLongColored = "|--QUEN--"

	def GetPossibleMoves(self, board, prevMove):
		possibleMoves = list()

		# Move options like a rook
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

		# Move options like a bishop
		# Up right
		j = self._pos[1]
		for i in range(self._pos[0] + 1, 8):
			j = j + 1
			if j > 7: break
			newPos = (i, j)
			piece = board.GetPiece(newPos)
			if piece:
				if piece.Color != self._color:
					possibleMoves.append(newPos)
					break
				else:
					break
			else:
				possibleMoves.append(newPos)

		# Up Left
		j = self._pos[1]
		for i in range(self._pos[0] - 1, -1):
			j = j + 1
			if j > 7: break
			newPos = (i, j)
			piece = board.GetPiece(newPos)
			if piece:
				if piece.Color != self._color:
					possibleMoves.append(newPos)
					break
				else:
					break
			else:
				possibleMoves.append(newPos)

		# Down Right
		j = self._pos[1]
		for i in range(self._pos[0] + 1, 8):
			j = j - 1
			if j < 0: break
			newPos = (i, j)
			piece = board.GetPiece(newPos)
			if piece:
				if piece.Color != self._color:
					possibleMoves.append(newPos)
					break
				else:
					break
			else:
				possibleMoves.append(newPos)

		# Down Left
		j = self._pos[1]
		for i in range(self._pos[0] - 1, -1, -1):
			j = j - 1
			if j < 0: break
			newPos = (i, j)
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
