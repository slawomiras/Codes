word = input("What's the word?: ")
index = int(input("What's the position of letter?: "))


def main():
    if len(word) == 0:
        print("Empty string")
    elif index < len(word):
        i = index - 1
        print(word[i])
    else:
        print("index value is out of range")

main()