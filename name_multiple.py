import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments, give 2")
    
for arg in sys.argv[1:]:
    print("Hello my name is", arg)
