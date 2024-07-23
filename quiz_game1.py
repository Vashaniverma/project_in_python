print("welcome to my computer quiz! ")

playing=input("Do you want to play? ")

if playing.lower() =="yes":
    print("Okay!let's play 😊")
    score=0

    answer=input("what does CPU stand for? ")
    if answer.lower() =="centeral processing unit":
        print("Correct!")
        score+=1
    else:
        print("InCorrect!")

    answer=input("What does GPU stand for? ")
    if answer.lower() =="graphics processing unit":
        print("Correct!")
        score+=1
    else:
        print("InCorrect!")

    answer=input("What does RAM stand for? ")
    if answer.lower() =="random access memory":
        print("Correct!")
        score+=1
    else:
        print("InCorrect!")

    answer=input("What does PSU stand for? ")
    if answer =="power supply":
        print("Correct!")
        score+=1
    else:
        print("InCorrect!")

    print(f"You got {score} questions correct! " )
    print(f"You got {(score/4)*100}%. " )
else:
    exit()

