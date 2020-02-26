from figures import Pawn, Rook, Knight, Bishop, Queen, King, get_chessboard
from app import convert_to_tuple
import unittest


class PawnTests(unittest.TestCase):
    def setUp(self):
        self.pawn = Pawn()

    def test_chessboard_has_sixty_four_squares(self):
        """Test that the chessboard contains 64 squares"""
        chessboard = get_chessboard()
        self.assertEqual(len(chessboard), 64)

    # Tests for Pawn.listAvailableMoves
    def test_pawn_can_move_two_squares(self):
        """Test that pawn can move either one or two squares if it's standing in row B"""
        current_field = convert_to_tuple("b2")
        available_moves = self.pawn.listAvailableMoves(current_field)
        self.assertIn(convert_to_tuple("b3"), available_moves)
        self.assertIn(convert_to_tuple("b4"), available_moves)

    def test_pawn_can_move_one_square(self):
        """Test that pawn can move only one square if it's not standing in row B"""
        current_field = convert_to_tuple("a6")
        available_moves = self.pawn.listAvailableMoves(current_field)
        self.assertIn(convert_to_tuple("a7"), available_moves)
        self.assertNotIn(convert_to_tuple("a8"), available_moves)

    def test_pawn_cannot_move_to_other_squares(self):
        """Test that pawn cannot move to squares which are not permitted for this figure"""
        current_field = convert_to_tuple("a6")
        available_moves = self.pawn.listAvailableMoves(current_field)
        self.assertNotIn(convert_to_tuple("b6"), available_moves)

    # Tests for Pawn.validateMove
    def test_pawn_can_move_to_dest_field(self):
        """Test that pawn can move to one of the available squares permitted for this figure"""
        current_field = convert_to_tuple("a3")
        dest_feld = convert_to_tuple("a4")
        move_is_possible = self.pawn.validateMove(current_field, dest_feld)
        self.assertTrue(move_is_possible)

    def test_pawn_cannot_move_to_non_existing_square(self):
        """Test that pawn cannot move to squares which are not present on the chessboard"""
        current_field = convert_to_tuple("a8")
        dest_feld = convert_to_tuple("a9")
        move_is_possible = self.pawn.validateMove(current_field, dest_feld)
        self.assertFalse(move_is_possible)


class RookTests(unittest.TestCase):
    def setUp(self):
        self.rook = Rook()

    # Tests for Rook.listAvailableMoves
    def test_rook_can_move_horizontally(self):
        """Test that rook can move horizontally"""
        current_field = convert_to_tuple("d3")
        available_moves = self.rook.listAvailableMoves(current_field)
        self.assertIn(convert_to_tuple("a3"), available_moves)
        self.assertIn(convert_to_tuple("h3"), available_moves)

    def test_rook_can_move_vertically(self):
        """Test that rook can move vertically"""
        current_field = convert_to_tuple("d3")
        available_moves = self.rook.listAvailableMoves(current_field)
        self.assertIn(convert_to_tuple("d1"), available_moves)
        self.assertIn(convert_to_tuple("d8"), available_moves)

    def test_rook_cannot_move_to_other_squares(self):
        """Test that rook cannot move to squares which are not permitted for this figure"""
        current_field = convert_to_tuple("d3")
        available_moves = self.rook.listAvailableMoves(current_field)
        self.assertNotIn(convert_to_tuple("e4"), available_moves)

    # Tests for Rook.validateMove
    def test_rook_can_move_to_dest_field(self):
        """Test that rook can move to one of the available squares permitted for this figure"""
        current_field = convert_to_tuple("a5")
        dest_feld = convert_to_tuple("a8")
        move_is_possible = self.rook.validateMove(current_field, dest_feld)
        self.assertTrue(move_is_possible)

    def test_rook_cannot_move_to_non_existing_square(self):
        """Test that rook cannot move to squares which are not present on the chessboard"""
        current_field = convert_to_tuple("a1")
        dest_feld = convert_to_tuple("a9")
        move_is_possible = self.rook.validateMove(current_field, dest_feld)
        self.assertFalse(move_is_possible)


class KnightTests(unittest.TestCase):
    def setUp(self):
        self.knight = Knight()

    # Tests for Knight.listAvailableMoves
    def test_knight_can_move_in_l_shape(self):
        """Test that knight can move in the shape resembling the letter L"""
        current_field = convert_to_tuple("d4")
        available_moves = self.knight.listAvailableMoves(current_field)
        self.assertIn(convert_to_tuple("e6"), available_moves)
        self.assertIn(convert_to_tuple("c2"), available_moves)

    def test_knight_cannot_move_to_other_squares(self):
        """Test that knight cannot move to squares which are not permitted for this figure"""
        current_field = convert_to_tuple("d4")
        available_moves = self.knight.listAvailableMoves(current_field)
        self.assertNotIn(convert_to_tuple("e4"), available_moves)

    # Tests for Knight.validateMove
    def test_knight_can_move_to_dest_field(self):
        """Test that knight can move to one of the available squares permitted for this figure"""
        current_field = convert_to_tuple("c3")
        dest_feld = convert_to_tuple("e2")
        move_is_possible = self.knight.validateMove(current_field, dest_feld)
        self.assertTrue(move_is_possible)

    def test_knight_cannot_move_to_non_existing_square(self):
        """Test that knight cannot move to squares which are not present on the chessboard"""
        current_field = convert_to_tuple("c7")
        dest_feld = convert_to_tuple("b9")
        move_is_possible = self.knight.validateMove(current_field, dest_feld)
        self.assertFalse(move_is_possible)


