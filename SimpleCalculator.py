# A simple Calculator
num1=eval(input("Enter 1st Value: "))
num2=eval(input("Enter 2nd Value: "))
op=input("Enter Operator(+,-,*,/): ")
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else :
    print("Invalid term you use.")
