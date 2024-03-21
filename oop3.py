class student:
    n1=int(input("Enter your id :"))
    def name(self):
        print("Student of Northern University")
    def id(self):
        print("your ID: ",self.n1)
    if n1<=568 and n1>=524:
        print("Section E")
    else:
        print("Not in section E")
class indi(student):
    n=input("Enter your name:")
    #n1=int(input("Enter your id "))
    def name1(self):
        print("your name:",self.n)
obj=indi()
obj.name()
obj.name1()
obj.id()


