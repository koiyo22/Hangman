import os
import re

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
word = input("----------------------------------------------------\n         Welcome to the Hangman Game!\n----------------------------------------------------\nInput a word for others to guess: ")
while re.search(r"[!@#$%^&*()?~]", word) or re.search(r'\d', word):
    word= input("\nInvalid word. Please enter a word without numbers and symbols: ")

max_guesses = int(input("\nSet a limit for the number of guesses: "))

word_list = list(word)

clear_console()

print("----------------------------------------------------\nWe got your input!\nNow pass it over for your friends to guess!\n")

answer = []

for i in word:
    answer.append('_ ')
    
for i in answer:
    print(i, end='')

for i in range(1,max_guesses+1):
    
    guess = input("\nInput a character to guess the word: ")

    if len(guess) > 1:
        print("Please only enter ONE character.")
        guess=input("\nInput a character to guess the word: ")
    
    if guess in word_list:
        position = word_list.index(guess)
        print("Good guess! You have ", max_guesses-1, " attempt(s) left.\n")
        word_list[position] = 0
        answer[position] = guess
        for i in answer:
            print(i, end=' ')
        
        if "_ " not in answer:
            print("\nYou won! Great job on guessing all the letters!")
            break
            
    else:
        for i in answer:
            print(i, end=' ')
        print("\nAhh no luck there. You have ", max_guesses-1, " attempt(s) left.\n")
        
    max_guesses -=1
    
    if (max_guesses == 0) and ("_ " in answer):
        print("\n----------------------------------------------------\nGAME OVER. The answer was ",word.upper(),"\n----------------------------------------------------")
        break