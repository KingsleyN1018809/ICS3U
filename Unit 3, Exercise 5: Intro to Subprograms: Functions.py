#Predict:
#9
#No it doesnt work, because the str is not define
def add(a, b):
  return a + b

print(add(hello, e))

#Modify 1:
def add(a, b):
  return a + b
try:
  a = float(input("Give value of a as Numerical value: "))
  b = float(input("Give value of b as a Numerical value: "))
  print(add(a, b)*2)
except:
  print("Invalid number")

#Modify 2:
import math
def my_Pow(m, n):
  return math.pow(m,n)
try:
  m = float(input("Give value of m as Numerical value for base: "))
  n = float(input("Give value of n as a Numerical value for exponent: "))
  print(pow(m, n))
except:
  print("Invalid number")
