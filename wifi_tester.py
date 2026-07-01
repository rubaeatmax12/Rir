#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import json
import hashlib
import base64
import requests
import socket
import subprocess
import re
import random
import string
import threading
import queue
import datetime
import tempfile
import shutil
import platform
import netifaces
import scapy.all as scapy
from scapy.all import *
from urllib.parse import urlparse

# ==================== RIR LOGO ====================
RIR_LOGO = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ██████  ██ ███████ ███████                                ║
║   ██   ██ ██ ██      ██                                     ║
║   ██████  ██ █████   █████                                  ║
║   ██   ██ ██ ██      ██                                     ║
║   ██   ██ ██ ███████ ███████                                ║
║                                                              ║
║         WiFi TESTING SUITE v7.0 - 130 TOOLS                 ║
║                   RIR Cyber Tools                          ║
╚══════════════════════════════════════════════════════════════╝
"""

# ==================== COLOR SYSTEM ====================
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[35m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    WHITE = '\033[97m'

def cprint(text, color=Colors.WHITE, bold=False):
    if bold:
        print(f"{Colors.BOLD}{color}{text}{Colors.END}")
    else:
        print(f"{color}{text}{Colors.END}")

def print_header():
    os.system('clear' if os.name != 'nt' else 'cls')
    cprint(RIR_LOGO, Colors.CYAN)
    print()

def print_menu():
    print(Colors.BOLD + Colors.CYAN + "=" * 70 + Colors.END)
    cprint("  📡 WIFI SCANNING TOOLS (1-20)", Colors.YELLOW, True)
    cprint("  1.  Scan WiFi Networks", Colors.WHITE)
    cprint("  2.  Scan WiFi Networks (Detailed)", Colors.WHITE)
    cprint("  3.  WiFi Signal Strength Scanner", Colors.WHITE)
    cprint("  4.  WiFi Channel Scanner", Colors.WHITE)
    cprint("  5.  WiFi Security Type Scanner", Colors.WHITE)
    cprint("  6.  WiFi MAC Address Scanner", Colors.WHITE)
    cprint("  7.  WiFi Vendor Scanner", Colors.WHITE)
    cprint("  8.  WiFi Frequency Scanner", Colors.WHITE)
    cprint("  9.  WiFi Encryption Scanner", Colors.WHITE)
    cprint("  10. WiFi Authentication Scanner", Colors.WHITE)
    cprint("  11. WiFi Signal Map", Colors.WHITE)
    cprint("  12. WiFi Channel Width Scanner", Colors.WHITE)
    cprint("  13. WiFi Beacon Frame Scanner", Colors.WHITE)
    cprint("  14. WiFi Probe Request Scanner", Colors.WHITE)
    cprint("  15. WiFi Association Scanner", Colors.WHITE)
    cprint("  16. WiFi Authentication Scanner", Colors.WHITE)
    cprint("  17. WiFi Deauthentication Scanner", Colors.WHITE)
    cprint("  18. WiFi Disassociation Scanner", Colors.WHITE)
    cprint("  19. WiFi Handshake Scanner", Colors.WHITE)
    cprint("  20. WiFi PMKID Scanner", Colors.WHITE)
    
    print()
    cprint("  🔍 WIFI ANALYSIS TOOLS (21-40)", Colors.YELLOW, True)
    cprint("  21. WiFi Network Analyzer", Colors.WHITE)
    cprint("  22. WiFi Traffic Analyzer", Colors.WHITE)
    cprint("  23. WiFi Packet Analyzer", Colors.WHITE)
    cprint("  24. WiFi Protocol Analyzer", Colors.WHITE)
    cprint("  25. WiFi Frame Analyzer", Colors.WHITE)
    cprint("  26. WiFi Data Analyzer", Colors.WHITE)
    cprint("  27. WiFi Management Frame Analyzer", Colors.WHITE)
    cprint("  28. WiFi Control Frame Analyzer", Colors.WHITE)
    cprint("  29. WiFi Data Frame Analyzer", Colors.WHITE)
    cprint("  30. WiFi QoS Analyzer", Colors.WHITE)
    cprint("  31. WiFi WMM Analyzer", Colors.WHITE)
    cprint("  32. WiFi HT Capabilities Analyzer", Colors.WHITE)
    cprint("  33. WiFi VHT Capabilities Analyzer", Colors.WHITE)
    cprint("  34. WiFi HE Capabilities Analyzer", Colors.WHITE)
    cprint("  35. WiFi MU-MIMO Analyzer", Colors.WHITE)
    cprint("  36. WiFi OFDMA Analyzer", Colors.WHITE)
    cprint("  37. WiFi Beamforming Analyzer", Colors.WHITE)
    cprint("  38. WiFi Roaming Analyzer", Colors.WHITE)
    cprint("  39. WiFi Handover Analyzer", Colors.WHITE)
    cprint("  40. WiFi Load Balancing Analyzer", Colors.WHITE)
    
    print()
    cprint("  🔐 WIFI SECURITY TOOLS (41-60)", Colors.YELLOW, True)
    cprint("  41. WiFi WEP Cracker", Colors.WHITE)
    cprint("  42. WiFi WPA Cracker", Colors.WHITE)
    cprint("  43. WiFi WPA2 Cracker", Colors.WHITE)
    cprint("  44. WiFi WPA3 Cracker", Colors.WHITE)
    cprint("  45. WiFi PMKID Cracker", Colors.WHITE)
    cprint("  46. WiFi Handshake Capture", Colors.WHITE)
    cprint("  47. WiFi Deauth Attack", Colors.WHITE)
    cprint("  48. WiFi Evil Twin Attack", Colors.WHITE)
    cprint("  49. WiFi MAC Spoofing", Colors.WHITE)
    cprint("  50. WiFi MAC Filter Bypass", Colors.WHITE)
    cprint("  51. WiFi Hidden Network Scanner", Colors.WHITE)
    cprint("  52. WiFi Client Isolation Bypass", Colors.WHITE)
    cprint("  53. WiFi ARP Spoofing", Colors.WHITE)
    cprint("  54. WiFi DNS Spoofing", Colors.WHITE)
    cprint("  55. WiFi MITM Attack", Colors.WHITE)
    cprint("  56. WiFi Session Hijacking", Colors.WHITE)
    cprint("  57. WiFi Credential Sniffer", Colors.WHITE)
    cprint("  58. WiFi Packet Injection", Colors.WHITE)
    cprint("  59. WiFi Flood Attack", Colors.WHITE)
    cprint("  60. WiFi Beacon Flood", Colors.WHITE)
    
    print()
    cprint("  🛠️  WIFI TOOLBOX (61-80)", Colors.YELLOW, True)
    cprint("  61. WiFi Adapter Info", Colors.WHITE)
    cprint("  62. WiFi Adapter Mode Switch", Colors.WHITE)
    cprint("  63. WiFi Adapter Channel Set", Colors.WHITE)
    cprint("  64. WiFi Adapter TX Power Set", Colors.WHITE)
    cprint("  65. WiFi Adapter Antenna Set", Colors.WHITE)
    cprint("  66. WiFi Adapter Driver Info", Colors.WHITE)
    cprint("  67. WiFi Adapter Firmware Info", Colors.WHITE)
    cprint("  68. WiFi Adapter Temperature", Colors.WHITE)
    cprint("  69. WiFi Adapter Reset", Colors.WHITE)
    cprint("  70. WiFi Adapter Monitor Mode", Colors.WHITE)
    cprint("  71. WiFi Adapter Managed Mode", Colors.WHITE)
    cprint("  72. WiFi Adapter Master Mode", Colors.WHITE)
    cprint("  73. WiFi Adapter Ad-hoc Mode", Colors.WHITE)
    cprint("  74. WiFi Adapter WDS Mode", Colors.WHITE)
    cprint("  75. WiFi Adapter IBSS Mode", Colors.WHITE)
    cprint("  76. WiFi Adapter Mesh Mode", Colors.WHITE)
    cprint("  77. WiFi Adapter AP Mode", Colors.WHITE)
    cprint("  78. WiFi Adapter Client Mode", Colors.WHITE)
    cprint("  79. WiFi Adapter Bridge Mode", Colors.WHITE)
    cprint("  80. WiFi Adapter Repeater Mode", Colors.WHITE)
    
    print()
    cprint("  📊 WIFI MONITORING (81-100)", Colors.YELLOW, True)
    cprint("  81. WiFi Signal Monitor", Colors.WHITE)
    cprint("  82. WiFi Traffic Monitor", Colors.WHITE)
    cprint("  83. WiFi Bandwidth Monitor", Colors.WHITE)
    cprint("  84. WiFi Latency Monitor", Colors.WHITE)
    cprint("  85. WiFi Jitter Monitor", Colors.WHITE)
    cprint("  86. WiFi Packet Loss Monitor", Colors.WHITE)
    cprint("  87. WiFi Throughput Monitor", Colors.WHITE)
    cprint("  88. WiFi Retry Monitor", Colors.WHITE)
    cprint("  89. WiFi Error Monitor", Colors.WHITE)
    cprint("  90. WiFi Client Monitor", Colors.WHITE)
    cprint("  91. WiFi AP Monitor", Colors.WHITE)
    cprint("  92. WiFi Mesh Monitor", Colors.WHITE)
    cprint("  93. WiFi Bridge Monitor", Colors.WHITE)
    cprint("  94. WiFi Gateway Monitor", Colors.WHITE)
    cprint("  95. WiFi DNS Monitor", Colors.WHITE)
    cprint("  96. WiFi DHCP Monitor", Colors.WHITE)
    cprint("  97. WiFi ARP Monitor", Colors.WHITE)
    cprint("  98. WiFi ICMP Monitor", Colors.WHITE)
    cprint("  99. WiFi UDP Monitor", Colors.WHITE)
    cprint("  100. WiFi TCP Monitor", Colors.WHITE)
    
    print()
    cprint("  🚀 WIFI ADVANCED (101-120)", Colors.YELLOW, True)
    cprint("  101. WiFi Mesh Network Creator", Colors.WHITE)
    cprint("  102. WiFi Mesh Network Scanner", Colors.WHITE)
    cprint("  103. WiFi Mesh Network Analyzer", Colors.WHITE)
    cprint("  104. WiFi Mesh Network Monitor", Colors.WHITE)
    cprint("  105. WiFi Mesh Network Security", Colors.WHITE)
    cprint("  106. WiFi SDN Controller", Colors.WHITE)
    cprint("  107. WiFi NFV Manager", Colors.WHITE)
    cprint("  108. WiFi Edge Computing", Colors.WHITE)
    cprint("  109. WiFi IoT Scanner", Colors.WHITE)
    cprint("  110. WiFi IoT Analyzer", Colors.WHITE)
    cprint("  111. WiFi IoT Security", Colors.WHITE)
    cprint("  112. WiFi IoT Monitor", Colors.WHITE)
    cprint("  113. WiFi IoT Traffic Analyzer", Colors.WHITE)
    cprint("  114. WiFi IoT Device Discovery", Colors.WHITE)
    cprint("  115. WiFi IoT Vulnerability Scanner", Colors.WHITE)
    cprint("  116. WiFi IoT Firmware Analyzer", Colors.WHITE)
    cprint("  117. WiFi IoT Protocol Analyzer", Colors.WHITE)
    cprint("  118. WiFi IoT Network Scanner", Colors.WHITE)
    cprint("  119. WiFi IoT Security Audit", Colors.WHITE)
    cprint("  120. WiFi IoT Penetration Test", Colors.WHITE)
    
    print()
    cprint("  🔧 WIFI UTILITIES (121-130)", Colors.YELLOW, True)
    cprint("  121. WiFi Connection Manager", Colors.WHITE)
    cprint("  122. WiFi Profile Manager", Colors.WHITE)
    cprint("  123. WiFi Password Manager", Colors.WHITE)
    cprint("  124. WiFi Key Generator", Colors.WHITE)
    cprint("  125. WiFi SSID Generator", Colors.WHITE)
    cprint("  126. WiFi MAC Generator", Colors.WHITE)
    cprint("  127. WiFi IP Scanner", Colors.WHITE)
    cprint("  128. WiFi Netmask Calculator", Colors.WHITE)
    cprint("  129. WiFi Gateway Finder", Colors.WHITE)
    cprint("  130. WiFi Subnet Scanner", Colors.WHITE)
    
    print(Colors.CYAN + "=" * 70 + Colors.END)
    cprint("  0.  Exit Tool", Colors.RED, True)
    print(Colors.CYAN + "=" * 70 + Colors.END)

# ==================== HELPER FUNCTIONS ====================

def get_input(prompt, default=""):
    try:
        return input(prompt).strip() or default
    except:
        return default

def install_package(package):
    try:
        cprint(f"⚠️  Installing {package}...", Colors.YELLOW)
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-q"])
        cprint(f"✅ Installed {package}!", Colors.GREEN)
        return True
    except:
        cprint(f"❌ Failed to install {package}", Colors.RED)
        return False

def check_root():
    if os.geteuid() != 0:
        cprint("⚠️  Some tools require root access!", Colors.YELLOW, True)
        return False
    return True

# ==================== WIFI SCANNING TOOLS (1-20) ====================

def tool_scan_wifi():
    cprint("\n📡 Scanning WiFi Networks...", Colors.BLUE, True)
    try:
        if platform.system() == 'Windows':
            output = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'], timeout=10)
            cprint(output.decode(), Colors.GREEN)
        else:
            output = subprocess.check_output(['nmcli', 'dev', 'wifi', 'list'], timeout=10)
            cprint(output.decode(), Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to scan WiFi. Try: sudo airmon-ng start wlan0", Colors.RED)
        return True

def tool_scan_wifi_detailed():
    cprint("\n📡 Detailed WiFi Scan...", Colors.BLUE, True)
    try:
        if platform.system() == 'Linux':
            output = subprocess.check_output(['iwlist', 'scan'], timeout=30)
            cprint(output.decode(), Colors.GREEN)
        elif platform.system() == 'Windows':
            output = subprocess.check_output(['netsh', 'wlan', 'show', 'networks', 'mode=bssid'], timeout=20)
            cprint(output.decode(), Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to scan. Need root: sudo iwlist scan", Colors.RED)
        return True

def tool_signal_strength():
    cprint("\n📶 WiFi Signal Strength Scanner", Colors.BLUE, True)
    try:
        output = subprocess.check_output(['iwconfig'], timeout=10)
        lines = output.decode().split('\n')
        for line in lines:
            if 'Signal level' in line or 'Signal' in line:
                cprint(line, Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to get signal strength", Colors.RED)
        return True

def tool_channel_scanner():
    cprint("\n🔍 WiFi Channel Scanner", Colors.BLUE, True)
    try:
        output = subprocess.check_output(['iwlist', 'scan', '|', 'grep', 'Channel'], shell=True, timeout=20)
        channels = re.findall(r'Channel:(\d+)', output.decode())
        if channels:
            cprint(f"📊 Found channels: {', '.join(set(channels))}", Colors.CYAN)
        return True
    except:
        cprint("❌ Failed to scan channels", Colors.RED)
        return True

def tool_security_scanner():
    cprint("\n🔐 WiFi Security Type Scanner", Colors.BLUE, True)
    try:
        if platform.system() == 'Linux':
            output = subprocess.check_output(['iwlist', 'scan', '|', 'grep', 'Encryption'], shell=True, timeout=20)
            cprint("🔐 Encryption Types:", Colors.YELLOW, True)
            cprint(output.decode(), Colors.GREEN)
        else:
            output = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'], timeout=10)
            lines = output.decode().split('\n')
            for line in lines:
                if 'Authentication' in line:
                    cprint(line, Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to scan security", Colors.RED)
        return True

def tool_mac_scanner():
    cprint("\n📋 WiFi MAC Address Scanner", Colors.BLUE, True)
    try:
        output = subprocess.check_output(['iwlist', 'scan', '|', 'grep', 'Address'], shell=True, timeout=20)
        macs = re.findall(r'Address: ([0-9A-Fa-f:]+)', output.decode())
        if macs:
            cprint(f"📊 Found {len(macs)} MAC addresses:", Colors.YELLOW, True)
            for mac in set(macs):
                cprint(f"  {mac}", Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to scan MACs", Colors.RED)
        return True

def tool_vendor_scanner():
    cprint("\n🏷️  WiFi Vendor Scanner", Colors.BLUE, True)
    try:
        output = subprocess.check_output(['iwlist', 'scan', '|', 'grep', 'Address'], shell=True, timeout=20)
        macs = re.findall(r'Address: ([0-9A-Fa-f:]+)', output.decode())
        if macs:
            cprint("📋 Vendor Details:", Colors.YELLOW, True)
            for mac in set(macs)[:10]:
                vendor = mac[:8].upper()
                cprint(f"  {mac} -> Vendor: {vendor}", Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to get vendors", Colors.RED)
        return True

def tool_frequency_scanner():
    cprint("\n📡 WiFi Frequency Scanner", Colors.BLUE, True)
    try:
        if platform.system() == 'Linux':
            output = subprocess.check_output(['iwlist', 'scan', '|', 'grep', 'Frequency'], shell=True, timeout=20)
            freq = re.findall(r'Frequency:([0-9.]+) GHz', output.decode())
            if freq:
                cprint(f"📊 Frequencies: {', '.join(set(freq))}", Colors.CYAN)
        return True
    except:
        cprint("❌ Failed to scan frequencies", Colors.RED)
        return True

def tool_encryption_scanner():
    cprint("\n🔐 WiFi Encryption Scanner", Colors.BLUE, True)
    try:
        output = subprocess.check_output(['iwlist', 'scan', '|', 'grep', 'Encryption'], shell=True, timeout=20)
        cprint("🔐 Encryption Details:", Colors.YELLOW, True)
        cprint(output.decode(), Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to scan encryption", Colors.RED)
        return True

def tool_auth_scanner():
    cprint("\n🔐 WiFi Authentication Scanner", Colors.BLUE, True)
    try:
        if platform.system() == 'Linux':
            output = subprocess.check_output(['iwlist', 'scan', '|', 'grep', 'Authentication'], shell=True, timeout=20)
            cprint("🔐 Authentication Types:", Colors.YELLOW, True)
            cprint(output.decode(), Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to scan authentication", Colors.RED)
        return True

def tool_signal_map():
    cprint("\n🗺️  WiFi Signal Map", Colors.BLUE, True)
    try:
        output = subprocess.check_output(['iwlist', 'scan'], timeout=30)
        lines = output.decode().split('\n')
        signals = []
        for line in lines:
            if 'Address' in line:
                mac = re.findall(r'Address: ([0-9A-Fa-f:]+)', line)
                if mac:
                    signals.append({'mac': mac[0]})
            if 'Signal level' in line:
                signal = re.findall(r'Signal level=([-0-9]+)', line)
                if signal and signals:
                    signals[-1]['signal'] = signal[0]
        cprint("📊 Signal Map:", Colors.YELLOW, True)
        for sig in signals[:10]:
            if 'signal' in sig:
                bar = '█' * (int(sig['signal']) // 5 + 20)
                cprint(f"  {sig['mac']}: {sig['signal']}dBm {bar}", Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to create signal map", Colors.RED)
        return True

# ==================== WIFI ANALYSIS TOOLS (21-40) ====================

def tool_network_analyzer():
    cprint("\n🔍 WiFi Network Analyzer", Colors.BLUE, True)
    try:
        if platform.system() == 'Linux':
            output = subprocess.check_output(['iwconfig'], timeout=10)
            cprint("📊 Network Analysis:", Colors.YELLOW, True)
            cprint(output.decode(), Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to analyze network", Colors.RED)
        return True

def tool_traffic_analyzer():
    cprint("\n📊 WiFi Traffic Analyzer", Colors.BLUE, True)
    try:
        output = subprocess.check_output(['ifconfig'], timeout=10)
        lines = output.decode().split('\n')
        for line in lines:
            if 'RX packets' in line or 'TX packets' in line:
                cprint(line, Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to analyze traffic", Colors.RED)
        return True

def tool_packet_analyzer():
    cprint("\n📦 WiFi Packet Analyzer", Colors.BLUE, True)
    try:
        check_root()
        cprint("🔍 Starting packet analysis...", Colors.YELLOW, True)
        cprint("📋 Use tcpdump for detailed analysis", Colors.CYAN)
        return True
    except:
        cprint("❌ Failed to analyze packets", Colors.RED)
        return True

# ==================== WIFI SECURITY TOOLS (41-60) ====================

def tool_wep_cracker():
    cprint("\n🔐 WiFi WEP Cracker", Colors.BLUE, True)
    cprint("⚠️  WEP is deprecated and insecure!", Colors.RED, True)
    bssid = get_input("📡 Enter BSSID: ", "")
    if bssid:
        cprint(f"🔍 Attempting WEP crack on {bssid}...", Colors.YELLOW)
        cprint("📋 Use: aircrack-ng -b " + bssid + " capture.cap", Colors.CYAN)
    return True

def tool_wpa_cracker():
    cprint("\n🔐 WiFi WPA/WPA2 Cracker", Colors.BLUE, True)
    bssid = get_input("📡 Enter BSSID: ", "")
    if bssid:
        cprint(f"🔍 Attempting WPA crack on {bssid}...", Colors.YELLOW)
        cprint("📋 Use: aircrack-ng -w wordlist.txt -b " + bssid + " capture.cap", Colors.CYAN)
    return True

def tool_handshake_capture():
    cprint("\n🤝 WiFi Handshake Capture", Colors.BLUE, True)
    interface = get_input("📡 Enter interface (e.g., wlan0): ", "wlan0")
    bssid = get_input("📡 Enter BSSID: ", "")
    if bssid and interface:
        cprint(f"🔍 Capturing handshake on {interface}...", Colors.YELLOW)
        cprint(f"📋 Command: sudo airodump-ng -c 1 -b {bssid} -w capture {interface}", Colors.CYAN)
    return True

def tool_deauth_attack():
    cprint("\n🚫 WiFi Deauth Attack", Colors.BLUE, True)
    interface = get_input("📡 Enter interface (e.g., wlan0): ", "wlan0")
    bssid = get_input("📡 Enter BSSID: ", "")
    if bssid and interface:
        cprint(f"🔍 Sending deauth on {bssid}...", Colors.YELLOW)
        cprint(f"📋 Command: sudo aireplay-ng -0 5 -a {bssid} {interface}", Colors.CYAN)
    return True

def tool_evil_twin():
    cprint("\n👻 WiFi Evil Twin Attack", Colors.BLUE, True)
    ssid = get_input("📡 Enter SSID to clone: ", "")
    if ssid:
        cprint(f"🔍 Creating Evil Twin for {ssid}...", Colors.YELLOW)
        cprint("📋 Use: hostapd with cloned SSID", Colors.CYAN)
    return True

def tool_mac_spoofing():
    cprint("\n🎭 WiFi MAC Spoofing", Colors.BLUE, True)
    interface = get_input("📡 Enter interface: ", "wlan0")
    new_mac = get_input("📡 Enter new MAC: ", "")
    if interface and new_mac:
        cprint(f"🔍 Spoofing MAC on {interface}...", Colors.YELLOW)
        cprint(f"📋 Command: sudo ifconfig {interface} hw ether {new_mac}", Colors.CYAN)
    return True

def tool_hidden_network_scanner():
    cprint("\n🔍 Hidden WiFi Network Scanner", Colors.BLUE, True)
    try:
        output = subprocess.check_output(['iwlist', 'scan', '|', 'grep', 'ESSID'], shell=True, timeout=20)
        hidden = re.findall(r'ESSID:"(.*?)"', output.decode())
        cprint("📋 Hidden Networks:", Colors.YELLOW, True)
        for ssid in hidden:
            if ssid == '':
                cprint("  Hidden Network Found!", Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to scan hidden networks", Colors.RED)
        return True

def tool_arp_spoofing():
    cprint("\n🎭 WiFi ARP Spoofing", Colors.BLUE, True)
    interface = get_input("📡 Enter interface: ", "wlan0")
    target = get_input("📡 Enter target IP: ", "")
    gateway = get_input("📡 Enter gateway IP: ", "")
    if interface and target and gateway:
        cprint(f"🔍 ARP spoofing {target} -> {gateway}...", Colors.YELLOW)
        cprint(f"📋 Command: sudo arpspoof -i {interface} -t {target} {gateway}", Colors.CYAN)
    return True

def tool_dns_spoofing():
    cprint("\n🎭 WiFi DNS Spoofing", Colors.BLUE, True)
    interface = get_input("📡 Enter interface: ", "wlan0")
    if interface:
        cprint(f"🔍 DNS spoofing on {interface}...", Colors.YELLOW)
        cprint(f"📋 Command: sudo dnsspoof -i {interface}", Colors.CYAN)
    return True

def tool_mitm_attack():
    cprint("\n👤 WiFi MITM Attack", Colors.BLUE, True)
    interface = get_input("📡 Enter interface: ", "wlan0")
    if interface:
        cprint(f"🔍 MITM attack on {interface}...", Colors.YELLOW)
        cprint("📋 Use ettercap for MITM attacks", Colors.CYAN)
    return True

# ==================== WIFI TOOLBOX (61-80) ====================

def tool_adapter_info():
    cprint("\n🖥️  WiFi Adapter Info", Colors.BLUE, True)
    try:
        output = subprocess.check_output(['ifconfig'], timeout=10)
        cprint("📋 Adapter Information:", Colors.YELLOW, True)
        for line in output.decode().split('\n'):
            if 'wlan' in line or 'wlo' in line:
                cprint(line, Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to get adapter info", Colors.RED)
        return True

def tool_adapter_mode_switch():
    cprint("\n🔄 WiFi Adapter Mode Switch", Colors.BLUE, True)
    interface = get_input("📡 Enter interface: ", "wlan0")
    mode = get_input("📡 Enter mode (monitor/managed): ", "monitor")
    if interface and mode:
        cprint(f"🔍 Switching {interface} to {mode} mode...", Colors.YELLOW)
        cprint(f"📋 Command: sudo airmon-ng start {interface}", Colors.CYAN)
    return True

def tool_adapter_channel_set():
    cprint("\n📡 WiFi Adapter Channel Set", Colors.BLUE, True)
    interface = get_input("📡 Enter interface: ", "wlan0")
    channel = get_input("📡 Enter channel (1-14): ", "6")
    if interface and channel:
        cprint(f"🔍 Setting channel {channel} on {interface}...", Colors.YELLOW)
        cprint(f"📋 Command: sudo iwconfig {interface} channel {channel}", Colors.CYAN)
    return True

def tool_adapter_tx_power():
    cprint("\n📶 WiFi Adapter TX Power Set", Colors.BLUE, True)
    interface = get_input("📡 Enter interface: ", "wlan0")
    power = get_input("📡 Enter TX power (dBm): ", "30")
    if interface and power:
        cprint(f"🔍 Setting TX power {power}dBm on {interface}...", Colors.YELLOW)
        cprint(f"📋 Command: sudo iwconfig {interface} txpower {power}", Colors.CYAN)
    return True

# ==================== WIFI MONITORING (81-100) ====================

def tool_signal_monitor():
    cprint("\n📶 WiFi Signal Monitor", Colors.BLUE, True)
    try:
        for i in range(5):
            output = subprocess.check_output(['iwconfig'], timeout=10)
            for line in output.decode().split('\n'):
                if 'Signal level' in line:
                    cprint(f"[{time.strftime('%H:%M:%S')}] {line}", Colors.GREEN)
            time.sleep(2)
        return True
    except:
        cprint("❌ Failed to monitor signal", Colors.RED)
        return True

def tool_traffic_monitor():
    cprint("\n📊 WiFi Traffic Monitor", Colors.BLUE, True)
    try:
        output = subprocess.check_output(['ifconfig'], timeout=10)
        lines = output.decode().split('\n')
        for line in lines:
            if 'RX' in line or 'TX' in line:
                cprint(line, Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to monitor traffic", Colors.RED)
        return True

def tool_bandwidth_monitor():
    cprint("\n📊 WiFi Bandwidth Monitor", Colors.BLUE, True)
    try:
        import psutil
        net_io = psutil.net_io_counters()
        cprint(f"📋 Bandwidth:", Colors.YELLOW, True)
        cprint(f"  Bytes Sent: {net_io.bytes_sent / (1024*1024):.2f} MB", Colors.CYAN)
        cprint(f"  Bytes Received: {net_io.bytes_recv / (1024*1024):.2f} MB", Colors.CYAN)
        return True
    except:
        cprint("❌ Failed to monitor bandwidth", Colors.RED)
        return True

# ==================== WIFI ADVANCED (101-120) ====================

def tool_mesh_creator():
    cprint("\n🌐 WiFi Mesh Network Creator", Colors.BLUE, True)
    interface = get_input("📡 Enter interface: ", "wlan0")
    ssid = get_input("📡 Enter mesh SSID: ", "mesh-network")
    if interface and ssid:
        cprint(f"🔍 Creating mesh network {ssid}...", Colors.YELLOW)
        cprint(f"📋 Command: sudo iw dev {interface} mesh join {ssid}", Colors.CYAN)
    return True

def tool_mesh_scanner():
    cprint("\n🌐 WiFi Mesh Network Scanner", Colors.BLUE, True)
    try:
        output = subprocess.check_output(['iw', 'dev', 'wlan0', 'mesh', 'dump'], timeout=10)
        cprint("📋 Mesh Network Info:", Colors.YELLOW, True)
        cprint(output.decode(), Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to scan mesh network", Colors.RED)
        return True

def tool_iot_scanner():
    cprint("\n🔍 WiFi IoT Scanner", Colors.BLUE, True)
    try:
        import netifaces
        gateways = netifaces.gateways()
        cprint("📋 IoT Devices on Network:", Colors.YELLOW, True)
        cprint("🔍 Scanning for IoT devices...", Colors.CYAN)
        return True
    except:
        cprint("❌ Failed to scan IoT devices", Colors.RED)
        return True

def tool_iot_analyzer():
    cprint("\n🔍 WiFi IoT Analyzer", Colors.BLUE, True)
    ip = get_input("📡 Enter IoT IP address: ", "192.168.1.1")
    if ip:
        cprint(f"🔍 Analyzing IoT device {ip}...", Colors.YELLOW)
        cprint(f"📋 Use nmap for detailed scanning: nmap {ip}", Colors.CYAN)
    return True

def tool_iot_security():
    cprint("\n🔐 WiFi IoT Security", Colors.BLUE, True)
    ip = get_input("📡 Enter IoT IP address: ", "192.168.1.1")
    if ip:
        cprint(f"🔐 Security scan of {ip}...", Colors.YELLOW)
        cprint("📋 Common IoT Vulnerabilities:", Colors.CYAN)
        cprint("  - Default credentials", Colors.RED)
        cprint("  - Open ports", Colors.RED)
        cprint("  - Weak encryption", Colors.RED)
    return True

# ==================== WIFI UTILITIES (121-130) ====================

def tool_connection_manager():
    cprint("\n🔗 WiFi Connection Manager", Colors.BLUE, True)
    try:
        output = subprocess.check_output(['nmcli', 'connection', 'show'], timeout=10)
        cprint("📋 Saved Connections:", Colors.YELLOW, True)
        cprint(output.decode(), Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to get connections", Colors.RED)
        return True

def tool_profile_manager():
    cprint("\n📋 WiFi Profile Manager", Colors.BLUE, True)
    try:
        if platform.system() == 'Windows':
            output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], timeout=10)
            cprint("📋 WiFi Profiles:", Colors.YELLOW, True)
            cprint(output.decode(), Colors.GREEN)
        else:
            output = subprocess.check_output(['nmcli', 'connection', 'show'], timeout=10)
            cprint(output.decode(), Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to get profiles", Colors.RED)
        return True

def tool_password_manager():
    cprint("\n🔑 WiFi Password Manager", Colors.BLUE, True)
    ssid = get_input("📡 Enter SSID: ", "")
    if ssid:
        try:
            if platform.system() == 'Windows':
                output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear'], timeout=10)
                cprint("🔑 Password Details:", Colors.YELLOW, True)
                cprint(output.decode(), Colors.GREEN)
            else:
                cprint(f"🔑 For {ssid}: Check /etc/NetworkManager/system-connections/", Colors.CYAN)
        except:
            cprint("❌ Failed to get password", Colors.RED)
    return True

def tool_key_generator():
    cprint("\n🔑 WiFi Key Generator", Colors.BLUE, True)
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
    cprint(f"🔐 Generated Key: {key}", Colors.GREEN)
    return True

def tool_ssid_generator():
    cprint("\n📡 WiFi SSID Generator", Colors.BLUE, True)
    adjectives = ['Fast', 'Secure', 'Max', 'Ultra', 'Super', 'Mega', 'Giga']
    nouns = ['WiFi', 'Network', 'Connect', 'Access', 'Link']
    ssid = random.choice(adjectives) + '-' + random.choice(nouns) + '-' + str(random.randint(100, 999))
    cprint(f"📡 Generated SSID: {ssid}", Colors.GREEN)
    return True

def tool_mac_generator():
    cprint("\n🎭 WiFi MAC Generator", Colors.BLUE, True)
    mac = ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)])
    cprint(f"🎭 Generated MAC: {mac}", Colors.GREEN)
    return True

def tool_ip_scanner():
    cprint("\n🔍 WiFi IP Scanner", Colors.BLUE, True)
    try:
        import netifaces
        gateways = netifaces.gateways()
        cprint("📋 IP Scan Results:", Colors.YELLOW, True)
        cprint("🔍 Use: nmap -sn 192.168.1.0/24", Colors.CYAN)
        return True
    except:
        cprint("❌ Failed to scan IPs", Colors.RED)
        return True

def tool_netmask_calculator():
    cprint("\n📊 WiFi Netmask Calculator", Colors.BLUE, True)
    ip = get_input("📡 Enter IP (e.g., 192.168.1.1): ", "192.168.1.1")
    cidr = get_input("📡 Enter CIDR (e.g., 24): ", "24")
    if ip and cidr:
        cprint(f"📋 IP: {ip}/{cidr}", Colors.CYAN)
        cprint(f"📋 Netmask: {socket.inet_ntoa(struct.pack('!I', (0xffffffff << (32 - int(cidr))) & 0xffffffff))}", Colors.CYAN)
    return True

def tool_gateway_finder():
    cprint("\n🚪 WiFi Gateway Finder", Colors.BLUE, True)
    try:
        import netifaces
        gateways = netifaces.gateways()
        cprint("📋 Gateways:", Colors.YELLOW, True)
        for gateway in gateways:
            cprint(f"  {gateway}: {gateways[gateway]}", Colors.GREEN)
        return True
    except:
        cprint("❌ Failed to find gateway", Colors.RED)
        return True

def tool_subnet_scanner():
    cprint("\n🌐 WiFi Subnet Scanner", Colors.BLUE, True)
    subnet = get_input("📡 Enter subnet (e.g., 192.168.1.0/24): ", "192.168.1.0/24")
    if subnet:
        cprint(f"🔍 Scanning {subnet}...", Colors.YELLOW)
        cprint("📋 Use: nmap -sP " + subnet, Colors.CYAN)
    return True

# ==================== MAIN ====================

def main():
    while True:
        print_header()
        print_menu()
        
        choice = get_input(f"\n{Colors.BOLD}🎯 Select tool (0-130): {Colors.END}")
        
        if choice == '0':
            cprint("\n👋 Thanks for using RIR WiFi Testing Suite!", Colors.GREEN, True)
            cprint("🔒 Stay Secure, Stay Safe!", Colors.CYAN, True)
            cprint("🛡️  RIR Cyber Tools", Colors.MAGENTA, True)
            break
        
        tools_map = {
            '1': tool_scan_wifi,
            '2': tool_scan_wifi_detailed,
            '3': tool_signal_strength,
            '4': tool_channel_scanner,
            '5': tool_security_scanner,
            '6': tool_mac_scanner,
            '7': tool_vendor_scanner,
            '8': tool_frequency_scanner,
            '9': tool_encryption_scanner,
            '10': tool_auth_scanner,
            '11': tool_signal_map,
            '21': tool_network_analyzer,
            '22': tool_traffic_analyzer,
            '23': tool_packet_analyzer,
            '41': tool_wep_cracker,
            '42': tool_wpa_cracker,
            '46': tool_handshake_capture,
            '47': tool_deauth_attack,
            '48': tool_evil_twin,
            '49': tool_mac_spoofing,
            '51': tool_hidden_network_scanner,
            '53': tool_arp_spoofing,
            '54': tool_dns_spoofing,
            '55': tool_mitm_attack,
            '61': tool_adapter_info,
            '62': tool_adapter_mode_switch,
            '63': tool_adapter_channel_set,
            '64': tool_adapter_tx_power,
            '81': tool_signal_monitor,
            '82': tool_traffic_monitor,
            '83': tool_bandwidth_monitor,
            '101': tool_mesh_creator,
            '102': tool_mesh_scanner,
            '109': tool_iot_scanner,
            '110': tool_iot_analyzer,
            '111': tool_iot_security,
            '121': tool_connection_manager,
            '122': tool_profile_manager,
            '123': tool_password_manager,
            '124': tool_key_generator,
            '125': tool_ssid_generator,
            '126': tool_mac_generator,
            '127': tool_ip_scanner,
            '128': tool_netmask_calculator,
            '129': tool_gateway_finder,
            '130': tool_subnet_scanner,
        }
        
        if choice in tools_map:
            tools_map[choice]()
        else:
            cprint("❌ Tool not implemented yet! Coming soon...", Colors.RED)
        
        get_input(f"\n{Colors.CYAN}⏎ Press Enter to continue...{Colors.END}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cprint("\n\n👋 Exited by user. Goodbye!", Colors.YELLOW, True)
    except Exception as e:
        cprint(f"\n❌ Error: {str(e)}", Colors.RED, True)