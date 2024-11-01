"""
Author : Kingsley Nguyen
Student Number: 1018809
Revison date : 23 October 2024
Program : School Yearbook
Description : A program that find the minimum area and dimensions for photos with 
    1x1 units being placed in a yearbook.
VARIABLE DICTIONARY :
    done (bool) = Boolean value of if the user has entered done and if the loop should keep running
    valid (bool) = Boolean value of if the user has entered valid input
    num_photos (int) = Number of photos the user has input
    user (str) = User input for the amount of photos or "done"
    user_int (int) = The input amount of photos converted to int
    factor (list) = List of factors a number has
    photos (int) = Max factor of the photo inputed by user
    x (int) = X value of the dimensions
    y (int) = Y value of the dimensions
    perimeter (int) = The perimeter of the photos
"""
#import math libary
import math

#Create function call factorize of N
def factorize(N):
    #Variable photos equal to the round down of square root of N
    photos = math.floor(math.sqrt(N))
    #Make a list name factors
    factors = []
    #For loop for the number of photos starting from 1 to max
    for x in range(1, photos + 1):
        #Find if the factor of N divide by x is equal to 0
        if N % x == 0:
            #add x to factors list
            factors.append(x)
    #return the factors
    return factors

#Create function minimum_perimeter of N
def minimum_perimeter(N):
    #List of factors equal to function factorize(N)
    factors = factorize(N)
    #Set x = 0
    x = 0
    #For the amount of number in factors list
    for number in factors:
        #Check if number is bigger than x
        if number > x:
            #Set x = number if number is bigger than x
            x = number
    #Y = N divide by x
    y = N / x
    #Find perimeter
    perimeter = 2 * (x + y)
    print("Minimum perimeter is %d with demensions of %d x %d" % (perimeter, x, y))

#Start of the program with a welcome output
print("Welcome to the school yearbook program!")
#Set done as false
done = False
#While done is not true
while not done:
    #Print blank space
    print()
    #Set valid is false
    valid = False
    num_photos = 0
    while not valid:
        #Ask for user input
        user = input("Please input your number of photograpghs: ")
        #Check user input to see if it "done"
        if user.lower() == "done":
            #Set valid to true
            valid = True
            #Set done to true
            done = True
            #Print Goodbye!
            print("Goodbye!")
            #Exit program
            break
        #Create try
        try:
            #Set user_int to integer of user input
            user_int = int(user)
            #Check if the user_int is bigger than 0
            if user_int > 0:
                #Set valid to true
                valid = True
                #num_photos set equal to user_int
                num_photos = user_int
            else:
                #If not a valid number, print "user_int" is not a valid number of photos
                print("%d is not a valid number of photos." % user_int)
        #If user_int is not an integer
        except:
            #If not a valid number, print "user_int" is not a valid number of photos
            print("%s is not a valid number of photos." % user)
    #If user input is not done
    if not done:
        #Set num_photos into minimum perimeter
        minimum_perimeter(num_photos)
