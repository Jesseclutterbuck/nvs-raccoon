#!/usr/bin/env python

print("WELCOME TO AUTO PORT")
print("THE AUTOMATIC PORT FORWARDING TOOL")


import subprocess

subprocess.call("echo 1>/proc/sys/net/ipv4/ip_forward", shell=True)
subprocess.call("arp -a", shell=True)