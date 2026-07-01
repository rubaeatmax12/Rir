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
import urllib.parse
import ssl
import platform
import datetime
import threading
import queue
import tempfile
import shutil
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
║         WEB TESTING SUITE v6.0 - 100 TOOLS                  ║
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
    cprint("  📡 NETWORK TESTING TOOLS (1-20)", Colors.YELLOW, True)
    cprint("  1.  Website Status Checker", Colors.WHITE)
    cprint("  2.  Ping Tool", Colors.WHITE)
    cprint("  3.  DNS Lookup", Colors.WHITE)
    cprint("  4.  IP Geolocation", Colors.WHITE)
    cprint("  5.  Port Scanner", Colors.WHITE)
    cprint("  6.  SSL Certificate Checker", Colors.WHITE)
    cprint("  7.  Domain WHOIS Lookup", Colors.WHITE)
    cprint("  8.  Reverse DNS Lookup", Colors.WHITE)
    cprint("  9.  HTTP Headers Checker", Colors.WHITE)
    cprint("  10. Server Location Finder", Colors.WHITE)
    cprint("  11. Subdomain Finder", Colors.WHITE)
    cprint("  12. Traceroute Tool", Colors.WHITE)
    cprint("  13. IP Address Validator", Colors.WHITE)
    cprint("  14. Domain Availability Checker", Colors.WHITE)
    cprint("  15. MX Record Lookup", Colors.WHITE)
    cprint("  16. NS Record Lookup", Colors.WHITE)
    cprint("  17. TXT Record Lookup", Colors.WHITE)
    cprint("  18. CNAME Record Lookup", Colors.WHITE)
    
    print()
    cprint("  🔐 SECURITY TESTING TOOLS (19-35)", Colors.YELLOW, True)
    cprint("  19. XSS Vulnerability Scanner", Colors.WHITE)
    cprint("  20. SQL Injection Tester", Colors.WHITE)
    cprint("  21. CSRF Tester", Colors.WHITE)
    cprint("  22. Security Headers Checker", Colors.WHITE)
    cprint("  23. SSL/TLS Vulnerability Scanner", Colors.WHITE)
    cprint("  24. Password Strength Tester", Colors.WHITE)
    cprint("  25. JWT Token Validator", Colors.WHITE)
    cprint("  26. CORS Tester", Colors.WHITE)
    cprint("  27. Cookie Scanner", Colors.WHITE)
    cprint("  28. CSP Header Checker", Colors.WHITE)
    cprint("  29. Directory Traversal Test", Colors.WHITE)
    cprint("  30. Open Redirect Checker", Colors.WHITE)
    cprint("  31. Clickjacking Test", Colors.WHITE)
    cprint("  32. MIME Sniffing Test", Colors.WHITE)
    cprint("  33. Subresource Integrity Check", Colors.WHITE)
    
    print()
    cprint("  🚀 PERFORMANCE TESTING TOOLS (34-45)", Colors.YELLOW, True)
    cprint("  34. Website Load Time", Colors.WHITE)
    cprint("  35. Page Speed Test", Colors.WHITE)
    cprint("  36. Load Tester (Multiple Requests)", Colors.WHITE)
    cprint("  37. Stress Tester", Colors.WHITE)
    cprint("  38. Concurrent User Test", Colors.WHITE)
    cprint("  39. API Load Tester", Colors.WHITE)
    cprint("  40. Response Time Analyzer", Colors.WHITE)
    
    print()
    cprint("  🌐 API TESTING TOOLS (41-48)", Colors.YELLOW, True)
    cprint("  41. REST API Tester", Colors.WHITE)
    cprint("  42. GraphQL API Tester", Colors.WHITE)
    cprint("  43. Webhook Tester", Colors.WHITE)
    cprint("  44. API Response Time", Colors.WHITE)
    cprint("  45. JSON API Validator", Colors.WHITE)
    cprint("  46. API Authentication Test", Colors.WHITE)
    cprint("  47. Rate Limit Tester", Colors.WHITE)
    cprint("  48. Mock API Generator", Colors.WHITE)
    
    print()
    cprint("  📝 TEXT & DATA TOOLS (49-65)", Colors.YELLOW, True)
    cprint("  49. JSON Formatter & Validator", Colors.WHITE)
    cprint("  50. XML Formatter & Validator", Colors.WHITE)
    cprint("  51. Base64 Encoder/Decoder", Colors.WHITE)
    cprint("  52. URL Encoder/Decoder", Colors.WHITE)
    cprint("  53. HTML Formatter", Colors.WHITE)
    cprint("  54. HTML to Text Converter", Colors.WHITE)
    cprint("  55. Text to Slug Converter", Colors.WHITE)
    cprint("  56. Regex Tester", Colors.WHITE)
    cprint("  57. Text Diff Checker", Colors.WHITE)
    cprint("  58. Character/Word/Lines Counter", Colors.WHITE)
    cprint("  59. Text Reverser", Colors.WHITE)
    cprint("  60. Case Converter", Colors.WHITE)
    
    print()
    cprint("  🔑 GENERATOR TOOLS (61-75)", Colors.YELLOW, True)
    cprint("  61. Random Password Generator", Colors.WHITE)
    cprint("  62. UUID Generator", Colors.WHITE)
    cprint("  63. Random Data Generator", Colors.WHITE)
    cprint("  64. Hash Generator (MD5/SHA)", Colors.WHITE)
    cprint("  65. JWT Token Generator", Colors.WHITE)
    cprint("  66. API Key Generator", Colors.WHITE)
    cprint("  67. Fake User Generator", Colors.WHITE)
    cprint("  68. Lorem Ipsum Generator", Colors.WHITE)
    cprint("  69. Random Number Generator", Colors.WHITE)
    cprint("  70. QR Code Generator", Colors.WHITE)
    
    print()
    cprint("  🖥️ SYSTEM TOOLS (71-85)", Colors.YELLOW, True)
    cprint("  71. System Information", Colors.WHITE)
    cprint("  72. Disk Usage Checker", Colors.WHITE)
    cprint("  73. Python Environment Info", Colors.WHITE)
    cprint("  74. Network Interface Info", Colors.WHITE)
    cprint("  75. File System Monitor", Colors.WHITE)
    cprint("  76. System Benchmark", Colors.WHITE)
    cprint("  77. Memory Info", Colors.WHITE)
    cprint("  78. CPU Info", Colors.WHITE)
    cprint("  79. System Uptime", Colors.WHITE)
    cprint("  80. User Info", Colors.WHITE)
    
    print()
    cprint("  🛠️  UTILITY TOOLS (81-100)", Colors.YELLOW, True)
    cprint("  81. Email Extractor", Colors.WHITE)
    cprint("  82. Phone Number Extractor", Colors.WHITE)
    cprint("  83. Link Extractor", Colors.WHITE)
    cprint("  84. Text Analyzer", Colors.WHITE)
    cprint("  85. Website Sitemap Generator", Colors.WHITE)
    cprint("  86. Keyword Extractor", Colors.WHITE)
    cprint("  87. Hashtag Generator", Colors.WHITE)
    cprint("  88. Text to Speech (Basic)", Colors.WHITE)
    cprint("  89. QR Code Reader", Colors.WHITE)
    cprint("  90. Color Converter", Colors.WHITE)
    cprint("  91. Unit Converter", Colors.WHITE)
    cprint("  92. Temperature Converter", Colors.WHITE)
    cprint("  93. Currency Converter (Basic)", Colors.WHITE)
    cprint("  94. Time Zone Converter", Colors.WHITE)
    cprint("  95. Date Calculator", Colors.WHITE)
    cprint("  96. Age Calculator", Colors.WHITE)
    cprint("  97. BMI Calculator", Colors.WHITE)
    cprint("  98. Loan Calculator", Colors.WHITE)
    cprint("  99. Discount Calculator", Colors.WHITE)
    cprint("  100. Tip Calculator", Colors.WHITE)
    
    print(Colors.CYAN + "=" * 70 + Colors.END)
    cprint("  0.  Exit Tool", Colors.RED, True)
    print(Colors.CYAN + "=" * 70 + Colors.END)

