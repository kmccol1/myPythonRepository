#10-June-2020
#mySpeedTester.py
#A simple network transfer speed calculator.
#Requires speedtest.py module from https://pypi.org/project/speedtest-cli/
#Requires Python 3.7.4

import speedtest

def calculateSpeeds ( ):
    myTest = speedtest.Speedtest()
    myTest.get_servers()
    myTest.get_best_server()
    myTest.download()
    myTest.upload()
    results = myTest.results.dict()
    return results["download"], results["upload"], results["ping"]

download , upload , ping = calculateSpeeds()
print ( 'Testing speeds....')
print('Download: ' + str(download))
print('Upload: ' + str(upload))
