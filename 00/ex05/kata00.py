t = (19,42,21)
s = "The {} numbers are {}"

print(s.format(len(t), ", ".join(str(i) for i in t)))