class area:
    def area(self,a="none",b="none"):
        if(a!="none" and b!="none"):
            print("area:",(a*b))
        else:
            print("Area: ",(a*a))
obj=area()
obj.area(10)