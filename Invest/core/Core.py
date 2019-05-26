from urllib.request import urlopen as urlopen
from Invest.core.WebAccess import parse_website
from bs4 import BeautifulSoup as Soup
from pathlib import Path
import locale
import datetime


"""
def parse_website(website):
    
    Get access to the HTML of a website

    :param website: Wedsite to be parsed
    :return: parsed HTML of parameter
   
    client = urlopen(website)
    client_read = client.read()
    client.close()
    client_soup = Soup(client_read, "html.parser")
    return client_soup
"""


class Ecse:
    main_url = "http://www.ecseonline.com/historical_data/equity/"

    def __init__(self, stock_symbol, save_location=(Path(Path.home(), "Documents"))):
        self.stock = str(stock_symbol).lower()
        self.stock_info_url = str(self.main_url + self.stock + ".php")  # Site with stock general info
        self.stock_data_url = None
        self.share_authorized = None
        self.share_issued = None
        self.save = save_location

        self.page_soup = parse_website(self.stock_info_url)
        self.get_dashboard()
        # print(self.get_dashboard())

    def get_dashboard(self, ):
        """
        Gets dashboard information for symbol
        :return: dictionary with relevant pieces of data named in initialization
        """

        left_side = self.page_soup.find("table").find("tbody").find("tr").find("td").find_next_sibling("td").find("p")
        right_side = self.page_soup.find("table").find("tbody").find("tr").find("td").find_next_sibling("td").find(
            "td").find_next_sibling("td").find_all("tr")[7]

        return {'left_sec': left_side, 'right_sec': right_side}

    def set_shares(self, html):
        information = html.get('left_sec')
        print(information)


class Stock:
    """
    Make calculation on a stock based on the inputs which are the parameters
    Create a report to express the information gathered
    """

    @staticmethod
    def money_format(figure):
        return float(format(figure, ".2f"))

    def __init__(self, shares, bid_price, avg_div):
        """
        :param shares: Number of shares to purchase
        :param bid_price: highest price willing o pay for stock per stock basis
        :param avg_div: average level of dividends
        """
        self.shares = int(shares)
        self.avg_div = float(avg_div)
        self.b_price = float(bid_price)
        self.total_bid_price = float(self.shares * self.b_price)
        self.fee_type()

    #
    def min_num_shares(self):
        """

        :return: minimum amount of shares for transaction cost to be $35
        """

        formula = 35 / (self.b_price * .023)

        return int(formula)

    # Fees related  to transaction
    def fee_type(self, money=35, percentage=.023):
        """
        :return: is fee $35 or 2.3% of total share price
        """

        if self.shares > self.min_num_shares():
            return percentage
        else:
            return money

    def fee(self):
        """
        :return: monetary fee of transaction
        """
        if self.fee_type() == 35:
            return self.money_format(35)
        else:
            return self.money_format((self.total_bid_price * .023))

    def total_cost(self):
        """
        :return: sum cost of monetary transaction.
        Formula
        Sum of - total market value of shares to be purchased AND brokerage fee

        """
        return self.money_format((self.total_bid_price + self.fee()))

    # Fees Quantified for analysis purpose
    def cost_per_share(self):
        """

        :return: cost of each share based on the total fee paid for transaction.
        Formula:
         quotient of - transaction fee AND number of shares to be purchased

        """
        return self.money_format((self.fee() / self.shares))

    def cost_per_dollar(self):
        """

        :return: per dollar cost of each share relative to transaction fee.
        Formula
        - Quotient of - cost per share AND share
        """
        return self.money_format((self.fee() / self.b_price))

    def avg_div_per_dollar(self):
        """

        :return: average dividend paid per dollar invested in stock
        Formula
        - Quotient of - average dividends and share price
        """
        return self.money_format(self.avg_div / self.b_price)

    def years_required_till_return(self):
        """

        :return: the number of years the security needs to held before it pays for itself ceteris paribus
        Formula
        -Quotient of -  cost per share AND average dividend

        """
        return format(self.cost_per_share() / self.avg_div, ",.2f")

    def gain_loss(self, ):
        difference = (self.avg_div_per_dollar()-self.cost_per_dollar())

        if self.avg_div_per_dollar() > self.cost_per_dollar():
            return ("Gain", difference)
        else:
            return ("Loss", difference)

    def write(self,file_name,index):
       #return []
        pass
