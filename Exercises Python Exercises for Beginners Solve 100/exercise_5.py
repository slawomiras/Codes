s = input("Write a word: ")
new_s = ""

for i in range(1, len(s), 2):
        new_s += s[i]

print(new_s)