#*******************************************************************************
#Kyle McColgan
#jobChart.py
#This program visualizes my job applications in a flowchart.
#11 December 2020
#*******************************************************************************

import sqlite3
import tkinter
import sys
import pickle

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

def getChoice ( ):
    choice = -1

    while choice < 1 or choice > 5:
        try:
            choice = int ( input ('Enter choice: ' )

            if choice < 1 or choice > 5:
                print('Please try again: Enter a valid option: ' )

    return choice

#*******************************************************************************

def processChoice ( choice ):
    if choice == 1:
        addApplication ( )
    elif choice == 2:
        updateApplication ( )
    elif choice == 3:
        display ( )
    elif choice == 4:
        getStatistics ( )
    else:
        sys.exit ( )

#*******************************************************************************

def addApplication ( ):

#*******************************************************************************

def updateApplication ( ):

#*******************************************************************************

def display ( ):

#*******************************************************************************

def getStatistics ( ):

#*******************************************************************************

if __name__ == '__main__':
    main ( )
