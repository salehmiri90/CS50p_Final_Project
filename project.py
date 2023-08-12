import random

def main():
    print("Welcome to Backgammon!")
    play_game()

def play_game():
    board = initialize_board()
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        move = get_move(current_player, board)
        make_move(board, move, current_player)
        if check_winner(board, current_player):
            print("Player", current_player, "wins!")
            game_over = True
        else:
            current_player = switch_player(current_player)

def initialize_board():
    return {
        1: ["X", "X", "X", "X", "X"],
        6: ["O", "O", "O", "O", "O"],
        8: ["O", "O", "O", "O", "O"],
        12: ["X", "X", "X", "X", "X"],
        13: ["O", "O", "O", "O", "O"],
        17: ["X", "X", "X", "X", "X"],
        19: ["X", "X", "X", "X", "X"],
        24: ["O", "O", "O", "O", "O"]
    }

def print_board(board):
    for i in range(24, 0, -1):
        if i in board:
            print("|".join(board[i]), end=" ")
        else:
            print("| |", end=" ")
        if i % 6 == 1:
            print()

def get_move(player, board):
    roll1, roll2 = roll_dice()
    print("Player", player, "rolls", roll1, "and", roll2)
    moves = []
    for roll in [roll1, roll2]:
        if can_move(player, board, roll):
            move = input("Enter move for roll " + str(roll) + ": ")
            moves.append((move, roll))
        else:
            moves.append(None)
    return moves

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def can_move(player, board, roll):
    for i in range(1, 25):
        if i in board and board[i][0] == player:
            if i + roll in board:
                if len(board[i+roll]) <= 5 or board[i+roll][0] == player:
                    return True
            else:
                return True
    return False

def make_move(board, moves, player):
    for move in moves:
        if move:
            src, dest = move[0].split("-")
            src, dest = int(src), int(dest)
            if src in board and board[src][0] == player:
                if dest in board:
                    if len(board[dest]) <= 5 or board[dest][0] == player:
                        board[src].pop(0)
                        board[dest].insert(0, player)
                else:
                    board[src].pop(0)
                    board[dest] = [player]

def check_winner(board, player):
    return all(cell == player for cell in board[1][:5]) or all(cell == player for cell in board[24][:5])

def switch_player(player):
    return "O" if player == "X" else "X"