def validate(N):
    N = reverse_string(N)
    total = 0
    for i in range(len(N)):
        digit = int(N[i])
        if i % 2 == 1:
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digit
    return total % 10 == 0

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print("Validate a number with the Luhn Algorithm!")
num = input("Input a number to validate: ")
isValid = validate(num)
if isValid:
    print(num, "is valid!")
else:
    print(num, "is not valid!")
