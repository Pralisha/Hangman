import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

import hangman_art
import hangman_words
lives=6
# random_words=['camel', 'entertainment', 'school','vehicle']
chosen_word=random.choice(hangman_words.word_list)
print(hangman_art.logo)
print(chosen_word)
display=[]
for _ in chosen_word:
    display+='_'
word_length=len(chosen_word)    
end_of_game=False
while not end_of_game:
        
    guess=input("Enter a guess letter :").lower()
    cls()
    if guess in display:
        print (f'You have already guessed the letter {guess}')
    else:
    
        
        for i in range(0,word_length):
            letter=chosen_word[i]
            
            if letter==guess:
                
                display[i]=letter
    
    if guess not in chosen_word:    
        lives=lives-1
        print(f'You guessed wrong letter {guess}, you lose a life.')
    if lives == 0:
        end_of_game=True
        print("\n You lose :/")
    print (hangman_art.stages[lives])
    print(display)    
    
    
    if '_' not in display:
        end_of_game=True 
        print("\n You win!")
    