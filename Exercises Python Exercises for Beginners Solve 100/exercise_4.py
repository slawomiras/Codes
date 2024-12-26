s = input("Give string: ")

if len(s) < 6:
    print("")
else:
    print(s[:3] + s[-3:])