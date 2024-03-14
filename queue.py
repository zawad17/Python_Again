l=[]
while True:
    c=int(input('''
    1.Enqueue 
    2.Dequeue
    3.Front
    4.Rear
    5.Display
    6.Exit
    '''))
    if c==1:
        n=input("Enter: ")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("empty")
        else :
            del l[0]
            #print(p)
            print(l)

    elif c==3:
        if len(l) == 0:
            print("empty")
        else:
            print("Front value ",l[0])
    elif c==4:
        print("Last Value",l[-1])
    elif c==5:
        print("Display",l)
    elif c==6:
        break
    else:
        print("Invalid Operation ")

