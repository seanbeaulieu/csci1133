# Problem A: find_password
#==========================================
# Purpose:
#   Given an encrypted file, tries every possible four letter lowercase
#   password for that file until one works, and then returns the password.
# Input Parameter(s):
#   filename is a string representing the name of the encrypted file.
#   The file must be in the same folder as this script.
# Return Value:
#   Returns the password that successfully decrypts the given file
#==========================================

def find_password(filename):
    fp = open(filename)
    data = fp.read()
    #TODO: Try all possible four letter passwords, not just 'pwnd'
    password = ''
    for letter in range(26):
            for letter2 in range(26):
                for letter3 in range(26):
                    for letter4 in range(26):
                        password = chr(97 + letter) + chr(97 + letter2) + chr(97 + letter3)+ chr(97 + letter4)
                        if decrypt(data,password):
                            return password           
           
    
# Problem B: count_primes
#==========================================
# Purpose:
#   Prints out all prime numbers between low and high, inclusve, and
#   returns a count of how many there were.
# Input Parameter(s):
#   low is a positive integer 
#   high is a positive integer, which should be >= low
# Return Value:
#   Returns the number of prime numbers between low and high, inclusive
#==========================================
def count_primes(low, high):
    number = 0
    tf = False
    for n1 in range(low, high + 1):
        tf = False
        for no in range(2,n1):
            
            if((n1 % no) == 0):
                #print(n1, " divided by", no)
                tf = True
            
        if(tf == False):
            if(n1 != 1):
                print(n1, "is prime")
                number += 1       
    return number


# Problem C: population
#==========================================
# Purpose:
#   Simulates the population of smallfish, middlefish, and bigfish over time
# Input Parameter(s):
#   small is an integer, the initial number of smallfish in the lake
#   middle is an integer, the initial number of middlefish in the lake
#   big is an integer, the initial number of bigfish in the lake
# Return Value:
#   Returns the number of weeks required for one of the populations to
#   fall below 10, or 100 if the populations are all still >= 10 after
#   100 weeks
#==========================================
def population(s, m, b):
    weeks = 0  
    a1 = 0
    a2 = 0
    a3 = 0    
    while (s >= 10 and m >= 10 and b >= 10 and weeks < 100):
        a1 = 0.1*s - 0.0002*s*m
        a2 = -0.05*m + 0.0001*s*m - 0.00025*m*b
        a3 = -0.1*b + 0.0002*m*b
        s += a1
        m += a2
        b += a3
        weeks += 1
        print("Week: ", weeks,"-","Small: ",int(s)," Middle: ",int(m),"Big: ", int(b))    
    return weeks
        



#DO NOT EDIT ANYTHING BELOW THIS LINE
#Below are helper functions used for decrypting the text files.
#You don't have to understand how any of these work.

# decrypt
#==========================================
# Purpose:
#   Check whether the password is correct for a given encrypted
#   file, and print out the decrypted contents if it is.
# Input Parameter(s):
#   data is a string, representing the contents of an encrypted file.
#   password is a four letter lowercase string, representing the password
#   used to encrypt/decrypt the file contents.
# Return Value:
#   Returns True if the password is correct and the file contents
#   were printed.  Returns False and prints nothing otherwise.
#==========================================
def decrypt(data, password):
    data = data.split('\n')
    if encode(password) == int(data[0]):
        print(vigenere(data[1],password))
        return True
    return False

# encode
#==========================================
# Purpose:
#   Turn a password into a ~9 digit number
# Input Parameter(s):
#   key is a four letter string representing a password
# Return Value:
#   Returns a number between 0 and 547120140, using modular exponentiation
#   to make it difficult to reverse engineer the password from the number.
#==========================================
def encode(key):
    total = 0
    for ltr in key:
        total += ord(ltr)
        total *= 123
    return pow(total,2011,547120141)

# vigenere
#==========================================
# Purpose:
#   Decipher a message using the Vigenere cipher
# Input Parameter(s):
#   msg a string, representing the encrypted message
#   key is a four letter string, representing the cipher key
# Return Value:
#   Returns a string representing the deciphered text
#==========================================
def vigenere(msg,key):
    i = 0
    out_msg = ''
    for ltr in msg:
        out_msg += chr((ord(ltr)-ord(key[i]))%28 +97)
        i = (i+1)%len(key)
    return out_msg.replace('{',' ').replace('|','.')


