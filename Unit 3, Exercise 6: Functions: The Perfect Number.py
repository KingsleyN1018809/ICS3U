# Make
def factorize(N):
    factor = []
    for i in range(1, N):
        if N % i == 0:
            factor.append(i)
    return factor

print(factorize(6))
print(factorize(24))
print(factorize(0))
print(factorize(1))
print(factorize(7))

# Make more
def factorize(N):
    factor = []
    for i in range(1, N):
        if N % i == 0:
            factor.append(i)
    return factor

def sum(N):
  amount = 0
  for i in N:
    amount += i
  return amount

try:
  n = int(input("Please enter a positive integer: "))
  if n > 0:
    n_factors = factorize(n)
    n_sum = sum(n_factors)
    print("Factor sum: %d" % n_sum)
    if n_sum == n:
      print("%d is perfect" % n)
    elif n_sum > n:
      print("%d is abundant" % n)
    elif n_sum < n:
      print("%d is deficient" % n)
  else:
    print("Goodbye!") 
except:
  print("Goodbye!")
