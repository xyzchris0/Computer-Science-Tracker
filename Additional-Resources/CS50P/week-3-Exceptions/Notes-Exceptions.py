###Part 1: Using 'Try' Blocks

#The line indented are the blocks you are trying
#try:
#    x = int(input("What's X?"))

#except ValueError:

#    print("X is not an integer")

#else:
#    print(f"X is {x}")


###Part 2: Using 'While'

while True:
    try:
         x = int(input("What's X?"))
    except ValueError:
    
        print("X is not an integer")

    else:
        print(f"X is {x}")
