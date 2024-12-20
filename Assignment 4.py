"""
Author: Kingsley Nguyen
Student number: 1018809
Revision date: 12/19/2024
Program : Reading files and searching for data
Description : Reads Wordle data from a file and allows the user to search for specific words or dates. 
VARIABLE DICTIONARY :
    filename: str - Name of the file containing Wordle data
    fh: file object - File handle for reading the Wordle data file
    lines: list - List of lines read from the file
    words: list - List to store words from the file
    dates: list - List to store dates from the file
    line: str - A single line read from the file
    month: str - Month component of the date
    day: str - Day component of the date
    year: str - Year component of the date
    word: str - Word from the file
    myDate: int - Merged date in integer format
    startDate: int - The earliest date in the dates list
    endDate: int - The latest date in the dates list
    original_dates: list - Copy of the dates list to maintain original order
    original_words: list - Copy of the words list to maintain original order
    valid: bool - Flag to validate user input
    userOption: str - User's choice for search option
    userInput: str - User's input word for search
    date: int - Date corresponding to the user's input word
    year: str - User's input year for date search
    month: str - User's input month for date search
    day: str - User's input day for date search
"""

"""
Function to perform merge sort on two arrays.
Parameters:
    arr (list): Array to be sorted.
    arr2 (list): Second array to be sorted.
    l (int): Left index of the subarray.
    r (int): Right index of the subarray.
"""
def mergeSort(arr, arr2, l, r):
    # Check if the subarray has more than one element
    if l < r:
        # Find the middle point to divide the array into two halves
        # Avoids potential overflow for large values of l and r
        m = l + (r - l) // 2
        
        # Sort first and second halves
        mergeSort(arr, arr2, l, m)
        mergeSort(arr, arr2, m + 1, r)
        mergeSortMerge(arr, arr2, l, m, r)

"""
Function to merge two sorted arrays.
Parameters:
    arr (list): Array to be sorted.
    arr2 (list): Second array to be sorted.
    l (int): Left index of the subarray.
    m (int): Middle index of the subarray.
    r (int): Right index of the subarray.
"""
def mergeSortMerge(arr, arr2, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
    L2 = [0] * (n1)
    R2 = [0] * (n2)
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
        L2[i] = arr2[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        R2[j] = arr2[m + 1 + j]
    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            arr2[k] = L2[i]
            i += 1
        else:
            arr[k] = R[j]
            arr2[k] = R2[j]
            j += 1
        k += 1
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        i += 1
        k += 1
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        j += 1
        k += 1 

"""
Function to merge year, month, and day into a single integer.
Parameters:
    year (str): Year component of the date.
    month (str): Month component of the date.
    day (str): Day component of the date.
"""
def merge(year, month, day):
    try:
        months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
        line_int = ""
        line_int += year
        month_str = ""
        for i in range(len(months)):
            if months[i] == month.lower():
                month_str += str(i + 1)
                if len(month_str) == 1:
                    month_str = "0" + month_str
        line_int += month_str
        line_int += day
        return(int(line_int))
    except:
        return 0

"""
Function to search for a word or date in a sorted array.
Parameters:
    A (str): Word or date to be searched.
    arr1 (list): Array to be searched.
    arr2 (list): Second array to return result.
"""
def isMatch(A, arr1, arr2):
    index = binarySearch(arr1, A)
    if index != -1:
        return arr2[index]
    return 0

"""
Function to perform binary search on a sorted array.
Parameters:
    arr (list): Array to be searched.
    x (int): Element to be searched.
"""
def binarySearch(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# Open the file containing Wordle data
filename = "wordle.dat"
fh = open(filename, "r")

# Read all lines from the file
lines = fh.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

# Initialize lists to store words and dates
words = []
dates = []
for line in lines:
    # Split each line into components
    month, day, year, word = line.split()
    # Merge date components into a single date
    myDate = merge(year, month, day)
    # Append the date to the dates list
    dates.append(myDate)
    # Append the word to the words list
    words.append(word)

# Get the start and end dates from the dates list
startDate = dates[0]
endDate = dates[len(dates) - 1]

# Create a copy of dates to maintain the original order
original_dates = dates.copy()
original_words = words.copy()

# Sort the words and dates using merge sort
mergeSort(words, dates, 0, len(words) - 1)

print("Welcome to the Wordle Database!")
valid = False
userOption = ""
while not valid:
    # Prompt the user to choose an option
    userOption = input("Enter w if you are looking for a word, or d for a word on a certain date: ")
    if userOption.lower() == "w":
        valid = True
    elif userOption.lower() == "d":
        valid = True

if userOption == "w":
    valid = False
    while not valid:
        # Prompt the user to enter a word
        userInput = input("What word are you looking for? ").upper()
        if len(userInput) == 5:
            valid = True
    # Check if the word matches any in the database
    date = isMatch(userInput, words, dates)
    if date:
        print("The word %s was the solution to the puzzle on %d." % (userInput, date))
    else:
        print("%s was not found in the database." % userInput)
elif userOption == "d":
    valid = False
    while not valid:
        # Prompt the user to enter a date
        year = input("Enter the year: ")
        month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
        day = input("Enter the day: ")
        # Pad single-digit days with a leading zero
        if len(day) == 1:
            day = "0" + day
        # Merge date components into a single date
        date = merge(year, month, day)
        if date != 0:
            valid = True
    word = isMatch(date, original_dates, original_words)
    if date < startDate:
        print("%d is too early. No wordles occured before %d. Enter a later date." % (date, startDate))
    elif date > endDate:
        print("%d is too recent. Our records only go as late as %d. Please enter an earlier date." % (date, endDate))
    if word:
        print("The word entered on %d was %s." % (date, word))
