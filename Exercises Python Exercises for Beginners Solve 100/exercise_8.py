s = input("Write a string: ")
old_char = input("Write a letter to be replaced: ")
new_char = input("Write a letter to replace with: ")

if old_char in s:
    print(s.replace(old_char, new_char))
else:
    print(s)

#Option 2
""" 
s = input("Write a string: ")
curr_char = input("Write a letter to be replaced: ")
new_char = input("Write a letter to replace with: ")
new_s = ""

for char in s:
    if char == curr_char:
        new_s += new_char
    else:
        new_s += char

print(new_s)
 """