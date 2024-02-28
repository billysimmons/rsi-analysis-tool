# RSI Analysis Program

DESCRIPTION: This program is a Relative Strength Index Tool.

OVERVIEW: The user enters a ticker code for a stock (e.g. GLD, TSLA) and a start date, then the program will use yahoo finance to retrieve the RSI data
for that stock, from the start date provided, to the current date. The program will then give the user that information in a graphical representation using the matplotlib library. 

  
Libraries:  
- tkinter
- tkcalendar
- yfinance (yahoo finance)
- pandas
- pandas_datareader
- datetime
- matplotlib.pyplot

Key Definitions and Concepts
- Relative Strength Index (RSI): Momentum oscillator that measures the speed and change of price movements
- Relative strength: Type of momentum investing where investors select investments that have been outperforming their market or benchmark
- RSI Formula: RSI = 100.0 - (100.0 / (1.0 + Relative Strength))
- RS Formula: RS = average gain / average loss
- Moving Average: Average change overtime to determine trend direction 
- Over bought/ sold lines: RSI is considered overbought when above 70 and oversold when below 30.

Sudoku Puzzle 🧩
=============

Sudoku puzzle solver and playable console game. Created using .NET and C#.

Features
--------

-   Solver: A Sudoku solver using a recursive backtracking algorithm.
    - The recursive backtracking algorithm systematically fills Sudoku cells, exploring valid digit choices for each empty cell, backtracking when necessary until a solution is found or all possibilities are exhausted.
-   Board Creation: Boards are created based on the difficulty level provided by the user.
    - First, random numbers are placed throughout the board to ensure each puzzle created differs from the last. The board is then solved, where a set amount of cells is set back to 0 based on the difficulty level. 
-   Game Mode: An interactive game mode that allows you to play the generated Sudoku puzzles.
    - The board is interacted with via coordinates, where 0's represent empty cells. Instructions are included to assist users in playing the game.
-   Cell Checking: Cell checking to identify invalid cells by comparing them to the solved board.

Getting Started
---------------

### Prerequisites

-   .NET SDK installed on your machine.

### Installation

1.  Clone the repository:

    `git clone https://github.com/billysimmons/sudoku-puzzle.git`

3.  Navigate to the project directory:

    `cd sudoku-puzzle`
    
    `cd SudokuPuzzle`

5.  Build the project:

    `dotnet build`

7.  Run the application:

    `dotnet run`
