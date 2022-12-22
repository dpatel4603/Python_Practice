name = "Dev"
age = 15
print("Hello, %s is %d years old" % (name, age))

# %s means string, or any object with a string representation ie numbers
# %d means integers
# %f means floating numbers
data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string + " %s %s Your Current Balance is %s " % data)
# print(format_string + data[0] + data[1] + " Your Current Balance is" + data[2])
