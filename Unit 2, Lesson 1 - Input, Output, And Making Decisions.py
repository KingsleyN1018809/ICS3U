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
grade = int(input("Please enter your grade: "))

if (grade >= 80 and grade <= 100):
    print("You got an A")
elif (grade >= 70 and grade <= 79):
    print("You got a B")
elif (grade >= 60 and grade <= 69):
    print("You got a C")
elif (grade >= 50 and grade <= 59):
    print("You got a D")
elif (grade >= 0 and grade <= 49):
    print("You got a F")
else:
    print("invalid grade")
