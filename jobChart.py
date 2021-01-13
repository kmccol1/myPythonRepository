#*******************************************************************************
#    Name: Kyle McColgan
#    Date: 12 January 2021
#    File name: jobChart.py - Python 3.9.1
#
#    Description: Command-line application that tracks and visualizes 
#                 my job applications in a sankey flowchart.
#
#*******************************************************************************

import sys
import pickle
import random
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

#*******************************************************************************

def main ( ):
    QUIT = 7
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
        DEFAULT_STATUS = 0
        INTERVIEW_STATUS = 1

        result = f'Company Name: {self.getCompanyName()} \
                   \nRole: {self.getTitle()}\nJob ID: {self.getJobID()}'
        
        if self.getJobStatus() == DEFAULT_STATUS:
            result += '\nStatus: No response.'
        elif self.getJobStatus() == REJECT_STATUS:
            result += '\nStatus: Application rejected.'
        elif self.getJobStatus ( ) == INTERVIEW_STATUS:
            result += '\nStatus: Interviewing'

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

    print ('-' * NUM_SEPARATOR, 'Job Flowchart Main Menu', '-' * NUM_SEPARATOR,
           '1. Create a new application', '2. Read an existing application',
           '3. Update an application','4. Delete an existing application',
           '5. Display sankey diagram', '6. Display statistics', '7. Quit',
           '-' * NUM_SEPARATOR , sep='\n')

#*******************************************************************************

def getChoice ( ):
    MIN_CHOICE = 1
    MAX_CHOICE = 7
    choice = -1

    while ( choice < MIN_CHOICE ) or ( choice > MAX_CHOICE ):
        try:
            choice = int ( input ('\nEnter menu choice: ' ))

            if ( choice < MIN_CHOICE ) or ( choice > MAX_CHOICE ):
                print('Error: entered value not in range:', 
                     f'({MIN_CHOICE}-{MAX_CHOICE})')

        except ValueError or EOFError as error:
            print('Error: Please enter a positive value in range:',
                 f'({MIN_CHOICE}-{MAX_CHOICE})', error )
    
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
    NUM_SEPARATOR = 81
    companyName = input ('Enter company name to search: ' )

    if companyName in applicationDict.keys ( ):
        print (f'You have {len(applicationDict[companyName])}',
              f'job applications to {companyName}.')
        print ('-' * NUM_SEPARATOR )

        for application in applicationDict[companyName]:
            print ( f'{application.getJobID ( )} - {application.getTitle()}')

        print ('-' * NUM_SEPARATOR)

        try:
            selectedID = int ( input ( '\nEnter a Job ID to display: '))

            for application in applicationDict[companyName]:
                if selectedID == application.getJobID ( ):
                    print ( application )

        except ValueError as error:
            print (f'Error: Invalid job ID input detected.', error )
    else:
        print (f'No saved application data found for {companyName}.')

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
            print ('Successfully deleted Application with ID #', 
                  f'{selectedID} at {companyName}.')
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
    NUM_SEPARATOR = 81
    MIN_ID = 0
    MAX_ID = 9999
    MIN_STATUS = -1
    MAX_STATUS = 3

    status = -2
    selectedID = -1
    outFile = None
    validJobID = []

    print ('-' * NUM_SEPARATOR )

    for company in applicationDict.keys ( ):
        print ( company )
    
    print ('-' * NUM_SEPARATOR )

    companyName = input('Enter a company name from above list \
                         \nto update an application: ')

    while companyName not in applicationDict.keys ( ):
        print (f'{companyName} has no existing applications. \
                \nPlease try again.' )
        companyName = input('Enter company to update an application: ')
        
    if companyName in applicationDict:
        for app in applicationDict[companyName]:
            validJobID.append ( app.getJobID ( ) )
            print ( app )

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
            print ('Error: please enter a valid job ID selection.' , error )
        finally:
            outFile.close ( )

#*******************************************************************************

def display ( applicationDict ):
    REJECT_STATUS = -1
    DEFAULT_STATUS = 0
    INTERVIEW_STATUS = 1

    numReject = 0
    numGhost = 0
    numInterviews = 0
    totalNumApplications = 0
    statisticsList = []

    for company, applicationList in applicationDict.items ( ):
        for position in applicationList:
            if position.getJobStatus() == REJECT_STATUS:
                numReject += 1
            elif position.getJobStatus() == DEFAULT_STATUS:
                numGhost += 1
            elif position.getJobStatus ( ) == INTERVIEW_STATUS:
                numInterviews += 1


    totalNumApplications = numReject + numGhost

    statisticsList.append(-numReject)
    statisticsList.append(-numGhost)
    statisticsList.append (-numInterviews )
    statisticsList.append(totalNumApplications)
            
    print ('Opening flowchart display' )
    fig = plt.figure()

    subPlot = fig.add_subplot(1,1,1,xticks=[],yticks=[],
                              title='Sankey Diagram - Employment Search 2021')

    myChart = Sankey(ax=subPlot, scale = 0.1, offset=0.25,head_angle=180,
                     format='%.0f', gap = 0.6, radius = 0.3, shoulder = .05,
                     margin = 0.5, unit=' Job applications')

    myChart.add(flows= statisticsList, 
                labels=['Rejected', 'No Response', 'Interviewed', 'Total: '],
                orientations=[0,0,0,0], pathlengths=[0.5,0.5,0.5,0.5],
                trunklength=3.0, facecolor = 'r')

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

    print ('\n***Employment application statistics***', '-' * NUM_SEPARATOR,
           'Formatting example: Company name - Number of applications',
           '-' * NUM_SEPARATOR, sep='\n')

    if size > MIN_SIZE:
        for company, applicationList in applicationDict.items ( ):
            totalApplications += len(applicationList)
            print (f'{company} - {len(applicationList)} job applications')

        print ('-' * NUM_SEPARATOR + '\n', 
              f'You have {totalApplications} total job applications to', 
              f'{size} different companies.')
    else:
        print ('\nThere are no current job applications to display.')

#*******************************************************************************

if __name__ == '__main__':
    main ( )
