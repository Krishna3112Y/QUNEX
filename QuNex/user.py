

class user:

    def __init__(self):
        self.money = 10000
        self.lock_money = 0
        self.stock = {}
        self.locked_stock ={}

    def buy(self,order_id,ticker, shares , stock_price):

        if self.money >= shares*stock_price:
            self.money = self.money - shares*stock_price
            self.lock_money += shares*stock_price
            self.locked_stock[order_id] = [ticker , stock_price , shares ]

            return True

        else :
            return False
        