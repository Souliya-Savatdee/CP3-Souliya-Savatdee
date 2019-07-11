a=2
b=1
while(True):
    print(str(a)+" "+"x"+" "+str(b)+" "+"="+" "+str(a*b))
    b=b+1
    if(b>12):
        a=a+1
        b=1
        if(a>12):
            break