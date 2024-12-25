print("Here's your calculator. Give two numbers")
x = float(input("What's x? "))
y = float(input("What's y? "))

print("Here's your result")

#rounding digits - one way below
#z = round(x / y, 3)

z = x / y

#second way below

print(f"{z:.2f}")


