def main():

    list = {}

    try:
        while True:
            item = input("Item:  ").title()
            if item in list:
                list[item] += 1
            else:
                list[item] = 1
                
    except EOFError:
        print("\nItems:")
        for item, count in list.items():
            print(f"{item}: {count}")


if __name__ == "__main__":
    main()