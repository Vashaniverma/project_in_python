print("Player 2 is Computer ")
print("Rules of Game, if any one print 21 will lose the game ! ")
a=input("Do you want to start the game? (yes/no):\n").lower()

computer=[]
c=0
if (a=="no"):
    exit()
else:
    A=input("Enter 'F' to take the First chance or Enter 'S' to take the Second chance. \n").lower()
    
    def F():
        global c
        if 21 not in computer and len(computer)<21:
            n=int(input("How many numbers do you wish to enter? \n"))
            print("Enter your values: ")
            for _ in range(n):
                
                while True:
                    b=int(input("> "))
                    if b not in computer and 1 <= b <= 21:
                        computer.append(b)
                        break
                    else:
                        print("Number already used or out of range. Enter a different number:")
                
            
        computer.sort()
        c=len(computer)
        print("Order of inputs after your turn is:", computer)
        if c >= 21:
            print("YOU lost! Computer WON! ")
            exit()
        return c
    
    
    def com():
        global c
        
        if 21 not in computer and len(computer)<21:
            for i in range(1,3):
                if c+i not in computer:
                    
                    computer.append(c+i)
            computer.sort()
            c=len(computer)
            
            print("Order of inputs after computer's turn is:", computer)

        
            if c>21:
                print("I lost! YOU WON! ")
                exit()
            return c
    
    while True:
        if(A=='f' and c<21):
            F()
            if c>=21:
                break
            com()
        elif(A=='s' and c<21):
            com()
            F()
            if c>=21:
                break
        else: 
            break
print("Game Over. Final computer list:", list(set(computer)))