# ==================== HELPER FUNCTIONS ====================

def get_input(prompt, default=""):
    try:
        return input(prompt).strip() or default
    except:
        return default

def safe_request(url, method='GET', timeout=10, **kwargs):
    try:
        if method.upper() == 'GET':
            return requests.get(url, timeout=timeout, verify=False, **kwargs)
        elif method.upper() == 'POST':
            return requests.post(url, timeout=timeout, verify=False, **kwargs)
        elif method.upper() == 'HEAD':
            return requests.head(url, timeout=timeout, verify=False, **kwargs)
        elif method.upper() == 'OPTIONS':
            return requests.options(url, timeout=timeout, verify=False, **kwargs)
    except:
        return None

def install_package(package):
    try:
        cprint(f"⚠️  Installing {package}...", Colors.YELLOW)
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-q"])
        cprint(f"✅ Installed {package}!", Colors.GREEN)
        return True
    except:
        cprint(f"❌ Failed to install {package}", Colors.RED)
        return False

# ==================== TOOL FUNCTIONS (1-20: NETWORK) ====================

def tool_website_status():
    cprint("\n📡 Website Status Checker", Colors.BLUE, True)
    url = get_input("🌐 Enter website URL (e.g., https://google.com): ", "https://google.com")
    
    response = safe_request(url)
    if response:
        cprint(f"✅ Status: {response.status_code} - {response.reason}", Colors.GREEN)
        cprint(f"⏱️  Response Time: {response.elapsed.total_seconds():.3f} seconds", Colors.CYAN)
        cprint(f"📦 Content Size: {len(response.content) / 1024:.2f} KB", Colors.CYAN)
        cprint(f"🌐 Server: {response.headers.get('Server', 'Unknown')}", Colors.CYAN)
        cprint(f"📅 Date: {response.headers.get('Date', 'Unknown')}", Colors.CYAN)
    else:
        cprint("❌ Website is down or unreachable!", Colors.RED)
    return True

def tool_ping():
    cprint("\n📡 Ping Tool", Colors.BLUE, True)
    host = get_input("🌐 Enter host/IP (e.g., google.com): ", "google.com")
    
    try:
        if platform.system() == 'Windows':
            cmd = ['ping', '-n', '4', host]
        else:
            cmd = ['ping', '-c', '4', host]
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=15)
        cprint(output.decode(), Colors.GREEN)
        return True
    except subprocess.TimeoutExpired:
        cprint("❌ Ping timeout", Colors.RED)
    except Exception as e:
        cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def tool_dns_lookup():
    cprint("\n📡 DNS Lookup", Colors.BLUE, True)
    domain = get_input("🌐 Enter domain (e.g., google.com): ", "google.com")
    
    try:
        import dns.resolver
        record_types = ['A', 'AAAA', 'MX', 'TXT', 'CNAME', 'NS']
        
        for record in record_types:
            try:
                answers = dns.resolver.resolve(domain, record)
                cprint(f"{record} Records:", Colors.YELLOW, True)
                for r in answers:
                    cprint(f"  {r}", Colors.GREEN)
            except:
                cprint(f"  No {record} records found", Colors.RED)
        return True
    except ImportError:
        if install_package("dnspython"):
            cprint("✅ Installed! Please run the tool again.", Colors.GREEN)
        return False
    except Exception as e:
        cprint(f"❌ Error: {str(e)}", Colors.RED)
        return True

def tool_ip_geolocation():
    cprint("\n📍 IP Geolocation", Colors.BLUE, True)
    ip = get_input("🌐 Enter IP address: ", "8.8.8.8")
    
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}', timeout=10)
        data = response.json()
        
        if data.get('status') == 'success':
            cprint(f"📍 Location: {data.get('city')}, {data.get('regionName')}, {data.get('country')}", Colors.CYAN)
            cprint(f"📊 Coordinates: {data.get('lat')}, {data.get('lon')}", Colors.CYAN)
            cprint(f"🌐 ISP: {data.get('isp')}", Colors.CYAN)
            cprint(f"⏰ Timezone: {data.get('timezone')}", Colors.CYAN)
            cprint(f"🏢 Organization: {data.get('org')}", Colors.CYAN)
        else:
            cprint("❌ IP not found", Colors.RED)
        return True
    except Exception as e:
        cprint(f"❌ Error: {str(e)}", Colors.RED)
        return True

def tool_port_scanner():
    cprint("\n🔍 Port Scanner", Colors.BLUE, True)
    host = get_input("🌐 Enter host/IP: ", "google.com")
    ports_input = get_input("🔢 Enter ports (comma separated, e.g., 80,443,22): ", "80,443,22")
    
    try:
        ports = [int(p.strip()) for p in ports_input.split(',')]
    except:
        cprint("❌ Invalid port format", Colors.RED)
        return True
    
    cprint(f"🔍 Scanning {host}...", Colors.YELLOW, True)
    open_ports = []
    
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
                cprint(f"✅ Port {port}: OPEN", Colors.GREEN)
            else:
                cprint(f"❌ Port {port}: CLOSED", Colors.RED)
            sock.close()
        except:
            cprint(f"❌ Port {port}: ERROR", Colors.RED)
    
    cprint(f"\n📊 Open Ports: {open_ports}", Colors.CYAN)
    return True

def tool_ssl_check():
    cprint("\n🔒 SSL Certificate Checker", Colors.BLUE, True)
    domain = get_input("🌐 Enter domain (e.g., google.com): ", "google.com")
    
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                
                cprint("✅ SSL Certificate Details:", Colors.GREEN, True)
                cprint(f"📋 Subject: {cert.get('subject')}", Colors.CYAN)
                cprint(f"📋 Issuer: {cert.get('issuer')}", Colors.CYAN)
                cprint(f"📅 Expiry: {cert.get('notAfter')}", Colors.CYAN)
                cprint(f"🔑 Serial: {cert.get('serialNumber')}", Colors.CYAN)
                
                # Check expiry
                from datetime import datetime
                expiry = datetime.strptime(cert.get('notAfter'), '%b %d %H:%M:%S %Y %Z')
                days_left = (expiry - datetime.now()).days
                if days_left < 30:
                    cprint(f"⚠️  Certificate expires in {days_left} days!", Colors.RED)
                elif days_left < 90:
                    cprint(f"⚠️  Certificate expires in {days_left} days", Colors.YELLOW)
                else:
                    cprint(f"✅ Certificate valid for {days_left} more days", Colors.GREEN)
        return True
    except Exception as e:
        cprint(f"❌ Error: {str(e)}", Colors.RED)
        return True

