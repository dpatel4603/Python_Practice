import random


def odd_even_pred(total_nums, highest_num):
    odd = 0
    even = 0
    sum = 0
    randomlist = []
    for i in range(0, total_nums):
        n = random.randint(1, highest_num)
        randomlist.append(n)
    for number in randomlist:
        if number % 2 == 1:
            odd = odd + 1
        if number % 2 == 0:
            even = even + 1
        sum = sum + number
    avg = sum / len(randomlist)
    print(f"There are {even} even number(s)")
    print(f"There are {odd} odd number(s)")
    print(f"The average of the list is {avg}")


odd_even_pred(100, 50)

