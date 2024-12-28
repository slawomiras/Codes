s = input("Write a string: ")
curr_char = ","
new_char = "."
new_s = ""

for char in s:
    if char == curr_char:
        new_s += new_char
    else:
        new_s += char

print(new_s)