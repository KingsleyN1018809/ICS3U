#Code
print("factorial calculator for dummies")
n = int(input("Give the factorial: "))
num = 0
while (num <= n):
    fac = num
    count = num
    while (count > 0):
        count -= 1
        if (count != 0):
            fac *= count
    if (num == 0):
        fac = 1
    print("%d! = %d" % (num, fac))
    num += 1
