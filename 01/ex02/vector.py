import sys

class Vector:
    def __init__(self, values):
        if type(values) == tuple:
            if len(values) != 2:
                sys.exit("Bad range")
            self.values = None
            for x in range(values[0], values[1]):
                self.values += list((x, 0))

    def shape(self):
        print(sum(1 for i in self.values))