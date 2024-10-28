import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments, give 2")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments, give only 2")
    
print("Hello my name is", sys.argv[1])