def tool_whois_lookup():
    cprint("\n📋 WHOIS Lookup", Colors.BLUE, True)
    domain = get_input("🌐 Enter domain: ", "google.com")
    
    try:
        import whois
        w = whois.whois(domain)
        
        cprint(f"📋 Registrar: {w.registrar}", Colors.CYAN)
        cprint(f"📅 Creation Date: {w.creation_date}", Colors.CYAN)
        cprint(f"📅 Expiration Date: {w.expiration_date}", Colors.CYAN)
        cprint(f"🌐 Name Servers: {w.name_servers}", Colors.CYAN)
        cprint(f"📧 Email: {w.emails}", Colors.CYAN)
        cprint(f"🏢 Organization: {w.org}", Colors.CYAN)
        return True
    except ImportError:
        if install_package("python-whois"):
            cprint("✅ Installed! Please run the tool again.", Colors.GREEN)
        return False
    except Exception as e:
        cprint(f"❌ Error: {str(e)}", Colors.RED)
        return True

def tool_reverse_dns():
    cprint("\n🔄 Reverse DNS Lookup", Colors.BLUE, True)
    ip = get_input("🌐 Enter IP address: ", "8.8.8.8")
    
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        cprint(f"✅ Hostname: {hostname}", Colors.GREEN)
        cprint(f"IP: {ip}", Colors.CYAN)
        return True
    except:
        cprint(f"❌ No reverse DNS record for {ip}", Colors.RED)
        return True

def tool_http_headers():
    cprint("\n📋 HTTP Headers Checker", Colors.BLUE, True)
    url = get_input("🌐 Enter URL: ", "https://google.com")
    
    response = safe_request(url, 'HEAD')
    if response:
        cprint("📋 Headers:", Colors.YELLOW, True)
        for key, value in sorted(response.headers.items()):
            cprint(f"  {key}: {value}", Colors.GREEN)
        return True
    else:
        cprint("❌ Failed to get headers", Colors.RED)
        return True

def tool_server_location():
    cprint("\n📍 Server Location Finder", Colors.BLUE, True)
    url = get_input("🌐 Enter URL: ", "https://google.com")
    
    try:
        parsed = urlparse(url)
        domain = parsed.netloc or parsed.path
        ip = socket.gethostbyname(domain)
        
        response = requests.get(f'http://ip-api.com/json/{ip}', timeout=10)
        data = response.json()
        
        if data.get('status') == 'success':
            cprint(f"🌐 Domain: {domain}", Colors.CYAN)
            cprint(f"🔢 IP: {ip}", Colors.CYAN)
            cprint(f"📍 Location: {data.get('city')}, {data.get('regionName')}, {data.get('country')}", Colors.CYAN)
            cprint(f"📊 Coordinates: {data.get('lat')}, {data.get('lon')}", Colors.CYAN)
            cprint(f"🌐 ISP: {data.get('isp')}", Colors.CYAN)
        else:
            cprint("❌ Location not found", Colors.RED)
        return True
    except Exception as e:
        cprint(f"❌ Error: {str(e)}", Colors.RED)
        return True

def tool_subdomain_finder():
    cprint("\n🔍 Subdomain Finder", Colors.BLUE, True)
    domain = get_input("🌐 Enter domain: ", "google.com")
    
    subdomains = ['www', 'mail', 'ftp', 'api', 'blog', 'shop', 'admin', 'test', 'dev', 'staging', 'demo', 'beta']
    found = []
    
    cprint(f"🔍 Scanning for subdomains...", Colors.YELLOW, True)
    
    for sub in subdomains:
        try:
            subdomain = f"{sub}.{domain}"
            socket.gethostbyname(subdomain)
            found.append(subdomain)
            cprint(f"✅ Found: {subdomain}", Colors.GREEN)
        except:
            pass
    
    if not found:
        cprint("❌ No subdomains found in common list", Colors.RED)
    else:
        cprint(f"\n📊 Found {len(found)} subdomains", Colors.CYAN)
    return True

def tool_traceroute():
    cprint("\n🔍 Traceroute Tool", Colors.BLUE, True)
    host = get_input("🌐 Enter host/IP: ", "google.com")
    
    try:
        if platform.system() == 'Windows':
            cmd = ['tracert', '-d', '-h', '10', host]
        else:
            cmd = ['traceroute', '-n', '-m', '10', host]
        
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=30)
        cprint(output.decode(), Colors.GREEN)
        return True
    except subprocess.TimeoutExpired:
        cprint("❌ Traceroute timeout", Colors.RED)
    except Exception as e:
        cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def tool_ip_validator():
    cprint("\n✅ IP Address Validator", Colors.BLUE, True)
    ip = get_input("🌐 Enter IP address: ", "192.168.1.1")
    
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ip):
        parts = ip.split('.')
        valid = all(0 <= int(p) <= 255 for p in parts)
        if valid:
            cprint(f"✅ {ip} is a valid IP address", Colors.GREEN)
            first = int(parts[0])
            if first == 10 or (first == 172 and 16 <= int(parts[1]) <= 31) or (first == 192 and parts[1] == '168'):
                cprint("📋 This is a private IP address", Colors.YELLOW)
            else:
                cprint("📋 This is a public IP address", Colors.CYAN)
        else:
            cprint(f"❌ {ip} is invalid (numbers must be 0-255)", Colors.RED)
    else:
        cprint(f"❌ {ip} is not a valid IP address format", Colors.RED)
    return True

def tool_domain_availability():
    cprint("\n🌐 Domain Availability Checker", Colors.BLUE, True)
    domain = get_input("🌐 Enter domain (e.g., example.com): ", "example.com")
    
    try:
        import whois
        w = whois.whois(domain)
        if w.domain_name:
            cprint(f"❌ {domain} is already registered!", Colors.RED)
            cprint(f"📋 Registrar: {w.registrar}", Colors.CYAN)
            cprint(f"📅 Expires: {w.expiration_date}", Colors.CYAN)
        else:
            cprint(f"✅ {domain} is available!", Colors.GREEN)
    except:
        cprint(f"✅ {domain} might be available!", Colors.GREEN)
    return True

def tool_mx_lookup():
    cprint("\n📧 MX Record Lookup", Colors.BLUE, True)
    domain = get_input("🌐 Enter domain: ", "google.com")
    
    try:
        import dns.resolver
        answers = dns.resolver.resolve(domain, 'MX')
        cprint(f"MX Records for {domain}:", Colors.YELLOW, True)
        for r in sorted(answers, key=lambda x: x.preference):
            cprint(f"  {r.preference} - {r.exchange}", Colors.GREEN)
        return True
    except ImportError:
        if install_package("dnspython"):
            cprint("✅ Installed! Please run the tool again.", Colors.GREEN)
        return False
    except Exception as e:
        cprint(f"❌ Error: {str(e)}", Colors.RED)
        return True

