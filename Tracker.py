#!/usr/bin/python
# << CODE BY RIR TEAM
# << RECODE? ASK PERMISSION FIRST
# << RESPECT THE DEVELOPER

# IMPORT MODULE

import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr
import re
import socket

# ===== RIR TEAM COLOR =====
Bl = '\033[30m'
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'
Gold = '\033[1;33m'

# utilities

# decorator for attaching run_banner to a function
def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)

    return wrapper

# FUNCTIONS FOR MENU
@is_option
def IP_Track():
    ip = input(f"{Wh}\n[?] Enter IP target : {Gr}")
    print()
    print(f' {Wh}============= {Gr}IP INFORMATION {Wh}=============')
    req_api = requests.get(f"http://ipwho.is/{ip}")
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    print(f"{Wh}\n IP Target       :{Gr}", ip)
    print(f"{Wh} Type IP         :{Gr}", ip_data["type"])
    print(f"{Wh} Country         :{Gr}", ip_data["country"])
    print(f"{Wh} Country Code    :{Gr}", ip_data["country_code"])
    print(f"{Wh} City            :{Gr}", ip_data["city"])
    print(f"{Wh} Continent       :{Gr}", ip_data["continent"])
    print(f"{Wh} Continent Code  :{Gr}", ip_data["continent_code"])
    print(f"{Wh} Region          :{Gr}", ip_data["region"])
    print(f"{Wh} Region Code     :{Gr}", ip_data["region_code"])
    print(f"{Wh} Latitude        :{Gr}", ip_data["latitude"])
    print(f"{Wh} Longitude       :{Gr}", ip_data["longitude"])
    lat = int(ip_data['latitude'])
    lon = int(ip_data['longitude'])
    print(f"{Wh} Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
    print(f"{Wh} EU              :{Gr}", ip_data["is_eu"])
    print(f"{Wh} Postal          :{Gr}", ip_data["postal"])
    print(f"{Wh} Calling Code    :{Gr}", ip_data["calling_code"])
    print(f"{Wh} Capital         :{Gr}", ip_data["capital"])
    print(f"{Wh} Borders         :{Gr}", ip_data["borders"])
    print(f"{Wh} Country Flag    :{Gr}", ip_data["flag"]["emoji"])
    print(f"{Wh} ASN             :{Gr}", ip_data["connection"]["asn"])
    print(f"{Wh} ORG             :{Gr}", ip_data["connection"]["org"])
    print(f"{Wh} ISP             :{Gr}", ip_data["connection"]["isp"])
    print(f"{Wh} Domain          :{Gr}", ip_data["connection"]["domain"])
    print(f"{Wh} ID              :{Gr}", ip_data["timezone"]["id"])
    print(f"{Wh} ABBR            :{Gr}", ip_data["timezone"]["abbr"])
    print(f"{Wh} DST             :{Gr}", ip_data["timezone"]["is_dst"])
    print(f"{Wh} Offset          :{Gr}", ip_data["timezone"]["offset"])
    print(f"{Wh} UTC             :{Gr}", ip_data["timezone"]["utc"])
    print(f"{Wh} Current Time    :{Gr}", ip_data["timezone"]["current_time"])

@is_option
def phoneGW():
    User_phone = input(f"\n {Wh}[?] Enter phone number {Gr}Ex [+8801xxxxxxxxx] {Wh}: {Gr}")
    default_region = "BD"  # Changed to BD for Bangladesh

    parsed_number = phonenumbers.parse(User_phone, default_region)
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)

    print(f"\n {Wh}========== {Gr}PHONE INFORMATION {Wh}==========")
    print(f"\n {Wh}Location             :{Gr} {location}")
    print(f" {Wh}Region Code          :{Gr} {region_code}")
    print(f" {Wh}Timezone             :{Gr} {timezoneF}")
    print(f" {Wh}Operator             :{Gr} {jenis_provider}")
    print(f" {Wh}Valid number         :{Gr} {is_valid_number}")
    print(f" {Wh}Possible number      :{Gr} {is_possible_number}")
    print(f" {Wh}International format :{Gr} {formatted_number}")
    print(f" {Wh}Mobile format        :{Gr} {formatted_number_for_mobile}")
    print(f" {Wh}Original number      :{Gr} {parsed_number.national_number}")
    print(f" {Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f" {Wh}Country code         :{Gr} {parsed_number.country_code}")
    print(f" {Wh}Local number         :{Gr} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}Type                 :{Gr} This is a mobile number")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}Type                 :{Gr} This is a fixed-line number")
    else:
        print(f" {Wh}Type                 :{Gr} This is another type of number")

