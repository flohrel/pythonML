import string

def text_analyzer(*args):
    '''
    Summarizes upper-case and lower-case letters, punctuation, and space characters in the text given as parameter.
    If no argument is given, reads from standard input.
    '''
    if len(args) > 1:
        print("ERROR")
        exit()
    elif not len(args):
        print("What is the text to analyse?")
        arg = input(">> ")
    else:
        arg = args[0]
    if not len(arg):
        print("ERROR")
        exit()
    upper = sum(1 for c in arg if c.isupper())
    lower = sum(1 for c in arg if c.islower())
    punc = sum(1 for c in arg if c in string.punctuation)
    space = sum(1 for c in arg if c.isspace())
    print("The text contains", len(arg), "character" if len(arg) < 2 else "characters")
    print("-", upper, "upper", "letter" if upper < 2 else "letters")
    print("-", lower, "lower", "letter" if lower < 2 else "letters")
    print("-", punc, "punctuation", "mark" if punc < 2 else "marks")
    print("-", space, "space" if space < 2 else "spaces")