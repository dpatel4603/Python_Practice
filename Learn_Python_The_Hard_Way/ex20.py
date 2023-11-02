from sys import argv  # imports the necessary libraries

script, input_file = argv  # sets up the values for argv


def print_all(f):  # sets up the function print_all
    print(f.read())  # prints each character in the file


def rewind(f):  # sets up the function rewind
    f.seek(0)  # resets the file back to the first character


def print_a_line(line_count, f):  # defines a function called print_a_line
    print(line_count, f.readline())  # based off of the line count it reads that line


current_file = open(input_file)

print("First let's print the whole file: \n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