@is_option
def TrackLu():
    try:
        username = input(f"\n {Wh}[?] Enter Username : {Gr}")
        results = {}
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
        ]
        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
            else:
                results[site['name']] = (f"{Ye}Not Found!{Ye}")
    except Exception as e:
        print(f"{Re}Error : {e}")
        return

    print(f"\n {Wh}========== {Gr}USERNAME INFORMATION {Wh}==========")
    print()
    for site, url in results.items():
        print(f" {Wh}[ {Gr}+ {Wh}] {site} : {Gr}{url}")

@is_option
def showIP():
    respone = requests.get('https://api.ipify.org/')
    Show_IP = respone.text

    print(f"\n {Wh}========== {Gr}YOUR IP INFORMATION {Wh}==========")
    print(f"\n {Wh}[{Gr} + {Wh}] Your IP Address : {Gr}{Show_IP}")
    print(f"\n {Wh}==============================================")

@is_option
def WebToIP():
    print(f"\n {Wh}========== {Gr}WEBSITE TO IP + PORT SCAN {Wh}==========")
    url = input(f"\n {Wh}[?] Enter Website URL {Gr}Ex: example.com {Wh}: {Gr}")
    
    try:
        # Clean URL
        domain = re.sub(r'^https?://', '', url)
        domain = domain.split('/')[0]
        
        print(f"\n {Ye}[+] Resolving IP...{Wh}")
        time.sleep(1)
        
        # Get IP
        ip_addr = socket.gethostbyname(domain)
        
        print(f"\n {Gr}[+] IP Found: {Wh}{ip_addr}")
        print(f"\n {Wh}========== {Gr}IP INFORMATION {Wh}==========")
        print(f" {Wh}Website    : {Gr}{domain}")
        print(f" {Wh}IP Address : {Gr}{ip_addr}")
        
        # Scan Ports
        print(f"\n {Ye}[+] Scanning Open Ports...{Wh}")
        open_ports = []
        common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
        
        for port in common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip_addr, port))
                if result == 0:
                    open_ports.append(port)
                    print(f" {Gr}[+] Port {Wh}{port}{Gr} is OPEN")
                sock.close()
            except:
                pass
        
        if open_ports:
            print(f"\n {Wh}========== {Gr}OPEN PORTS {Wh}==========")
            for port in open_ports:
                print(f" {Wh}[ {Gr}+ {Wh}] Port {Gr}{port}{Wh} is OPEN")
        else:
            print(f"\n {Ye}[!] No open ports found{Wh}")
        
        # Get Location Info
        print(f"\n {Ye}[+] Getting Location Info...{Wh}")
        req_api = requests.get(f"http://ipwho.is/{ip_addr}")
        ip_data = json.loads(req_api.text)
        time.sleep(1)
        
        print(f"\n {Wh}========== {Gr}LOCATION INFO {Wh}==========")
        print(f" {Wh}Country      : {Gr}{ip_data.get('country', 'N/A')}")
        print(f" {Wh}City         : {Gr}{ip_data.get('city', 'N/A')}")
        print(f" {Wh}Region       : {Gr}{ip_data.get('region', 'N/A')}")
        print(f" {Wh}Latitude     : {Gr}{ip_data.get('latitude', 'N/A')}")
        print(f" {Wh}Longitude    : {Gr}{ip_data.get('longitude', 'N/A')}")
        print(f" {Wh}ISP          : {Gr}{ip_data.get('connection', {}).get('isp', 'N/A')}")
        
        if ip_data.get('latitude') and ip_data.get('longitude'):
            lat = ip_data['latitude']
            lon = ip_data['longitude']
            print(f" {Wh}Maps         : {Gr}https://www.google.com/maps/@{lat},{lon},8z")
            
    except socket.gaierror:
        print(f"\n {Re}[!] Invalid Domain or Website!{Wh}")
    except Exception as e:
        print(f"\n {Re}[!] Error: {e}{Wh}")
    
    time.sleep(2)

