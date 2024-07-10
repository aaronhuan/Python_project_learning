import random
from hangman_art import stages
from hangman_words import word_list
from hangman_art import logo
lives = 6 
word_chosen= random.choice(word_list)
word_len = len(word_chosen) #length of word 


end_game = False 

print (logo) 
#print (word_chosen) #debugging testing code


display = []            #display list for user 

for letter in word_chosen:      #loop through the word chosen
    display.append("_")         #add underscores to signify letter

while end_game != True:
    guess = input("Guess a letter: ").lower() #user input 
    if guess in display:
        print (f"You've already guessed {guess}")


    for check in range(word_len):  # for loop to check the input 
        letter = word_chosen[check]        #sets variable letter = the letter of the word chosen we are checking 
        if letter== guess:              #if input and letter matches 
            display[check]= letter       #replace "_" with the letter

    if guess not in word_chosen:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives ==0:
            end_game = True
            print("you lose.")

    print(f"{' '.join(display)}")

    if "_" not in display: 
        end_of_game = True
        print("You win.")
        
    
    print (stages[lives])

