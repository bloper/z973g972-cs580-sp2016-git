#Programmed using Python 3.4.2
#Testing times of sorting lists of N length (set by user) using QuickSort
#Help with "PARTITION" code from a forum:
#       http://stackoverflow.com/questions/18262306/quick-sort-with-python
#somewhere about halfway down the page.

import time
import random
import sys


#Since max recursion range is 1000 by default, we must raise this to over 1000 for program use
sys.setrecursionlimit(6500)

MAX_RANGE = 10000

########################################

#QuickSort
def QUICKSORT(myList, start, end):
    if start < end:
        mid = PARTITION(myList, start, end)
        QUICKSORT(myList, start, mid-1)
        QUICKSORT(myList, mid+1, end)
    else:
        return

########################################

#Partition
def PARTITION(myList, start, end):
    pivot = start
    for i in range(start+1, end+1):
        if myList[i] <= myList[start]:
            pivot += 1
            myList[i], myList[pivot] = myList[pivot], myList[i]
    myList[pivot], myList[start] = myList[start], myList[pivot]
    return pivot

########################################
#Other Functions

def buildSameList(numIntegers):
    myList = []
    num = random.randrange(0,MAX_RANGE)
    for i in range(0,numIntegers):
        myList.append(num)
    return myList

def buildRandomList(numIntegers):
    myList = []
    for i in range(0,numIntegers):
        num = random.randrange(0,MAX_RANGE) #selects a number between 0 and 10,000 (MAX_RANGE)
        myList.append(num)
    return myList

def printList(myList, end, label):
    outfile = open("output.txt", 'a')
    outfile.write(str(label) + ":\n")
    for i in range(0, end):
        outfile.write(str(myList[i]) + "\n")
    outfile.close()

########################################

def main():
    print("This program shows the time it takes for a set of numbers to be sorted by a QuickSort algorithm.")
    print("(The limit for input is 5000, because Python code limits for recursion is below 10000.)\n")

    #Get valid input from User, must be 5000 or less
    valid = 0
    while not valid:
        numIntegers = eval(input("Please enter the number of integers you would like to sort (5000 or less): "))
        if (numIntegers <= 5000) and (numIntegers > 0):
            valid = 1
        else:
            print("INVALID INPUT: Try again")

    print("We will sort ", numIntegers, " of all the same number, and ", numIntegers, " random numbers ranging between 0 and 10,000.\n")

    #print("Recursion limit is: ", sys.getrecursionlimit())

    #Build lists to test with Quicksort
    sameList = buildSameList(numIntegers)
    randomList = buildRandomList(numIntegers)

    #Quicksort the Lists
    startTime = 0
    endTime = 0
    sameTime = 0
    end = numIntegers - 1
    #startTime = time.clock() #not accurate enough
    startTime = time.time()
    QUICKSORT(sameList, 0, end)
    endTime = time.time()
    sameTime = endTime - startTime

    startTime = 0
    endTime = 0
    randomTime = 0
    startTime = time.time()
    QUICKSORT(randomList, 0, end)
    endTime = time.time()
    randomTime = endTime - startTime

    #Test print both Lists:
    print("Saving both lists sorted with QuickSort to output file for review:")
    outfile = open("output.txt", 'a')
    outfile.write("***Lists sorted using QuickSort***\n")
    outfile.close()
    print("Writing \"same list\" to output.txt")
    printList(sameList, len(sameList), "Same List")
    print("Writing \"random list\" to output.txt")
    printList(randomList, len(randomList), "Random List")

    #Print times
    print("\nList with the same number time was: ", "{0:.20f}".format(sameTime), "seconds")
    print("List with all random numbers time was: ", "{0:.20f}".format(randomTime), "seconds")
    print("This shows that worst case for QuickSort is an already sorted set of numbers (e.g. all same numbers).")

    print("\n\nEND OF PROGRAM")

main()
