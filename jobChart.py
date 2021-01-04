#*******************************************************************************
#    Kyle McColgan
#    jobChart.py - Python 3.9.1
#    This program visualizes my job applications in a sankey flowchart.
#    4 January 2021
#*******************************************************************************

import sys
import pickle
import random
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

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
    def __init__ ( self, jobID, title, companyName, jobStatus = 0 ):
        self.__jobID = jobID
        self.__title = title
        self.__companyName = companyName
        self.__jobStatus = jobStatus

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

    def getJobStatus ( self ):
        return self.__jobStatus

#*******************************************************************************
    
    def setJobStatus ( self, jobStatus ):
        self.__jobStatus = jobStatus

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
    MIN_ID = 0
    MAX_ID = 9999
    MIN_STATUS = -1
    MAX_STATUS = 3

    status = -2
    selectedID = -1
    outFile = None
    validJobID = []

    companyName = input('Enter company to update an application: ')

    if companyName in applicationDict:
        for app in applicationDict[companyName]:
            validJobID.append ( app.getJobID ( ) )
            print ( str(app))

    while ( selectedID < MIN_ID ) or ( selectedID > MAX_ID ):
        try:
            selectedID = int(input('Choose a job ID to update: ' ))

            if ( selectedID < MIN_ID ) or ( selectedID > MAX_ID ):
                print ('Error: please input a valid Job ID to update. Please try again.' )
            else:
                outFile = open('jobChartData.pickle', 'wb' )

                for position in applicationDict[companyName]:
                    if position.getJobID() == selectedID:
                        jobID = random.randrange(MIN_ID, MAX_ID)
                        companyName = input ('Enter new company name: ' )
                        jobTitle = input('Enter new job title: ' )
                        
                        while ( status < MIN_STATUS ) or ( status > MAX_STATUS ):
                            try:
                                status = int ( input ('Enter current application status: \
                                                      \n[-1 == Rejection, 0 == No response, 1 == Interview...]: ' ))

                                if ( status < MIN_STATUS ) or ( status > MAX_STATUS ):
                                    print(f'Error: Enter a valid status in range ({MIN_STATUS}-{MAX_STATUS})' )
                            except ValueError as error:
                                print(f'Error: Enter a valid status from ({MIN_STATUS}-{MAX_STATUS})', error )

                        applicationDict[companyName].remove(position)

                        if companyName not in applicationDict.keys():
                            applicationDict [companyName] = [Application(jobID,jobTitle,companyName, status)]
                        else:
                            applicationDict[companyName].append((Application(jobID,jobTitle,companyName, status)))

                        pickle.dump ( applicationDict, outFile )

        except OSError as error:
            print ('Error occured while writing to file.' , error )
        except ( ValueError or TypeError ) as error:
            print ('Error: please enter a valid job ID number value from above.' , error )
        finally:
            outFile.close ( )

#*******************************************************************************

def display ( applicationDict ):
    REJECT_STATUS = -1
    GHOST_STATUS = 0

    numReject = 0
    numGhost = 0
    totalNumApplications = 0
    statisticsList = []

    for company, applicationList in applicationDict.items ( ):
        for position in applicationList:
            if position.getJobStatus() == REJECT_STATUS:
                numReject += 1
            elif position.getJobStatus() == GHOST_STATUS:
                numGhost += 1

    totalNumApplications = numReject + numGhost

    statisticsList.append(-numReject)
    statisticsList.append(-numGhost)
    statisticsList.append(totalNumApplications)
            
    print ('Opening flowchart display' )
    fig = plt.figure()

    subPlot = fig.add_subplot(1,1,1,xticks=[],yticks=[],
                              title='Sankey Diagram of Job Applications')

    myChart = Sankey(ax=subPlot, scale = 0.1, offset=0.25,head_angle=180,
                     format='%.0f', unit=' Applications')

    myChart.add(flows= statisticsList, labels=['Rejected', 'No Response',
                f'Results of {totalNumApplications} Job Applications'],
                orientations=[0,0,0], pathlengths=[0.5, 0.5, 0.5],
                facecolor = 'r')

    diagrams = myChart.finish()
    diagrams[0].texts[-1].set_color('b')
    diagrams[0].texts[-1].set_fontweight('bold')
    diagrams[0].text.set_fontweight('bold')

    plt.show()

#*******************************************************************************

def getStatistics ( applicationDict ):
    NUM_SEPARATOR = 10

    for company, applicationList in applicationDict.items ( ):
        for position in applicationList:
            print (f'{company}', '-' * NUM_SEPARATOR, str(position) )

#*******************************************************************************

if __name__ == '__main__':
    main ( )
