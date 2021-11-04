def getApples():
    price_of_apples = int(20)
    apples_to_buy = int(input("How many apples would you like to buy? "))
    apple_amount = (apples_to_buy) * (price_of_apples)
    return apple_amount

def getOranges():
    price_of_oranges = int(25)
    oranges_to_buy = int(input("How many oranges would you like to buy? "))
    orange_amount = (oranges_to_buy) * (price_of_oranges)
    return orange_amount

def getCompute():
    computation = (apples) + (oranges)
    return computation


def displayOutput():
    print(f"The total amount is {computation}.")



apples = getApples()
oranges = getOranges()
computation = getCompute()
displayOutput ()