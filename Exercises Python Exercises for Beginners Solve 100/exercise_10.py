# -----------------
# One way
# -----------------

# import string

# s = input("Write a string: ").strip().lower()
# set_s = set(s)

# print(set_s == set(string.ascii_lowercase))

# -------------
# another way
# -------------

import string

s = input("Write a string: ").strip().lower()

is_char = True

for char in string.ascii_lowercase:
    if char not in s:
        is_char = False
        break

print(is_char)
