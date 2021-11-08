import sys
import string

if len(sys.argv) != 3 or sys.argv[1].isnumeric() or not sys.argv[2].isnumeric():
    print("ERROR")
    exit()

max_len = int(sys.argv[2])
str1 = sys.argv[1].translate(str.maketrans('', '', string.punctuation))
str2 = str1.split(" ")
lst = [word for word in str2 if len(word) > max_len]
print(lst)