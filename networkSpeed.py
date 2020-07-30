#12-June-2020
#mySpeedTester.py
#A simple network transfer speed calculator script, set to execute every 5 minutes.
#Requires speedtest API for python interface
#Requires Python 3.8.5

#******************************************************************************

import speedtest
import time
import datetime

#******************************************************************************

def calculateSpeeds ( ):
    myTest = speedtest . Speedtest ( )
    myTest . get_servers ( )
    myTest . get_best_server ( )
    myTest . download ( )
    myTest . upload ( )
    results = ( myTest.results ) . dict ( )
    return results["download"] , results["upload"] , results ["ping"]

startTime = time . time ( )
print ( 'Testing speeds....')
numExecutions = 0
with open ( 'speeds.txt' , 'w' ) as fout:
    fout.write ( 'Download / Upload / Ping\n')
    while True:
        testTime = datetime.datetime.now()
        downloadSpeed , uploadSpeed , ping = calculateSpeeds ( )
        fout.write ( "\n***Test #" + str( numExecutions ) + ' Results*** \n')
        fout.write ( str ( round( downloadSpeed / 2048 )) + ' mbps \t /')
        fout.write ( str ( round( uploadSpeed / 2048 ) ) + ' mbps \t /')
        fout.write ( str ( round( ping ) ) + ' seconds')
        fout.write ( '\nTested at ' + '{0:%H:%M:%S on %Y-%m-%d}'.format(testTime) )
        fout.write ( 'THANKS AT&T')
        fout.write( '*************************************\n\n' )
        fout.flush()
        numExecutions += 1
        time.sleep ( 300 - ((time.time() - startTime) % 300) )
        
        
#******************************************************************************
