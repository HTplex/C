import fruitShopClass

name1 = 'izaac fruit shop'
fruitprices1 = {'apple': 4.0, 'strawberry': 5.0, 'shit': 0.5, 'holyshit': 5.0}
izaacShop = fruitShopClass.FruitShop(name1, fruitprices1)

htlist = [('apple', 2), ('shit', 1)]
price = izaacShop.gettotalpriceoforder(htlist)
print price
