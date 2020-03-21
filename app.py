from flask import Flask, jsonify
import os
from figures import Pawn, Rook, Knight, Bishop, Queen, King, get_chessboard
from converters import convert_to_tuple, convert_from_tuple
from flask import make_response


app = Flask(__name__)
app.url_map.strict_slashes = False
basedir = os.path.abspath(os.path.dirname(__file__))


@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({"error": "Internal server error"}), 500)


@app.errorhandler(404)
def internal_error(error):
    return make_response(jsonify({"error": "Not found"}), 404)


@app.route("/api/v1/<chess_figure>/<current_field>", methods=["GET"])
def get_possible_moves(chess_figure, current_field):

    # Check if the user passed correct field name
    try:
        # Convert a string into a tuple of 2 integers
        current_field_tuple = convert_to_tuple(current_field.lower())
    except ValueError:
        return make_response(jsonify({"error": "Conflict"}), 409)

    # Check if the given figure exists
    try:
        figure_cls = eval(chess_figure.title())
        figure = figure_cls()
    except NameError:
        response = {
            "availableMoves": [],
            "error": "Figure does not exist.",
            "figure": chess_figure,
            "currentField": current_field.title(),
        }
        return jsonify(response), 404

    # Check if the field exists
    if current_field_tuple not in get_chessboard():
        response = {
            "availableMoves": [],
            "error": "Field does not exist.",
            "figure": chess_figure,
            "currentField": current_field.title(),
        }
        return jsonify(response), 409

    # List all the available moves
    else:

        available_moves = figure.listAvailableMoves(current_field_tuple)
        available_moves = list(map(convert_from_tuple, available_moves))

        response = {
            "availableMoves": [move.title() for move in available_moves],
            "error": None,
            "figure": chess_figure,
            "currentField": current_field.title(),
        }
        return jsonify(response), 200


@app.route("/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=["GET"])
def check_if_move_is_possible(chess_figure, current_field, dest_field):

    # Check if the user passed correct field name
    try:
        # Convert a string into a tuple of 2 integers
        current_field_tuple = convert_to_tuple(current_field.lower())
        dest_field_tuple = convert_to_tuple(dest_field.lower())
    except ValueError:
        return make_response(jsonify({"error": "Conflict"}), 409)

    # Check if the given figure exists
    try:
        figure_cls = eval(chess_figure.title())
        figure = figure_cls()
    except NameError:
        response = {
            "move": "invalid",
            "error": "Figure does not exist.",
            "figure": chess_figure,
            "currentField": current_field.title(),
            "destField": dest_field.title(),
        }
        return jsonify(response), 404

    # Check if the fields exist
    if (
        current_field_tuple not in get_chessboard()
        or dest_field_tuple not in get_chessboard()
    ):
        response = {
            "move": "invalid",
            "error": "Field does not exist.",
            "figure": chess_figure,
            "currentField": current_field.title(),
            "destField": dest_field.title(),
        }
        return jsonify(response), 409

    # Check if the move is possible
    is_possible = figure.validateMove(current_field_tuple, dest_field_tuple)

    if is_possible:
        response = {
            "move": "valid",
            "figure": chess_figure,
            "error": None,
            "currentField": current_field.title(),
            "destField": dest_field.title(),
        }
        return jsonify(response), 200

    elif not is_possible:
        response = {
            "move": "invalid",
            "figure": chess_figure,
            "error": "Current move is not permitted.",
            "currentField": current_field.title(),
            "destField": dest_field.title(),
        }
        return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)
