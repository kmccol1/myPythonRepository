#*******************************************************************************************
#This program reads network traffic 
#and displays a table of current bandwidth usage by pairs of host addresses.
#Requires Python 3.8.5, Scapy network API
#*******************************************************************************************

from scapy.all import *
from collections import Counter
import threading
import time

#*******************************************************************************************

captureTimeInSeconds = 30
networkInterface = "Wi-Fi"
packetCounter = Counter()
hostDict = {}

#*******************************************************************************************

def displayBandwith ( totalBytes ):
    formattedBytes = str()

    if totalBytes < 1024:
        formattedBytes = "%3.2f Bytes" % ( totalBytes )
    else:
        totalBytes /= 1024
        displayBandwith ( totalBytes )

    return formattedBytes

#*******************************************************************************************

def filterPackets ( packet ):
    if IP in packet:
        ipPacket = packet [ IP ]
        packetCounter.update ( { tuple ( sorted ( map ( atol , ( ipPacket.src, ipPacket.dst)))): ipPacket.len})

#*******************************************************************************************

def updatePacketCounter ( ):
    sniff ( iface = networkInterface, prn = filterPackets, store = False,
        timeout = None )

#*******************************************************************************************

def printCommonHosts ( ):
    
    for ( sourceAddr , destAddr ), bytesTransferred in packetCounter.most_common(10):
        sourceAddr , destAddr = map ( ltoa , ( sourceAddr , destAddr ) )

        for activeHost in ( sourceAddr , destAddr ):
            if activeHost not in hostDict:
                try:
                    hostName = socket.gethostbyaddr(activeHost)
                    hostDict [ activeHost ] = hostName [ 0 ]
                except:
                    hostDict [ activeHost ] = None

        sourceAddr = "%s (%s)" % ( hostDict [ sourceAddr ] , sourceAddr ) if hostDict [ sourceAddr ] is not None else sourceAddr
        destAddr = "%s (%s)" % ( hostDict[ destAddr ], destAddr ) if hostDict[ destAddr ] is not None else destAddr
        bandwithFmt = displayBandwith( float ( bytesTransferred ) / captureTimeInSeconds )
        print ( sourceAddr[0:20] , ' ' * ( 20 + (len(sourceAddr) - 20) ), '=>' , destAddr[0:20] , ' ' * ( 20 + (len(destAddr) - 20)) , ' ' * (20 - (len(sourceAddr) + len(destAddr))) , bandwithFmt , flush = True)
        print ( )


#*******************************************************************************************

def printHeader ( ):
    print ( '=' * 120)
    print ( 'Host name' , ' ' * 33 , 'Destination Address' , ' ' * 33 , 'Total traffic ( bytes )' )
    print ( '=' * 120)

#*******************************************************************************************

def threadFunction():
    sniff ( iface = networkInterface, prn = filterPackets, store = False , timeout = None )


myThread = threading.Thread ( target = threadFunction)
myThread.start()

printHeader()

while True:
    printCommonHosts()
    time.sleep(3)
    print ( '\r' * 20)


