#==========================================
# Purpose: returns a sound for each weight class of dog
# Input Parameter(s): weight is the weight of the dog
# Return Value(s): returns a string, a bark depending on the size of the dog
# yip ruff bark or boof
#==========================================

def sound(weight):
    if weight < 13:
        return 'Yip'
    elif 13 <= weight <= 30:
        return 'Ruff'
    elif 30 < weight <= 70:
        return 'Bark'
    else:
        return 'Boof'

#==========================================
# Purpose: allows user to select a choice out of 3
# Input Parameter(s): text is a question prompt, and option1, option2, and
# option3 are all answers the user can select
# Return Value(s): the option user selected gets returned
#==========================================

def choice(text,option1,option2,option3):
    print(text)
    print('1. ', option1)
    print('2. ', option2)
    print('3. ', option3)
    optionchosen = ' '
    while(optionchosen != '1' or optionchosen != '2' or optionchosen != '3'):
        print('Choose 1, 2, or 3')
        optionchosen = input()
        if(optionchosen == '1' or optionchosen == '2' or optionchosen == '3'):
            return optionchosen
            break
        else:
            print('Invalid option')
            continue

#==========================================
# Purpose: plays a text game with three options
# Input Parameter(s): no parameters
# Return Value(s): true or false, true is a good ending and false is a bad ending
#==========================================

def adventure():
    state = 1
    
    
    if state == 1:     
        an = choice("You need to find your friend, where to start",
                   "Forget finding the friend",
                   "Text him",
                   "Look in the library")
        if an == '1':
            return False
        elif an == '2':
            state = 2
        elif an == '3':
            state = 3
        else:
            print("didnt work")

        if state == 2:
            an = choice("He responds back: 'At the store'",
                        "Check target",
                        "Check CVS",
                        "Check Walgreens")
            if an == '1':
                return True
            elif an == '2':
                state = 4
            elif an == '3':
                state = 4
        
        if state == 3:
            an = choice("In the library you do not find him.",
                        "Leave",
                        "Ask the librarian",
                        "Go to the bathroom")
            if an == '1':
                return False
            elif an == '2':
                state = 4
            elif an == '3':
                state = 5

        if state == 4:
            an = choice("The store is closed",
                        "Call him again",
                        "Give up",
                        "Break the door")
            if an == '1':
                return True
            elif an == '2':
                state = 5
            elif an == '3':
                return False

        if state == 5:
            an = choice("Couldn't think of an ending",
                        "Ending 1",
                        "Ending 2",
                        "Ending 3")
            if an == '1':
                return True
            elif an == '2':
                return False
            elif an == '3':
                return True
                
                        
                        
             
             
             
        

        
  
