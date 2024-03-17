class BikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total Bike ",self.stock)
    def RentForBike(self,Q):
        if Q<=0:
            print("Enter Positive Value: ")
        elif Q >= self.stock:
            print("Enter the Value less than stock")
        else:
            self.stock = self.stock-Q
            print("Total price: ",Q*100)
            print("Total Bike: ",self.stock)
while True:
    obj=BikeShop(100)
    uc=int(input('''
        1.Display Stock
        2.Rent a Bike
        3.Exit
    
    '''))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter Quantity: "))
        obj.RentForBike(n)
    else:
        break
