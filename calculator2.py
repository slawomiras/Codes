def main():
    print("Hello to my calculator, human. Please give x and you will receive square :)")
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n
    
main()
