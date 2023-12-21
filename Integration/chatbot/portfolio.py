# portfolio.py

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, stock_name, quantity):
        if stock_name in self.stocks:
            self.stocks[stock_name] += quantity
        else:
            self.stocks[stock_name] = quantity

    def get_portfolio(self):
        return self.stocks
