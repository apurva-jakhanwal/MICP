'''
Problem description:
Design a vending machine.

Clarify:
No more restrictions, just design a general vending machine we are familiar with.

Use case list:

select item and get price
accept bills/coins
dispense items purchased and return change
refund when cancelling the request
Possible exceptions:

Sold out
Not fully paid
Not enough changes
'''

class Item :
    '''A class to keep track of item name, price and  availibility.'''
    
    def __init__(self, name, price, available, count):
        self.name = name
        self.price = price
        self.available = available
        self.count = count

    def getItemName(self):
        return self.name

    def getItemPrice(self):
        return self.price

    def getItemAvailibility(self):
        return self.available

    def getItemCount(self):
        return self.count

class ItemRequest:
    '''A class to keep track of the requested item's name, price, cancellation and success of sale.'''

    def __init__(self, name, price_paid):
        self.name = name
        self.price_paid = price_paid

    def getItemName(self):
        return self.name

    def getPricePaid(self):
        return self.price_paid
    
class Money:
    '''A class to keep track of the type, balance, change and if the item was bought'''

    def __init__(self, typeof, balance, change):
        self.typeof = typeof #either a bill or coins
        self.balance = balance #to keep track of the amount of money to be retuned if the user does not provide the exact change
        self.change = change #to keep track of the change to be issued

    def getType(self):
        return self.typeof

    def getbalance(self):
        return self.balance

    def getChange(self):
        return self.change

class Transaction:
    '''A class to keep track of cancellations'''

    def __init__(self, bought):
        self.bought = bought #to keep track of whether the item was finally purchased because if not then a refund needs to be issued

    def getBought(self):
        return self.bought

class VendingMachine:
    '''A class to handle the vending machine operations'''

    def __init__(self, item, reqItem, money, trans):
        self.Item = item
        self.ItemRequest = reqItem
        self.Money = money
        self.Transaction = trans

    def issueChange(self):
        requiredChange = self.ItemRequest.getPricePaid() - self.Item.getItemPrice()
        self.Money.balance -= requiredChange
        return requiredChange
    
    def sellItem(self):
        self.Item.count -= 1
        if self.Item.count is 0:
            self.Item.availible = False
        return self.ItemRequest.name
    

    def handleSale(self):
        #checking for Sold out, Not fully paid, Not enough changes
        
        if not self.Item.getItemAvailibility():
            print("Item is currently all sold out")
            success = False
            print("Issuing the refund...")
            print(self.ItemRequest.getPricePaid()) #issuing the refund
            return success

        if not (self.ItemRequest.getPricePaid() >= self.Item.getItemPrice()):
            print("Not fully paid/Unpaid Balance")
            success = False
            return success
    
        if not ((self.ItemRequest.getPricePaid() - self.Item.getItemPrice()) <= self.Money.balance):
            print("Not enough change")
            success = False
            print("Issuing the refund...")
            print(self.ItemRequest.getPricePaid())#issuing the refund
            return success

        #if transaction is cancelled then issue the refund
        if not self.Transaction.bought: 
            print("Your Request Has Been Cancelled")
            success = False
            print("Issuing the refund...")
            print(self.ItemRequest.getPricePaid()) #issuing the refund
            return success

        #if evrything turns out to be fine then sell the item
        self.issueChange()
        self.sellItem()
        success = True

        return success

    
def testVendingMachine():
    '''Test cases'''
    
    #simple pass
    print("Test Case 1")
    item1 = Item("Granola Bar", 2, True, 4)
    itemReq1= ItemRequest("Granola Bar", 5)
    money1 = Money("coins", 10, 3)
    trans1 = Transaction(True)
    successful1 = VendingMachine(item1, itemReq1, money1, trans1)
    print("Successful? ", successful1.handleSale())
    print()

    #sold out
    print("Test Case 2")
    item2 = Item("Chips", 10, False, 0)
    itemReq2 = ItemRequest("Chips", 10)
    money2 = Money("coins", 10, 0)
    trans2 = Transaction(True)
    successful2 = VendingMachine(item2, itemReq2, money2, trans2)
    print("Successful? ", successful2.handleSale())
    print()

    #not fully paid
    print("Test Case 3")
    item3 = Item("Soda", 8, True, 1)
    itemReq3 = ItemRequest("Soda", 5)
    money3 = Money("coins", 10, 0)
    trans3 = Transaction(True)
    successful3 = VendingMachine(item3, itemReq3, money3, trans3)
    print("Successful? ", successful3.handleSale())
    print()

    #not enough change
    print("Test Case 4")
    item4 = Item("Coookies", 1, True, 10)
    itemReq4 = ItemRequest("Cookies", 5)
    money4 = Money("coins", 1, 4)
    trans4 = Transaction(True)
    successful4 = VendingMachine(item4, itemReq4, money4, trans4)
    print("Successful? ", successful4.handleSale())
    print()

    #cancelled
    print("Test Case 5")
    item5 = Item("Coookies", 1, True, 10)
    itemReq5 = ItemRequest("Cookies", 1)
    money5 = Money("coins", 1, 0)
    trans5 = Transaction(False)
    successful5 = VendingMachine(item5, itemReq5, money5, trans5)
    print("Successful? ", successful5.handleSale())
    print()

testVendingMachine()

