from random import randint
from colorama import *
from time import sleep


def GenerateQuestionNumbers(amount,start):
    Numbers = []
    if start == 0:
        for i in range(0,amount):
            Numbers.append(i)
    elif start == 0:
        for i in range(1,amount+1):
            Numbers+=1
    else:
        raise Exception
    return Numbers

def RandomQuestionNumber(options):
    QuestionNumber = options[randint(0,len(options)-1)]
    return QuestionNumber

def green(text):
    print(Fore.GREEN+str(text)+Fore.RESET)

def red(text):
    print(Fore.RED+str(text)+Fore.RESET)

def cyan(text):
    print(Fore.CYAN+str(text)+Fore.RESET)

def blue(text):
    print(Fore.BLUE+str(text)+Fore.RESET)

def yellow(text):
    print(Fore.YELLOW+str(text)+Fore.RESET)

def rainbow():
    red("test")
    yellow("test")
    green("test")
    blue("test")
    cyan("test")

if input("Press [ENTER] to start. During test, type EXIT to stop program.") == "rainbow":
    rainbow()
else:
    sleep(0.1)