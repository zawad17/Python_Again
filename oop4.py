#Encapsulation
# class demo:
#     __name="Biva"
#     def __init__(self):
#         print(self.__name)
# obj=demo()
class hello:
    def __init__(self):
        self.__name=" "
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name
obj=hello()
obj.setname("Zawad")
print(obj.getname())
