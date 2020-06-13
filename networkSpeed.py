#1-June-2020
#mySpeedTester.py
#A simple network transfer speed calculator script, set to execute every 5 minutes.
#Requires speedtest.py module
#Requires Python 3.7.4

import speedtest
import time

def calculateSpeeds ( ):
    myTest = speedtest.Speedtest()
    myTest.get_servers()
    myTest.get_best_server()
    myTest.download()
    myTest.upload()
    results = ( myTest.results ) . dict ( )
    return results["download"] , results["upload"] , results ["ping"]

start = time.time()
print ( 'Testing speeds....')
count = 0
with open ( 'speeds.txt' , 'w' ) as fout:
    fout.write ( 'Download / Upload / Ping\n\n')
    while True:
        dl , ul , ping = calculateSpeeds ( )
        fout.write ( "\nTest #" + str(count) + '\n')
        fout.write ( str ( round( dl / 2048 )) + ' mbps \t /')
        fout.write ( str ( round( ul / 2048 ) ) + ' mbps \t /')
        fout.write ( str (round(ping)) + ' seconds')
        fout.flush()
        #time.sleep ( 300 - ((time.time() - start) % 300)
