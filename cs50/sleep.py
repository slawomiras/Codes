def main():
    n = int(input("What's n? (how many sheeps) "))
    for s in sheep(n):
        print(s)
    
        
def sheep(n):
    flock = []
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()
