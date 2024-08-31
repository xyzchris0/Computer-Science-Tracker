###Part 1: Using 'While' loops

#i = 0
#while i != 0:
#while i < 3:
#    print("hello")
#    i += 1 #Same as 'i = + 1'

###Part 2: Using 'List'

#Helps to simplify things a bit; 

# The brackets represent a List '[]'

#for i in [0, 1, 2]:
#    print("Hello")

###Part 3: Using 'Ranges'

# The Range is a Function and will need 1 argument

# The 'i' is used for counting 

# Will go up to but not thru that number

#for i in range(10):
#    print("Hello")

###Part 4: Renaming 'i' as a single underscore (Dont have to but
# it helps)

#for _ in range(3):
#    print("Hello")

###Part 5: Using 'Print' instead to do on 1 line. Use 'end=""' to remove space

#print("hello\n" * 3, end="")

###Part 6: Using 'While Loops'

#while True:
#    n = int(input("What's n? "))

#    if n > 0:
#        break

#for _ in range(n):
#    print("Hello")

###Part 7: Using 'List'

#students = ["H", "H2", "R"]

#for student in students:
#    print(student)

###Part 8: Using Numbers to iterate over

#students = ["H", "H2", "R"]

#for i in range(len(students)):
#    print(i + 1, students[i])

###Part 9: Using a 'Dict' or 'Key Values' for 2 items

#students = {
#    "H": "Hello",
#     "H2": "GoodBye",
#     "R": "Dias",
#     "L": "Hola"
#     }
#for student in students:
#    print(student, students[student], sep=", ")

###Part 9: Using a 'Dict' or 'Key Values' for 3 items

students = [
    {"name": "H", "House": "Casa", "Check": "Mate"},
    {"name": "H2", "House": "Casa1", "Check": "Mate"},
    {"name": "H3", "House": "Casa2", "Check": "Mate"},
    {"name": "H4", "House": "Casa3", "Check": "None"},

]

for student in students:
    print(student["name"], student["House"], student["Check"], sep=", ")