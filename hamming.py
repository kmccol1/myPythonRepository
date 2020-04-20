#Kyle McColgan
#19-April-2020
#hamming.py

import re

def calculateParity ( bits , flag ):
	parity = 0
	numOnes = 0

	for bit in bits:
		if bit == 1:
			numOnes += 1
	
	if (numOnes % 2 != 0) & (flag == 1):
		parity = 1

	return parity
			
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
	p2 = [ hamming[1],hamming[2],hamming[5],hamming[6],hamming[9],hamming[10]]
	p4 = [hamming[3],hamming[4],hamming[5],hamming[6],hamming[11]]
	p8 = [0,0,0,0,0]

	count = 0
	pIndex = 0
	for val in hamming:
		if count % 2 == 0:
			p1[pIndex] = val
			pIndex += 1
		count += 1

	count = 7
	for val in p8:
		val = hamming [ count ]
		count += 1

	hamming[0] = calculateParity ( p1 , flag )
	hamming[1] = calculateParity ( p2, flag )
	hamming[3] = calculateParity ( p4, flag )
	hamming[7] = calculateParity ( p8 , flag )
			
	return hamming

def decodeHamming ( hamming , flag ):
	decoded = [None] * 8
	errorCode = [None] * 4

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

	errorPos = 0
	if 1 in errorCode:
		if error1 == 1:
			errorPos += 1
		elif error2 == 1:
			errorPos += 2
		elif error3 == 1:
			errorPos += 4
		elif error4 == 1:
			errorPos += 8
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

def getMsg ( ):
	msg = '1'
	print ( "\nEnter 8-bit data on single line: ")
	print ( "Sample input formatting: XXXXXXXX" )

	while not re.match("\d{8}" , msg ):
		msg = input ( "Please enter the 8-bit message: ")
		if not re.match ("\d{8}" , msg ):
			print ( "Error! Only 8-digit string required")

	msg = [ int ( x ) for x in msg ]

	return msg



msg = getMsg ( )
evenOddFlag = input ( "Even/odd parity bit? (e/o): " ) [0]

if evenOddFlag == 'e':
	evenOddFlag = 1
else:
	evenOddFlag = 0

print ( "\nYou entered: " )
print ( msg )
print ( "\nhamming code: " )
data = getHammingCode ( msg , evenOddFlag)
print ( data )
print ( decodeHamming ( data , evenOddFlag ) )


