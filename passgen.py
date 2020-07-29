#5-June-2020
#passgen.py
#A cryptographically secure password generator using PRNG. A function for password
#cracking using brute-force is also implemented.
#Requires Python 3.8.4

#******************************************************************************

import random
import os
import string
import secrets
import re
from timeit import default_timer as timer
from itertools import product

#******************************************************************************

def getUserChoice ( ):
    continueFlag = None

    while continueFlag is None:
        try:
            continueFlag = str ( input ( "\nGenerate more passwords? (y/n): " ) )

            if continueFlag != 'y' and continueFlag != 'n':
                print ( "Continue? Enter 'y' for yes, 'n' for no. Please try again.")
                continueFlag = None

        except ValueError:
            print ( "ValueError: Value must be a string (y/n). Please try again." )
        except TypeError:
            print ( "TypeError: Value must be a string (y/n). Please try again.")
    
    return continueFlag

#******************************************************************************

def getNumberOfPasswords ( ):
    numPasswords = None

    while numPasswords is None:
        try:
            numPasswords = int ( input ( "\n Enter the number of passwords to generate: " ) )

            if numPasswords <= 0:
                print ( "Value must be greater than 0. Please try again.")
                numPasswords = None

        except ValueError:
            print ( "ValueError: Value must be an integer. Please try again." )
        except TypeError:
            print ( "TypeError: Value must be a positive integer value. Please try again.")
    
    return numPasswords

#******************************************************************************

def getPassLength ( ):
    passwordLength = None

    while passwordLength is None:
        try:
            passwordLength = int ( input ( "\n Enter length of desired password to generate: " ) )

            if passwordLength <= 0:
                print ( "Length must be greater than 0. Please try again.")
                passwordLength = None

        except ValueError:
            print ( "ValueError: Length must be an integer. Please try again." )
        except TypeError:
            print ( "TypeError: Length must be a positive integer value. Please try again.")
    
    return passwordLength

#******************************************************************************

def generatePassword ( passwordLength ):
    validAlphabet = string.ascii_letters + string.digits
    generatedPassword = " " * passwordLength

    try:
        if passwordLength > 0:
            #urandom arg: num of bytes to return
            #randomBits = str( os.urandom ( passwordLength ) )
            generatedPassword = ''.join ( secrets.choice(validAlphabet) for i in range(passwordLength))
    except NotImplementedError:
        print( 'Runtime error: "randomness source not found" ')

    #generated bits example: "b'\x18\xe2.\xeeRR\x11\xd0b\x87'"
    #validBits += randomBits [5:len(randomBits)]
    #passcode = str( re.sub(r"\\x" , '', str(validBits) ) )
    #passcode = passcode[0:passwordLength - 1]

    #return passcode
    return generatedPassword

#******************************************************************************

def guessPassword ( passwordLength ):
    start = timer()
    guess = " "
    password = ""
    final = " " * passwordLength
    numCorrectGuesses = 0
    print ( "Password is: " )
    print ( password )
    count = int(0)
    incorrectGuesses = []
    numIncorrectGuesses = int(0)

    while ( str(final) != str(guess) and int(numCorrectGuesses) < int(passwordLength)):
        print ("Total guesses: " + " " + str(count) + " numCorrectGuesses: " + str(numCorrectGuesses))

        guess = generatePassword(4)

        print() 
        print ( "RANDOM GUESS: " + guess )
        print ( "\nComparision: " + guess + " == " + password[numCorrectGuesses])

        if str( guess) == str( password ):
            final = guess
            numCorrectGuesses += 1
        else:
            incorrectGuesses.insert (numIncorrectGuesses , guess)
            numIncorrectGuesses += 1

        count+=1

    end = timer ( )

    print ( "your password is: ")   
    print ( final )
    print ("Exeuction time: ")
    print ( end - start )

loopFlag = 'y'
numPasswords = None

def bruteForce ( passwordLength ):
    start = timer ( )
    guess = " "
    password = "password"
    final = str()
    validAlphabet = string.ascii_lowercase
    totalGuesses = 0

    for passwordLen in range(1, passwordLength + 1):
        for combination in product (validAlphabet , repeat = passwordLength):
            totalGuesses += 1
            if totalGuesses %50000000 == 0:
                update = timer ( )
                print ( "Guess count: " + str( totalGuesses) + " guesses in " + str ( update ) + "seconds.")
            if ''.join ( combination ) == password:
                final = ''.join(combination)
                end = timer ( )
                print ( "Found password: " + final + " in " + str(totalGuesses) + " guesses.")   
                print ( final )
                print ("Exeuction time: ")
                print ( end - start )
            
                return final

print ( "\n Welcome to a simple Python 3.7.4 crytographic password generator.")

while loopFlag == 'y':
    numPasswords = getNumberOfPasswords ( )
    passwordLength = getPassLength ( )


    for i in range (numPasswords):
        print ( generatePassword ( passwordLength ) )

    loopFlag = getUserChoice ( )

print ( "Goodbye!" )

bruteForce ( 8 )
