count = 9
while (count != 0):
    print(count)
    count -= 1
#Predict
#This will print out
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Prediction is right
# >>> %Run -c $EDITOR_CONTENT
#9
#8
#7
#6
#5
#4
#3
#2
#1
#>>> 

#Modify 1:
count = 9
while (count != 0):
    count -= 1
    print(count)

#This will print out
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
#This doesnt print out 9 because it subtract 1 first then print, as the first one print first then subtract
#PART B
num = 1
num_count  = num
while (num <= 6):
    if (num == 1):
        print("The 1st triangular number is: ", num)
        num_count += 1
        num += num_count
        if (num == num):
            print("The 2nd triangular number is: ", num)
            num_count += 1
            num += num_count
            if (num == num):
                print("The 3rd triangular number is: ", num)
                num_count += 1
                num += num_count
                if (num == num):
                    print("The 4th triangular number is: ", num)
                    num_count += 1
                    num += num_count
                    if (num == num):
                        print("The 5th triangular number is: ", num)
                        num_count += 1
                        num += num_count
                        if (num == num):
                            print("The 6th triangular number is: ", num)
                            #while (num <= 1000):
                                #num_count += 1
                                #num += num_count
                                #if (num == num):
                                    #print("The next triangular number is: ", num)
                          #funny line of code
