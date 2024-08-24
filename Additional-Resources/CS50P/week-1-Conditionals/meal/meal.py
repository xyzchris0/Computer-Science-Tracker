def main():
    meal_time = input("What time is it?  ").strip()
    time_in_hours = convert(meal_time)

    if 7.0 <= time_in_hours <= 8.0:
        print("It's breakfast time!")
    elif 12.0 <= time_in_hours <= 8.0:
        print("It's lunch time!")
    elif 18.0 <= time_in_hours <= 19.0:
        print("It's dinner time!")

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    return hours + minutes /60
    ...


if __name__ == "__main__":
    main()
