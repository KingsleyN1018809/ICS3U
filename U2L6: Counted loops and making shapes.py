# Try this
s = "--8<--"
print(s*10)

# Predict
# It would output:
"""
#
##
###
####
#####
######
#######
########
#########
##########
"""

# The sequence listed for this range function: range(-5, 5) is:
# -5, -4, -3, -2, -1, 0, 1, 2, 3, 4

# Try this
S = "#"
for i in range(10, 0, -1):
    print(S * i)

# Modify 2
S = "#"
space_count = 4
for i in range(1, 10, 2):
    print(" " * space_count, S * i)
    space_count -= 1

# Modify 3
S = "#"
space_count = 5
for i in range(1, 12, 2):
    print(" " * space_count, S * i)
    space_count -= 1
space_count = 1
for i in range(9, 0, -2):
    print(" " * space_count, S * i)
    space_count += 1
