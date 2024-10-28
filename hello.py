# Ask user for their name, remove spaces, make capital letters
name = input("What's your name? ").strip().title()

#Split users name in two
first, last = name.split(" ")

# Say hello to user
print("Hello," , last, first)
