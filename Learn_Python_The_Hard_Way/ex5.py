# Sets the variables
name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # in inches
weight = 180  # lbs
eyes = "blue"
teeth = "white"
hair = "brown"
# Prints a small paragraph about Zed A. Shaw
print(f"Lets Talk about {name}.")
print(f"He's {height} inches tall")
print(f"He's {weight} pounds heavy")
print("Actually that's not heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")
# Converts height and weight to the metric system, with weight in Kg and height in cm
weight_kg = round(180 / 2.2)
print(f"Approximate Weight in Kilograms {weight_kg}kg")
height_cm = height + 2.54
print(f"Height in centimeters {height_cm}cm")
# Adds up all of the numbers of age, height, and weight
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
