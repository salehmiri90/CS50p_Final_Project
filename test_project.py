import game
import pytest

def test_initialize_board():
    board = game.initialize_board()
    assert len(board) == 7
    assert all(len(board[i]) == 5 for i in board)

def test_roll_dice():
    roll1, roll2 = game.roll_dice()
    assert 1 <= roll1 <= 6
    assert 1 <= roll2 <= 6

def test_can_move():
    board = {
        1: ["X", "X", "X", "X", "X"],
        6: ["O", "O", "O", "O", "O"],
        8: ["O", "O", "O", "O", "O"],
        12: ["X", "X", "X", "X", "X"],
        13: ["O", "O", "O", "O", "O"],
        17: ["X", "X", "X", "X", "X"],
        19: ["X", "X", "X", "X", "X"],
        24: ["O", "O", "O", "O", "O"]
    }
    assert game.can_move("X", board, 6) == True
    assert game.can_move("X", board, 5) == False

def test_make_move():
    board = {
        1: ["X", "X", "X", "X", "X"],
        6: ["O", "O", "O", "O", "O"],
        8: ["O", "O", "O", "O", "O"],
        12: ["X", "X", "X", "X", "X"],
        13: ["O", "O", "O", "O", "O"],
        17: ["X", "X", "X", "X", "X"],
        19: ["X", "X", "X", "X", "X"],
        24: ["O", "O", "O", "O", "O"]
    }
    moves = [("1-3", 1), ("6-5", 5)]
    game.make_move(board, moves, "X")
    assert board[1] == ["X", "X"]
    assert board[3] == ["X", "X", "X"]
    assert board[5] == ["X"]
    assert board[6] == ["O", "O", "O", "O", "O"]

def test_check_winner():
    board = {
        1: ["X", "X", "X", "X", "X"],
        6: ["O", "O", "O", "O", "O"],
        8: ["O", "O", "O", "O", "O"],
        12: ["X", "X", "X", "X", "X"],
        13: ["O", "O", "O", "O", "O"],
        17: ["X", "X", "X", "X", "X"],
        19: ["X", "X", "X", "X", "X"],
        24: ["O", "O", "O", "O", "O"]
    }
    assert game.check_winner(board, "X") == True
    assert game.check_winner(board, "O") == False

def test_switch_player():
    assert game.switch_player("X") == "O"
    assert game.switch_player("O") ==