def tool_ns_lookup():
    cprint("\n🌐 NS Record Lookup", Colors.BLUE, True)
    domain = get_input("🌐 Enter domain: ", "google.com")
    
    try:
        import dns.resolver
        answers = dns.resolver.resolve(domain, 'NS')
        cprint(f"NS Records for {domain}:", Colors.YELLOW, True)
        for r in answers:
            cprint(f"  {r}", Colors.GREEN)
        return True
    except ImportError:
        if install_package("dnspython"):
            cprint("✅ Installed! Please run the tool again.", Colors.GREEN)
        return False
    except Exception as e:
        cprint(f"❌ Error: {str(e)}", Colors.RED)
        return True

def tool_txt_lookup():
    cprint("\n📝 TXT Record Lookup", Colors.BLUE, True)
    domain = get_input("🌐 Enter domain: ", "google.com")
    
    try:
        import dns.resolver
        answers = dns.resolver.resolve(domain, 'TXT')
        cprint(f"TXT Records for {domain}:", Colors.YELLOW, True)
        for r in answers:
            cprint(f"  {r}", Colors.GREEN)
        return True
    except ImportError:
        if install_package("dnspython"):
            cprint("✅ Installed! Please run the tool again.", Colors.GREEN)
        return False
    except Exception as e:
        cprint(f"❌ No TXT records found or error: {str(e)}", Colors.RED)
        return True

# ==================== TOOL FUNCTIONS (19-35: SECURITY) ====================

def tool_xss_scanner():
    cprint("\n🔐 XSS Vulnerability Scanner", Colors.BLUE, True)
    url = get_input("🌐 Enter URL (e.g., https://example.com): ", "https://example.com")
    
    if '?' not in url:
        if url.endswith('/'):
            url = url + '?q='
        else:
            url = url + '?q='
    
    payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert(1)>",
        "javascript:alert('XSS')",
        "'><script>alert('XSS')</script>",
        "<body onload=alert('XSS')>",
        "><script>alert(1)</script>",
        "onerror=alert(1)",
        "<svg/onload=alert(1)>"
    ]
    
    cprint("🔍 Scanning for XSS vulnerabilities...", Colors.YELLOW, True)
    found = False
    
    for payload in payloads:
        try:
            encoded = urllib.parse.quote(payload)
            test_url = url + encoded
            response = safe_request(test_url)
            if response and payload in response.text:
                cprint(f"⚠️  VULNERABLE to: {payload[:40]}...", Colors.RED)
                found = True
            else:
                cprint(f"✅ Safe from: {payload[:40]}...", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)[:50]}", Colors.RED)
    
    if not found:
        cprint("\n✅ No XSS vulnerabilities found.", Colors.GREEN, True)
    else:
        cprint("\n⚠️  XSS vulnerabilities detected!", Colors.RED, True)
    return True

def tool_sql_injection():
    cprint("\n🔐 SQL Injection Tester", Colors.BLUE, True)
    url = get_input("🌐 Enter URL (e.g., https://example.com?id=): ", "https://example.com?id=1")
    
    if '?' not in url:
        if url.endswith('/'):
            url = url + '?id='
        else:
            url = url + '?id='
    
    payloads = [
        "'",
        "1' OR '1'='1",
        "1; DROP TABLE users",
        "' UNION SELECT NULL--",
        "' AND 1=1--",
        "1' AND '1'='1",
        "admin'--",
        "1' OR 1=1--"
    ]
    
    cprint("🔍 Scanning for SQL Injection...", Colors.YELLOW, True)
    found = False
    sql_errors = ['mysql', 'sql', 'syntax', 'error', 'database', 'unclosed', 'quoted', 'warning', 'mysqli']
    
    for payload in payloads:
        try:
            encoded = urllib.parse.quote(payload)
            test_url = url + encoded
            response = safe_request(test_url)
            if response:
                text_lower = response.text.lower()
                if any(error in text_lower for error in sql_errors):
                    cprint(f"⚠️  VULNERABLE to: {payload[:30]}...", Colors.RED)
                    found = True
                else:
                    cprint(f"✅ Safe from: {payload[:30]}...", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)[:50]}", Colors.RED)
    
    if not found:
        cprint("\n✅ No SQL Injection vulnerabilities found.", Colors.GREEN, True)
    else:
        cprint("\n⚠️  SQL Injection vulnerabilities detected!", Colors.RED, True)
    return True

def tool_csrf_tester():
    cprint("\n🔐 CSRF Tester", Colors.BLUE, True)
    url = get_input("🌐 Enter URL: ", "https://example.com")
    
    try:
        response = safe_request(url)
        if response:
            csrf_tokens = re.findall(r'csrf|token|_token', response.text, re.IGNORECASE)
            if csrf_tokens:
                cprint(f"✅ Found CSRF protection: {len(csrf_tokens)} tokens found", Colors.GREEN)
                cprint("📋 Tokens found in:", Colors.CYAN)
                for token in set(csrf_tokens[:5]):
                    cprint(f"  - {token}", Colors.CYAN)
            else:
                cprint("⚠️  No CSRF tokens found! May be vulnerable", Colors.RED)
        return True
    except Exception as e:
        cprint(f"❌ Error: {str(e)}", Colors.RED)
        return True

def tool_security_headers():
    cprint("\n🔒 Security Headers Checker", Colors.BLUE, True)
    url = get_input("🌐 Enter URL: ", "https://google.com")
    
    response = safe_request(url)
    if not response:
        cprint("❌ Failed to fetch headers", Colors.RED)
        return True
    
    headers = response.headers
    checks = {
        'X-Frame-Options': headers.get('X-Frame-Options'),
        'X-XSS-Protection': headers.get('X-XSS-Protection'),
        'X-Content-Type-Options': headers.get('X-Content-Type-Options'),
        'Content-Security-Policy': headers.get('Content-Security-Policy'),
        'Strict-Transport-Security': headers.get('Strict-Transport-Security'),
        'Referrer-Policy': headers.get('Referrer-Policy')
    }
    
    score = sum(1 for v in checks.values() if v)
    
    cprint("📋 Security Headers:", Colors.YELLOW, True)
    for key, value in checks.items():
        if value:
            cprint(f"  ✅ {key}: {value[:50]}...", Colors.GREEN)
        else:
            cprint(f"  ❌ {key}: Missing", Colors.RED)
    
    cprint(f"\n📊 Security Score: {score}/{len(checks)}", Colors.CYAN)
    
    if score < 3:
        cprint("⚠️  Security headers are weak!", Colors.RED, True)
    elif score < 5:
        cprint("⚠️  Security headers are average.", Colors.YELLOW, True)
    else:
        cprint("✅ Security headers are strong!", Colors.GREEN, True)
    return True

