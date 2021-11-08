import sys

if len(sys.argv) != 2:
    print("ERROR")

try:
    arg = int(sys.argv[1])
except:
    print("ERROR")
    exit()

if arg == 0:
    print("I'm zero")
elif (arg % 2) == 0:
    print("I'm even")
else:
    print("I'm odd")