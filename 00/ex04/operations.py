import sys

def error_msg(arg):
    print("Input error:", arg)
    exit()

argc = len(sys.argv)

if argc < 3:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("\tpython operations.py 10 3")
    exit()
elif argc > 3:
    error_msg("too many arguments.")

try:
    nb1 = int(sys.argv[1])
    nb2 = int(sys.argv[2])
except:
    error_msg("only numbers")
    
print("Sum:\t\t", nb1 + nb2)
print("Difference:\t", nb1 - nb2)
print("Product:\t", nb1 * nb2)

if (nb2 == 0):
    print("Quotient:\t ERROR (div by zero)")
    print("Remainder:\t ERROR (modulo by zero)")
else:
    print("Quotient:\t", float(nb1 / nb2))
    print("Remainder:\t", nb1 % nb2)