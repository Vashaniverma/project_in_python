import random
fruit_name='''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''

fruit_name=fruit_name.split(' ')

computer=random.choice(fruit_name)
 
user_name=input("Enter Your name: ")
print("Good Luck '{user_name}'for the Hangman Game")
print("Guss the word! HINT: word is a name of a fruit")
print("Word length:", len(computer))
lenth=len(computer)

gussed_word=["_"]*lenth
attempts= lenth + 4

while attempts > 0 and "_" in gussed_word:
    print("\nCurrent word: ", " ".join(gussed_word))

    user=input("enter a letter to guss: ").lower()
    
    if user in computer:
        for index, letter in enumerate(computer):
            if letter == user:
                gussed_word[index] = user
        print(f"Good guess! '{user}' is in the word.")
    else:
        attempts -= 1
        print(f"'{user}' is not in the word. Attempts left: {attempts}")
    if "_" not in gussed_word:
        print("\nCongratulations! You guessed the word:", computer)
        break

if "_" in gussed_word:
    print("\nSorry, you've run out of attempts. The word was:", computer)    