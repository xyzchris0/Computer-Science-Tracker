number = input("Expression:  ").strip()

x, y, z = number.split(" ")

x = int(x)
z = int(z)

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "/":
    result = x / z
elif y == "*":
    result = x * z

print(f"{result:.1f}")