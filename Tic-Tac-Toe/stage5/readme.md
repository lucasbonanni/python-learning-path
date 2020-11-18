# Description

We are at the finish line! But playing alone is not so interesting, is it? Let's combine all our success from the past stages and get the Tic-Tac-Toe with the ability to play from the beginning (empty field) to the result (win or draw).

Now it is time to make a working game!

In the last stage, make it so you can play a full game with a friend. The first one of you moves as X, and then the other one moves as O.
Objectives

In this stage, you should write a program that:

    Prints an empty field at the beginning of the game.
    Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness, and shows a field with the changes if everything is ok.
    Ends the game when someone wins or there is a draw.

You need to output the final result after the end of the game.

Good luck gaming!
## Example

The example below shows how your program should work.
The greater-than symbol followed by space (> ) represents the user input. Note that it's not part of the input.

    ---------
    |       |
    |       |
    |       |
    ---------
    Enter the coordinates: > 2 2
    ---------
    |       |
    |   X   |
    |       |
    ---------
    Enter the coordinates: > 2 2
    This cell is occupied! Choose another one!
    Enter the coordinates: > two two
    You should enter numbers!
    Enter the coordinates: > 1 4
    Coordinates should be from 1 to 3!
    Enter the coordinates: > 1 3
    ---------
    | O     |
    |   X   |
    |       |
    ---------
    Enter the coordinates: > 3 1
    ---------
    | O     |
    |   X   |
    |     X |
    ---------
    Enter the coordinates: > 1 2
    ---------
    | O     |
    | O X   |
    |     X |
    ---------
    Enter the coordinates: > 1 1
    ---------
    | O     |
    | O X   |
    | X   X |
    ---------
    Enter the coordinates: > 3 2
    ---------
    | O     |
    | O X O |
    | X   X |
    ---------
    Enter the coordinates: > 2 1
    ---------
    | O     |
    | O X O |
    | X X X |
    ---------
    X wins