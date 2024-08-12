import random
computer=random.randint(1000,10000)
print(computer)

user= int(input(f"Guess the 4 digit number: "))

if(user==computer):
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    n=0
    while(user!=computer):
        n=n+1
        count=0
        user=str(user)
        computer=str(computer)
    
        gussed_number=["X"]*4
    
        for i in range(0,4):
            if(user[i]==computer[i]):
                count=count+1
                gussed_number[i]=user[i]
            else:
                continue

        print(f"Not quite the number. But you did get '{count}' digit(s) correct!")
       
        print(" ".join(gussed_number))
        
        
        while "X" in gussed_number:
            user=int(input("Enter your choice of number: "))
            break
        
        if(count==0):
            print("None of the numbers in your input match.")
            user=int(input("Enter your choice of number: "))

    if(user==computer):
        n=n+1
        print("You've become a Mastermind!")
        print("It took you only", n, "tries.")


    

    
