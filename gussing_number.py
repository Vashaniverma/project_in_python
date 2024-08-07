a=input("Enter the first number where the range is start: ")
b=input("enter the second number where the range is end: ")

a=int(a)
b=int(b)

import random
d=random.randint(a,b)
i=0

while True:
    i=i+1
    c=input("Guess a number: ")
    c=int(c)

    if(d>c):
        print("Try Again! Your gussed too small")
    elif(d<c):
        print("Try Again! Your gussed too high")
    else:
        print("your gussed is right")
        break
print("Total number of Guesses=",i)
