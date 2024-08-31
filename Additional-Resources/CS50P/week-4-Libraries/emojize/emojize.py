import emoji 

def main():

    input_user = input("Input:  ")

    emojized = emoji.emojize(input_user, language='alias')

    print(emojized)


if __name__ == "__main__":
    main()