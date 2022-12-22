import random

print("Shaking the Dice")


def generateRandnum(number):
    number_of_rolls_list = []
    constant = 1 / 6
    theoretical = constant ** number
    for i in range(number):
        randNum = random.randint(1, 6)
        number_of_rolls_list.append(randNum)
        print("You rolled a", randNum)
    if number >= 1:
        print("Theoretical probability of rolling these number(s) is", theoretical * 100)
    return randNum


number_of_questions = input("How many numbers do you want answered:  ")
number_of_questions = int(number_of_questions)
if number_of_questions < 1:
    print("[INFO] ERROR please input a number greater than 1")
generateRandnum(number_of_questions)
