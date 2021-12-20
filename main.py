# Conversation bot
answer = input("What's your name?\n>")
acceptedNames = ["Thomas", "Kenzie" , "kenzie", "Mackenzie" , "mackenzie" , "Javi" , "javi"]
if answer not in acceptedNames:
    print("Sorry, user not recognized. Goodbye.")
good = ["good", "Good" , "great", "Great"]
yes = ["yeah", "Yeah", "Yes", "yes", "Yep", "yep", "sure", "Sure" ,"why not"]
if answer.lower() == "thomas":
    print("Hello sir. How are you?")
    reply = input()
    if reply.lower() in good:
        print("Glad to hear it!\nSee you later!")
    if reply.lower() not in good:
        print("What's wrong?")
        whatsWrong = input()
        if whatsWrong.lower() == "nothing":
            print("Bullshit")
            import sys
            from time import sleep
            sleep(1)
            print("What's wrong?")
            whatsWrong = input()
        if whatsWrong.lower() != "nothing":
            import sys
            from time import sleep
            sleep(1)
            print("I'm sorry to hear that. Is there anything I can do to help? >y/n")
            yesOrNo = input()
            if yesOrNo.lower() == "y":
                print("Ok, how can I help?")
            howToHelp = input()
            if yesOrNo.lower() == "n":
                print("Are you sure?")
                canIHelp = input()
                if canIHelp.lower() in yes:
                    print("Okay, I'm sorry. I hope your day gets better.")
                if canIHelp.lower() not in yes:
                    print("Okay, how can I help?")
                howToHelp = input()

kenzie = ["Kenzie", "kenzie", "Mackenzie" , "mackenzie"]
if answer.lower() in kenzie:
    print("Hello " + answer + ", I have heard so much about you. Glad we could finally meet.")
    howAreYou = input("How are you? \n>")
    if howAreYou.lower() in good:
        print("That's good!\nAnything you want to talk about?")
        wantToTalk = input()
        if wantToTalk in yes:
            print("Well then tell me!")
            input()
            import sys
            from time import sleep
            sleep(1)
            print("Thank you for telling me.")
        if wantToTalk not in yes:
            print("Alright, have a good day!")




    if howAreYou.lower() not in good:
        print("What's wrong?")
        whatsWrongK = input()
        if whatsWrongK.lower() == "nothing":
            print("Are you sure?")
            aYS = input()
        if aYS in yes:
            print("Okay, sorry for bothering you. See you later!")
            exit()
            import sys
            from time import sleep
            sleep(1)
        if aYS not in yes:
            print("What's wrong?")
            whatsWrongK = input()
        if whatsWrongK.lower() != "nothing":
            import sys
            from time import sleep
            sleep(1)
            print("I'm sorry to hear that. Is there anything I can do to help? y/n")
            yN = input()
            if yN.lower() == "y":
                print("Ok, how can I help?")
            howToHelpK = input()
            print("Ok, I'm sorry but I'm not yet programmed to help.")
        if yN.lower() == "n":
            print("Are you sure?")
            canIHelpK = input()
            if canIHelpK.lower() in yes:
                print("Okay, I'm sorry. I hope your day gets better.")
            if canIHelpK.lower() not in yes:
                print("Okay, let me know if there is anything I can do.")




if answer.lower() == "javi":
    print("Hey fucktard, how are you")
    response = input()
    if response in good:
        print("That's good, anything you wanna talk about?")
        wannaTalk = input()
        if wannaTalk not in yes:
            print("Ok well cya later.")
        if wannaTalk in yes:
            print("Well what do you wanna talk about?")
            input()
            import sys
            from time import sleep
            sleep(1)
            print("Tell me about it")
            input()
            print("Alright, well I gotta go. Cya")
    if response not in good:
        print("What's going on?")
        whatsGoingOn = input()
        print("Oh")

