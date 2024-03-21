class demo:
    a=20
    b=5
    def sum(self):
        self.c=self.a+self.b
        print(self.c)
    def __init__(self):
       self.c=self.a+self.a
       print(self.c)
obj= demo()
obj.sum()

class demo():
    a=10
    def __init__(self):
        self.c=self.a+self.a
        print(self.c)
obj=demo()