def main():
    x = input("Input: ")

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    result = ""

    for i in range(len(x)):
        if x[i] not in vowels:
            result = result + x[i]

    print(f"Output: {result}")

if __name__ == "__main__":
    main()