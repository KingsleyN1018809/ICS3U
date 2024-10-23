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
import math

def factorize(N):
    photos = math.floor(math.sqrt(N))
    factors = []
    for x in range(1, photos + 1):
        if N % x == 0:
            factors.append(x)
    return factors
        
def minimum_perimeter(N):
    factors = factorize(N)
    x = 0
    for number in factors:
        if number > x:
            x = number
    y = N / x
    perimeter = 2 * (x + y)
    print("Minimum perimeter is %d with demensions of %d x %d" % (perimeter, x, y))
    
print("Welcome to the school yearbook program!")
done = False
while not done:
    print()
    valid = False
    num_photos = 0
    while not valid:
        user = input("Please input your number of photograpghs: ")
        if user.lower() == "done":
            valid = True
            done = True
            print("Goodbye!")
            break
        try:
            user_int = int(user)
            if user_int > 0:
                valid = True
                num_photos = user_int
            else:
                print("%d is not a valid number of photos." % user_int)
        except:
            print("%s is not a valid number of photos." % user)
    if not done:
        minimum_perimeter(num_photos)
