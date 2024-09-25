# Predict:
# This will always print out I prefer cherries, because it can only be apples or bananas if you type in upper case letter
print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch == "A"):
    print("I prefer apples")
elif (ch == "B"):
    print("I prefer bananas")
else:
    print("I prefer cherries")
    
#Modify 1:
print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")
ch.upper()

if (ch == "A" or ch == "a"):
    print("I prefer apples")
elif (ch == "B" or ch == "b"):
    print("I prefer bananas")
elif (ch == "C" or ch == "c"):
    print("I prefer cherries")
else:
    print("Choose A, B, or C")

#Modify 2:
