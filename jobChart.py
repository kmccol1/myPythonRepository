#*******************************************************************************
#    Kyle McColgan
#    jobChart.py - Python 3.9.0
#    This program visualizes my job applications in a flowchart.
#    20 December 2020
#*******************************************************************************

import tkinter
import sys
import pickle
import random

#*******************************************************************************

def main ( ):
    QUIT = 5
    choice = -1
    applicationDict = { }

    applicationDict = loadDict ( )

    while choice != QUIT:
        printMenu ( )
        choice = getChoice ( )
        processChoice ( choice, applicationDict )

#*******************************************************************************

class Application:
    def __init__ ( self, jobID, title, companyName ):
        self.__jobID = jobID
        self.__title = title
        self.__companyName = companyName

#*******************************************************************************
    
    def getJobID ( self ):
        return self.__jobID

#*******************************************************************************

    def getTitle ( self ):
        return self.__title

#*******************************************************************************

    def getCompanyName ( self ):
        return self.__companyName

#*******************************************************************************

    def setJobID ( self, jobID ):
        self.__jobID = jobID

#*******************************************************************************
    def setTitle ( self, title ):
        self.__title = title

#*******************************************************************************

    def setCompanyName ( self, companyName ):
        self.__companyName = companyName

#*******************************************************************************

    def __str__ ( self ):
        return f'Company Name: {self.getCompanyName()} \
                \nJob ID: {self.getJobID()}\nTitle: {self.getTitle( )}\n'

#*******************************************************************************

def loadDict ( ):
    applicationDict = {}

    try:
        inFile = open('jobChartData.pickle', 'rb')
        applicationDict = pickle.load(inFile)
    except OSError as error:
        print ('Error: failed while reading data from file', error )
    except EOFError as error:
        print ('No saved data to load, creating new file.')
    finally:
        inFile.close()

    return applicationDict

#*******************************************************************************

def printMenu ( ):
    NUM_SEPARATOR = 81

    print ('Main menu')
    print ('-' * NUM_SEPARATOR)
    print ('1. Add a new application')
    print ('2. Update application status')
    print ('3. Display flowchart')
    print ('4. Display statistics' )
    print ('5. Quit')

#*******************************************************************************

def getChoice ( ):
    MIN_CHOICE = 1
    MAX_CHOICE = 5
    choice = -1

    while ( choice < MIN_CHOICE ) or ( choice > MAX_CHOICE ):
        try:
            choice = int ( input ('Enter choice: ' ))

            if ( choice < MIN_CHOICE ) or ( choice > MAX_CHOICE ):
                print('Please try again: Enter a valid option: ' )
        except ValueError as error:
            print(f'Error: Enter a valid option ({MIN_CHOICE}-{MAX_CHOICE})', error )
    
    return choice

#*******************************************************************************

def processChoice ( choice, applicationDict ):
    ADD_JOB = 1
    UPDATE_JOB = 2
    OPEN_CHART = 3
    PRINT_JOBS = 4

    if choice == ADD_JOB:
        addApplication ( applicationDict )
    elif choice == UPDATE_JOB:
        updateApplication ( applicationDict )
    elif choice == OPEN_CHART:
        display ( applicationDict )
    elif choice == PRINT_JOBS:
        getStatistics ( applicationDict )
    else:
        print ( '\nExiting the program. Goodbye' )
        sys.exit ( )

#*******************************************************************************

def addApplication ( applicationDict ):
    MIN_ID = 0
    MAX_ID = 9999

    jobID = random.randrange(MIN_ID, MAX_ID)
    jobTitle = input('Enter job title: ' )
    companyName = input ('Enter company: ' )

    if companyName not in applicationDict.keys():
        applicationDict [companyName] = [Application(jobID,jobTitle,companyName)]
    else:
        (applicationDict[companyName]).append((Application(jobID,jobTitle,companyName)))

    try:
        outFile = open ('jobChartData.pickle', 'wb' )
        pickle.dump(applicationDict, outFile )
    except OSError as error:
        print('Error: error saving to the file.', error )
    finally:
        outFile.close()

#*******************************************************************************

def updateApplication ( applicationDict ):
    companyName = input('Enter company: ')

    print (applicationDict[companyName])
    jobID = int(input('Chose a job ID to update: ' ))

#*******************************************************************************

def display ( applicationDict ):
    print ('Opening flowchart display' )
    myWindow = tkinter.Tk ( )

    myCanvas = tkinter.Canvas( )

    myCanvas.pack ( )
    myWindow.mainloop ( )

#*******************************************************************************

def getStatistics ( applicationDict ):
    NUM_SEPARATOR = 10

    for company, applicationList in applicationDict.items ( ):
        for position in applicationList:
            print (f'{company}', '-' * NUM_SEPARATOR, str(position) )

#*******************************************************************************

if __name__ == '__main__':
    main ( )
