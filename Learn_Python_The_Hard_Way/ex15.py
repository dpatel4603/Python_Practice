from sys import argv # import the argv library from system
# Parses the script and filename using argv
script, filename = argv
# opens the file
txt = open(filename)
# outputs the filename name and reads it
print(f"Here's your file {filename}:")
print(txt.read())
# Asks for hte filename
print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
