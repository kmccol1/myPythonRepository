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
    applicationDict = { }
    choice = -1

    loadDict ( applicationDict )

    while choice != 5:
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

def loadDict ( applicationDict ):
    try:
        inFile = open('jobChartData.pickle', 'rb')
        pickle.load(inFile, applicationDict )
    except OSError as error:
        print ('Error: failed while reading data from file', error )

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
            choice = int ( input ('Enter choice: ' ))

            if choice < 1 or choice > 5:
                print('Please try again: Enter a valid option: ' )
        except ValueError as error:
            print('Error: Enter a valid option (1-5)', error )
    
    return choice

#*******************************************************************************

def processChoice ( choice, applicationDict ):
    if choice == 1:
        addApplication ( applicationDict )
    elif choice == 2:
        updateApplication ( applicationDict )
    elif choice == 3:
        display ( applicationDict )
    elif choice == 4:
        getStatistics ( applicationDict )
    else:
        sys.exit ( )

#*******************************************************************************

def addApplication ( applicationDict ):
    jobID = random.randrange(0,9999)
    jobTitle = input('Enter job title: ' )
    companyName = input ('Enter company: ' )

    applicationDict [companyName] = Application(jobID,jobTitle,companyName)

    try:
        outFile = open ('jobChartData.pickle', 'wb' )
        pickle.dump(applicationDict, outFile )
    except OSError as error:
        print('Error: error saving to the file.', error )

#*******************************************************************************

def updateApplication ( applicationDict ):
    print ('Hello')

#*******************************************************************************

def display ( applicationDict ):
    print ('Opening flowchart display' )
    myWindow = tkinter.Tk ( )

    myCanvas = tkinter.Canvas( )






    myCanvas.pack ( )
    myWindow.mainloop ( )

#*******************************************************************************

def getStatistics ( applicationDict ):

    for job, company in applicationDict.items ( ):
        print ( job, str(company))

#*******************************************************************************

if __name__ == '__main__':
    main ( )
