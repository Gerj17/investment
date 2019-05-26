import Invest.core.Core as Core
import tkinter as tk
import Invest.gui.Gui2 as Gui2
from urllib.request import urlopen as urlopen
from bs4 import BeautifulSoup as Soup
from pathlib import Path
import time

# bon = Core.Ecse("BON")
# bon.set_shares(bon.get_dashboard())


"""for key,value in bon.get_dashboard().items():
    print( key,":\n", value,"\n"*2)"""


def gui():
    """
    Creates GUI from GUI2 file
    :return: The Data to create the report in a list .
     Each group of data is a dictionary, all the dictionaries are held in a list

    """
    root = tk.Tk()

    Gui2.Block1(root)
    print("hi")

    root.mainloop()
    print("bye")

    print("finall", Gui2.reports)
    return Gui2.reports


# gui()


def create_reports():
    #  Collect Variables for report
    space = "\n"
    lines = "--------->"
    for x in gui():
        name = x.get("name")
        shares = x.get("shares")
        price = x.get("price")
        avg_div = x.get("avg_div")
        location = x.get("location")

        #print("\n"*3,type(avg_div),"n", avg_div, "\n"*3)

        #  Open file and create report
        filename = f"{ location }\{ name }.txt"


        #  calculations from Code Module
        calc = Core.Stock(shares, price, avg_div)

        with open(filename, "w") as file:
            file.write(f" {space}{lines[:-1]} Report {lines[:-1]} {space} ")
            file.write(f" {str(name).capitalize()} {space*3}")

            file.write(f" Number of stocks intended to purchase {lines} {shares} {space} ")
            file.write(f" Price of shares {lines} {price} {space} ")
            file.write(f" Average dividends based on stated number of years  {lines} {avg_div} {space*2} ")

            file.write(f" Rough Analysis of this Security {lines[:-1]}{ str(name).capitalize()} {space*2}")

            file.write(f" Transaction Fee {lines} { calc.fee()} {space} ")
            file.write(f" Total Transaction Fee {lines} { calc.total_cost()} {space} ")
            file.write(f" Cost Per Share {lines} { calc.cost_per_share()} {space} ")
            file.write(f" Cost Per Dollar {lines} { calc.cost_per_dollar()} {space} ")
            file.write(f" Average Dividend Per Dollar Invested  {lines} { calc.avg_div_per_dollar()} {space} ")
            file.write(f" Number of Years the Security Must Be held to Recapture Investment cost"
                       f"  {lines} { calc.years_required_till_return()} {space*2} ")

            file.write(f"{lines[:-1]} Over Relevant Data    {lines[:-1]} {space*2} ")
            file.write(f" Max Number of Shares for Cost Price of $35{lines} { calc.min_num_shares()} {space} ")
            file.write(f" Net Per Dollar {calc.gain_loss()[0] } {lines} { calc.gain_loss()[1] } until "
                       f"{ calc.years_required_till_return()} years later where gain = {calc.avg_div_per_dollar()}"
                       f"{space} ")






create_reports()

me = Core.Stock(20, 8.88, .08)

Core.Stock(20, 8.88, .08)

print("Fee Type:", me.fee_type(), "\n")
print("Fee:$", me.fee(), "\n")
print("total_cost:$", me.total_cost(), "\n")
print("cost_per_share:$", me.cost_per_share(), "\n")
print("cost_per_dollar:$", me.cost_per_dollar(), "\n")
print("avg_div_per_dollar:$", me.avg_div_per_dollar(), "\n")
print("years_required_till_return:", me.years_required_till_return(), "\n")