def tool_ssl_vulnerability():
    cprint("\n🔒 SSL/TLS Vulnerability Scanner", Colors.BLUE, True)
    domain = get_input("🌐 Enter domain: ", "google.com")
    
    try:
        versions = {
            'SSLv2': ssl.PROTOCOL_SSLv2 if hasattr(ssl, 'PROTOCOL_SSLv2') else None,
            'SSLv3': ssl.PROTOCOL_SSLv3 if hasattr(ssl, 'PROTOCOL_SSLv3') else None,
            'TLSv1.0': ssl.PROTOCOL_TLSv1 if hasattr(ssl, 'PROTOCOL_TLSv1') else None,
            'TLSv1.1': ssl.PROTOCOL_TLSv1_1 if hasattr(ssl, 'PROTOCOL_TLSv1_1') else None,
            'TLSv1.2': ssl.PROTOCOL_TLSv1_2 if hasattr(ssl, 'PROTOCOL_TLSv1_2') else None
        }
        
        cprint("🔍 Scanning SSL/TLS versions...", Colors.YELLOW, True)
        for name, protocol in versions.items():
            if protocol:
                try:
                    context = ssl.SSLContext(protocol)
                    with socket.create_connection((domain, 443), timeout=5) as sock:
                        with context.wrap_socket(sock, server_hostname=domain) as ssock:
                            cprint(f"  ✅ {name}: Supported", Colors.GREEN)
                except:
                    cprint(f"  ❌ {name}: Not supported", Colors.RED)
            else:
                cprint(f"  ❌ {name}: Not available", Colors.RED)
        
        # Check certificate
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                cprint(f"\n📋 Certificate Info:", Colors.YELLOW, True)
                cprint(f"  Subject: {cert.get('subject')}", Colors.CYAN)
                cprint(f"  Issuer: {cert.get('issuer')}", Colors.CYAN)
                cprint(f"  Expiry: {cert.get('notAfter')}", Colors.CYAN)
        return True
    except Exception as e:
        cprint(f"❌ Error: {str(e)}", Colors.RED)
        return True

def tool_password_strength():
    cprint("\n🔐 Password Strength Tester", Colors.BLUE, True)
    pwd = get_input("🔑 Enter password to test: ", "Password123!")
    
    score = 0
    if len(pwd) >= 8: score += 1
    if len(pwd) >= 12: score += 1
    if re.search(r'[a-z]', pwd): score += 1
    if re.search(r'[A-Z]', pwd): score += 1
    if re.search(r'[0-9]', pwd): score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd): score += 1
    
    strengths = ['Very Weak', 'Weak', 'Medium', 'Strong', 'Very Strong', 'Excellent']
    colors = [Colors.RED, Colors.RED, Colors.YELLOW, Colors.CYAN, Colors.GREEN, Colors.GREEN]
    
    cprint(f"📊 Score: {score}/6", Colors.CYAN)
    cprint(f"💪 Strength: {strengths[min(score, 5)]}", colors[min(score, 5)], True)
    
    cprint("\n📋 Details:", Colors.YELLOW, True)
    cprint(f"  📏 Length: {len(pwd)} characters", Colors.WHITE)
    cprint(f"  {'✅' if re.search(r'[a-z]', pwd) else '❌'} Lowercase letters", Colors.WHITE)
    cprint(f"  {'✅' if re.search(r'[A-Z]', pwd) else '❌'} Uppercase letters", Colors.WHITE)
    cprint(f"  {'✅' if re.search(r'[0-9]', pwd) else '❌'} Numbers", Colors.WHITE)
    cprint(f"  {'✅' if re.search(r'[!@#$%^&*(),.?\":{}|<>]', pwd) else '❌'} Special characters", Colors.WHITE)
    
    if score < 3:
        cprint("\n⚠️  Password is weak! Use longer password with mix of characters.", Colors.RED, True)
    elif score < 5:
        cprint("\n⚠️  Password is moderate. Add more characters and symbols.", Colors.YELLOW, True)
    else:
        cprint("\n✅ Strong password! Good job.", Colors.GREEN, True)
    return True

