#19-April-2020
#hammingCode.py
#implementation of Hamming single-bit forward
#error correction algorithim.
#Requires Python 3.8.5
#Precondition: operates on 1 byte of data (8-bits).

import re

#******************************************************************************

def calculateParity ( bits , flag ):
	parity = 0
	numOnes = bits.count(1)
	
	if (numOnes % 2 != 0) & (flag == 1):
		parity = 1

	return parity

#******************************************************************************
			
def getHammingCode ( bits , flag ):
	hamming = [2,2,0,2,0,0,0,2,0,0,0,0]

	hamIndex = 0
	count = 0
	for val in hamming:
		if val != 2:
			hamming[hamIndex] = bits[count]
			count += 1
		hamIndex += 1
	
	p1 = [0,0,0,0,0,0]
	p2 = [hamming[1],hamming[2],hamming[5],hamming[6],hamming[9],hamming [10]]
	p4 = [hamming[3],hamming[4],hamming[5],hamming[6],hamming[11]]
	p8 = [hamming[7],hamming[8],hamming[9],hamming[10],hamming[11]]

	count = 0
	pIndex = 0
	for val in hamming:
		if count % 2 == 0:
			p1[pIndex] = val
			pIndex += 1
		count += 1

	hamming[0] = calculateParity ( p1 , flag )
	hamming[1] = calculateParity ( p2, flag )
	hamming[3] = calculateParity ( p4, flag )
	hamming[7] = calculateParity ( p8 , flag )
			
	return hamming

#******************************************************************************

def decodeHamming ( hamming , flag ):
	decoded = [None] * 8
	errorCode = [None] * 4
	errorPos = 0

	parity1 = [hamming[0], hamming[2], hamming[4], hamming[6], hamming[8], hamming[10] ]
	parity2 = [hamming[1], hamming[2], hamming[5], hamming[6], hamming[9], hamming[10] ]
	parity3 = [hamming[2],hamming[3],hamming[4],hamming[8],hamming[9],hamming[10]] 
	parity4 = [hamming[3],hamming[4],hamming[5],hamming[6],hamming[11] ]

	error1 = calculateParity ( parity1 , flag )
	error2 = calculateParity ( parity2 , flag )
	error3 = calculateParity ( parity3 , flag )
	error4 = calculateParity ( parity4 , flag )

	errorCode = [ error4 , error3 , error2 , error1 ]
 
	print ( "\nError code: ")
	print ( errorCode )

	errorPos = int( str(error4)+str(error3)+str(error2)+str(error1), 2)

	if 1 in errorCode:
		print ( "\nError detected at element: " + str(errorPos) )
		print ( "Correcting single-bit error..." )
		
		if hamming [ errorPos - 1 ] == 1:
			hamming [ errorPos - 1 ] = 0
		else:
			hamming [ errorPos - 1 ] = 1
	else:
		print ( "\nNo error detected. Decoding original message..." )

	decoded[0] = hamming[2]	
	decoded[1] = hamming[4]
	decoded[2] = hamming[5]
	decoded[3] = hamming[6]
	decoded[4] = hamming[8]
	decoded[5] = hamming[9]
	decoded[6] = hamming[10]
	decoded[7] = hamming[11]

	print ( "\nOriginal message: " )

	return decoded

#******************************************************************************

def getMsg ( ):
	msg = '1'
	print ( "\nEnter 8-bit data on single line: ")
	print ( "Sample input formatting: XXXXXXXX" )

	while not re.match("\d{8}" , msg ):
		msg = input ( "Please enter the 8-bit message: ")
		if not re.match ("\d{8}" , msg ):
			print ( "Error! Only 8-bit string allowed")

	msg = [ int ( x ) for x in msg ]

	return msg

#******************************************************************************

continueFlag = 'y'

while continueFlag == 'y':
	msg = getMsg()
	evenOddFlag = input("Even/odd parity bit? (e/o): ") [0]

	if evenOddFlag.lower() == 'e':
		evenOddFlag = 1
	else:
		evenOddFlag = 0

	print("\nYou entered: ")
	print(msg )
	print("\nhamming code: ")
	data = getHammingCode (msg , evenOddFlag)
	print (data)
	print (decodeHamming(data, evenOddFlag))

	continueFlag = input("\nEnter another codeword? (y/n): ") [0]

print ( "\nGoodbye!" )

#******************************************************************************

#Enter 8-bit data on single line: 
#Sample input formatting: XXXXXXXX
#Please enter the 8-bit message: 10100000
#Even/odd parity bit? (e/o): e

#You entered: 
#[1, 0, 1, 0, 0, 0, 0, 0]

#hamming code: 
#[1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0]

#Error code: 
#[0, 0, 0, 0]

#No error detected. Decoding original message...

#Original message: 
#[1, 0, 1, 0, 0, 0, 0, 0]

#Enter another codeword? (y/n): y

#Enter 8-bit data on single line: 
#Sample input formatting: XXXXXXXX
#Please enter the 8-bit message: 01101010
#Even/odd parity bit? (e/o): o

#You entered: 
#[0, 1, 1, 0, 1, 0, 1, 0]

#hamming code: 
#[0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0]

#Error code: 
#[0, 0, 0, 0]

#No error detected. Decoding original message...

#Original message: 
#[0, 1, 1, 0, 1, 0, 1, 0]

#Enter another codeword? (y/n): y

#Enter 8-bit data on single line: 
#Sample input formatting: XXXXXXXX
#Please enter the 8-bit message: 10011010
#Even/odd parity bit? (e/o): e

#You entered: 
#[1, 0, 0, 1, 1, 0, 1, 0]

#hamming code: 
#[0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0]

#Error code: 
#[0, 0, 0, 0]

#No error detected. Decoding original message...

#Original message: 
#[1, 0, 0, 1, 1, 0, 1, 0]

#Enter another codeword? (y/n): y

#Enter 8-bit data on single line: 
#Sample input formatting: XXXXXXXX
#Please enter the 8-bit message: 10101010
#Even/odd parity bit? (e/o): e

#You entered: 
#[1, 0, 1, 0, 1, 0, 1, 0]

#hamming code: 
#[1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0]

#Error code: 
#[0, 0, 0, 0]

#No error detected. Decoding original message...

#Original message: 
#[1, 0, 1, 0, 1, 0, 1, 0]

#Enter another codeword? (y/n): y

#Enter 8-bit data on single line: 
#Sample input formatting: XXXXXXXX
#Please enter the 8-bit message: 10000100
#Even/odd parity bit? (e/o): e

#You entered: 
#[1, 0, 0, 0, 0, 1, 0, 0]

#hamming code: 
#[1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]

#Error code: 
#[0, 0, 0, 0]

#No error detected. Decoding original message...

#Original message: 
#[1, 0, 0, 0, 0, 1, 0, 0]

#Enter another codeword? (y/n): y

#Enter 8-bit data on single line: 
#Sample input formatting: XXXXXXXX
#Please enter the 8-bit message: 11001100
#Even/odd parity bit? (e/o): e

#You entered: 
#[1, 1, 0, 0, 1, 1, 0, 0]

#hamming code: 
#[1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0]

#Error code: 
#[0, 1, 0, 0]

#Error detected at element: 4
#Correcting single-bit error...

#Original message: 
#[1, 1, 0, 0, 1, 1, 0, 0]

#Enter another codeword? (y/n): n

#Goodbye!

