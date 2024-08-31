def main():
    months = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            if "/" in date:
                month, day, year = date.split("/")
                if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                    print(f"{int(year):04}-{int(month):02}-{int(day):02}")
                    break

            elif "," in date:
                month_str, day, year = date.replace(",", "").split()
                if month_str in months and 1 <= int(day) <= 31:
                    month = months.index(month_str) + 1
                    print(f"{int(year):04}-{month:02}-{int(day):02}")
                    break

        except (ValueError, IndexError):
            pass

if __name__ == "__main__":
    main()
