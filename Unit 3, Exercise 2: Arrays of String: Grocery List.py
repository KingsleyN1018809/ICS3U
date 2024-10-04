# Predict:
#['Apples', 'Bananas', 'Cherries', 'Dosa']
#The number of items is 4.
#Apples
#Bananas
#Cherries
#Dosa
#0 Apples
#1 Bananas
#2 Cherries
#3 Dosa
items = ["Apples", "Bananas", "Cherries", "Dosa"]
print(items) # Predict A - Does this really print anything?
print("The number of items is %d." % len(items)) # Predict B
for i in items: # Predict C
    print(i)

for c in range(len(items)): # Prediction D
    print(c, items[c])

#Modify
items = []
items_amount = int(input("Enter amount of items: "))
print("ENTER YOUR ITEMS NOW!!!")
for item in range(items_amount):
  items.append(input("Next item:"))
print("You have entered", items_amount, "items.")
print(items)
