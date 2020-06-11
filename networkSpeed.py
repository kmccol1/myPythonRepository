#11-June-2020
#mySpeedTester.py
#A simple network transfer speed calculator.
#Requires speedtest.py module
#Requires Python 3.7.4

import speedtest

def calculateSpeeds ( ):
    myTest = speedtest.Speedtest ( )
    myTest . get_servers ( )
    myTest . get_best_server ( )
    myTest . download ( )
    myTest . upload ( )
    results = ( myTest.results ) . dict ( )
    print ( results["download"] )
    print ( results["upload"] )
    print ( results["ping"] )

calculateSpeeds ( )
#print ( 'Testing speeds....')
#print('Download: ' + str( (download / 2048).round() ) )
#print('Upload: ' + str(upload / 2048))
