# Write a python program to check the user input abbreviation.
# If the user enters "lol", print "laughing out loud".
# If the user enters "rofl", print "rolling on the floor laughing".
# If the user enters "lmk", print "let me know".
# If the user enters "smh", print "shaking my head"

def check(abbr):
    if abbr == "lol":
        print("laughing out loud")
    elif abbr == "rofl":
        print("rolling on the floor laughing")
    elif abbr == "lmk":
        print("let me know")
    elif abbr == "smh":
        print("shaking my head")
    else:
        print("No abbreviations!!")


if __name__ == '__main__':
    abbr = input("Enter input abbreviation : ")
    check(abbr)
