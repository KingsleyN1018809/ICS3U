import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
print("Now deciding if", y, "is a factor of", x, "...")
rem = x % y
if rem == 0:
    print("Yes!", y, "is a factor of", x)
#Predict:
#This code will say Yes! 3 is a factor of 6. When inputted x as 6 and y as 3
#Will only print out deciding if x is 6 and y is 5, because you only put it to print out when remainder is 0

#Modify 1/ Modify 2:
import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number: ")
y = int(y)
print("Now deciding if", y, "is a factor of", x, "...")
if (y != 0):
    rem = x % y
    if rem == 0:
        print("Yes!", y, "is a factor of", x)
else:
    print("You cannot divide by 0")
    print("No!", y, "is not a factor of", x)

#Modfiy 3:
import math

x = input("Please input a whole number between 1 - 20: ")
x = int(x)
if (x > 0 and x <= 20):
    y = input("Please input another nonzero whole number 1 - 20: ")
    y = int(y)
    if (y > 0 and y <= 20):
      rem = x % y
      if rem == 0:
        print("Now deciding if", y, "is a factor of", x)
        print("Yes!", y, "is a factor of", x)
      else:
            print("No!, is a factor of", x)
    else:
        print("You cannot divide by 0")
        print("No!", y, "is not a factor of", x)
else:
    print("X cannot be below 1 or above 20")