def tool_jwt_validator():
    cprint("\n🔐 JWT Token Validator", Colors.BLUE, True)
    token = get_input("🔑 Enter JWT token: ", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")
    
    try:
        import jwt
        decoded = jwt.decode(token, options={"verify_signature": False})
        cprint("✅ Valid JWT Token", Colors.GREEN, True)
        cprint("📋 Payload:", Colors.YELLOW, True)
        for key, value in decoded.items():
            cprint(f"  {key}: {value}", Colors.CYAN)
        return True
    except ImportError:
        if install_package("PyJWT"):
            cprint("✅ Installed! Please run the tool again.", Colors.GREEN)
        return False
    except Exception as e:
        cprint(f"❌ Invalid Token: {str(e)}", Colors.RED)
        return True

def tool_cors_tester():
    cprint("\n🌐 CORS Tester", Colors.BLUE, True)
    url = get_input("🌐 Enter URL: ", "https://example.com")
    
    try:
        response = safe_request(url, 'OPTIONS')
        if response:
            cors_headers = {
                'Access-Control-Allow-Origin': response.headers.get('Access-Control-Allow-Origin'),
                'Access-Control-Allow-Methods': response.headers.get('Access-Control-Allow-Methods'),
                'Access-Control-Allow-Headers': response.headers.get('Access-Control-Allow-Headers'),
                'Access-Control-Allow-Credentials': response.headers.get('Access-Control-Allow-Credentials')
            }
            
            cprint("📋 CORS Headers:", Colors.YELLOW, True)
            for key, value in cors_headers.items():
                if value:
                    cprint(f"  ✅ {key}: {value}", Colors.GREEN)
                else:
                    cprint(f"  ❌ {key}: Not Set", Colors.RED)
            
            if cors_headers['Access-Control-Allow-Origin'] == '*':
                cprint("\n⚠️  CORS is allowing all origins!", Colors.RED, True)
            elif cors_headers['Access-Control-Allow-Origin']:
                cprint("\n✅ CORS is configured properly", Colors.GREEN, True)
        else:
            cprint("❌ Failed to fetch CORS headers", Colors.RED)
        return True
    except Exception as e:
        cprint(f"❌ Error: {str(e)}", Colors.RED)
        return True

def tool_cookie_scanner():
    cprint("\n🍪 Cookie Scanner", Colors.BLUE, True)
    url = get_input("🌐 Enter URL: ", "https://google.com")
    
    response = safe_request(url)
    if response and response.cookies:
        cprint(f"Found {len(response.cookies)} cookies:", Colors.YELLOW, True)
        for cookie in response.cookies:
            cprint(f"\n  📋 {cookie.name}:", Colors.CYAN, True)
            cprint(f"    Value: {cookie.value[:30]}{'...' if len(cookie.value) > 30 else ''}", Colors.WHITE)
            cprint(f"    Secure: {'✅' if cookie.secure else '❌'}", Colors.WHITE)
            cprint(f"    HttpOnly: {'✅' if cookie.has_nonstandard_attr('HttpOnly') else '❌'}", Colors.WHITE)
            cprint(f"    Domain: {cookie.domain}", Colors.WHITE)
    else:
        cprint("❌ No cookies found", Colors.RED)
    return True

def tool_csp_checker():
    cprint("\n🔒 CSP Header Checker", Colors.BLUE, True)
    url = get_input("🌐 Enter URL: ", "https://google.com")
    
    response = safe_request(url)
    if response:
        csp = response.headers.get('Content-Security-Policy', '')
        if csp:
            cprint("✅ Content-Security-Policy header is present!", Colors.GREEN, True)
            cprint("📋 CSP Policy:", Colors.YELLOW, True)
            policies = csp.split(';')
            for policy in policies:
                if policy.strip():
                    cprint(f"  {policy.strip()}", Colors.CYAN)
        else:
            cprint("❌ No Content-Security-Policy header found!", Colors.RED, True)
    else:
        cprint("❌ Failed to fetch headers", Colors.RED)
    return True

# ==================== TOOL FUNCTIONS (34-45: PERFORMANCE) ====================

def tool_load_time():
    cprint("\n⏱️  Website Load Time", Colors.BLUE, True)
    url = get_input("🌐 Enter URL: ", "https://google.com")
    
    start = time.time()
    response = safe_request(url)
    load_time = time.time() - start
    
    if response:
        cprint(f"⏱️  Load Time: {load_time:.3f} seconds", Colors.GREEN)
        cprint(f"📦 Page Size: {len(response.content) / 1024:.2f} KB", Colors.CYAN)
        cprint(f"📊 Status: {response.status_code}", Colors.CYAN)
        
        if load_time < 1:
            cprint("✅ Excellent speed! (< 1s)", Colors.GREEN, True)
        elif load_time < 2:
            cprint("✅ Good speed! (1-2s)", Colors.CYAN, True)
        elif load_time < 4:
            cprint("⚠️  Average speed (2-4s)", Colors.YELLOW, True)
        else:
            cprint("❌ Slow speed! (> 4s)", Colors.RED, True)
    else:
        cprint("❌ Failed to load website", Colors.RED)
    return True

def tool_page_speed():
    cprint("\n🚀 Page Speed Test", Colors.BLUE, True)
    url = get_input("🌐 Enter URL: ", "https://google.com")
    
    times = []
    for i in range(3):
        start = time.time()
        response = safe_request(url)
        if response:
            times.append(time.time() - start)
        time.sleep(1)
    
    if times:
        avg = sum(times) / len(times)
        cprint(f"📊 Average Load Time: {avg:.3f} seconds", Colors.CYAN)
        cprint(f"⏱️  Best: {min(times):.3f}s, Worst: {max(times):.3f}s", Colors.CYAN)
        
        if avg < 1:
            cprint("✅ Excellent speed!", Colors.GREEN, True)
        elif avg < 2:
            cprint("✅ Good speed!", Colors.CYAN, True)
        elif avg < 4:
            cprint("⚠️  Average speed", Colors.YELLOW, True)
        else:
            cprint("❌ Slow speed!", Colors.RED, True)
    else:
        cprint("❌ Failed to load website", Colors.RED)
    return True

def tool_load_tester():
    cprint("\n🚀 Load Tester", Colors.BLUE, True)
    url = get_input("🌐 Enter URL: ", "https://google.com")
    
    try:
        count = int(get_input("🔢 Number of requests (default 10): ", "10"))
    except:
        count = 10
    
    cprint(f"🔍 Sending {count} requests to {url}...", Colors.YELLOW, True)
    results = []
    success = 0
    
    for i in range(count):
        try:
            start = time.time()
            response = requests.get(url, timeout=10, verify=False)
            elapsed = time.time() - start
            results.append(elapsed)
            success += 1
            status_color = Colors.GREEN if response.status_code == 200 else Colors.YELLOW
            cprint(f"  Request {i+1}: {response.status_code} - {elapsed:.3f}s", status_color)
        except Exception as e:
            cprint(f"  Request {i+1}: Failed - {str(e)[:30]}", Colors.RED)
    
    if results:
        cprint(f"\n📊 Results:", Colors.YELLOW, True)
        cprint(f"  ✅ Successful: {success}/{count}", Colors.GREEN)
        cprint(f"  ❌ Failed: {count - success}/{count}", Colors.RED)
        cprint(f"  ⏱️  Average: {sum(results)/len(results):.3f}s", Colors.CYAN)
        cprint(f"  ⏱️  Min: {min(results):.3f}s", Colors.CYAN)
        cprint(f"  ⏱️  Max: {max(results):.3f}s", Colors.CYAN)
    return True

def tool_api_response_time():
    cprint("\n⏱️  API Response Time Analyzer", Colors.BLUE, True)
    url = get_input("🌐 Enter API URL: ", "https://jsonplaceholder.typicode.com/posts/1")
    
    results = []
    cprint("🔍 Testing 5 requests...", Colors.YELLOW, True)
    
    for i in range(5):
        try:
            start = time.time()
            response = requests.get(url, timeout=10, verify=False)
            elapsed = time.time() - start
            results.append(elapsed)
            status_color = Colors.GREEN if response.status_code == 200 else Colors.YELLOW
            cprint(f"  Request {i+1}: {elapsed:.3f}s - Status: {response.status_code}", status_color)
        except Exception as e:
            cprint(f"  Request {i+1}: Failed - {str(e)[:30]}", Colors.RED)
    
    if results:
        avg = sum(results) / len(results)
        cprint(f"\n📊 Results:", Colors.YELLOW, True)
        cprint(f"  Min: {min(results):.3f}s", Colors.CYAN)
        cprint(f"  Max: {max(results):.3f}s", Colors.CYAN)
        cprint(f"  Avg: {avg:.3f}s", Colors.CYAN)
        
        if avg < 0.5:
            cprint("✅ Excellent response time!", Colors.GREEN, True)
        elif avg < 1:
            cprint("✅ Good response time!", Colors.CYAN, True)
        elif avg < 2:
            cprint("⚠️  Average response time", Colors.YELLOW, True)
        else:
            cprint("❌ Slow response time!", Colors.RED, True)
    return True

# ==================== TOOL FUNCTIONS (41-48: API) ====================

def tool_graphql_tester():
    cprint("\n🔍 GraphQL API Tester", Colors.BLUE, True)
    url = get_input("🌐 Enter GraphQL endpoint: ", "https://graphqlzero.almansi.me/api")
    query = get_input("📝 Enter GraphQL query: ", "query { users { id name email } }")
    
    try:
        response = requests.post(url, json={'query': query}, timeout=10, verify=False)
        if response.status_code == 200:
            cprint("✅ GraphQL request successful", Colors.GREEN, True)
            cprint("📋 Response:", Colors.YELLOW, True)
            cprint(json.dumps(response.json(), indent=2), Colors.CYAN)
        else:
            cprint(f"❌ Error: {response.status_code}", Colors.RED)
            cprint(response.text[:500], Colors.RED)
        return True
    except Exception as e:
        cprint(f"❌ Error: {str(e)}", Colors.RED)
        return True

# ==================== TOOL FUNCTIONS (49-65: TEXT & DATA) ====================

def tool_json_formatter():
    cprint("\n📝 JSON Formatter & Validator", Colors.BLUE, True)
    cprint("📄 Enter JSON data (type 'END' on new line when done):", Colors.YELLOW)
    
    lines = []
    while True:
        line = input()
        if line.strip() == 'END':
            break
        lines.append(line)
    
    json_str = '\n'.join(lines)
    try:
        parsed = json.loads(json_str)
        formatted = json.dumps(parsed, indent=2)
        cprint("\n✅ Valid JSON", Colors.GREEN, True)
        cprint("📋 Formatted JSON:", Colors.YELLOW, True)
        cprint(formatted, Colors.CYAN)
        return True
    except Exception as e:
        cprint(f"\n❌ Invalid JSON: {str(e)}", Colors.RED)
        return True

def tool_base64_encoder():
    cprint("\n📝 Base64 Encoder/Decoder", Colors.BLUE, True)
    text = get_input("📄 Enter text to encode: ", "Hello World!")
    
    encoded = base64.b64encode(text.encode()).decode()
    cprint(f"🔐 Encoded: {encoded}", Colors.GREEN)
    decoded = base64.b64decode(encoded).decode()
    cprint(f"🔓 Decoded: {decoded}", Colors.CYAN)
    return True

def tool_url_encoder():
    cprint("\n📝 URL Encoder/Decoder", Colors.BLUE, True)
    url = get_input("📄 Enter URL: ", "https://example.com?q=hello world")
    
    encoded = urllib.parse.quote(url)
    cprint(f"🔐 Encoded: {encoded}", Colors.GREEN)
    decoded = urllib.parse.unquote(encoded)
    cprint(f"🔓 Decoded: {decoded}", Colors.CYAN)
    return True

def tool_hash_generator():
    cprint("\n🔐 Hash Generator", Colors.BLUE, True)
    text = get_input("📄 Enter text: ", "Hello World!")
    
    cprint(f"MD5: {hashlib.md5(text.encode()).hexdigest()}", Colors.GREEN)
    cprint(f"SHA1: {hashlib.sha1(text.encode()).hexdigest()}", Colors.GREEN)
    cprint(f"SHA256: {hashlib.sha256(text.encode()).hexdigest()}", Colors.GREEN)
    cprint(f"SHA512: {hashlib.sha512(text.encode()).hexdigest()}", Colors.GREEN)
    return True

def tool_regex_tester():
    cprint("\n🔍 Regex Tester", Colors.BLUE, True)
    text = get_input("📄 Enter text to test: ", "The quick brown fox jumps over the lazy dog")
    pattern = get_input("📋 Enter regex pattern: ", r"\b\w+")
    
    try:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            cprint(f"✅ Found {len(matches)} matches:", Colors.GREEN, True)
            for i, match in enumerate(matches, 1):
                cprint(f"  {i}. {match}", Colors.CYAN)
        else:
            cprint("❌ No matches found", Colors.RED)
    except Exception as e:
        cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def tool_text_counter():
    cprint("\n📊 Character/Word/Lines Counter", Colors.BLUE, True)
    cprint("📄 Enter text (type 'END' on new line when done):", Colors.YELLOW)
    
    lines = []
    while True:
        line = input()
        if line.strip() == 'END':
            break
        lines.append(line)
    
    text = '\n'.join(lines)
    cprint(f"\n📊 Results:", Colors.YELLOW, True)
    cprint(f"  Characters: {len(text)}", Colors.CYAN)
    cprint(f"  Words: {len(re.findall(r'\\b\\w+\\b', text))}", Colors.CYAN)
    cprint(f"  Lines: {len(lines)}", Colors.CYAN)
    cprint(f"  Sentences: {len(re.findall(r'[.!?]+', text))}", Colors.CYAN)
    return True

# ==================== TOOL FUNCTIONS (61-75: GENERATORS) ====================

def tool_password_generator():
    cprint("\n🔑 Random Password Generator", Colors.BLUE, True)
    try:
        length = int(get_input("🔢 Password length (default 12): ", "12"))
    except:
        length = 12
    
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(random.choice(chars) for _ in range(length))
    
    cprint(f"🔐 Generated Password: {pwd}", Colors.GREEN, True)
    
    # Check strength
    score = 0
    if len(pwd) >= 8: score += 1
    if len(pwd) >= 12: score += 1
    if re.search(r'[a-z]', pwd): score += 1
    if re.search(r'[A-Z]', pwd): score += 1
    if re.search(r'[0-9]', pwd): score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd): score += 1
    
    strengths = ['Very Weak', 'Weak', 'Medium', 'Strong', 'Very Strong', 'Excellent']
    colors = [Colors.RED, Colors.RED, Colors.YELLOW, Colors.CYAN, Colors.GREEN, Colors.GREEN]
    cprint(f"💪 Strength: {strengths[min(score, 5)]}", colors[min(score, 5)], True)
    return True

