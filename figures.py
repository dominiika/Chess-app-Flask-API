def get_chessboard():
    """Create a chessboard"""
    letters = [num for num in range(1, 9)]
    numbers = [num for num in range(1, 9)]
    chessboard = []
    for letter in letters:
        for number in numbers:
            chessboard.append((letter, number))
    return chessboard


def field_exists(field):
    """Check if the field is present on the chessboard"""
    if 1 <= field[0] <= 8 and 1 <= field[1] <= 8:
        return True
    return False


def diagonal_moves(currentField):
    """Get possible diagonal moves"""

    letter = currentField[0]
    num = currentField[1]

    lower_right = [
        (x, y) for x, y in zip((range(letter + 1, 9)), (range(num - 1, 0, -1)))
    ]
    lower_left = [
        (x, y) for x, y in zip((range(letter - 1, 0, -1)), (range(num - 1, 0, -1)))
    ]
    upper_left = [(x, y) for x, y in zip(range(letter - 1, 0, -1), (range(num + 1, 9)))]
    upper_right = [(x, y) for x, y in zip((range(letter + 1, 9)), (range(num + 1, 9)))]

    moves = lower_left + lower_right + upper_left + upper_right
    available_moves = list(filter(field_exists, moves))

    return available_moves


def horizontal_vertical_moves(currentField):
    """Get possible horizontal and vertical moves"""

    letter = currentField[0]
    num = currentField[1]

    moves = [(letter, y) for y in range(1, 9) if (letter, y) != currentField]
    moves += [(x, num) for x in range(1, 9) if (x, num) != currentField]
    available_moves = list(filter(field_exists, moves))

    return available_moves


class Figure:
    def listAvailableMoves(self, currentField):
        raise NotImplementedError

    def validateMove(self, currentField, destField):
        raise NotImplementedError


class Pawn(Figure):
    def listAvailableMoves(self, currentField):
        """Return a list with all the possible moves"""
        moves = []

        letter = currentField[0]
        num = currentField[1]

        if num == 2:
            moves.append((letter, num + 2))
        moves.append((letter, num + 1))

        available_moves = list(filter(field_exists, moves))

        return available_moves

    def validateMove(self, currentField, destField):
        """Check if a given move is possible"""
        return destField in self.listAvailableMoves(currentField)


class Rook(Figure):
    def listAvailableMoves(self, currentField):
        """Return a list with all the possible moves"""

        available_moves = horizontal_vertical_moves(currentField)
        return available_moves

    def validateMove(self, currentField, destField):
        """Check if a given move is possible"""

        return destField in self.listAvailableMoves(currentField)


class Knight(Figure):
    def listAvailableMoves(self, currentField):
        """Return a list with all the possible moves"""

        letter = currentField[0]
        num = currentField[1]

        distances = [
            (-2, -1),
            (-2, 1),
            (2, -1),
            (2, +1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
        ]
        moves = list(
            map(lambda distance: (letter + distance[0], num + distance[1]), distances)
        )
        available_moves = list(filter(field_exists, moves))

        return available_moves

    def validateMove(self, currentField, destField):
        """Check if a given move is possible"""

        return destField in self.listAvailableMoves(currentField)


class Bishop(Figure):
    def listAvailableMoves(self, currentField):
        """Return a list with all the possible moves"""

        available_moves = diagonal_moves(currentField)
        return available_moves

    def validateMove(self, currentField, destField):
        """Check if a given move is possible"""

        return destField in self.listAvailableMoves(currentField)


class Queen(Figure):
    def listAvailableMoves(self, currentField):
        """Return a list with all the possible moves"""

        available_moves = diagonal_moves(currentField) + horizontal_vertical_moves(
            currentField
        )
        return available_moves

    def validateMove(self, currentField, destField):
        """Check if a given move is possible"""

        return destField in self.listAvailableMoves(currentField)


class King(Figure):
    def listAvailableMoves(self, currentField):
        """Return a list with all the possible moves"""

        letter = currentField[0]
        num = currentField[1]

        distances = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
        ]
        moves = list(
            map(lambda distance: (letter + distance[0], num + distance[1]), distances)
        )
        available_moves = list(filter(field_exists, moves))

        return available_moves

    def validateMove(self, currentField, destField):
        """Check if a given move is possible"""

        return destField in self.listAvailableMoves(currentField)
