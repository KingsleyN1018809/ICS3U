"""
Author: Kingsley Nguyen
Student No: 1018809
Revision date: Dec 05, 2024
Program: Graphic Designer
Description: A program that ask user for a file with symbols as color and draw out using that
Variable Dictionary:
    - filename (str) = The file name or path for any xpm file
    - rotate (bool) = Boolean value to rotate the image
    - valid (bool) = Boolean value that check for the validation of the image file
    - user_input (str) = User input in string as a variable
    - colorData (str) = String value of color data
    - rows (int) = Number of rows
    - cols (int) = Number of cols
    - numColors (int) = Number of colors
    - colorDefs (list) = List of colors and symbols
    - imageData (list) = List of image with color
"""
#Import turtle libary
import turtle  
#Set the canvas background color to gray
turtle.bgcolor("gray40") 
turtle.tracer(0,0)
#Change turtle to t as a variable for easier reading
t = turtle.Turtle()      
#Hide Turtle as a cursor
t.hideturtle()          

#Create function to modify string to get rid of character
def modify(ln):
    #Set mod_string as nothing for a variable
    mod_string = ""
    #Set badChars as (" and ,)
    badChars = ['"', ',']
    #Strip variable Ln
    ln = ln.strip()
    #Loop c through Ln
    for c in ln:
        #Check if c doesnt belong to the badChars list
        if c not in badChars:
            #If c is not then mod_string add c
            mod_string = mod_string + c
    #Return back to the loop
    return mod_string
#Plot a point on the canva using the data given
def plotIt(T, x, y, d, color):
    #Release the pen to stop drawing
    T.penup()
    #Bring the pen to the given point
    T.goto(x, y)
    #Put pen down to start drawing
    T.pendown()
    #Choose the pen as dot size and color given
    T.dot(d, color)
    #Stop drawing
    T.penup()
#
def drawImage(img, pixel_size, rows, cols, x_rot, y_rot):
    # Set x and y half to negative value of half of the rows/cols (so image can be centered)
    x_half = int(-cols // 2)
    y_half = int(-rows // 2)
    # Loops through x values of image
    for x in range(len(img)):
        # Increase y_half counter by 1
        y_half += 1
        # Loops through y values of image
        for y in range(len(img[x])):
            # Plot the point on canvas using plotIt function
            plotIt(t, x_half * pixel_size * x_rot, -y_half * pixel_size * y_rot, pixel_size, img[x][y])
            # Increase x_half counter by 1
            x_half += 1
        # Reset x_half counter for next iteration
        x_half = int(-cols // 2)

def getImageData(fh, rows, cols, colorDefs):
    # Initialize image data list
    imageData = []
    # Loop through number of rows
    for i in range(rows):
        # Read the line and set to row variable
        row = fh.readline()
        # Modify the string to get rid of unwanted characters
        row = modify(row)
        # Initialize row array
        rowArr = []
        # Loop through each character/symbol in thr row
        for j in range(len(row)):
            color = row[j]
            # Compare symbol to colorDefs list and set to the right color
            for k in range(numColors):
                if color == colorDefs[k][0]:
                    color = colorDefs[k][1]
            # Add the color to the row array
            rowArr.append(color)
        # Add the row array to the imageData list
        imageData.append(rowArr)
    # Return imageData
    return imageData


def getColorData(fh, rows, cols):
    # Initialize colorDefs list
    colorDefs = []
    # Loop through number of colors
    for i in range(numColors):
        # Read the line and set to colorLine
        colorLine = fh.readline()
        # Modify the string to get rid of unwanted characters
        colorLine = modify(colorLine)
        # Split the colorLine into symbol, c, and color
        sym, c, color = colorLine.split()
        # Check if sym is ~  and change it to a space
        if sym == '~':
            sym = ' '
        # Add color and symbol to colorDefs list
        colorDefs.append([sym, color])
    # Return colorDefs
    return colorDefs

#Set filename to nothing
filename = ""
#Set variable rotate as false
rotate = False

# Set valid to false
valid = False
# Loop until a valid option is chosen
while not valid:
    # Prompt user to choose an option
    user_input = input("Choose an option to draw: \n A: rocky_bullwinkle_mod.xpm \n B: smiley_emoji_mod.xpm \n C: Enter a file name \n")
    # Check if user chose option A
    if user_input.lower() == 'a':
        # Set filename and valid to true
        filename = "rocky_bullwinkle_mod.xpm"
        valid = True
    # Check if user chose option B
    elif user_input.lower() == 'b':
        # Set filename and valid to true
        filename = "smiley_emoji_mod.xpm"
        valid = True
    # Check if user chose option C
    elif user_input.lower() == 'c':
        # Promt user to choose a filename and set valid to true
        filename = input("Enter the file name: ")
        valid = True

# Set valid to false
valid = False
# Loop until a valid option is chosen
while not valid:
    # Prompt user to choose if they want to rotate the image
    user_input = input("Would you like to rotate the image (Y/N): ")
    # Check if user chose yes
    if user_input.lower() == 'y':
        # Set rotate and valid to true
        rotate = True
        valid = True
    # Check if user chose no
    elif user_input.lower() == 'n':
        # Set valid to true
        valid = True

# Open the chosen file for reading
fh = open(filename, "r")

# Read the first line of the file
colorData = fh.readline()
# Modify the line to get rid of unwanted characters
colorData = modify(colorData)
# Initialize variables for columns, rows, and number of colors
cols, rows, numColors = (0,0,0)
# Split the color data into columns, rows, and number of colors
if len(colorData.split()) == 4:
    cols, rows, numColors, temp = colorData.split()
else:
    cols, rows, numColors = colorData.split()

# Convert rows, columns, and number of colors to int
rows = int(rows)
cols = int(cols)
numColors = int(numColors)

# Call getColorData function and set it to colorDefs
colorDefs = getColorData(fh, numColors)
# Call getImageData function and set it to imageData
imageData = getImageData(fh, rows, colorDefs)
# Close the file
fh.close()

# Print the dimensions of the image
print("\nDimensions: %d x %d" % (rows, cols))
# Print the number of colors
print("Number of colors:", numColors)
# Print the color definitions
print("Colors:", colorDefs)
# Draw the image, and rotate if rotate is true
if rotate:
    drawImage(imageData, 3, rows, cols, -1, -1)
else:
    drawImage(imageData, 3, rows, cols, 1, 1)