def tool_uuid_generator():
    cprint("\n🔑 UUID Generator", Colors.BLUE, True)
    try:
        count = int(get_input("🔢 Number of UUIDs (default 5): ", "5"))
    except:
        count = 5
    
    import uuid
    cprint(f"📋 Generated {count} UUIDs:", Colors.YELLOW, True)
    for i in range(count):
        cprint(f"  {i+1}. {uuid.uuid4()}", Colors.GREEN)
    return True

def tool_lorem_ipsum():
    cprint("\n📝 Lorem Ipsum Generator", Colors.BLUE, True)
    try:
        paragraphs = int(get_input("🔢 Number of paragraphs (default 3): ", "3"))
    except:
        paragraphs = 3
    
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    
    result = "\n\n".join([lorem for _ in range(paragraphs)])
    cprint("📋 Generated Lorem Ipsum:", Colors.YELLOW, True)
    cprint(result, Colors.CYAN)
    return True

def tool_random_number():
    cprint("\n🎲 Random Number Generator", Colors.BLUE, True)
    try:
        min_val = int(get_input("🔢 Minimum value (default 1): ", "1"))
        max_val = int(get_input("🔢 Maximum value (default 100): ", "100"))
        count = int(get_input("🔢 How many numbers (default 5): ", "5"))
    except:
        min_val, max_val, count = 1, 100, 5
    
    nums = [random.randint(min_val, max_val) for _ in range(count)]
    cprint(f"📋 Generated {count} random numbers:", Colors.YELLOW, True)
    cprint(f"  {', '.join(map(str, nums))}", Colors.CYAN)
    cprint(f"  Min: {min(nums)}, Max: {max(nums)}, Sum: {sum(nums)}", Colors.CYAN)
    return True

# ==================== TOOL FUNCTIONS (71-85: SYSTEM) ====================

def tool_system_info():
    cprint("\n🖥️  System Information", Colors.BLUE, True)
    
    cprint(f"OS: {platform.system()} {platform.release()}", Colors.CYAN)
    cprint(f"Hostname: {platform.node()}", Colors.CYAN)
    cprint(f"Python: {platform.python_version()}", Colors.CYAN)
    cprint(f"Processor: {platform.processor()}", Colors.CYAN)
    cprint(f"Machine: {platform.machine()}", Colors.CYAN)
    cprint(f"Architecture: {platform.architecture()}", Colors.CYAN)
    
    try:
        import multiprocessing
        cprint(f"CPU Cores: {multiprocessing.cpu_count()}", Colors.CYAN)
    except:
        pass
    
    return True

