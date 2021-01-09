#*******************************************************************************
#    Kyle McColgan
#    jobChart.py - Python 3.9.1
#    This program visualizes my job applications in a sankey flowchart.
#    9 January 2021
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
        REJECT_STATUS = -1
        GHOST_STATUS = 0

        result = f'Company Name: {self.getCompanyName()} \
                  \nRole: {self.getTitle()}\nJob ID: {self.getJobID( )}'
        
        if self.getJobStatus() == GHOST_STATUS:
            result += '\nStatus: No response.'
        elif self.getJobStatus() == REJECT_STATUS:
            result += '\nStatus: Application rejected.'

        return result

#*******************************************************************************

def loadDict ( ):
    applicationDict = {}

    try:
        inFile = open('jobChartData.pickle', 'rb')
        applicationDict = pickle.load(inFile)
    except OSError as error:
        print ('Error: failed to read from file', error )
    except EOFError as error:
        print ('No previous file found, creating a new file.', error)
    finally:
        inFile.close()

    return applicationDict

#*******************************************************************************

def printMenu ( ):
    NUM_SEPARATOR = 81

    print ('\n', '-' * NUM_SEPARATOR)
    print ('Job Flowchart Main Menu')
    print ('-' * NUM_SEPARATOR)
    print ('1. Create a new application')
    print ('2. Read a saved application')
    print ('3. Update an application')
    print ('4. Delete an application' )
    print ('5. Display sankey diagram')
    print ('6. Display statistics')
    print ('7. Quit')
    print ('-' * NUM_SEPARATOR)

#*******************************************************************************

def getChoice ( ):
    MIN_CHOICE = 1
    MAX_CHOICE = 7
    choice = -1

    while ( choice < MIN_CHOICE ) or ( choice > MAX_CHOICE ):
        try:
            choice = int ( input ('\nEnter menu choice: ' ))

            if ( choice < MIN_CHOICE ) or ( choice > MAX_CHOICE ):
                print(f'Error: enter a valid menu option from ({MIN_CHOICE}-{MAX_CHOICE})' )
        except ValueError or EOFError as error:
            print(f'Error: Please enter a positive value in range ({MIN_CHOICE}-{MAX_CHOICE})', error )
    
    return choice

#*******************************************************************************

def processChoice ( choice, applicationDict ):
    CREATE_APP = 1
    READ_APP = 2
    UPDATE_APP = 3
    DELETE_APP = 4
    DISPLAY_SANKEY = 5
    DISPLAY_STATS = 6
    QUIT = 7

    if choice == CREATE_APP:
        addApplication ( applicationDict )
    elif choice == READ_APP:
        readApplication ( applicationDict )
    elif choice == UPDATE_APP:
        updateApplication ( applicationDict )
    elif choice == DELETE_APP:
        deleteApplication ( applicationDict )
    elif choice == DISPLAY_SANKEY:
        display ( applicationDict )
    elif choice == DISPLAY_STATS:
        getStatistics ( applicationDict )
    else:
        print ( '\nExiting the program. Goodbye' )
        sys.exit ( )

#*******************************************************************************

def readApplication ( applicationDict ):
    companyName = input ('Enter company name to search: ' )

    if companyName in applicationDict.keys ( ):
        for application in applicationDict[companyName]:
            print ( f'{application}\n')

        try:
            selectedID = int ( input ( '\nEnter a Job ID to display: '))

            for application in applicationDict[companyName]:
                if selectedID == application.getJobID ( ):
                    print ( application )

        except ValueError as error:
            print (f'Error: Invalid job ID input detected.', error )

#*******************************************************************************

def deleteApplication ( applicationDict ):
    outFile = None
    companyName = input ('Enter company name to search: ' )

    if companyName in applicationDict.keys ( ):
        for application in applicationDict[companyName]:
            print ( application )

        try:
            selectedID = int ( input ( 'Enter a Job ID to delete: '))

            for application in applicationDict[companyName]:
                if selectedID == application.getJobID ( ):
                    applicationDict[companyName].remove(application)

            outFile = open ('jobChartData.pickle', 'wb' )
            pickle.dump ( applicationDict, outFile )
            print (f'Successfully deleted Application with ID #{selectedID} at {companyName}.')
        except ValueError as error:
            print ('Error: Invalid job ID input detected.', error )
        except OSError as error:
            print ('Error: failed to update data file', error )
        finally:
            outFile.close ( )
    else:
        print (f'Error: {companyName} not found.')

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
                                                      \n[-1 == Rejection, 0 == No response, 1 == Interview]: ' ))

                                if ( status < MIN_STATUS ) or ( status > MAX_STATUS ):
                                    print(f'Error: Enter a valid status in range ({MIN_STATUS}-{MAX_STATUS})' )
                            except ValueError as error:
                                print(f'Error: Enter a valid status from ({MIN_STATUS}-{MAX_STATUS})', error )

                        if ( companyName in applicationDict ) and ( position in applicationDict[companyName] ):
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
                              title='Sankey Diagram - Employment Search 2021')

    myChart = Sankey(ax=subPlot, scale = 0.1, offset=0.25,head_angle=180,
                     format='%.0f', gap = 0.6, radius = 0.3, shoulder = .05, margin = 0.5, unit=' Job applications')

    myChart.add(flows= statisticsList, labels=['Rejected', 'No Response','Total: '],
                orientations=[0,0,0], pathlengths=[0.5, 0.5, 0.5],
                facecolor = 'r')

    diagrams = myChart.finish()
    diagrams[0].texts[-1].set_color('b')
    diagrams[0].texts[-1].set_fontweight('bold')
    diagrams[0].text.set_fontweight('bold')

    plt.show()

#*******************************************************************************

def getStatistics ( applicationDict ):
    MIN_SIZE = 0
    NUM_SEPARATOR = 81

    totalApplications = 0
    size = len(applicationDict)

    print ('\n***Employment application statistics***')
    print ('-' * NUM_SEPARATOR)
    print('Formatting example: Company name - Number of applications')
    print ('-' * NUM_SEPARATOR)

    if size > MIN_SIZE:
        for company, applicationList in applicationDict.items ( ):
            totalApplications += len(applicationList)
            print (f'{company} - {len(applicationList)} job applications')

        print ('-' * NUM_SEPARATOR)
        print (f'You have {totalApplications} total job applications to {size} different companies.')
    else:
        print ('\nThere are no current job applications to display.')

#*******************************************************************************

if __name__ == '__main__':
    main ( )
