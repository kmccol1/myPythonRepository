#*******************************************************************************
#Kyle McColgan
#jobChart.py
#This program visualizes my job applications in a flowchart.
#11 December 2020
#*******************************************************************************

import sqlite3
import tkinter

#*******************************************************************************

def main ( ):
    printMenu ( )

#*******************************************************************************

def printMenu ( ):
    print ('Main menu')
    print ('-' * 81)
    print ('1. Add a new application')
    print ('2. Update application status')
    print ('3. Display flowchart')
    print ('4. Display statistics' )
    print ('5. Quit')

#*******************************************************************************

if __name__ == '__main__':
    main ( )