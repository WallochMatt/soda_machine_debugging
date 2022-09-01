import coins

class Wallet:
    def __init__(self):
        self.money = self.fill_wallet()
        # self.money = []
        #self.fill_wallet() #caused error, shouldnt need this


    def fill_wallet(self):
        """Method will fill wallet's money list with certain amount of each type of coin when called."""
        money_have = []
        for index in range(8):
            money_have.append(coins.Quarter())
        for index in range(10):
            money_have.append(coins.Dime())
        for index in range(20):
            money_have.append(coins.Nickel())
        for index in range(50):
            money_have.append(coins.Penny())
        return money_have