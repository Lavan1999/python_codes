# python_codes
# Using if else statement for finding max number
# Without using buildin function like max()
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a>b:
    if a>c:
        if a>d:
            if a>e:
                print(a)
            else:
                print(e)
        elif d>e:
            print(d)
        else:
            print(e)
    elif c>d:
        if c>e:
            print(c)
        else:
            print(e)
    elif d>e:
        print(d)
    else:
        print(e)
elif b>c:
    if b>d:
        if b>e:
            print(b)
        else:
            print(e)
    elif d>e:
        print(d)
    else:
        print(e)
elif c>d:
    if c>e:
        print(c)
    else:
        print(e)
elif d>e:
    print(d)
else:
    print(e)
