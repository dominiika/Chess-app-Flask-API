from app import app
import unittest


class FlaskTests(unittest.TestCase):
    def setUp(self):
        """Create a test client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_get_possible_moves_status_code_ok(self):
        """Test if the status code is 200 if the user enters an existing figure and existing field"""
        result = self.app.get("/api/v1/queen/a2")
        self.assertEqual(result.status_code, 200)

    def test_get_possible_moves_status_code_not_found(self):
        """Test if the status code is 404 if the user enters a non-existing figure"""
        result = self.app.get("/api/v1/queennn/a2")
        self.assertEqual(result.status_code, 404)

    def test_get_possible_moves_status_code_conflict(self):
        """Test if the status code is 409 if the user enters a square which is not present on the chessboard"""
        result = self.app.get("/api/v1/queen/a10")
        self.assertEqual(result.status_code, 409)

    def test_get_possible_moves_incorrect_square_conflict(self):
        """Test if the status code is 409 if the user enters an incorrect value in the currentField parameter"""
        result = self.app.get("/api/v1/queen/a")
        self.assertEqual(result.status_code, 409)

    def test_check_if_move_is_possible_status_code_ok(self):
        """Test if the status code is 200 if the user enters an existing figure and existing fields"""
        result = self.app.get("/api/v1/queen/a2/a8")
        self.assertEqual(result.status_code, 200)

    def test_check_if_move_is_possible_status_code_not_found(self):
        """Test if the status code is 404 if the user enters non-existing figure"""
        result = self.app.get("/api/v1/queennn/a2/a8")
        self.assertEqual(result.status_code, 404)

    def test_check_if_move_is_possible_status_code_conflict(self):
        """Test if the status code is 409 if the user enters a square which is not present on the chessboard"""
        result = self.app.get("/api/v1/queen/a1/a10")
        self.assertEqual(result.status_code, 409)

    def test_check_if_move_is_possible_incorrect_square_conflict(self):
        """Test if the status code is 409 if the user enters incorrect values
        in the currentField or destField parameter"""
        result = self.app.get("/api/v1/queen/a1/b")
        self.assertEqual(result.status_code, 409)


if __name__ == "__main__":
    unittest.main()
