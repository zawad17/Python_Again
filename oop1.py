class demo:
    a = " "
    def sum(self,a,b):
        z=a+b
        print(z)      #create object
obj=demo()
N1=int(input("N1"))
N2=int(input("N2"))
obj.sum(N1,N2)
obj.a = "zawad"
obj1=demo()
obj1.sum(10,12)

obj1.a="pulok"
print(f"my 1st name is {obj.a}")
print(f"my 2nd name is {obj1.a}")