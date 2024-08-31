def main():
    total_due = 50
    accepted_coins = [25, 10, 5]

    while total_due > 0:
        print(f"Amount due is: {total_due} cents")

        coin = int(input("Insert Coin:  "))

        if coin in accepted_coins:
            total_due -= coin
        
    print(f"Change owed: {abs(total_due)} cents")
    

if __name__ == "__main__":
    main()