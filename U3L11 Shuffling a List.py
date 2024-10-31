import random

def shuffle(A):
  for i in range(len(A)):
    temp = B[i]
    j = random.randint(0, len(A) + 1)
    B[i] = B[j]
    B[j] = temp
    return A
    
size = 6
B = []
for i in range(1, size + 1):
  B.append(i)

print(B)
B = shuffle(B)
print(B)
