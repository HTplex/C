class FruitShop:
    def __init__(self, name, fruitprices):
        """
        :param name: name of the fruit shop, you know, name is important
        :param fruitPrices: it's a dictionary which key is the name of fruit and value is it's prices
        """
        self.fruitPrices = fruitprices
        self.name = name
        print 'welcome to %s' % name

    def getcostperserv(self, fruit):
        """
        :param fruit: the name of the fruit you wanna get the price
        :return: assuming fruit is on the menu return price, else return the nothing
        """
        if fruit not in self.fruitPrices:
            print 'sorry we do not have %s today' % fruit
            return None
        return self.fruitPrices[fruit]

    def gettotalpriceoforder(self, orderlist):
        """

        :param orderlist: list of fruit names and numbers need in (name, amount) tuples
        :return: totalprice
        """
        totalcost = 0.0
        for name, amount in orderlist:
            costperserv = self.getcostperserv(name)
            if costperserv is not None:
                totalcost += costperserv * amount
        return totalcost

    def getname(self):
        return self.name