class BishopTests(unittest.TestCase):
    def setUp(self):
        self.bishop = Bishop()

    # Tests for Bishop.listAvailableMoves
    def test_rook_can_move_diagonally(self):
        """Test that bishop can move diagonally"""
        current_field = convert_to_tuple("d4")
        available_moves = self.bishop.listAvailableMoves(current_field)
        self.assertIn(convert_to_tuple("a1"), available_moves)
        self.assertIn(convert_to_tuple("a7"), available_moves)

    def test_bishop_cannot_move_to_other_squares(self):
        """Test that bishop cannot move to squares which are not permitted for this figure"""
        current_field = convert_to_tuple("d4")
        available_moves = self.bishop.listAvailableMoves(current_field)
        self.assertNotIn(convert_to_tuple("c4"), available_moves)

    # Tests for Bishop.validateMove
    def test_bishop_can_move_to_dest_field(self):
        """Test that bishop can move to one of the available squares permitted for this figure"""
        current_field = convert_to_tuple("e1")
        dest_feld = convert_to_tuple("h4")
        move_is_possible = self.bishop.validateMove(current_field, dest_feld)
        self.assertTrue(move_is_possible)

    def test_bishop_cannot_move_to_non_existing_square(self):
        """Test that bishop cannot move to squares which are not present on the chessboard"""
        current_field = convert_to_tuple("c4")
        dest_feld = convert_to_tuple("h9")
        move_is_possible = self.bishop.validateMove(current_field, dest_feld)
        self.assertFalse(move_is_possible)


class QueenTests(unittest.TestCase):
    def setUp(self):
        self.queen = Queen()

    # Tests for Queen.listAvailableMoves
    def test_queen_can_move_horizontally(self):
        """Test that queen can move horizontally"""
        current_field = convert_to_tuple("d3")
        available_moves = self.queen.listAvailableMoves(current_field)
        self.assertIn(convert_to_tuple("a3"), available_moves)
        self.assertIn(convert_to_tuple("h3"), available_moves)

    def test_queen_can_move_vertically(self):
        """Test that queen can move vertically"""
        current_field = convert_to_tuple("d3")
        available_moves = self.queen.listAvailableMoves(current_field)
        self.assertIn(convert_to_tuple("d1"), available_moves)
        self.assertIn(convert_to_tuple("d8"), available_moves)

    def test_queen_can_move_diagonally(self):
        """Test that queen can move diagonally"""
        current_field = convert_to_tuple("d4")
        available_moves = self.queen.listAvailableMoves(current_field)
        self.assertIn(convert_to_tuple("a1"), available_moves)
        self.assertIn(convert_to_tuple("a7"), available_moves)

    def test_queen_cannot_move_to_other_squares(self):
        """Test that queen cannot move to squares which are not permitted for this figure"""
        current_field = convert_to_tuple("d3")
        available_moves = self.queen.listAvailableMoves(current_field)
        self.assertNotIn(convert_to_tuple("a4"), available_moves)

    # Tests for Queen.validateMove
    def test_queen_can_move_to_dest_field(self):
        """Test that queen can move to one of the available squares permitted for this figure"""
        current_field = convert_to_tuple("d5")
        dest_feld = convert_to_tuple("d1")
        move_is_possible = self.queen.validateMove(current_field, dest_feld)
        self.assertTrue(move_is_possible)

    def test_queen_cannot_move_to_non_existing_square(self):
        """Test that queen cannot move to squares which are not present on the chessboard"""
        current_field = convert_to_tuple("a1")
        dest_feld = convert_to_tuple("a9")
        move_is_possible = self.queen.validateMove(current_field, dest_feld)
        self.assertFalse(move_is_possible)


class KingTests(unittest.TestCase):
    def setUp(self):
        self.king = King()

    # Tests for King.listAvailableMoves
    def test_king_can_move_one_square_horizontally(self):
        """Test that king can move only one square horizontally"""
        current_field = convert_to_tuple("d3")
        available_moves = self.king.listAvailableMoves(current_field)
        self.assertIn(convert_to_tuple("c3"), available_moves)
        self.assertIn(convert_to_tuple("e3"), available_moves)

    def test_king_can_move_one_square_vertically(self):
        """Test that king can move only one square vertically"""
        current_field = convert_to_tuple("d3")
        available_moves = self.king.listAvailableMoves(current_field)
        self.assertIn(convert_to_tuple("d2"), available_moves)
        self.assertIn(convert_to_tuple("d4"), available_moves)

    def test_king_can_move_one_square_diagonally(self):
        """Test that king can move diagonally"""
        current_field = convert_to_tuple("d4")
        available_moves = self.king.listAvailableMoves(current_field)
        self.assertIn(convert_to_tuple("e4"), available_moves)
        self.assertIn(convert_to_tuple("c4"), available_moves)

    def test_king_cannot_move_more_than_one_square(self):
        """Test that king cannot move more than one square"""
        current_field = convert_to_tuple("d4")
        available_moves = self.king.listAvailableMoves(current_field)
        self.assertNotIn(convert_to_tuple("f6"), available_moves)
        self.assertNotIn(convert_to_tuple("b6"), available_moves)

    # Tests for King.validateMove
    def test_king_can_move_to_dest_field(self):
        """Test that king can move to one of the available squares permitted for this figure"""
        current_field = convert_to_tuple("g5")
        dest_feld = convert_to_tuple("g6")
        move_is_possible = self.king.validateMove(current_field, dest_feld)
        self.assertTrue(move_is_possible)

    def test_king_cannot_move_to_non_existing_square(self):
        """Test that king cannot move to squares which are not present on the chessboard"""
        current_field = convert_to_tuple("a8")
        dest_feld = convert_to_tuple("a9")
        move_is_possible = self.king.validateMove(current_field, dest_feld)
        self.assertFalse(move_is_possible)


if __name__ == "__main__":
    unittest.main()
