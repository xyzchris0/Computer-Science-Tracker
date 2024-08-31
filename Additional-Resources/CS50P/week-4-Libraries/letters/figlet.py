import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

def main():

    if len(sys.argv) == 1:
        isRandomFont = True

    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        isRandomFont = False
    
    else:
        sys.exit(1)


    figlet.getFonts()

    if isRandomFont == False:
        try:
            figlet.setFont(font=sys.argv[2])
        
        except:
            print("Not Valid input")
            sys.exit(1)

    else:
        font = random.choice(figlet.getFonts())

    
    user_input = input("Input:  ")

    print("Output: ")
    print(figlet.renderText(user_input))




if __name__ == "__main__":
    main()