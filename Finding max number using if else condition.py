# To find maximum numbers from the users 5 numbers by using if else condition:
# First we need to chack number1 is bigger than number2, if yes, then check number1 greater than number2, if yes, again checks with number4
  # if yes, again checks with number5. All the conditions are satisfied then number1 is maximum number.
  # or else it compete with other numbers.


number1 = int(input('Enter number1: '))
number2 = int(input('Enter number2: '))
number3 = int(input('Enter number3: '))
number4 = int(input('Enter number4: '))
number5 = int(input('Enter number5: '))
if number1 > number2:
    if number1 > number3:
        if number1 > number4:
            if number1 > number5:
                print('Maximum number is: ', number1)
            else:
                print('Maximum number is: ', number5)
        elif number4 > number5:
            print('Maximum number is: ',number4)
        else:
            print('Maximum number is: ',number5)
    elif number3 > number4:
        if number3 > number5:
            print('Maximum number is: ',number3)
        else:
            print('Maximum number is: ',number5)
    elif number4 > number5:
        print('Maximum number is: ',number4)
    else:
        print('Maximum number is: ',number5)
elif number2 > number3:
    if number2 > number4:
        if number2 > number5:
            print('Maximum number is: ',number2)
        else:
            print('Maximum number is: ',number5)
    elif number4 > number5:
        print('Maximum number is: ',number4)
    else:
        print('Maximum number is: ',number5)
elif number3 > number4:
    if number3 > number5:
        print('Maximum number is: ',number3)
    else:
        print('Maximum number is: ',number5)
elif number4 > number5:
    print('Maximum number is: ',number4)
else:
    print('Maximum number is: ',number5)


# Named with simple variable for easily identify the code:

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

