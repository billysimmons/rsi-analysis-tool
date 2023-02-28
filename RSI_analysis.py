#RSI_analysis.py 

## NOTES
# Relative Strength Index (RSI): Momentum oscillator that measures the speed and change of price movements
# Relative strength: Type of momentum investing where investors select investments that have been outperforming their market or benchmark
# RSI Formula RSI = 100.0 - (100.0 / (1.0 + Relative Strength))
# Moving Average: Average change overtime to determine trend direction 
# Over bought/ sold lines: RSI is considered overbought when above 70 and oversold when below 30.


## IMPORTS
from tkinter import *
from tkcalendar import *
import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd 
import datetime as dt
import matplotlib.pyplot as plt


## CALCULATE RELATIVE STRENGTH FUNCTION ##
def calculate_rs(data, ticker, button):
    # DESCRIPTION: Will use the positive and negative difference values in closing prices
    # to get an average gain and loss value (using a moving average specified as "days") 
    # for a stock, then calculate the RSI using these values

    button.destroy() # Delete the "Graph Now!" Button

    difference = data["Adj Close"].diff(1) # Calculate adjusted close difference using the current row and previous row  
    difference.dropna(inplace=True) # Uses pandas method dropna to remove rows that contain NULL values

    positive = difference.copy() # Create a new DF for positive differences
    negative = difference.copy() # Create a new DF for negative differences

    positive[positive < 0] = 0 # All negative values become 0 and positive values stay the same
    negative[negative > 0] = 0 # All positive values become 0 and negative values stay the same

    days = 14 # Moving average timeframe 
    avg_gain = positive.rolling(window=days).mean() # Calculates the moving average based on close price using set amount of days
    avg_loss = abs(negative.rolling(window=days).mean()) # Calculates the moving average based on close price using set amount of days (made absolute to avoid negative numbers)

    ## Calculate RSI
    rs = avg_gain / avg_loss
    RSI = 100.0 - (100.0 / (1.0 + rs))

    ## Create dataframe for graphing
    combinedDF = pd.DataFrame()
    combinedDF["Adj Close"] = data["Adj Close"]
    combinedDF["RSI"] = RSI

    graph(combinedDF, ticker)


def graph(data, ticker):
    # DESCRIPTION: This function will present the RSI data gathered in a graph 
    # with over bought and over sold indicator lines

    plt.figure(figsize=(10, 6)) # Set window
    plt.plot(data.index, data["RSI"]) # Plot data (combinedDF)
    plt.title("Relative Strength Analysis of " + ticker)

    # Add over bought/sold lines
    plt.axhline(0, color="red")
    plt.axhline(10, color="yellow")
    plt.axhline(20, color="green")
    plt.axhline(30, color="black")
    plt.axhline(70, color="black")
    plt.axhline(80, color="green")
    plt.axhline(90, color="yellow")
    plt.axhline(100, color="red")

    plt.show()


## MAIN FUNCTION ##
def main():
    # DESCRIPTION: Main function for RSI program and GUI

    ## Create GUI with tkinter
    root = Tk()
    root.title("RSI PROGRAM")
    root.geometry("1000x600")

    ## Info 1 label
    info = Label(root, 
        text="""Welcome to the RSI Analysis Program!!\n\n
        RSI (Relative Strength Index):\n
        The momentum oscillator measuring speed and change of price movement\n""",
        bd=1, relief="sunken",
        width=150,
        borderwidth=0,
        font=("Helvetica", 13)) 
    info.pack(pady = 20) # Info label 1

    ## Info 2 label
    info2 = Label(root, 
        text="Please enter the ticker code of your stock, and a start date for the data",
        bd=1 ,relief="sunken",
        width=150,
        borderwidth=0,
        font = ("Helvetica", 13))
    info2.pack(pady=20) # Info Label 2

    ## Ticker 
    ticker_entry = Entry(root, width=50)
    ticker_entry.pack()
    ticker_entry.insert(0, "Enter Ticker Identifier")
    ticker = ""

    ## Start & End Date
    end = dt.datetime.now()
    start_cal = Calendar(root, selectmode="day", year=2023, month=3, mindate=dt.datetime(2018, 1, 1))
    start_cal.pack(pady=20)
    start = "01/01/2023"


    def handle_confirm():
        # DESCRIPTION: Will retrieve the values from the ticker entry box and calendar entry,
        # then will trigger the gathering of stock data using pandas datareader and yahoo fincance 
        # which then displays the graph button, that executes the calculate_rs function
        
        nonlocal ticker, start # Allows changing of variables in parent function

        ## Handle Stock Data
        ticker = ticker_entry.get()
        start_str = start_cal.get_date()
        start = dt.datetime.strptime(start_str, "%m/%d/%y")

        ## Get yahoo data
        yf.pdr_override() # Overide data output for yahoo finance due to API change (TypeError: string indices must be integers)
        data = pdr.get_data_yahoo(ticker, start=start, end=end) # Yahoo finance request 
        
        ## Graph Button 
        graph_button = Button(root, text="Graph Now!", 
            command= lambda: calculate_rs(data, ticker, graph_button)) # Call calculate_rs function passing itself as a parameter
        graph_button.pack()


    ## Confirm button 
    confirm_button = Button(root, text="Confirm Ticker", command=handle_confirm)
    confirm_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()