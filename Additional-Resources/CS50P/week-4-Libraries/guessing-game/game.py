import random

def main():
    
    while True:

        try:
            level_game = int(input("Level: "))
            if  level_game > 0:
                break
        
        except:
            pass

    random_number = random.randint(1, level_game)

    while True:

        try:
            guess = int(input("Guess:  "))
            if guess > 0:
                print("Too Small!")

            elif guess > random_number:
                print("Too Large!")
            else:
                print("Just Right!")
                break
    

        except:
            pass

if __name__ == "__main__":
    main()