# OPTIONS
options = [
    {'num': 1, 'text': 'IP Tracker', 'func': IP_Track},
    {'num': 2, 'text': 'Show Your IP', 'func': showIP},
    {'num': 3, 'text': 'Phone Number Tracker', 'func': phoneGW},
    {'num': 4, 'text': 'Username Tracker', 'func': TrackLu},
    {'num': 5, 'text': 'Website to IP + Port Scan', 'func': WebToIP},
    {'num': 0, 'text': 'Exit', 'func': exit}
]

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('Option not found')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('No function detected')

def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Press Enter to continue')
        main()
    except ValueError as e:
        print(e)
        time.sleep(2)
        execute_option(opt)
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()

def option_text():
    text = ''
    for opt in options:
        text += f'{Wh}[ {opt["num"]} ] {Gr}{opt["text"]}\n'
    return text

def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False

def option():
    clear()
    stderr.writelines(f"""
    {Gold}╔═══════════════════════════════════════════════════════╗
    {Gold}║  {Gr}██╗  ██╗██╗██████╗     ████████╗██╗███╗   ███╗ {Gold}║
    {Gold}║  {Gr}██║  ██║██║██╔══██╗    ╚══██╔══╝██║████╗ ████║ {Gold}║
    {Gold}║  {Gr}███████║██║██████╔╝       ██║   ██║██╔████╔██║ {Gold}║
    {Gold}║  {Gr}██╔══██║██║██╔══██╗       ██║   ██║██║╚██╔╝██║ {Gold}║
    {Gold}║  {Gr}██║  ██║██║██║  ██║       ██║   ██║██║ ╚═╝ ██║ {Gold}║
    {Gold}║  {Gr}╚═╝  ╚═╝╚═╝╚═╝  ╚═╝       ╚═╝   ╚═╝╚═╝     ╚═╝ {Gold}║
    {Gold}║                                                       ║
    {Gold}║        {Wh}🚀 RIR TEAM PRESENTS 🚀                    {Gold}║
    {Gold}║        {Ye}GLOBAL TRACKER TOOLS v5.0                  {Gold}║
    {Gold}║                                                       ║
    {Gold}║        {Wh}CODED BY : RIR TEAM                        {Gold}║
    {Gold}║        {Wh}GITHUB   : github.com/rir-team            {Gold}║
    {Gold}║                                                       ║
    {Gold}╚═══════════════════════════════════════════════════════╝{Wh}
    """)

    stderr.writelines(f"""
    {Gold}═══════════════════════════════════════════════════════════
    {Wh}  [!] {Re}EDUCATIONAL PURPOSE ONLY [!]
    {Wh}  [!] {Re}USE AT YOUR OWN RISK [!]
    {Gold}═══════════════════════════════════════════════════════════
    """)

    stderr.writelines(f"\n\n{option_text()}")

def run_banner():
    clear()
    time.sleep(1)
    stderr.writelines(f"""
    {Gold}╔═══════════════════════════════════════════════════════╗
    {Gold}║                                                       ║
    {Gold}║  {Wh}██╗  ██╗██╗██████╗     ████████╗██╗███╗   ███╗  {Gold}║
    {Gold}║  {Wh}██║  ██║██║██╔══██╗    ╚══██╔══╝██║████╗ ████║  {Gold}║
    {Gold}║  {Wh}███████║██║██████╔╝       ██║   ██║██╔████╔██║  {Gold}║
    {Gold}║  {Wh}██╔══██║██║██╔══██╗       ██║   ██║██║╚██╔╝██║  {Gold}║
    {Gold}║  {Wh}██║  ██║██║██║  ██║       ██║   ██║██║ ╚═╝ ██║  {Gold}║
    {Gold}║  {Wh}╚═╝  ╚═╝╚═╝╚═╝  ╚═╝       ╚═╝   ╚═╝╚═╝     ╚═╝  {Gold}║
    {Gold}║                                                       ║
    {Gold}║           {Cy}🔍 TRACKING SYSTEM ACTIVE 🔍              {Gold}║
    {Gold}║                                                       ║
    {Gold}║           {Ye}⚡ RIR TEAM ⚡                           {Gold}║
    {Gold}╚═══════════════════════════════════════════════════════╝
    """)
    time.sleep(0.5)

def main():
    clear()
    option()
    time.sleep(1)
    try:
        opt = int(input(f"{Wh}\n[?] Select Option : {Gr}"))
        execute_option(opt)
    except ValueError:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Please input number')
        time.sleep(2)
        main()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()