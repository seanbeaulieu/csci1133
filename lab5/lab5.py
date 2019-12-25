import random
def random_list(n):
    list1 = []
    for ran in range(1,n+1):
        rand = random.randint(1,n)
        list1.append(rand)
    return list1

def swap_min(a):
    i = a.index(min(a))
    b = min(a)
    a[i] = a[0]
    a[0] = b
    return a

    
def strcheck(word):

    for letter in range(1,len(word)):
        if word[letter] == word[0]:
            return True
    return False


def lowercase():
    list1 = []
    b = 'a'
    while(b != ''):
        b = input("Enter a word")
        if strcheck(b) == True:
            list1.append(b)
    for i in list1:
        print(i)
        
def selectionsort():
    a = int(input("Enter a number"))
    list1 = random_list(a)
    print(list1)

    for i in range(len(list1)):
        #for ii in range(i,len(list1):
        list1 = list1[:i] + swap_min(list1[i:])                  
    print(list1)

def bjscore(hand):
    
    
