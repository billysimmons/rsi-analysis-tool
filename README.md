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
