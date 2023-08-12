# Backgammon GAME

  ### Video Demo: https://youtu.be/9SShWprH3qQ

  ## Description:
   This game is allows two players to play the game. The game is set up on a board with 24 triangles known as points. Each player starts with 15 checkers, and the objective of the game is to get all of one's pieces off the board as quickly as possible. The legal moves are determined by rolling dice at the start of each player's turn.
   
   The program consists of a main function and 9 additional functions namely play_game, initialize_board, print_board, get_move, roll_dice, can_move, make_move, check_winner and switch_player.
  
  ### Project Requirements:
  &#9745; Your project must be implemented in Python.

  &#9745; Your project must have a main function and at least three other functions, each of which must be accompanied by tests that can be executed with pytest.

  &#9745; Your main function must be in a file called project.py, which should be in the “root” (i.e., top-level folder) of your project.

  &#9745; Your 3 required custom functions other than main must also be in project.py and defined at the same indentation level as main (i.e., not nested under any classes or functions).

  &#9745; Your test functions must be in a file called test_project.py, which should also be in the “root” of your project. Be sure they have the same name as your custom functions, prepended with test_ (test_custom_function, for example, where custom_function is a function you’ve implemented in project.py).

&#9745; You are welcome to implement additional classes and functions as you see fit beyond the minimum requirement.

&#9745; Implementing your project should entail more time and effort than is required by each of the course’s problem sets.

&#9745; Any pip-installable libraries that your project requires must be listed, one per line, in a file called requirements.txt in the root of your project.

  ### Function Definition:

  &#9745; main(): This function is the entry point of the program and prints a welcome message. It then calls the play_game() function to start the game.
  
  &#9745; play_game(): This function initializes the board, sets the current player to "X", and starts a loop that continues until the game is over. In each iteration of the loop, it prints the current state of the board, gets the move for the current player using the get_move() function, makes the move using the make_move() function, and checks if the game is over using the check_winner() function. If the game is over, it prints the winner and sets the game_over flag to True. Otherwise, it switches the current player using the switch_player() function.
  
  &#9745; initialize_board(): This function returns a dictionary that represents the initial state of the board. Each key in the dictionary represents a point on the board, and the value is a list of checkers on that point. The first element of the list represents the color of the checkers on that point.
  
  &#9745; print_board(board): This function takes a board dictionary as input and prints the current state of the board to the console.
  
  &#9745; get_move(player, board): This function takes the current player and the board dictionary as input and returns a list of moves for the player. It rolls two dice using the roll_dice() function and prompts the player to enter a move for each roll. It checks if the move is valid using the can_move() function and returns a list of valid moves.
  
  &#9745; roll_dice(): This function returns two random integers between 1 and 6, which represent the values of two dice.
  
  &#9745; can_move(player, board, roll): This function takes the current player, the board dictionary, and the value of a roll as input and returns True if the player can make a move with the given roll, and False otherwise.
  
  &#9745; make_move(board, moves, player): This function takes the board dictionary, a list of moves, and the current player as input and updates the board according to the moves made by the player.
  
  &#9745; check_winner(board, player): This function takes the board dictionary and the current player as input and returns True if the player has won the game, and False otherwise.
  
  &#9745; switch_player(player): This function takes the current player as input and returns the other player.
  
  ### Test the GAME:

  The code also includes a test file test_game.py that contains five test functions for the initialize_board(), roll_dice(), can_move(), make_move(), and check_winner() functions. These tests can be executed with pytest.
  
  To run the code, save the game.py and test_game.py files in the same directory and run the game.py file using a Python interpreter. The game will start and prompt the players to enter their moves. The tests can be executed by running the pytest command in the terminal while in the directory containing the test_game.py file.
