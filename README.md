# Sodoku-Solver

Sodoku Solver

Author: Dylan Straub

This is a Sodoku solver written in Python3 with no dependencies, demonstrating
object oriented programming and recursion.

Inspired by a YouTube lecture series by Richard Buckland, UNSW
https://www.youtube.com/user/BucklandRichard/videos

This program consists of three classes:

    Tile:   models an indivial square of the Sodoku board
            aware of its own row/column position and value

    Board:  a collection of 81 tile objects in a list
            able to check if a move is valid

    Solve:  recursive solving logic
            must instantiate with a board object
            a solution is generated upon creation

The Sodoku board is represented as a list indexed in a left-to-right, top-to-bottom order.

A valid input string is an 81 character string indexed in this manner.
All blank spaces shall be represented by the ```.``` character.

For example, the the following board:
```
  ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
  ║   │   │   ║ 9 │   │   ║   │ 2 │   ║
  ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
  ║   │   │ 3 ║   │   │   ║ 7 │ 9 │   ║
  ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
  ║ 8 │   │   ║   │   │ 6 ║ 5 │   │   ║
  ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
  ║ 6 │ 7 │   ║   │   │ 3 ║   │   │   ║
  ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
  ║   │   │ 1 ║   │   │   ║ 8 │   │   ║
  ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
  ║   │   │   ║ 1 │ 5 │ 4 ║   │   │ 3 ║
  ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
  ║ 7 │   │   ║   │ 4 │   ║   │   │   ║
  ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
  ║   │   │   ║   │ 7 │ 9 ║   │   │ 1 ║
  ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
  ║ 3 │   │ 8 ║   │   │ 2 ║   │   │   ║
  ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝
```
would be represented by the following input string:
```...9...2...3...79.8....65..67...3.....1...8.....154..37...4........79..13.8..2```

You are expected to provide a valid and solvable input.

This code will run as-is to produce a solution to the example above
every attemptted solution will be printed on the console to visualize the
recursive mechanism in action.
