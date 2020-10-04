#!/usr/bin/env python

print("WELCOME TO AUTO KISMET")
print("PLEASE WAIT..... ")


import subprocess

subprocess.call("sudo airmon-ng start wlan0", shell=True)
subprocess.call("sudo kismet -c wlan0mon", shell=True)