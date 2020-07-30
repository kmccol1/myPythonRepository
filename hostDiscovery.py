#very basic network reconaissance tool using layer 2 for host discovery.
#7-20-20
#Requires Python 3.8.5, Scapy API

#******************************************************************************

from scapy.all import *

#******************************************************************************

def displayActiveHosts ( ):
    conf.verb = 0
    ipAddressRange = "192.168.1.0/24"
    activeHostList = list()

    arp = ARP(pdst= ipAddressRange )
    ethernetFrame = Ether ( dst="ff:ff:ff:ff:ff:ff" )
    arpPacket = ethernetFrame / arp
    answersList = srp ( arpPacket, timeout = 3)[0]

    for sent, received in answersList:
        activeHostList.append({'ip': received.psrc, 'mac': received.hwsrc})

    print ( "Active host list:")
    print ( "IP" + " " * 18 + "MAC" )
    for host in activeHostList:
        print("{:16}    {}".format(host['ip'], host['mac'])) 
        
#******************************************************************************

displayActiveHosts()
