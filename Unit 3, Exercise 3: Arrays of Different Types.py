#Predict:
#6 Apples
#7 Bananas
#8 Cherries
#4 Dosa
items = ["Apples", "Bananas", "Cherries", "Dosa"]
sizes = []
for i in range(len(items)): # Predict A: State the purpose,
                            # data types, and any output
    sizeI = len(items[i])
    sizes.append(sizeI)

for i in range(len(sizes)): # Predict B: State the output
    print("%d %s" % (sizes[i], items[i]))

#Modify
items = ["Apples", "Bananas", "Cherries", "Dosa"]
sizes = []
matches = []
for i in range(len(items)):
    sizeI = len(items[i])
    sizes.append(sizeI)

for i in range(len(sizes)):
  if sizes[i] == len(items[i]):
    matches.append("True")
  else:
    matches.append("False")
for i in range(len(sizes)):
    print("%d %s, %s" % (sizes[i], items[i], matches[i]))
