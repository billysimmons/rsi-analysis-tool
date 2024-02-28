## IMPORTS
from tkinter import *
from tkinter import ttk
from tkcalendar import *
import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd 
import datetime as dt
import matplotlib.pyplot as plt

def calculate_rs(data, ticker, button):
    # DESCRIPTION: Will use the positive and negative difference values in closing prices
    # to get an average gain and loss value (using a moving average specified as "days") 
    # for a stock, then calculate the RSI using these values

    button.destroy()

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


def main():
    root = Tk()
    root.title("RSI PROGRAM")
    root.geometry("1000x600")
    root.configure(bg="#f0f0f0") 

    style = ttk.Style()
    style.theme_use('clam')

    info_text = "Welcome to the RSI Analysis Program!!\n"
    info_label = ttk.Label(root, text=info_text, font=("Helvetica", 14), background="#f0f0f0", foreground="#333")
    info_label.pack(pady=20)

    info2_text = "Please enter the ticker code of your stock:"
    info2_label = ttk.Label(root, text=info2_text, font=("Helvetica", 14), background="#f0f0f0", foreground="#333")
    info2_label.pack(pady=10)

    ticker_entry = ttk.Entry(root, width=30, font=("Helvetica", 12))
    ticker_entry.insert(0, "Enter Ticker Identifier")
    ticker_entry.pack(pady=10)
    ticker = ""

    info3_text = "Now enter your start date:"
    info3_label = ttk.Label(root, text=info3_text, font=("Helvetica", 14), background="#f0f0f0", foreground="#333")
    info3_label.pack(pady=10)

    start_cal = Calendar(root, selectmode="day", year=2023, month=3, mindate=dt.datetime(2018, 1, 1),
                         font=("Helvetica", 12), selectbackground="#3498db", selectforeground="white",
                         background="white", foreground="black", bordercolor="black", bd=2, relief="solid", dayforeground="black",
                         date_pattern="mm/dd/yyyy")
    start_cal.pack(pady=10)
    start = "01/01/2023"

    def handle_confirm():
        nonlocal ticker, start # Allows changing of variables in parent function

        ## Handle Stock Data
        ticker = ticker_entry.get()
        start_str = start_cal.get_date()
        start = dt.datetime.strptime(start_str, "%m/%d/%Y")
        end = dt.datetime.now() 

        ## Get yahoo data
        yf.pdr_override() # Overide data output for yahoo finance due to API change (TypeError: string indices must be integers)
        data = pdr.get_data_yahoo(ticker, start=start, end=end) # Yahoo finance request 
        
        ## Graph Button 
        graph_button = Button(root, text="Graph Now!", 
                            command=lambda: calculate_rs(data, ticker, graph_button))
        graph_button.configure(bg="white")
        graph_button.pack()

    confirm_button = ttk.Button(root, text="Confirm Ticker", command=handle_confirm)
    confirm_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
