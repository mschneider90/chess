class Piece(object):
    def __init__(self):
        pass

    def getName(self):
        """ Get the full name of this piece """
        raise NotImplementedError()

    def getSymbol(self):
        """ Get the symbol of this piece """
        raise NotImplementedError()

    def getMoves(self, board):
        """ Given a Board, return the potential moves for this piece """
        raise NotImplementedError()

class Pawn(Piece):
    def __init__(self):
        super(self, Pawn).__init__()

    def getName(self):
        return "pawn"

    def getSymbol(self):
        return "p"

    def getMoves(self, board):
        return None

class Knight(Piece):
    def __init__(self):
        super(self, Knight).__init__()

    def getName(self):
        return "knight"

    def getSymbol(self):
        return "n"

    def getMoves(self, board):
        return None

class Rook(Piece):
    def __init__(self):
        super(self, Rook).__init__()

    def getName(self):
        return "rook"

    def getSymbol(self):
        return "r"

    def getMoves(self, board):
        return None

class Bishop(Piece):
    def __init__(self):
        super(self, Bishop).__init__()

    def getName(self):
        return "bishop"

    def getSymbol(self):
        return "b"

    def getMoves(self, board):
        return None

class Queen(Piece):
    def __init__(self):
        super(self, Queen).__init__()

    def getName(self):
        return "queen"

    def getSymbol(self):
        return "q"

    def getMoves(self, board):
        return None


class King(Piece):
    def __init__(self):
        super(self, Queen).__init__()

    def getName(self):
        return "king"

    def getSymbol(self):
        return "k"

    def getMoves(self, board):
        return None