n = int(input("Give value of n: "))
print("counting from j = 1 to:", n)
for j in range (1, n + 1):
  tri = 0
  fac = 1
  for i in range(1, j +1):
    tri += i
    fac *= i
  print("%1s %5s %10s" % (str(j), str(tri), str(fac)))
