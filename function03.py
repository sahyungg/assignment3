def getMoney():
    money_owned = input("How much money do I have? ")
    amount_of_money = int(money_owned)
    return amount_of_money

def getPrice():
    price_of_apple = input("How much does an apple cost? ")
    apple_price = int(price_of_apple)
    return apple_price

def getMax():
    maximum = money // price
    return maximum

def getChange():
    change = money % price
    return change

def displayOutput():
    print(f"You can buy {max} apples and your change is {change} pesos.")


money = getMoney()
price = getPrice()
max = getMax()
change = getChange()
displayOutput()