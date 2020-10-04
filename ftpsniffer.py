#!/usr/bin/env python
import scapy.all as scapy

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet , filter="port 80")

dif Process_sniffed_packet(packet):
    print(packet)

sniff("wlan0")