#  What you'll do in this stage 1/5: Initial setup 

Description

In this project, you'll write a game called Tic-Tac-Toe that you can play with your computer. The computer will have three levels of difficulty - easy, medium, hard.

But, for starters, let's write a program that knows how to work with coordinates and determine the state of the game.

Suppose the bottom left cell has the coordinates (1, 1) and the top right cell has the coordinates (3, 3) like in this table:

    (1, 3) (2, 3) (3, 3)
    (1, 2) (2, 2) (3, 2)
    (1, 1) (2, 1) (3, 1)

The program should ask to enter the coordinates where the user wants to make a move.

Keep in mind that the first coordinate goes from left to right and the second coordinate goes from bottom to top. Also, notice that coordinates start with 1 and can be 1, 2 or 3.

But what if the user enters incorrect coordinates? The user could enter symbols instead of numbers or enter coordinates representing occupied cells. You need to prevent all of that by checking a user's input and catching possible exceptions.
Objectives

The program should work in the following way:

    Get the 3x3 field from the first input line (it contains 9 symbols containing X, O and _, the latter means it's an empty cell),
    Output this 3x3 field with cells before the user's move,
    Then ask the user about his next move,
    Then the user should input 2 numbers that represent the cell on which user wants to make his X or O. (9 symbols representing the field would be on the first line and these 2 numbers would be on the second line of the user input). Since the game always starts with X, if the number of X's and O's on the field is the same, the user should make a move with X, and if X's is one more than O's, then the user should make a move with O.
    Analyze user input and show messages in the following situations:
    •"This cell is occupied! Choose another one!" - if the cell is not empty;
    •"You should enter numbers!" - if the user enters other symbols;
    •"Coordinates should be from 1 to 3!" - if the user goes beyond the field.
    Then output the table including the user's most recent move.
    Then output the state of the game.

Possible states:

    "Game not finished" - when no side has a three in a row but the field has empty cells;
    "Draw" - when no side has a three in a row and the field has no empty cells;
    "X wins" - when the field has three X in a row;
    "O wins" - when the field has three O in a row;

If the user input wrong coordinates, the program should keep asking until the user enters coordinate that represents an empty cell on the field and after that output the field with that move. You should output the field only 2 times - before the move and after a legal move.
Examples

The examples below show how your program should work.
The greater-than symbol followed by space (> ) represents the user input. Notice that it's not the part of the input.

Example 1:

    Enter cells: > _XXOO_OX_
    ---------
    |   X X |
    | O O   |
    | O X   |
    ---------
    Enter the coordinates: > 1 1
    This cell is occupied! Choose another one!
    Enter the coordinates: > one
    You should enter numbers!
    Enter the coordinates: > one three
    You should enter numbers!
    Enter the coordinates: > 4 1
    Coordinates should be from 1 to 3!
    Enter the coordinates: > 1 3
    ---------
    | X X X |
    | O O   |
    | O X   |
    ---------
    X wins

Example 2:

    Enter cells: > XX_XOXOO_
    ---------
    | X X   |
    | X O X |
    | O O   |
    ---------
    Enter the coordinates: > 3 1
    ---------
    | X X   |
    | X O X |
    | O O O |
    ---------
    O wins

Example 3:

    Enter cells: > OX_XOOOXX
    ---------
    | O X   |
    | X O O |
    | O X X |
    ---------
    Enter the coordinates: > 3 3
    ---------
    | O X X |
    | X O O |
    | O X X |
    ---------
    Draw

Example 4:

    Enter cells: >  _XO_OX___
    ---------
    |   X O |
    |   O X |
    |       |
    ---------
    Enter the coordinates: > 1 1
    ---------
    |   X O |
    |   O X |
    | X     |
    ---------
    Game not finished