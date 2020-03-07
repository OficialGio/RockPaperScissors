'''
Created on Feb 1, 2020

@author: ITAUser
'''
import random
keepPlaying = True
while (keepPlaying == True):
    print("Welcome!!!")
    print("Rock Paper Scissors rules: Best 2 out of 3 wins, Press 'q' to quit")
    #rock is 1, paper is 2, scissors is 3
    
    scoreComp = 0
    scorePlayer = 0
    
    
    while(scorePlayer < 2) and (scoreComp < 2):
        choiceComp = random.randint(1,3)
        choicePlayer = input("pick your item: Rock, paper, or scissors!")
       
        if(choicePlayer == "q"):
            keepPlaying = False
            break
        elif(choicePlayer == "rock" ) and (choiceComp == 1) or (choicePlayer == "paper" ) and (choiceComp == 2) or (choicePlayer == "scissors" ) and (choiceComp == 3):
            print("Bright minds think alike, it's a draw!")
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
           
        elif((choicePlayer == "rock" ) and (choiceComp == 2)) or ((choicePlayer == "paper" ) and (choiceComp == 3)) or ((choicePlayer == "scissors" ) and (choiceComp == 1)):
            print("And the computer takes this one! unlucky")
            scoreComp = scoreComp + 1
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
        elif((choicePlayer == "rock" ) and (choiceComp == 3)) or ((choicePlayer == "paper" ) and (choiceComp == 1)) or ((choicePlayer == "scissors" ) and (choiceComp == 2)):
            print("...that was all luck")
            scorePlayer = scorePlayer + 1
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
        else :
            print("It's a tough one")
           
    if (scorePlayer == 2):
            print("WINNER WINNER CHICKEN DINNER")
         
           
    if (scoreComp == 2):
            print("Lost against a computer? Really?")
           
    print("Computer's Score: ", + scoreComp , "Your Score: ", + scorePlayer)
    
