import random

isInternet = False

def askInternet(isInternet):
    isInternet = input("Do you have internet? ")
    if isInternet == "Yes":
        isInternet = True
    else:
        isInternet = False
    whatToDo(isInternet=isInternet)

def whatToDo(isInternet):
    thingsToDo = ["Read a book", "Write a Python Script", "Hop on MC", "Just.. excist."]
    if isInternet == False:
        print(random.choice(thingsToDo))
    else:
        print("Then get back to work?")

askInternet(isInternet=isInternet)
