mode=input("Welcome to my hangman game what mode would you like to play - easy,medium or hard ")
print("You selected",mode)
answer="watermelon"
correctLetters= set()
lettersInAnswer=len(set(answer))

correctAnswers=0
numberOfLives=11
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
    if guess in answer:
        correctAnswers=correctAnswers+1
        correctLetters.add(guess)
        print("")
        print("That is correct")
    
    else: 
        numberOfLives=numberOfLives-1
        print("")
        print("That is not in the word")
if numberOfLives==0:
    print("You have lost the answer was watermelon")
if correctAnswers==lettersInAnswer:
    print("You have won the word was watermelon")