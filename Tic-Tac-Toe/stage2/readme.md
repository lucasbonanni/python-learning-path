# Description

However, our game should show the field in an "intermediate" states too. Let's try to visualize different combinations that the user will determine from the input. It is also important to think about the interface and set boundaries for our field.
Objectives

In this stage, you should write a program that:

    Reads 9 symbols from the input and writes an appropriate 3x3 field. Elements of the field can contain only 'X', 'O' and '_' symbols.
    Sets the field to a specific format, i.e. the field should start and end with ---------, all lines in between should start and end with '|' symbol and everything in the middle should be separated with a single space.

# Examples

The examples below show how your output should look.
The greater-than symbol followed by space (> ) represents the user input. Note that it's not the part of the input.

## Example 1:

    Enter cells: > O_OXXO_XX
    ---------
    | O _ O |
    | X X O |
    | _ X X |
    ---------

## Example 2:

    Enter cells: > OXO__X_OX
    ---------
    | O X O |
    | _ _ X |
    | _ O X |
    ---------

## Example 3:

    Enter cells: > _XO__X___
    ---------
    | _ X O |
    | _ _ X |
    | _ _ _ |
    ---------