'''
Author: Alice Mungamuri
KUID: 3117704
Date:03/05/2024
Lab: lab#3
Last modified: 03/05/2024
Purpose:Secret Word Guess
'''
word = 'bringcoffee'.upper()
numGuess = 0
ltrsCorrect = 0
guess = input('Guess the secret phrase!\n').upper()
numGuess+= 1

while guess != word.upper():
  if len(guess) < len(word):
    print('Too few characters')
    guess = input('Guess: ').upper()
    numGuess +=1
  elif len(guess) > len(word):
    print('Too many characters')
    guess = input('Guess: ').upper()
    numGuess += 1
  elif len(guess) == len(word):
    ltrsCorrect = 0
    #for i in  (0, 10):
        #if guess[i]== word[i]:
            #ltrsCorrect += 1
    if guess[0]== word[0]:
        ltrsCorrect += 1
    if guess[1]== word[1]:
        ltrsCorrect += 1
    if guess[2]== word[2]:
        ltrsCorrect += 1
    if guess[3]== word[3]:
        ltrsCorrect += 1
    if guess[3]== word[3]:
        ltrsCorrect += 1
    if guess[4]== word[4]:
        ltrsCorrect += 1
    if guess[5]== word[5]:
        ltrsCorrect += 1
    if guess[6]== word[6]:
        ltrsCorrect += 1
    if guess[7]== word[7]:
        ltrsCorrect += 1
    if guess[8]== word[8]:
        ltrsCorrect += 1
    if guess[9]== word[9]:
        ltrsCorrect += 1
    if guess[10]== word[10]:
        ltrsCorrect += 1



         
     
         
         


    print('Correct Letters: '+ str(ltrsCorrect - 1))
    guess = input('Guess: ').upper()
    numGuess +=1



      
      
    
    
    

print('Correct!')
print('Number of Guesses: '+ str(numGuess))
    
