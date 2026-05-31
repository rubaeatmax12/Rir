import requests
import os
import json
import time
import sys
import random
import hashlib
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import threading

# Clear screen function
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Animated printing
def animate_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Color codes
class Colors:
    RED = '\033[1;91m'
    GREEN = '\033[1;92m'
    YELLOW = '\033[1;93m'
    BLUE = '\033[1;94m'
    PURPLE = '\033[1;95m'
    CYAN = '\033[1;96m'
    WHITE = '\033[1;97m'
    ORANGE = '\033[1;38;5;214m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Generate random device fingerprint
def generate_device_fingerprint():
    characters = '0123456789ABCDEF'
    return ''.join(random.choice(characters) for _ in range(64))

# Generate random user agent
def generate_user_agent():
    android_versions = ['11', '12', '13', '14']
    build_versions = ['2023', '2024', '2025']
    return f'Android/{random.choice(android_versions)}-{random.choice(build_versions)}'

# Banner with animation
def show_banner():
    banner = f"""
{Colors.CYAN}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                              ║
║  {Colors.BOLD}{Colors.PURPLE}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{Colors.CYAN}  ║
║  {Colors.PURPLE}▓▓                                                                                          ▓▓{Colors.CYAN}  ║
║  {Colors.BLUE}▓▓  {Colors.ORANGE}╔══════════════════════════════════════════════════════════════════════════════════════╗  {Colors.BLUE}▓▓{Colors.CYAN}  ║
║  {Colors.BLUE}▓▓  {Colors.ORANGE}║                                                                                      ║  {Colors.BLUE}▓▓{Colors.CYAN}  ║
║  {Colors.BLUE}▓▓  {Colors.ORANGE}║  {Colors.BOLD}{Colors.PURPLE}██████╗  █████╗ ███╗   ██╗ ██████╗ ██╗      █████╗ ███████╗██╗  ██╗  {Colors.ORANGE}║  {Colors.BLUE}▓▓{Colors.CYAN}  ║
║  {Colors.BLUE}▓▓  {Colors.ORANGE}║  {Colors.PURPLE}██╔══██╗██╔══██╗████╗  ██║██╔════╝ ██║     ██╔══██╗██╔════╝██║  ██║  {Colors.ORANGE}║  {Colors.BLUE}▓▓{Colors.CYAN}  ║
║  {Colors.BLUE}▓▓  {Colors.ORANGE}║  {Colors.BLUE}██████╔╝███████║██╔██╗ ██║██║  ███╗██║     ███████║███████╗███████║  {Colors.ORANGE}║  {Colors.BLUE}▓▓{Colors.CYAN}  ║
║  {Colors.BLUE}▓▓  {Colors.ORANGE}║  {Colors.BLUE}██╔══██╗██╔══██║██║╚██╗██║██║   ██║██║     ██╔══██║╚════██║██╔══██║  {Colors.ORANGE}║  {Colors.BLUE}▓▓{Colors.CYAN}  ║
║  {Colors.BLUE}▓▓  {Colors.ORANGE}║  {Colors.GREEN}██████╔╝██║  ██║██║ ╚████║╚██████╔╝███████╗██║  ██║███████║██║  ██║  {Colors.ORANGE}║  {Colors.BLUE}▓▓{Colors.CYAN}  ║
║  {Colors.BLUE}▓▓  {Colors.ORANGE}║  {Colors.GREEN}╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  {Colors.ORANGE}║  {Colors.BLUE}▓▓{Colors.CYAN}  ║
║  {Colors.BLUE}▓▓  {Colors.ORANGE}║                                                                                      ║  {Colors.BLUE}▓▓{Colors.CYAN}  ║
║  {Colors.BLUE}▓▓  {Colors.ORANGE}║    {Colors.YELLOW}{Colors.BOLD}            ░▒▓█ BANGLADESH CYBER EAGLE 2025 █▓▒░              {Colors.ORANGE}    ║  {Colors.BLUE}▓▓{Colors.CYAN}  ║
║  {Colors.BLUE}▓▓  {Colors.ORANGE}║    {Colors.CYAN}{Colors.BOLD}              ░▒▓█ NAGAD INFO CHECKER PRO █▓▒░                {Colors.ORANGE}    ║  {Colors.BLUE}▓▓{Colors.CYAN}  ║
║  {Colors.BLUE}▓▓  {Colors.ORANGE}╚══════════════════════════════════════════════════════════════════════════════════════╝  {Colors.BLUE}▓▓{Colors.CYAN}  ║
║  {Colors.PURPLE}▓▓                                                                                          ▓▓{Colors.CYAN}  ║
║  {Colors.PURPLE}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{Colors.CYAN}  ║
║                                                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}
"""
    animate_text(banner, 0.001)

