def main():
    total_cost = 0
    
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    
    while True:
        try:
            food = input("Item: ").title()
            if food in menu:
                total_cost += menu[food]
                print(f"Total: $",f"{total_cost:.2f}", sep="")
            
        except:
            return main
    

if __name__ == "__main__":
    main()
