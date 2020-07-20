#Simple network sniffer using Scapy API
#7-20-20
#Requires Python 3.8.4, Scapy API, Windows 10 OS

from scapy.all import *
from collections import Counter
import os
import time

captureLen = 10
networkInterface = "Wi-Fi"
packetCounter = Counter()
hostDict = {}

def displayBandwith ( totalBytes ):
    formattedBytes = str()

    if totalBytes < 1024:
        formattedBytes = "%3.2f Bytes" % ( totalBytes )
    else:
        totalBytes /= 1024
        displayBandwith ( totalBytes )

    return formattedBytes

def filterPackets ( packet ):
    if IP in packet:
        packet = packet [ IP ]
        packetCounter.update ( { tuple ( sorted ( map ( atol , ( packet.src, packet.dst)))): packet.len})

def getLiveOutput ( ):
    sniff ( iface = networkInterface, prn = filterPackets, store = False,
        timeout = captureLen )

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
        bandwithFmt = displayBandwith( float ( bytesTransferred ) / captureLen )


        print ( sourceAddr , ' ' * 30 , '=>' , destAddr , ' ' * 30 , bandwithFmt )
        print ( ) 



print ( 'Host name' , ' ' * 33 , 'Destination Address' , ' '* 33 , 'Total traffic ( bytes )' )
print ( '=' * 120)

while True:
    getLiveOutput()
    time.sleep(5)




