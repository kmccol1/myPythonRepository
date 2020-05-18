#17-May-2020
#passgen.py
#Cryptographic random data password generator, now implements regex for filter.
#Requires Python 3.7.4

#******************************************************************************

import random
import os
import re

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
    try:
        if passwordLength > 0:
            randomBits = str( os.urandom ( passwordLength ) )
    except NotImplementedError:
        print( 'Runtime error: "randomness source not found" ')

    #generated bits example: "b'\x18\xe2.\xeeRR\x11\xd0b\x87'"

    #trim '\x' byte marker repetitions in random generated bits...
    #validBits =  list((filter ( lambda bit: bit != 'x' and bit != '\\' , randomBits ) ))
    validBits = str()

    validBits += randomBits [5:len(randomBits)]
    passcode = str( re.sub(r"\\x" , '', str(validBits) ) )

    #print ( "\nGenerated: ")
    #print ( randomBits )
    #print ( "\nValid:" )
    #print ( validBits )

    passcode = passcode[0:passwordLength]

    return passcode

#******************************************************************************
#main()

loopFlag = 'y'
numPasswords = None

print ( "\n Welcome to a simple Python 3.7.4 crytographic password generator.")

while loopFlag == 'y':
    numPasswords = getNumberOfPasswords ( )
    passwordLength = getPassLength ( )


    for i in range (numPasswords):
        print ( generatePassword ( passwordLength ) )

    #print ( "Generate more passwords? (y/n): " )
    loopFlag = getUserChoice ( )

print ( "Goodbye!" )

