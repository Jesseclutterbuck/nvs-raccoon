#!/usr/bin/env python

print("WELCOME TO AUTO MON")
print("PLEASE WAIT .... PUTTING YOUR WIFI CARD INTO MONITOR MODE")


import subprocess

subprocess.call("sudo airmon-ng start wlan0", shell=True)
