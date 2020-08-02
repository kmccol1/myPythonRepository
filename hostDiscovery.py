#very basic network reconaissance tool using layer 2 broadcasting for host discovery.
#7-20-20
#Requires Python 3.8.5, Scapy library

#******************************************************************************

from scapy.all import *

#******************************************************************************

def displayActiveHosts ( ):
    conf.verb = 0
    ipAddressRange = "192.168.1.0/24" #CIDR notation
    activeHostList = list()

    arp = ARP ( pdst= ipAddressRange )
    ethernetFrame = Ether ( dst="ff:ff:ff:ff:ff:ff" ) #broadcast address
    arpPacket = ethernetFrame / arp
    
    
    responseList = srp ( arpPacket, timeout = 3)[0]

    for sentData, recvData in responseList:
        activeHostList.append({'layer3Addr': recvData.psrc, 'layer2Addr': recvData.hwsrc})

    print ( "Active host list:")
    print ( "IP address" + " " * 18 + "MAC" )
    for host in activeHostList:
        print("{:16}    {}".format(host['layer3Addr'], host['layer2Addr'])) 
        
#******************************************************************************

displayActiveHosts()
