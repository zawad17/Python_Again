class ws:
    def displayinfo(self,name=' '):
        print("welcome "+name)
        #overloading concept
obj = ws()
obj.displayinfo("zawad")
class ws:
    def display(self):
        print("welcome")
class ip (ws):
    def display(self):
        super().display()
        print("welcome Man")
obj=ip()
obj.display()

