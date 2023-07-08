import os
import random
import hangman_words 
import hangman_art
#delete word_list =["wood", "chair" , "beautiful"]

chosen_word=random.choice(hangman_words.word_list)
word_length=len(chosen_word)
print(hangman_art.logo)
lives=6


#testing section
print(f'the solution is {chosen_word}')

#cretae a empty list to fill blank with length of chosen word
display=[]
for _ in range(len(chosen_word)):
    display += "_"

end_of_game=False 

while not end_of_game  :    
    guess=input("guess a letter: ").lower()
    os.system('cls')
    #if the user thas entered letter before entered
    if guess in display:
        print(f'you have already guessed{guess}')
    
    #check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess :
            display[position]=letter  
    if guess not in chosen_word:
        print(f"you guessed {guess}, that's not in word.You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game= True
            print("you lose")   
    #check all things true          
    if "_" not in display:
        end_of_game =True
        print("You win")
    print(f'your lives is {hangman_art.stages[lives]}') 
    print(display)
