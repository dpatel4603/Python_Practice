
import random
import time

def setupVars():
    global rangeMin
    global rangeMax
    global intsList
    global evenNums
    global oddNums
    global sum
    global average
    global length
    global maxInt
    global minInt

    maxInt = 0
    minInt = 0
    rangeMin = 0
    rangeMax = 0
    intsList = []
    evenNums = 0
    oddNums = 0
    sum = 0
    average = 0
    length = 1

def receiveUserInputs():

    global rangeMin
    global rangeMax
    global length

    rangeMin = input("Input lowest number")
    rangeMax = input("Input highest number")
    length = input("How many numbers do you want")
def build_sortlist(rangeMin, rangeMax, length):
    global intsList
    global evenNums
    global oddNums
    global maxInt
    global minInt
    for i in range(0, int(length)):
        intsList.append(random.randint(rangeMin, rangeMax))
    for i in intsList:
        if i % 2 == 0:
            evenNums += 1
        else:
            oddNums += 1
    minInt = intsList[0]
    for i in intsList:
        if i < minInt:
            minInt= i
    maxInt = intsList[0]
    for i in intsList:
        if i < maxInt:
            maxInt = i
setupVars()

print("Lets create a list of random numbers")

time.sleep(2)

receiveUserInputs()

print("Building a list of length user desires")
time.sleep(1)
print("Filling list with random integers withing the givn range of", rangeMin, "and", rangeMax)
time.sleep(1)
print("Evaluating elements to count even numbers and odd numbers")
time.sleep(1)

build_sortlist(int(rangeMin), int(rangeMax), length)

print("the list: ", intsList)
print("There are ", evenNums, "even numbers in the list.")
print("There are ", oddNums, "odd numbers in the list..")


