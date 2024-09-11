def fibofunc(no):
    a=0
    b=1
    fl = []
    for counter in range(no+1):
        c = a+b 
        fl.append(a)
        a=b
        b=c
    print(fl)

fibofunc(10)