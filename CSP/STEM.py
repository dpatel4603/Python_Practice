
from math import log
import numpy as np

def calc_log(base, output):
    ans = log(output, base)
    if base <= 0:
        print("Base cannot be less than or equal to 0")
    for i in range(1):
        print("Function works for loop:  ", i)



    return ans
questions = int(input("How many questions do you want to answer:  "))

i = 0
ans_list = np.zeros(questions)

while questions > i:
    base = int(input("What base is the log: "))
    output = int(input("What is the argument of the log: "))
    if base == 1 & output != 1:
        print("ERROR not possible")
        break

    ans1 = calc_log(base, output)
    ans_list[i] = ans1

    print("The answer is: ", ans_list[i])
    i += 1



