#Predict:
#3 4 1 2 6 
#9 2 3 7 5 
#4 2 1 0 3 
#[[3, 4, 1, 2, 6], [9, 2, 3, 7, 5], [4, 2, 1, 0, 3]]
ar2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]
for i in range(len(ar2)):
  ar3 = ar2[i]
  for j in range(len(ar3)):
      print(ar3[j], end=" ")
  print() # PREDICT A

print(ar2) # PREDICT B

#Modify:
ar2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]
added_ar = []
for i in range(len(ar2)):
  ar3 = ar2[i]
  amount = 0
  for j in range(len(ar3)):
      amount += ar3[j]
  added_ar.append(amount)
  
print(added_ar)
