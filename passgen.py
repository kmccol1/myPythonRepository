#Kyle McColgan
#15-May-2020
#passgen.py

import random
import os

#print n random bytes ( 6 bits + '\0')
passwordLength = None
while passwordLength is None:
    try:
        passwordLength = int ( input ( "\n Enter length of desired password to generate: " ) )
    except ValueError:
        print ( "Length must be an integer." )

try:
    randomBits = str( os.urandom ( passwordLength ) )
except NotImplementedError:
    print( 'Runtime error: "randomness source not found" ')

#remove \x repetitions using filters...
validBits =  list((filter ( lambda bit: bit != 'x' and bit != '\\' , randomBits ) ))
validBits = ''.join(validBits)

print ( "Generated: ")
print ( randomBits )
print ( "\nValid:" )
print ( validBits )

bits = ''.join(list(validBits))

code = []
for i in range ( passwordLength ):
    code  += str(''.join(bits[i + 2] )) 
#offset is +2 to strip leading "'b" chars

passcode = ''.join(code)

print ( "Your password is: " )
print ( str(passcode) )