def tool_disk_usage():
    cprint("\n💿 Disk Usage", Colors.BLUE, True)
    
    try:
        path = '/' if os.name != 'nt' else 'C:'
        total, used, free = shutil.disk_usage(path)
        
        cprint(f"📊 Disk Usage for {path}:", Colors.YELLOW, True)
        cprint(f"Total: {total / (1024**3):.2f} GB", Colors.CYAN)
        cprint(f"Used: {used / (1024**3):.2f} GB", Colors.YELLOW)
        cprint(f"Free: {free / (1024**3):.2f} GB", Colors.GREEN)
        cprint(f"Used %: {(used / total) * 100:.2f}%", Colors.CYAN)
        
        percent = (used / total) * 100
        if percent > 90:
            cprint("⚠️  Disk almost full!", Colors.RED, True)
        elif percent > 70:
            cprint("⚠️  Disk usage is high!", Colors.YELLOW, True)
        else:
            cprint("✅ Disk usage is healthy!", Colors.GREEN, True)
        return True
    except Exception as e:
        cprint(f"❌ Error: {str(e)}", Colors.RED)
        return True

# ==================== TOOL FUNCTIONS (81-100: UTILITY) ====================

def tool_email_extractor():
    cprint("\n📧 Email Extractor", Colors.BLUE, True)
    cprint("📄 Enter text with emails (type 'END' on new line when done):", Colors.YELLOW)
    
    lines = []
    while True:
        line = input()
        if line.strip() == 'END':
            break
        lines.append(line)
    
    text = '\n'.join(lines)
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    
    if emails:
        cprint(f"✅ Found {len(emails)} emails:", Colors.GREEN, True)
        for i, email in enumerate(set(emails), 1):
            cprint(f"  {i}. {email}", Colors.CYAN)
    else:
        cprint("❌ No emails found", Colors.RED)
    return True

def tool_phone_extractor():
    cprint("\n📱 Phone Number Extractor", Colors.BLUE, True)
    cprint("📄 Enter text with phone numbers (type 'END' on new line when done):", Colors.YELLOW)
    
    lines = []
    while True:
        line = input()
        if line.strip() == 'END':
            break
        lines.append(line)
    
    text = '\n'.join(lines)
    phones = re.findall(r'\+?[0-9]{10,15}', text)
    
    if phones:
        cprint(f"✅ Found {len(phones)} phone numbers:", Colors.GREEN, True)
        for i, phone in enumerate(set(phones), 1):
            cprint(f"  {i}. {phone}", Colors.CYAN)
    else:
        cprint("❌ No phone numbers found", Colors.RED)
    return True

def tool_link_extractor():
    cprint("\n🔗 Link Extractor", Colors.BLUE, True)
    url = get_input("🌐 Enter URL to extract links from: ", "https://google.com")
    
    response = safe_request(url)
    if response:
        links = re.findall(r'href=["\'](https?://[^"\']+)["\']', response.text)
        if links:
            cprint(f"✅ Found {len(links)} links:", Colors.GREEN, True)
            for i, link in enumerate(set(links)[:20], 1):
                cprint(f"  {i}. {link}", Colors.CYAN)
            if len(set(links)) > 20:
                cprint(f"  ... and {len(set(links)) - 20} more", Colors.YELLOW)
        else:
            cprint("❌ No links found", Colors.RED)
    else:
        cprint("❌ Failed to fetch URL", Colors.RED)
    return True

def tool_text_analyzer():
    cprint("\n📊 Text Analyzer", Colors.BLUE, True)
    cprint("📄 Enter text to analyze (type 'END' on new line when done):", Colors.YELLOW)
    
    lines = []
    while True:
        line = input()
        if line.strip() == 'END':
            break
        lines.append(line)
    
    text = '\n'.join(lines)
    
    cprint("\n📊 Analysis Results:", Colors.YELLOW, True)
    cprint(f"  Characters: {len(text)}", Colors.CYAN)
    cprint(f"  Words: {len(re.findall(r'\\b\\w+\\b', text))}", Colors.CYAN)
    cprint(f"  Lines: {len(lines)}", Colors.CYAN)
    cprint(f"  Sentences: {len(re.findall(r'[.!?]+', text))}", Colors.CYAN)
    cprint(f"  Unique Words: {len(set(re.findall(r'\\b\\w+\\b', text.lower())))}", Colors.CYAN)
    
    words = re.findall(r'\\b\\w+\\b', text.lower())
    if words:
        from collections import Counter
        common = Counter(words).most_common(5)
        cprint("\n  Top 5 Most Common Words:", Colors.YELLOW)
        for word, count in common:
            cprint(f"    {word}: {count}", Colors.CYAN)
    return True

# ==================== MAIN ====================

def main():
    while True:
        print_header()
        print_menu()
        
        choice = get_input(f"\n{Colors.BOLD}🎯 Select tool (0-100): {Colors.END}")
        
        if choice == '0':
            cprint("\n👋 Thanks for using RIR Web Testing Suite!", Colors.GREEN, True)
            cprint("🔒 Stay Secure, Stay Safe!", Colors.CYAN, True)
            cprint("🛡️  RIR Cyber Tools", Colors.MAGENTA, True)
            break
        
        tools_map = {
            '1': tool_website_status,
            '2': tool_ping,
            '3': tool_dns_lookup,
            '4': tool_ip_geolocation,
            '5': tool_port_scanner,
            '6': tool_ssl_check,
            '7': tool_whois_lookup,
            '8': tool_reverse_dns,
            '9': tool_http_headers,
            '10': tool_server_location,
            '11': tool_subdomain_finder,
            '12': tool_traceroute,
            '13': tool_ip_validator,
            '14': tool_domain_availability,
            '15': tool_mx_lookup,
            '16': tool_ns_lookup,
            '17': tool_txt_lookup,
            '19': tool_xss_scanner,
            '20': tool_sql_injection,
            '21': tool_csrf_tester,
            '22': tool_security_headers,
            '23': tool_ssl_vulnerability,
            '24': tool_password_strength,
            '25': tool_jwt_validator,
            '26': tool_cors_tester,
            '27': tool_cookie_scanner,
            '28': tool_csp_checker,
            '34': tool_load_time,
            '35': tool_page_speed,
            '36': tool_load_tester,
            '40': tool_api_response_time,
            '42': tool_graphql_tester,
            '49': tool_json_formatter,
            '51': tool_base64_encoder,
            '52': tool_url_encoder,
            '56': tool_regex_tester,
            '58': tool_text_counter,
            '61': tool_password_generator,
            '62': tool_uuid_generator,
            '64': tool_hash_generator,
            '68': tool_lorem_ipsum,
            '69': tool_random_number,
            '71': tool_system_info,
            '72': tool_disk_usage,
            '81': tool_email_extractor,
            '82': tool_phone_extractor,
            '83': tool_link_extractor,
            '84': tool_text_analyzer,
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