# Developer info
def show_developer_info():
    info = f"""
{Colors.GREEN}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║{Colors.YELLOW}{Colors.BOLD}                                      🦅 BANGLADESH CYBER EAGLE 🦅                                       {Colors.GREEN}║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                                              ║
║  {Colors.CYAN}┌─[{Colors.GREEN}★{Colors.CYAN}]─[{Colors.WHITE} TEAM          {Colors.CYAN}: {Colors.YELLOW}BANGLADESH CYBER EAGLE 2025{Colors.CYAN}                          ]─┐{Colors.GREEN}  ║
║  {Colors.CYAN}├─[{Colors.GREEN}★{Colors.CYAN}]─[{Colors.WHITE} TOOL         {Colors.CYAN}: {Colors.YELLOW}NAGAD ADVANCED INFO CHECKER PRO{Colors.CYAN}                      ]─┤{Colors.GREEN}  ║
║  {Colors.CYAN}├─[{Colors.GREEN}★{Colors.CYAN}]─[{Colors.WHITE} VERSION      {Colors.CYAN}: {Colors.ORANGE}ULTIMATE PRO MAX 2025{Colors.CYAN}                             ]─┤{Colors.GREEN}  ║
║  {Colors.CYAN}├─[{Colors.GREEN}★{Colors.CYAN}]─[{Colors.WHITE} STATUS       {Colors.CYAN}: {Colors.GREEN}🟢 ACTIVE & UPDATED{Colors.CYAN}                                   ]─┤{Colors.GREEN}  ║
║  {Colors.CYAN}├─[{Colors.GREEN}★{Colors.CYAN}]─[{Colors.WHITE} CREATED      {Colors.CYAN}: {Colors.YELLOW}JANUARY 2025{Colors.CYAN}                                        ]─┤{Colors.GREEN}  ║
║  {Colors.CYAN}├─[{Colors.GREEN}★{Colors.CYAN}]─[{Colors.WHITE} DEVELOPER    {Colors.CYAN}: {Colors.CYAN}BANGLADESH CYBER EAGLE TEAM{Colors.CYAN}                          ]─┤{Colors.GREEN}  ║
║  {Colors.CYAN}├─[{Colors.GREEN}★{Colors.CYAN}]─[{Colors.WHITE} LICENSE      {Colors.CYAN}: {Colors.GREEN}FOR CYBER SECURITY RESEARCH ONLY{Colors.CYAN}                    ]─┤{Colors.GREEN}  ║
║  {Colors.CYAN}└─[{Colors.GREEN}★{Colors.CYAN}]─[{Colors.WHITE} FEATURES     {Colors.CYAN}: {Colors.GREEN}ADVANCED API | MULTI-THREADING | ENCRYPTED{Colors.CYAN}           ]─┘{Colors.GREEN}  ║
║                                                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(info)

# Loading animation with progress bar
def loading_animation(text="Processing", duration=3):
    animation = ["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"]
    start_time = time.time()
    i = 0
    
    print(f"\n{Colors.YELLOW}┌─────────────────────────────────────────────────────────────────────────────┐")
    print(f"│{Colors.CYAN}                        {text.upper()}                           {Colors.YELLOW}│")
    print(f"└─────────────────────────────────────────────────────────────────────────────┘{Colors.RESET}")
    
    while time.time() - start_time < duration:
        progress = int(((time.time() - start_time) / duration) * 50)
        bar = f"{Colors.GREEN}{'█' * progress}{Colors.WHITE}{'░' * (50 - progress)}{Colors.RESET}"
        sys.stdout.write(f"\r{Colors.YELLOW}[{animation[i % len(animation)]}] {Colors.CYAN}{text} [{bar}] {progress*2}%")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    print(f"\r{Colors.GREEN}[✓] {Colors.CYAN}{text} complete [{Colors.GREEN}{'█'*50}{Colors.CYAN}] 100%{Colors.RESET}")

# Advanced API request with retry mechanism
def make_advanced_request(msisdn):
    headers_list = [
        {
            'X-KM-User-AspId': '100012345612345',
            'X-KM-User-Agent': 'ANDROID/1152',
            'X-KM-DEVICE-FGP': generate_device_fingerprint(),
            'X-KM-Accept-language': 'bn',
            'X-KM-AppCode': '01',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'bn-BD,bn;q=0.9,en;q=0.8',
            'Origin': 'https://nagad.com',
            'Referer': 'https://nagad.com/',
            'Connection': 'keep-alive'
        },
        {
            'X-KM-User-AspId': '100098765432109',
            'X-KM-User-Agent': generate_user_agent(),
            'X-KM-DEVICE-FGP': generate_device_fingerprint(),
            'X-KM-Accept-language': 'en',
            'X-KM-AppCode': '02',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Origin': 'https://mynagad.com',
            'Referer': 'https://mynagad.com/'
        }
    ]
    
    endpoints = [
        'https://app.mynagad.com:20002/api/user/check-user-status-for-log-in',
        'https://api.nagad.com/api/user/check-user-status-for-log-in',
        'https://nagad.com.bd/api/user/check-user-status-for-log-in'
    ]
    
    params = {'msisdn': msisdn}
    
    for endpoint in endpoints:
        for headers in headers_list:
            try:
                loading_animation(f"Trying endpoint: {endpoint.split('//')[1].split('/')[0]}", 1)
                response = requests.get(
                    endpoint,
                    headers=headers,
                    params=params,
                    timeout=15,
                    verify=True
                )
                
                if response.status_code == 200:
                    return response
                elif response.status_code == 400:
                    # Try with different parameters
                    params2 = {'phone': msisdn, 'mobile': msisdn}
                    for param_key, param_value in params2.items():
                        response = requests.get(
                            endpoint,
                            headers=headers,
                            params={param_key: param_value},
                            timeout=15,
                            verify=True
                        )
                        if response.status_code == 200:
                            return response
            except requests.exceptions.RequestException:
                continue
    
    return None

# Check Nagad user info with advanced features
def check_nagad_user():
    clear_screen()
    show_banner()
    show_developer_info()
    
    print(f"\n{Colors.GREEN}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print(f"║{Colors.YELLOW}{Colors.BOLD}                                  🎯 USER INFORMATION CHECKER PRO 2025 🎯                                   {Colors.GREEN}║")
    print(f"╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    # Multiple input options
    print(f"{Colors.CYAN}┌─────────────────────────────────────────────────────────────────────────────┐")
    print(f"│{Colors.YELLOW}{Colors.BOLD}                         SELECT INPUT METHOD                               {Colors.CYAN}│")
    print(f"├─────────────────────────────────────────────────────────────────────────────┤")
    print(f"│{Colors.GREEN}[1]{Colors.WHITE} Single Phone Number Check                                    {Colors.CYAN}│")
    print(f"│{Colors.GREEN}[2]{Colors.WHITE} Multiple Numbers from File                                   {Colors.CYAN}│")
    print(f"│{Colors.GREEN}[3]{Colors.WHITE} Generate & Check Random Numbers                              {Colors.CYAN}│")
    print(f"│{Colors.GREEN}[4]{Colors.WHITE} Check Number Range                                           {Colors.CYAN}│")
    print(f"└─────────────────────────────────────────────────────────────────────────────┘{Colors.RESET}")
    
    try:
        method = input(f"\n{Colors.YELLOW}[{Colors.GREEN}+{Colors.YELLOW}] {Colors.CYAN}Select option (1-4): {Colors.WHITE}").strip()
        
        if method == '1':
            single_check()
        elif method == '2':
            file_check()
        elif method == '3':
            random_check()
        elif method == '4':
            range_check()
        else:
            print(f"{Colors.RED}[!] Invalid option. Please select 1-4{Colors.RESET}")
            time.sleep(2)
            check_nagad_user()
            
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Operation cancelled by user{Colors.RESET}")
        sys.exit(0)

def single_check():
    # Get phone number with validation
    while True:
        try:
            print(f"\n{Colors.CYAN}┌─────────────────────────────────────────────────────────────────────────────┐")
            print(f"│{Colors.YELLOW}{Colors.BOLD}                    📞 SINGLE NUMBER CHECK MODULE                        {Colors.CYAN}│")
            print(f"└─────────────────────────────────────────────────────────────────────────────┘{Colors.RESET}\n")
            
            msisdn = input(f"{Colors.YELLOW}[{Colors.GREEN}+{Colors.YELLOW}] {Colors.CYAN}Enter Phone Number ({Colors.GREEN}01XXXXXXXXX{Colors.CYAN}): {Colors.WHITE}").strip()
            
            if not msisdn:
                print(f"{Colors.RED}[!] Phone number cannot be empty{Colors.RESET}")
                continue
                
            if msisdn.isdigit() and len(msisdn) == 11 and msisdn.startswith('01'):
                break
            else:
                print(f"{Colors.RED}[!] Invalid format. Must be 11 digits starting with 01{Colors.RESET}")
                print(f"{Colors.YELLOW}[*] Example: 01712345678{Colors.RESET}")
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}[!] Operation cancelled{Colors.RESET}")
            return
    
    process_single_number(msisdn)

def file_check():
    print(f"\n{Colors.CYAN}┌─────────────────────────────────────────────────────────────────────────────┐")
    print(f"│{Colors.YELLOW}{Colors.BOLD}                    📁 FILE CHECK MODULE                               {Colors.CYAN}│")
    print(f"└─────────────────────────────────────────────────────────────────────────────┘{Colors.RESET}\n")
    
    filename = input(f"{Colors.YELLOW}[{Colors.GREEN}+{Colors.YELLOW}] {Colors.CYAN}Enter filename (with numbers, one per line): {Colors.WHITE}").strip()
    
    if not os.path.exists(filename):
        print(f"{Colors.RED}[!] File not found: {filename}{Colors.RESET}")
        time.sleep(2)
        check_nagad_user()
        return
    
    with open(filename, 'r') as f:
        numbers = [line.strip() for line in f if line.strip()]
    
    if not numbers:
        print(f"{Colors.RED}[!] No valid numbers found in file{Colors.RESET}")
        time.sleep(2)
        check_nagad_user()
        return
    
    print(f"{Colors.GREEN}[✓] Found {len(numbers)} numbers in file{Colors.RESET}")
    
    # Multi-threading for faster processing
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(process_single_number, numbers))
    
    # Save all results to a single file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"nagad_batch_results_{timestamp}.txt"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"BANGLADESH CYBER EAGLE - NAGAD BATCH RESULTS\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Numbers: {len(numbers)}\n")
        f.write("="*80 + "\n\n")
        for result in results:
            if result:
                f.write(f"{result}\n\n")
    
    print(f"\n{Colors.GREEN}[✓] All results saved to: {output_file}{Colors.RESET}")

def random_check():
    print(f"\n{Colors.CYAN}┌─────────────────────────────────────────────────────────────────────────────┐")
    print(f"│{Colors.YELLOW}{Colors.BOLD}                    🎲 RANDOM NUMBER CHECK MODULE                       {Colors.CYAN}│")
    print(f"└─────────────────────────────────────────────────────────────────────────────┘{Colors.RESET}\n")
    
    try:
        count = int(input(f"{Colors.YELLOW}[{Colors.GREEN}+{Colors.YELLOW}] {Colors.CYAN}How many random numbers to generate? (1-100): {Colors.WHITE}").strip())
        if count < 1 or count > 100:
            print(f"{Colors.RED}[!] Please enter between 1-100{Colors.RESET}")
            return
    except ValueError:
        print(f"{Colors.RED}[!] Invalid number{Colors.RESET}")
        return
    
    prefixes = ['013', '014', '015', '016', '017', '018', '019']
    random_numbers = []
    
    for _ in range(count):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choice('0123456789') for _ in range(8))
        random_numbers.append(prefix + suffix)
    
    print(f"\n{Colors.GREEN}[✓] Generated {count} random numbers{Colors.RESET}")
    
    # Check first 5 numbers
    for i, number in enumerate(random_numbers[:5]):
        print(f"\n{Colors.YELLOW}[{Colors.GREEN}{i+1}{Colors.YELLOW}] {Colors.CYAN}Checking: {number}{Colors.RESET}")
        process_single_number(number)
        time.sleep(1)  # Avoid rate limiting

def range_check():
    print(f"\n{Colors.CYAN}┌─────────────────────────────────────────────────────────────────────────────┐")
    print(f"│{Colors.YELLOW}{Colors.BOLD}                    🔢 RANGE CHECK MODULE                              {Colors.CYAN}│")
    print(f"└─────────────────────────────────────────────────────────────────────────────┘{Colors.RESET}\n")
    
    start_num = input(f"{Colors.YELLOW}[{Colors.GREEN}+{Colors.YELLOW}] {Colors.CYAN}Enter starting number (01710000000): {Colors.WHITE}").strip()
    end_num = input(f"{Colors.YELLOW}[{Colors.GREEN}+{Colors.YELLOW}] {Colors.CYAN}Enter ending number (01719999999): {Colors.WHITE}").strip()
    
    if len(start_num) != 11 or len(end_num) != 11:
        print(f"{Colors.RED}[!] Both numbers must be 11 digits{Colors.RESET}")
        return
    
    try:
        start = int(start_num[3:])
        end = int(end_num[3:])
        prefix = start_num[:3]
        
        if start > end:
            print(f"{Colors.RED}[!] Start must be less than end{Colors.RESET}")
            return
        
        count = end - start + 1
        if count > 50:
            print(f"{Colors.RED}[!] Range too large. Maximum 50 numbers allowed{Colors.RESET}")
            return
        
        print(f"{Colors.GREEN}[✓] Will check {count} numbers from {start_num} to {end_num}{Colors.RESET}")
        
        for i in range(start, end + 1):
            number = f"{prefix}{i:08d}"
            print(f"\n{Colors.YELLOW}[{Colors.GREEN}{(i-start)+1}{Colors.YELLOW}/{count}] {Colors.CYAN}Checking: {number}{Colors.RESET}")
            process_single_number(number)
            time.sleep(0.5)  # Avoid rate limiting
            
    except ValueError:
        print(f"{Colors.RED}[!] Invalid number format{Colors.RESET}")

def process_single_number(msisdn):
    print(f"\n{Colors.GREEN}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{Colors.RESET}")
    
    # Show loading animation
    loading_animation(f"Checking Nagad Account: {msisdn}", 2)
    
    # Make API request with advanced method
    response = make_advanced_request(msisdn)
    
    if response and response.status_code == 200:
        try:
            data = response.json()
            
            # Display results in beautiful format
            print(f"\n{Colors.GREEN}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
            print(f"║{Colors.YELLOW}{Colors.BOLD}                                    📊 ACCOUNT INFORMATION FOUND 📊                                   {Colors.GREEN}║")
            print(f"╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════╣")
            
            # Account details with emojis
            account_info = []
            
            if 'name' in data:
                account_info.append((f"👤 Full Name", f"{Colors.YELLOW}{data['name']}{Colors.RESET}"))
            
            if 'userId' in data or 'useld' in data:
                user_id = data.get('userId') or data.get('useld')
                account_info.append((f"🆔 User ID", f"{Colors.GREEN}{user_id}{Colors.RESET}"))
            
            if 'status' in data:
                status = data['status']
                status_emoji = "🟢" if status.lower() == 'active' else "🔴" if status.lower() == 'inactive' else "🟡"
                status_color = Colors.GREEN if status.lower() == 'active' else Colors.RED if status.lower() == 'inactive' else Colors.YELLOW
                account_info.append((f"📊 Status", f"{status_emoji} {status_color}{status}{Colors.RESET}"))
            
            if 'user_type' in data:
                user_type = data['user_type']
                type_emoji = "👑" if 'premium' in user_type.lower() else "👤" if 'regular' in user_type.lower() else "💼"
                account_info.append((f"🎭 User Type", f"{type_emoji} {Colors.CYAN}{user_type}{Colors.RESET}"))
            
            # Additional advanced information
            if 'hasActiveLoan' in data:
                loan_status = "✅ Yes" if data['hasActiveLoan'] else "❌ No"
                loan_color = Colors.RED if data['hasActiveLoan'] else Colors.GREEN
                account_info.append((f"💰 Active Loan", f"{loan_color}{loan_status}{Colors.RESET}"))
            
            if 'kycStatus' in data:
                kyc_status = data['kycStatus']
                kyc_emoji = "✅" if kyc_status.lower() == 'verified' else "⏳" if 'pending' in kyc_status.lower() else "❌"
                kyc_color = Colors.GREEN if kyc_status.lower() == 'verified' else Colors.YELLOW if 'pending' in kyc_status.lower() else Colors.RED
                account_info.append((f"📝 KYC Status", f"{kyc_emoji} {kyc_color}{kyc_status}{Colors.RESET}"))
            
            if 'accountCreationDate' in data:
                creation_date = data['accountCreationDate']
                account_info.append((f"📅 Created On", f"{Colors.WHITE}{creation_date}{Colors.RESET}"))
            
            if 'lastLogin' in data:
                last_login = data['lastLogin']
                account_info.append((f"⏰ Last Login", f"{Colors.WHITE}{last_login}{Colors.RESET}"))
            
            # Display all information
            for label, value in account_info:
                print(f"║  {Colors.CYAN}├─[{Colors.GREEN}★{Colors.CYAN}]─[{Colors.WHITE} {label:<15}{Colors.CYAN}: {value:<65}{Colors.CYAN}]─┤{Colors.GREEN}  ║")
            
            # Timestamp and phone number
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"║  {Colors.CYAN}├─[{Colors.GREEN}★{Colors.CYAN}]─[{Colors.WHITE} 🕐 Checked At  {Colors.CYAN}: {Colors.WHITE}{current_time:<65}{Colors.CYAN}]─┤{Colors.GREEN}  ║")
            print(f"║  {Colors.CYAN}└─[{Colors.GREEN}★{Colors.CYAN}]─[{Colors.WHITE} 📱 Phone Number{Colors.CYAN}: {Colors.YELLOW}{msisdn:<65}{Colors.CYAN}]─┘{Colors.GREEN}  ║")
            print(f"╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}")
            
            # Save to file option
            save_option = input(f"\n{Colors.YELLOW}[{Colors.GREEN}+{Colors.YELLOW}] {Colors.CYAN}Save this result to file? (y/n): {Colors.WHITE}").lower()
            if save_option == 'y':
                filename = f"nagad_info_{msisdn}_{int(time.time())}.txt"
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"BANGLADESH CYBER EAGLE - NAGAD ACCOUNT INFORMATION 2025\n")
                    f.write(f"{'='*70}\n")
                    f.write(f"Checked At: {current_time}\n")
                    f.write(f"Phone Number: {msisdn}\n")
                    f.write(f"{'-'*70}\n")
                    for key, value in data.items():
                        if key not in ['responseCode', 'message']:
                            f.write(f"{key.replace('_', ' ').title()}: {value}\n")
                print(f"{Colors.GREEN}[✓] Results saved to: {filename}{Colors.RESET}")
            
            return f"{msisdn} | {data.get('name', 'N/A')} | {data.get('status', 'N/A')} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            
        except json.JSONDecodeError:
            print(f"{Colors.RED}[!] Invalid JSON response from server{Colors.RESET}")
    else:
        if response:
            print(f"\n{Colors.RED}[!] API Error: Status Code {response.status_code}{Colors.RESET}")
            print(f"{Colors.YELLOW}[*] Response: {response.text[:200]}{Colors.RESET}")
        else:
            print(f"\n{Colors.RED}[!] Failed to connect to Nagad servers{Colors.RESET}")
            print(f"{Colors.YELLOW}[*] Possible reasons:{Colors.RESET}")
            print(f"{Colors.YELLOW}    - Network connection issue{Colors.RESET}")
            print(f"{Colors.YELLOW}    - Server maintenance{Colors.RESET}")
            print(f"{Colors.YELLOW}    - API endpoint changed{Colors.RESET}")
    
    return f"{msisdn} | NOT FOUND | ERROR | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def show_menu():
    print(f"\n{Colors.GREEN}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print(f"║{Colors.YELLOW}{Colors.BOLD}                                    🚀 MAIN MENU 2025 🚀                                     {Colors.GREEN}║")
    print(f"╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════╣")
    print(f"║                                                                                                              ║")
    print(f"║  {Colors.YELLOW}[{Colors.GREEN}1{Colors.YELLOW}]{Colors.CYAN} Check Another Number                                                          {Colors.GREEN}║")
    print(f"║  {Colors.YELLOW}[{Colors.GREEN}2{Colors.YELLOW}]{Colors.CYAN} Go Back to Main Menu                                                         {Colors.GREEN}║")
    print(f"║  {Colors.YELLOW}[{Colors.GREEN}3{Colors.YELLOW}]{Colors.CYAN} View Saved Results                                                           {Colors.GREEN}║")
    print(f"║  {Colors.YELLOW}[{Colors.GREEN}4{Colors.YELLOW}]{Colors.CYAN} Exit Program                                                                 {Colors.GREEN}║")
    print(f"║                                                                                                              ║")
    print(f"╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    try:
        choice = input(f"\n{Colors.YELLOW}[{Colors.GREEN}+{Colors.YELLOW}] {Colors.CYAN}Select option: {Colors.WHITE}")
        if choice == '1':
            single_check()
        elif choice == '2':
            check_nagad_user()
        elif choice == '3':
            view_saved_results()
        elif choice == '4':
            print(f"\n{Colors.GREEN}[✓] Thank you for using BANGLADESH CYBER EAGLE 2025 Tools!{Colors.RESET}")
            print(f"{Colors.CYAN}[*] Stay safe, stay secure! 🦅{Colors.RESET}\n")
            sys.exit(0)
        else:
            print(f"{Colors.RED}[!] Invalid option{Colors.RESET}")
            show_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Operation cancelled{Colors.RESET}")
        sys.exit(0)

def view_saved_results():
    print(f"\n{Colors.CYAN}┌─────────────────────────────────────────────────────────────────────────────┐")
    print(f"│{Colors.YELLOW}{Colors.BOLD}                    💾 SAVED RESULTS VIEWER                              {Colors.CYAN}│")
    print(f"└─────────────────────────────────────────────────────────────────────────────┘{Colors.RESET}\n")
    
    files = [f for f in os.listdir('.') if f.startswith('nagad_info_') or f.startswith('nagad_batch_results_')]
    
    if not files:
        print(f"{Colors.RED}[!] No saved results found{Colors.RESET}")
        time.sleep(2)
        return
    
    print(f"{Colors.GREEN}[✓] Found {len(files)} saved result files:{Colors.RESET}\n")
    
    for i, file in enumerate(sorted(files, reverse=True)[:10]):  # Show last 10 files
        size = os.path.getsize(file)
        print(f"  {Colors.YELLOW}[{Colors.GREEN}{i+1}{Colors.YELLOW}]{Colors.CYAN} {file} ({size} bytes){Colors.RESET}")
    
    try:
        choice = input(f"\n{Colors.YELLOW}[{Colors.GREEN}+{Colors.YELLOW}] {Colors.CYAN}Enter file number to view (0 to go back): {Colors.WHITE}")
        if choice == '0':
            return
        
        idx = int(choice) - 1
        if 0 <= idx < len(files):
            with open(files[idx], 'r', encoding='utf-8') as f:
                print(f"\n{Colors.GREEN}╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
                print(f"║{Colors.YELLOW}{Colors.BOLD}                                    📄 FILE CONTENT VIEWER 📄                                   {Colors.GREEN}║")
                print(f"╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════╣")
                print(f"║                                                                                                              ║")
                for line in f:
                    line = line.strip()
                    if line:
                        print(f"║  {Colors.CYAN}{line:<100}{Colors.GREEN}  ║")
                print(f"║                                                                                                              ║")
                print(f"╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}")
    except (ValueError, IndexError):
        print(f"{Colors.RED}[!] Invalid selection{Colors.RESET}")

# Main function
def main():
    try:
        while True:
            check_nagad_user()
            show_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}[!] Program terminated by user{Colors.RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()