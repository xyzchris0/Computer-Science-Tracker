#Step 1: Prompts user for a mass as an interger in Kilos

#Step 2: OutPuts the number as an integer.

m = int(input("M: "))
#int will convert the string into an integer

e = m * (300000000 ** 2)
#** 2 will cal the square of the speed of light

print("Energy:", e)
