def cheese_and_crackers(cheese_count, boxes_of_crackers):  # Sets up the function defination for cheese and crackers
    print(f"You have {cheese_count} cheeses!")  # prints the first line of how many cheeses there are
    print(f"You have {boxes_of_crackers} boxes of crackers!")  # prints the second line of how many crackers there are
    print("Man that's enough for a party")  # prints a statement
    print("Get a blanket. \n")  # prints a statement and new line


print("We can just give the function numbers directly:")  # prints a statement
cheese_and_crackers(20, 30)  # calls cheese and crackers

print("Or, we can use variables from our script:")  # prints a statement

amount_of_cheese = 10  # defines a variable of cheese
amount_of_crackers = 50  # define a variable of crackers

cheese_and_crackers(amount_of_cheese, amount_of_crackers)  # calls a cheese_and_crackers with input of new variables

print("We can even do math inside too:")  # prints a new statement
cheese_and_crackers(10 + 20, 5 + 6)  # calls cheese_and_crackers with a new values

print("And we can combine the two, variables and math: ")  # prints a new statement
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)  # calls the function and utilizes variables
# and math
