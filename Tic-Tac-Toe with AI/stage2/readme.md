# Description

Now it is time to make a working game. Let's create our first opponent! In this version of the program, the user will be playing as X, and the "easy" level computer will be playing as O. This will be our first small step to the AI!

Let's make it so that at this level the computer will make random moves. This level will be perfect for those who play this game for the first time! Well, though... You can create a level of difficulty that will always give in and never win the game. You can implement such a level along with "easy" level, if you want, but it will not be tested.
## Objectives

In this stage you should implement the following:

    When starting the program, an empty field should be displayed.
    The first to start the game should be the user as X. The program should ask the user to enter the cell coordinates.
    Next the computer should make its move as O. And so on until someone will win or there will be a draw.
    At the very end of the game you need to print the final result of the game.

## Example

The example below shows how your program should work.
The greater-than symbol followed by space (> ) represents the user input. Notice that it's not the part of the input.

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
    Making move level "easy"
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
    Making move level "easy"
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
    Making move level "easy"
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