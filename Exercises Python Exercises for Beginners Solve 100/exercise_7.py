s = input("Write a string: ")
n = (int(input("Pick a number: ")) - 1)

if (len(s) == 0) or (len(s) < n):
    print(s)
else:
    new_s = ""
    for i in range(len(s)):
        if i != n:
            new_s += s[i]
    print(new_s) 