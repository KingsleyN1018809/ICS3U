# Predict:
#Python
#P
#Python
#0 P
#1 y
#2 t
#3 h
#4 o
#5 n
progname = "Python"
print(progname)
print(progname[0])

for c in progname:
    print(c, sep="", end="") 
print()

for c in range(len(progname)):
    print(c, progname[c])

#Modify:
progname = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in."
print(progname)
space = 0
for c in progname:
  if c == " ":
    space += 1
print("There are:", space, "amount of space")
