### Notes for Week1 Conditionals

###Part 1: Using if Statements

#Create Compare.py

#x = int(input("What's x?"))
#y = int(input("What's y?"))

#boolen expression that has yes or no

#if x < y:
#    print("x is less than y")

#if x > y:
#    print("x is greater than y")

#if x == y:
#    print("x is equal to y")


###Part 2: elif


#if x < y:
#    print("x is less than y")

#elif x > y:
#    print("x is greater than y")

#else:
#    print("x is equal to y")


###Part 3: Added complexity
 
#if x < y or x > y :
#    print("x is not equal to y")

#else:
#    print("x is equal to y")

###Part 4: Using; Grade.py 

#score = int(input("Score: "))

#if score >= 90 and score <= 100:
#    print("Grade: A")
#elif score >= 80 and score <= 90:
#    print("Grade: B")
#elif score >= 70 and score <= 80:
#    print("Grade: C")
#elif score >= 60 and score <= 70:
#    print("Grade: D")
#else:
#    print("Grade: F")

###Part 5: Parity

#x = int(input("What's x? "))

#if x % 2 == 0:
#    print("Even")
#else:
#    print("Odd")

###Part 5.1: Parity def w/ bool

def main():
    x = int(input("What's X? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()