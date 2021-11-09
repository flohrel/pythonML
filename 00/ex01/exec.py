import sys

str = " ".join(sys.argv[1:])
str = str[::-1].capitalize()
print(str)