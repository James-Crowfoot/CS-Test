from random import randint
from functions import *
from colorama import *
from math import trunc
from time import sleep
import sys

print("CSTv4\\")


red("   _____  _____  _____ ______    _____                            _               _____      _                       _______        _            ")
red("  / ____|/ ____|/ ____|  ____|  / ____|                          | |             / ____|    (_)                     |__   __|      | |           ")
yellow(" | |  __| |    | (___ | |__    | |     ___  _ __ ___  _ __  _   _| |_ ___ _ __  | (___   ___ _  ___ _ __   ___ ___     | | ___  ___| |_ ___ _ __ ")
green(" | | |_ | |     \\___ \\|  __|   | |    / _ \\| '_ ` _ \\| '_ \\| | | | __/ _ \\ '__|  \\___ \\ / __| |/ _ \\ '_ \\ / __/ _ \\    | |/ _ \\/ __| __/ _ \\ '__|")
blue(" | |__| | |____ ____) | |____  | |___| (_) | | | | | | |_) | |_| | ||  __/ |     ____) | (__| |  __/ | | | (_|  __/    | |  __/\\__ \\ ||  __/ |   ")
cyan("  \\_____|\\_____|_____/|______|  \\_____\\___/|_| |_| |_| .__/ \\__,_|\\__\\___|_|    |_____/ \\___|_|\\___|_| |_|\\___\\___|    |_|\\___||___/\\__\\___|_|   ")
print("                                                     | |                                                                                         ")
print("                                                     |_|                                                                                         ")

sleep(2)

# Import Questions
cyan("Which Paper do you want to revise - 1 Computer Systems , or 2 Algorithmic Thinking, enter 1 or 2.")
if "1" in input():
    file = open("questions1.txt","rt")
elif "2" in input():
    file = open("questions2.txt","rt")
else:
    red("Invalid input, enter either 1 or 2")
    sys.exit("Please Restart Program")

questions = []
length = file.readline()
length = int(length[0:3])
for i in range(0,length):
    line = file.readline()
    questions.append(line)

CorrectAnswers = 0
IncorrectAnswers = 0

UnansweredQuestions = len(questions)
AnsweredQuestions = 0
UnansweredQuestionNumbers = GenerateQuestionNumbers(UnansweredQuestions,0)


while UnansweredQuestions > 0:
    CurrentQuestionNumber = RandomQuestionNumber(UnansweredQuestionNumbers) #Selects a random question which is unanswered
    UnansweredQuestionNumbers.remove(CurrentQuestionNumber) #Removes this question from unanswered list
    UnansweredQuestions -= 1 

    Question = (questions[CurrentQuestionNumber]).split(",") #breaks up question into the individual segments

    RequiredAnswers = int(Question[0]) #How many individual answers are needed for the question
    CurrentQuestion = Question[1] #the question to be asked
    CurrentAnswers=[]
    for i in range(2,len(Question)-1):
        CurrentAnswers.append(Question[i]) #extracts all answers for question into separate array

    print("") # creates line break
    cyan(CurrentQuestion) #prints question in cyan
    
    if RequiredAnswers == 1:
        UserAnswer = str(input())
        if UserAnswer.upper() in CurrentAnswers: #if the inputted answer matches answer data base
            green("Correct!")
            CurrentAnswers.remove(UserAnswer.upper())
            CorrectAnswers+=1
        else:
            red("Incorrect")
            print("Correct answers: ",CurrentAnswers) #shows possible answers that could have been 
            IncorrectAnswers+=1
    else:
        Correct = 0
        GivenAnswers = 0
        txt = ("Requires "+str(RequiredAnswers)+" answers.")
        yellow(txt)

        while GivenAnswers < RequiredAnswers:
            UserAnswer = str(input())
            GivenAnswers +=1
            if UserAnswer.upper() in CurrentAnswers:
                green("correct")
                Correct += 1
                CurrentAnswers.remove(UserAnswer.upper())
            else:
                red("incorrect")

        if Correct < RequiredAnswers:
            print("Correct answers: ",CurrentAnswers)
            IncorrectAnswers+=1
        elif Correct == RequiredAnswers:
            CorrectAnswers+=1
    

print("\n------------------")
print("Questions Complete")

Average = (CorrectAnswers/(CorrectAnswers+IncorrectAnswers))*100

txt = (str(CorrectAnswers)+" Correct")
green(txt)
txt = (str(IncorrectAnswers)+" Incorrect")
red(txt)
txt = ("Average of "+str(round(Average,2))+"%")
blue(txt)

