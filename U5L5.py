def getInt(prompt):
    valid = False
    while not valid:
        try:
            num = int(input(prompt))
            if num < 0:
                print("Please enter a positive number.")
            else:
                return num
                valid = True
        except ValueError:
            print("Invalid number.")

def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print("Program for printing the Fibonacci sequence!")
tn = getInt("Please input a whole number: ")

for i in range(1, tn + 1):
    print(fib(i), end=" ")
print()
