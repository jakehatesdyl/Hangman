import random
import os
mode=""
while mode!="easy" and mode!="medium"and mode!="hard":
    mode=input("Welcome to my hangman game what mode would you like to play - easy,medium or hard ").lower()
print("You selected",mode)
listOfWordTypes= os.listdir("quizfiles")
question = ("What word type would you like to play?",listOfWordTypes)
wordType=""
while wordType not in listOfWordTypes:
    wordType=input(question)

fileToOpenWithFullPath = "./quizfiles/" + wordType
print(fileToOpenWithFullPath)

with open(fileToOpenWithFullPath) as fileOfWords:
    listOfWords =  fileOfWords.readlines()
    wordToGuess = random.choice(listOfWords)
fileOfWords.close()


answer=wordToGuess.strip()


correctLetters= set()
lettersInAnswer=len(set(answer))
if mode == "easy":
    numberOfLives=11
elif mode == "medium":
    numberOfLives=8
if mode == "hard":
    numberOfLives=5
correctAnswers=0



while numberOfLives>0 and lettersInAnswer!=correctAnswers:
    printedanswer=""
    for letters in answer:
        if(letters) in correctLetters:
            printedanswer = printedanswer+ letters
        else:
            printedanswer = printedanswer +"*"
    print("The word is",printedanswer)
    print("You have",numberOfLives,"lives")
    guess=input("What is your guess?")
    if guess in answer and guess not in correctLetters:
        correctAnswers=correctAnswers+1
        correctLetters.add(guess)
        print("")
        print("That is correct")
    elif guess not in answer:
        numberOfLives=numberOfLives-1
        print("")
        print("That is not in the word")
    else:
        print("")
        print("You have already guessed that")
if numberOfLives==0:
    print("You have lost the answer was",answer)
if correctAnswers==lettersInAnswer:
    print("You have won the word was",answer)
