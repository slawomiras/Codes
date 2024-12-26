def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
   return n + n

#Można też napisać to tak
#def square(n):
#    n = pow(n, 2)
#    return n

if __name__ == "__main__":
    main()