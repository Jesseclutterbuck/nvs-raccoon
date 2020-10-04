#!/usr/bin/env python

print("port 4444 on your device is now open")
print("Ncat is ready")
print("waiting for a client to join the connection")

import subprocess

subprocess.call("nc -vv -l -p4444", shell=True)