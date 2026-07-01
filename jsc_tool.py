"""
JSC Decryptor Tool - 2025 (80 Systems Edition)
Original Logic by: Bartłomiej Duda
UI & Systems by: Community
"""

import gzip
import io
import os
import xxtea
import hashlib
import base64
import json
import random
import string
from zipfile import BadZipFile, ZipFile
from datetime import datetime
import urllib.parse
import urllib.request
import re
import time
import shutil
import filecmp

# ============================================
#  GLOBAL SYSTEM DESIGN - UI LAYER
#  Design Pattern: Modular CLI with 80 Services
#  Architecture: Dispatcher Pattern
#  Systems 1-50: File & Crypto Operations
#  Systems 51-80: Web Tools & Online Services
# ============================================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print("\033[1;36m" + "=" * 70)
    print("   🔥  JSC DECRYPTOR  •  80 SYSTEMS  🔥")
    print("=" * 70 + "\033[0m")
    print("\033[3;90m     Systems 1-50: File & Crypto • Systems 51-80: Web Tools\033[0m\n")

def print_menu():
    print("\033[1;33m╔══════════════════════════════════════════════════════════════════════╗\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m 1\033[0m. JSC Decrypt          \033[1;32m 2\033[0m. File Lock             \033[1;32m 3\033[0m. File Unlock      \033[1;32m 4\033[0m. Text Encrypt  \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m 5\033[0m. Text Decrypt          \033[1;32m 6\033[0m. Hash Generate         \033[1;32m 7\033[0m. Base64 Encode   \033[1;32m 8\033[0m. Base64 Decode \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m 9\033[0m. JSON Format          \033[1;32m10\033[0m. File Reader          \033[1;32m11\033[0m. File Writer    \033[1;32m12\033[0m. File Copy     \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m13\033[0m. File Move            \033[1;32m14\033[0m. File Delete          \033[1;32m15\033[0m. Create Folder  \033[1;32m16\033[0m. File Size    \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m17\033[0m. File Exists          \033[1;32m18\033[0m. Random String        \033[1;32m19\033[0m. Password Gen   \033[1;32m20\033[0m. URL Encode   \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m21\033[0m. URL Decode           \033[1;32m22\033[0m. HEX Encode           \033[1;32m23\033[0m. HEX Decode     \033[1;32m24\033[0m. ROT13        \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m25\033[0m. ROT47                \033[1;32m26\033[0m. XOR Cipher           \033[1;32m27\033[0m. Calculator     \033[1;32m28\033[0m. Date Time    \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m29\033[0m. Timer                \033[1;32m30\033[0m. Stopwatch            \033[1;32m31\033[0m. File Rename    \033[1;32m32\033[0m. Attribute    \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m33\033[0m. Dir List             \033[1;32m34\033[0m. Duplicate Finder     \033[1;32m35\033[0m. File Compare   \033[1;32m36\033[0m. Line Count   \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m37\033[0m. Word Count           \033[1;32m38\033[0m. Char Count           \033[1;32m39\033[0m. Reverse Str    \033[1;32m40\033[0m. Reverse File \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m41\033[0m. File Embed           \033[1;32m42\033[0m. File Extract         \033[1;32m43\033[0m. Zip File      \033[1;32m44\033[0m. Unzip File   \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m45\033[0m. File Merge           \033[1;32m46\033[0m. File Split           \033[1;32m47\033[0m. File Patch     \033[1;32m48\033[0m. Backup       \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m49\033[0m. Restore Backup       \033[1;32m50\033[0m. System Info          \033[1;32m51\033[0m. Website HTTP  \033[1;32m52\033[0m. Website HTTPS\033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m53\033[0m. Website Status       \033[1;32m54\033[0m. Website Headers      \033[1;32m55\033[0m. Website Title  \033[1;32m56\033[0m. Meta Tags    \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m57\033[0m. Extract Links        \033[1;32m58\033[0m. Extract Images       \033[1;32m59\033[0m. Extract Emails  \033[1;32m60\033[0m. Extract Phone  \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m61\033[0m. Extract CSS          \033[1;32m62\033[0m. Extract JS           \033[1;32m63\033[0m. Domain Info    \033[1;32m64\033[0m. IP Lookup    \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m65\033[0m. SSL Check            \033[1;32m66\033[0m. DNS Lookup           \033[1;32m67\033[0m. WHOIS         \033[1;32m68\033[0m. Subdomain      \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m69\033[0m. Port Scanner         \033[1;32m70\033[0m. Website Screenshot   \033[1;32m71\033[0m. URL Shortener  \033[1;32m72\033[0m. QR Code       \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m73\033[0m. XML to JSON          \033[1;32m74\033[0m. JSON to XML          \033[1;32m75\033[0m. CSV to JSON    \033[1;32m76\033[0m. JSON to CSV   \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m77\033[0m. HTML Minify          \033[1;32m78\033[0m. HTML Beautify        \033[1;32m79\033[0m. CSS Minify     \033[1;32m80\033[0m. JS Minify     \033[1;33m║\033[0m")
    print("\033[1;33m║\033[0m  \033[1;32m 0\033[0m. Exit                                                 \033[1;33m║\033[0m")
    print("\033[1;33m╚══════════════════════════════════════════════════════════════════════╝\033[0m")

# ============================================
#  SYSTEMS 1-50: File & Crypto Operations
#  (All existing systems remain unchanged)
# ============================================

def system_1_jsc_decrypt():
    print("\n\033[1;36m📂 JSC Decrypt System\033[0m")
    print("=" * 40)
    
    jsc_file_path = input("\n[?] .jsc file path: ").strip()
    if not os.path.exists(jsc_file_path):
        print("❌ File not found!")
        return
    
    encryption_key = input("[?] Encryption key: ").strip()
    if not encryption_key:
        print("❌ Key required!")
        return
    
    output_file_path = input("[?] Output name: ").strip() or "decrypted_output.js"
    
    try:
        with open(jsc_file_path, "rb") as f:
            jsc_file_data = f.read()
        
        output_data = xxtea.decrypt(jsc_file_data, encryption_key)
        if not output_data:
            print("❌ Decryption failed!")
            return
        
        try:
            output_data = gzip.decompress(output_data)
            print("✅ GZIP decompressed")
        except:
            pass
        
        with open(output_file_path, "wb") as f:
            f.write(output_data)
        
        print(f"✅ Saved: {output_file_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

def system_2_file_lock():
    print("\n\033[1;36m🔒 File Lock System\033[0m")
    file_path = input("File path: ").strip()
    if not os.path.exists(file_path):
        print("❌ File not found!")
        return
    
    password = input("Set password: ").strip()
    if not password:
        print("❌ Password required!")
        return
    
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        
        key = hashlib.sha256(password.encode()).digest()
        encrypted = bytearray()
        for i, byte in enumerate(data):
            encrypted.append(byte ^ key[i % len(key)])
        
        with open(file_path + '.locked', 'wb') as f:
            f.write(encrypted)
        
        print(f"✅ File locked: {file_path}.locked")
    except Exception as e:
        print(f"❌ Error: {e}")

def system_3_file_unlock():
    print("\n\033[1;36m🔓 File Unlock System\033[0m")
    file_path = input("Locked file path: ").strip()
    if not os.path.exists(file_path):
        print("❌ File not found!")
        return
    
    password = input("Password: ").strip()
    if not password:
        print("❌ Password required!")
        return
    
    try:
        with open(file_path, 'rb') as f:
            encrypted = f.read()
        
        key = hashlib.sha256(password.encode()).digest()
        decrypted = bytearray()
        for i, byte in enumerate(encrypted):
            decrypted.append(byte ^ key[i % len(key)])
        
        output_path = file_path.replace('.locked', '') + '.unlocked'
        with open(output_path, 'wb') as f:
            f.write(decrypted)
        
        print(f"✅ Unlocked: {output_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

def system_4_text_encrypt():
    print("\n\033[1;36m🔐 Text Encrypt\033[0m")
    text = input("Enter text: ").strip()
    key = input("Key: ").strip()
    
    if not text or not key:
        print("❌ Text and key required!")
        return
    
    key_bytes = key.encode()
    encrypted = base64.b64encode(xxtea.encrypt(text.encode(), key_bytes)).decode()
    print(f"\n✅ Encrypted: {encrypted}")

def system_5_text_decrypt():
    print("\n\033[1;36m🔓 Text Decrypt\033[0m")
    encrypted = input("Encrypted text: ").strip()
    key = input("Key: ").strip()
    
    if not encrypted or not key:
        print("❌ Encrypted text and key required!")
        return
    
    try:
        key_bytes = key.encode()
        decrypted = xxtea.decrypt(base64.b64decode(encrypted), key_bytes).decode()
        print(f"\n✅ Decrypted: {decrypted}")
    except:
        print("❌ Decryption failed! Wrong key?")

def system_6_hash_generate():
    print("\n\033[1;36m🔑 Hash Generator\033[0m")
    text = input("Enter text: ").strip()
    if not text:
        print("❌ Text required!")
        return
    
    print(f"\nMD5: {hashlib.md5(text.encode()).hexdigest()}")
    print(f"SHA1: {hashlib.sha1(text.encode()).hexdigest()}")
    print(f"SHA256: {hashlib.sha256(text.encode()).hexdigest()}")
    print(f"SHA512: {hashlib.sha512(text.encode()).hexdigest()}")

def system_7_base64_encode():
    text = input("Enter text: ")
    print(f"✅ {base64.b64encode(text.encode()).decode()}")

def system_8_base64_decode():
    text = input("Enter Base64 text: ")
    try:
        print(f"✅ {base64.b64decode(text).decode()}")
    except:
        print("❌ Invalid format!")

def system_9_json_format():
    data = input("Enter JSON data (key:value): ")
    try:
        parsed = json.loads(data)
        print(json.dumps(parsed, indent=2))
    except:
        print("❌ Invalid JSON!")

def system_10_file_reader():
    path = input("File path: ")
    if os.path.exists(path):
        with open(path, 'r') as f:
            print(f.read())
    else:
        print("❌ File not found!")

def system_11_file_writer():
    path = input("File name: ")
    content = input("Content: ")
    with open(path, 'w') as f:
        f.write(content)
    print(f"✅ Saved: {path}")

def system_12_file_copy():
    src = input("Source: ")
    dst = input("Destination: ")
    if os.path.exists(src):
        shutil.copy(src, dst)
        print("✅ Copied!")
    else:
        print("❌ Source not found!")

def system_13_file_move():
    src = input("Source: ")
    dst = input("Destination: ")
    if os.path.exists(src):
        shutil.move(src, dst)
        print("✅ Moved!")
    else:
        print("❌ Source not found!")

def system_14_file_delete():
    path = input("File path: ")
    if os.path.exists(path):
        os.remove(path)
        print("✅ Deleted!")
    else:
        print("❌ File not found!")

def system_15_create_folder():
    path = input("Folder name: ")
    os.makedirs(path, exist_ok=True)
    print(f"✅ Created: {path}")

def system_16_file_size():
    path = input("File path: ")
    if os.path.exists(path):
        size = os.path.getsize(path)
        print(f"📏 Size: {size} bytes ({size/1024:.2f} KB)")
    else:
        print("❌ File not found!")

def system_17_file_exists():
    path = input("File path: ")
    print(f"{'✅' if os.path.exists(path) else '❌'} File {'exists' if os.path.exists(path) else 'not found'}")

def system_18_random_string():
    length = int(input("Length: ") or 10)
    chars = string.ascii_letters + string.digits
    print(f"✅ {''.join(random.choice(chars) for _ in range(length))}")

def system_19_password_generate():
    length = int(input("Password length: ") or 12)
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    print(f"🔑 {''.join(random.choice(chars) for _ in range(length))}")

def system_20_url_encode():
    text = input("Enter text: ")
    print(f"✅ {urllib.parse.quote(text)}")

def system_21_url_decode():
    text = input("Enter encoded text: ")
    print(f"✅ {urllib.parse.unquote(text)}")

def system_22_hex_encode():
    text = input("Enter text: ")
    print(f"✅ {text.encode().hex()}")

def system_23_hex_decode():
    hex_text = input("Enter hex text: ")
    try:
        print(f"✅ {bytes.fromhex(hex_text).decode()}")
    except:
        print("❌ Invalid hex!")

def system_24_rot13():
    text = input("Enter text: ")
    result = ''.join(chr((ord(c) - 97 + 13) % 26 + 97) if 'a' <= c <= 'z' else 
                     chr((ord(c) - 65 + 13) % 26 + 65) if 'A' <= c <= 'Z' else c for c in text)
    print(f"✅ {result}")

def system_25_rot47():
    text = input("Enter text: ")
    result = ''.join(chr(33 + ((ord(c) - 33 + 47) % 94)) if 33 <= ord(c) <= 126 else c for c in text)
    print(f"✅ {result}")

def system_26_xor_cipher():
    text = input("Enter text: ")
    key = input("Key: ")
    result = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))
    print(f"✅ {result}")

def system_27_calculator():
    expr = input("Enter expression: ")
    try:
        print(f"= {eval(expr)}")
    except:
        print("❌ Invalid expression!")

def system_28_datetime():
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def system_29_timer():
    sec = int(input("Seconds: "))
    print(f"⏳ Waiting {sec} seconds...")
    time.sleep(sec)
    print("✅ Timer finished!")

def system_30_stopwatch():
    input("Press Enter to start...")
    start = time.time()
    input("Press Enter to stop...")
    end = time.time()
    print(f"⏱️ Time: {end - start:.2f} seconds")

def system_31_file_rename():
    old = input("Old name: ")
    new = input("New name: ")
    if os.path.exists(old):
        os.rename(old, new)
        print("✅ Renamed!")
    else:
        print("❌ File not found!")

def system_32_file_attribute():
    path = input("File path: ")
    if os.path.exists(path):
        print(f"📄 {path}")
        print(f"Size: {os.path.getsize(path)} bytes")
        print(f"Modified: {datetime.fromtimestamp(os.path.getmtime(path))}")
    else:
        print("❌ File not found!")

def system_33_directory_list():
    path = input("Directory path: ") or '.'
    if os.path.exists(path):
        for item in os.listdir(path):
            print(f"  📁 {item}" if os.path.isdir(os.path.join(path, item)) else f"  📄 {item}")
    else:
        print("❌ Directory not found!")

def system_34_duplicate_finder():
    print("⚠️ May take time for large directories!")
    path = input("Directory path: ") or '.'
    files = {}
    for root, _, filenames in os.walk(path):
        for file in filenames:
            full = os.path.join(root, file)
            size = os.path.getsize(full)
            if size in files:
                print(f"⚠️ Duplicate: {full} (Size: {size})")
            else:
                files[size] = full

def system_35_file_compare():
    f1 = input("File 1: ")
    f2 = input("File 2: ")
    if os.path.exists(f1) and os.path.exists(f2):
        print(f"{'✅' if filecmp.cmp(f1, f2) else '❌'} Files {'are identical' if filecmp.cmp(f1, f2) else 'are different'}")
    else:
        print("❌ File not found!")

def system_36_line_count():
    path = input("File path: ")
    if os.path.exists(path):
        with open(path, 'r') as f:
            lines = sum(1 for _ in f)
        print(f"📏 Lines: {lines}")
    else:
        print("❌ File not found!")

def system_37_word_count():
    path = input("File path: ")
    if os.path.exists(path):
        with open(path, 'r') as f:
            words = len(f.read().split())
        print(f"📝 Words: {words}")
    else:
        print("❌ File not found!")

def system_38_character_count():
    path = input("File path: ")
    if os.path.exists(path):
        with open(path, 'r') as f:
            chars = len(f.read())
        print(f"🔤 Characters: {chars}")
    else:
        print("❌ File not found!")

def system_39_reverse_string():
    text = input("Enter text: ")
    print(f"✅ {text[::-1]}")

def system_40_reverse_file():
    src = input("Source file: ")
    dst = input("Destination: ")
    if os.path.exists(src):
        with open(src, 'r') as f:
            data = f.read()
        with open(dst, 'w') as f:
            f.write(data[::-1])
        print("✅ Reversed!")
    else:
        print("❌ File not found!")

def system_41_file_embed():
    main = input("Main file: ")
    embed = input("Embed file: ")
    if os.path.exists(main) and os.path.exists(embed):
        with open(main, 'a') as f:
            f.write(f"\n# === EMBED START ===\n")
            with open(embed, 'r') as e:
                f.write(e.read())
            f.write(f"\n# === EMBED END ===\n")
        print("✅ Embedded!")
    else:
        print("❌ File not found!")

def system_42_file_extract():
    main = input("Main file: ")
    if os.path.exists(main):
        with open(main, 'r') as f:
            data = f.read()
        start = data.find("# === EMBED START ===")
        end = data.find("# === EMBED END ===")
        if start != -1 and end != -1:
            extracted = data[start + len("# === EMBED START ==="):end]
            with open('extracted.txt', 'w') as f:
                f.write(extracted)
            print("✅ Extracted: extracted.txt")
        else:
            print("❌ No embedded data found!")
    else:
        print("❌ File not found!")

def system_43_zip_file():
    folder = input("Folder path: ")
    output = input("Output zip name: ") or "archive.zip"
    with ZipFile(output, 'w') as zipf:
        for root, _, files in os.walk(folder):
            for file in files:
                zipf.write(os.path.join(root, file))
    print(f"✅ Zipped: {output}")

def system_44_unzip_file():
    zip_path = input("Zip file path: ")
    extract_to = input("Extract location: ") or "."
    with ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_to)
    print(f"✅ Unzipped: {extract_to}")

def system_45_file_merge():
    f1 = input("File 1: ")
    f2 = input("File 2: ")
    output = input("Output name: ") or "merged.txt"
    if os.path.exists(f1) and os.path.exists(f2):
        with open(output, 'w') as out:
            with open(f1, 'r') as f:
                out.write(f.read())
            out.write("\n")
            with open(f2, 'r') as f:
                out.write(f.read())
        print(f"✅ Merged: {output}")
    else:
        print("❌ File not found!")

def system_46_file_split():
    src = input("File path: ")
    chunk_size = int(input("Chunk size (KB): ")) * 1024
    if os.path.exists(src):
        with open(src, 'rb') as f:
            data = f.read()
        chunk_num = 1
        for i in range(0, len(data), chunk_size):
            with open(f"{src}.part{chunk_num}", 'wb') as out:
                out.write(data[i:i+chunk_size])
            chunk_num += 1
        print(f"✅ Split into {chunk_num-1} parts!")
    else:
        print("❌ File not found!")

def system_47_file_patch():
    print("⚠️ Patch System (Binary Modify)")
    src = input("File path: ")
    offset = int(input("Offset (bytes): "))
    new_byte = input("New hex value (e.g., 90): ").strip()
    if os.path.exists(src) and len(new_byte) == 2:
        try:
            with open(src, 'r+b') as f:
                f.seek(offset)
                f.write(bytes.fromhex(new_byte))
            print("✅ Patched!")
        except:
            print("❌ Patch failed!")
    else:
        print("❌ Invalid input!")

def system_48_backup_create():
    src = input("File/Folder to backup: ")
    if os.path.exists(src):
        backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        if os.path.isdir(src):
            shutil.copytree(src, backup_name)
        else:
            shutil.copy2(src, backup_name)
        print(f"✅ Backup created: {backup_name}")
    else:
        print("❌ File/Folder not found!")

def system_49_restore_backup():
    backup = input("Backup name: ")
    if os.path.exists(backup):
        dest = input("Restore location: ")
        if os.path.isdir(backup):
            shutil.copytree(backup, dest)
        else:
            shutil.copy2(backup, dest)
        print(f"✅ Restored: {dest}")
    else:
        print("❌ Backup not found!")

def system_50_system_info():
    print("\n\033[1;36m💻 System Info\033[0m")
    print(f"OS: {os.name}")
    print(f"Platform: {os.uname().sysname if hasattr(os, 'uname') else 'N/A'}")
    print(f"Current Directory: {os.getcwd()}")
    print(f"Python Version: {__import__('sys').version}")
    print(f"Disk Space: {os.statvfs('/').f_frsize * os.statvfs('/').f_blocks / (1024**3):.2f} GB" if os.name == 'posix' else "N/A")

# ============================================
#  SYSTEMS 51-80: Web Tools & Online Services
#  All use only built-in libraries (urllib, re)
#  No external installation required
# ============================================

def fetch_website_content(url):
    """Helper function to fetch website content"""
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8', errors='ignore')
            return content, response
    except Exception as e:
        return None, str(e)

def system_51_website_http():
    """Fetch website using HTTP (plain text)"""
    print("\n\033[1;36m🌐 Website HTTP Fetcher\033[0m")
    url = input("Enter website URL: ").strip()
    content, result = fetch_website_content(url)
    if content:
        print(f"\n✅ Content fetched successfully!")
        print(f"📄 First 500 characters:\n{'-' * 40}")
        print(content[:500] + "...")
    else:
        print(f"❌ Failed: {result}")

def system_52_website_https():
    """Fetch website using HTTPS (secure)"""
    print("\n\033[1;36m🔒 Website HTTPS Fetcher\033[0m")
    url = input("Enter website URL: ").strip()
    if not url.startswith('https://'):
        url = 'https://' + url
    content, result = fetch_website_content(url)
    if content:
        print(f"\n✅ Secure content fetched!")
        print(f"📄 First 500 characters:\n{'-' * 40}")
        print(content[:500] + "...")
    else:
        print(f"❌ Failed: {result}")

def system_53_website_status():
    """Check website status code"""
    print("\n\033[1;36m📊 Website Status Checker\033[0m")
    url = input("Enter website URL: ").strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    try:
        req = urllib.request.Request(url, method='HEAD')
        with urllib.request.urlopen(req, timeout=10) as response:
            print(f"✅ Status Code: {response.getcode()}")
            print(f"✅ Server: {response.headers.get('Server', 'Unknown')}")
            print(f"✅ Content-Type: {response.headers.get('Content-Type', 'Unknown')}")
    except Exception as e:
        print(f"❌ Failed: {e}")

def system_54_website_headers():
    """Extract website HTTP headers"""
    print("\n\033[1;36m📋 Website Headers Extractor\033[0m")
    url = input("Enter website URL: ").strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as response:
            print(f"\n✅ Headers:\n{'-' * 40}")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
    except Exception as e:
        print(f"❌ Failed: {e}")

def system_55_website_title():
    """Extract website title from HTML"""
    print("\n\033[1;36m📝 Website Title Extractor\033[0m")
    url = input("Enter website URL: ").strip()
    content, result = fetch_website_content(url)
    if content:
        match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        if match:
            print(f"✅ Title: {match.group(1).strip()}")
        else:
            print("❌ No title found!")
    else:
        print(f"❌ Failed: {result}")

def system_56_meta_tags():
    """Extract meta tags from website"""
    print("\n\033[1;36m🏷️ Meta Tags Extractor\033[0m")
    url = input("Enter website URL: ").strip()
    content, result = fetch_website_content(url)
    if content:
        meta_tags = re.findall(r'<meta\s+[^>]*>', content, re.IGNORECASE)
        if meta_tags:
            print(f"\n✅ Found {len(meta_tags)} meta tags:\n{'-' * 40}")
            for tag in meta_tags[:10]:
                print(tag)
        else:
            print("❌ No meta tags found!")
    else:
        print(f"❌ Failed: {result}")

def system_57_extract_links():
    """Extract all links from website"""
    print("\n\033[1;36m🔗 Link Extractor\033[0m")
    url = input("Enter website URL: ").strip()
    content, result = fetch_website_content(url)
    if content:
        links = re.findall(r'<a\s+(?:[^>]*?\s+)?href=["\']([^"\']*)["\']', content, re.IGNORECASE)
        if links:
            print(f"\n✅ Found {len(links)} links:\n{'-' * 40}")
            for link in set(links)[:20]:
                print(f"🔗 {link}")
        else:
            print("❌ No links found!")
    else:
        print(f"❌ Failed: {result}")

def system_58_extract_images():
    """Extract image URLs from website"""
    print("\n\033[1;36m🖼️ Image Extractor\033[0m")
    url = input("Enter website URL: ").strip()
    content, result = fetch_website_content(url)
    if content:
        images = re.findall(r'<img\s+(?:[^>]*?\s+)?src=["\']([^"\']*)["\']', content, re.IGNORECASE)
        if images:
            print(f"\n✅ Found {len(images)} images:\n{'-' * 40}")
            for img in set(images)[:20]:
                print(f"🖼️ {img}")
        else:
            print("❌ No images found!")
    else:
        print(f"❌ Failed: {result}")

def system_59_extract_emails():
    """Extract email addresses from website"""
    print("\n\033[1;36m📧 Email Extractor\033[0m")
    url = input("Enter website URL: ").strip()
    content, result = fetch_website_content(url)
    if content:
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
        if emails:
            print(f"\n✅ Found {len(emails)} emails:\n{'-' * 40}")
            for email in set(emails)[:20]:
                print(f"📧 {email}")
        else:
            print("❌ No emails found!")
    else:
        print(f"❌ Failed: {result}")

def system_60_extract_phone():
    """Extract phone numbers from website"""
    print("\n\033[1;36m📞 Phone Extractor\033[0m")
    url = input("Enter website URL: ").strip()
    content, result = fetch_website_content(url)
    if content:
        phones = re.findall(r'\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}', content)
        if phones:
            print(f"\n✅ Found {len(phones)} phone numbers:\n{'-' * 40}")
            for phone in set(phones)[:20]:
                print(f"📞 {phone}")
        else:
            print("❌ No phone numbers found!")
    else:
        print(f"❌ Failed: {result}")

def system_61_extract_css():
    """Extract CSS links from website"""
    print("\n\033[1;36m🎨 CSS Extractor\033[0m")
    url = input("Enter website URL: ").strip()
    content, result = fetch_website_content(url)
    if content:
        css = re.findall(r'<link\s+(?:[^>]*?\s+)?href=["\']([^"\']*\.css[^"\']*)["\']', content, re.IGNORECASE)
        if css:
            print(f"\n✅ Found {len(css)} CSS files:\n{'-' * 40}")
            for c in set(css)[:20]:
                print(f"🎨 {c}")
        else:
            print("❌ No CSS found!")
    else:
        print(f"❌ Failed: {result}")

def system_62_extract_js():
    """Extract JavaScript files from website"""
    print("\n\033[1;36m📜 JavaScript Extractor\033[0m")
    url = input("Enter website URL: ").strip()
    content, result = fetch_website_content(url)
    if content:
        js = re.findall(r'<script\s+(?:[^>]*?\s+)?src=["\']([^"\']*\.js[^"\']*)["\']', content, re.IGNORECASE)
        if js:
            print(f"\n✅ Found {len(js)} JS files:\n{'-' * 40}")
            for j in set(js)[:20]:
                print(f"📜 {j}")
        else:
            print("❌ No JS found!")
    else:
        print(f"❌ Failed: {result}")

def system_63_domain_info():
    """Get domain information"""
    print("\n\033[1;36m🌍 Domain Info\033[0m")
    url = input("Enter domain: ").strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    try:
        parsed = urllib.parse.urlparse(url)
        domain = parsed.netloc or parsed.path
        print(f"\n✅ Domain: {domain}")
        print(f"✅ Protocol: {parsed.scheme or 'Unknown'}")
        print(f"✅ Path: {parsed.path or '/'}")
        print(f"✅ Query: {parsed.query or 'None'}")
    except Exception as e:
        print(f"❌ Failed: {e}")

def system_64_ip_lookup():
    """Lookup IP address of website"""
    print("\n\033[1;36m🌐 IP Lookup\033[0m")
    domain = input("Enter domain: ").strip()
    try:
        import socket
        ip = socket.gethostbyname(domain)
        print(f"✅ IP Address: {ip}")
        print(f"✅ Hostname: {socket.gethostbyaddr(ip)[0] if socket.gethostbyaddr(ip) else 'Unknown'}")
    except Exception as e:
        print(f"❌ Failed: {e}")

def system_65_ssl_check():
    """Check SSL certificate of website"""
    print("\n\033[1;36m🔐 SSL Certificate Checker\033[0m")
    domain = input("Enter domain: ").strip()
    try:
        import socket
        import ssl
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                print(f"\n✅ SSL Certificate Information:")
                print(f"📋 Subject: {cert.get('subject', 'Unknown')}")
                print(f"📋 Issuer: {cert.get('issuer', 'Unknown')}")
                print(f"📋 Expiry: {cert.get('notAfter', 'Unknown')}")
    except Exception as e:
        print(f"❌ Failed: {e}")

def system_66_dns_lookup():
    """Perform DNS lookup"""
    print("\n\033[1;36m🔍 DNS Lookup\033[0m")
    domain = input("Enter domain: ").strip()
    try:
        import socket
        print(f"\n✅ DNS Records for {domain}:")
        print(f"🔹 A Record: {socket.gethostbyname(domain)}")
        try:
            addrs = socket.gethostbyname_ex(domain)
            print(f"🔹 A (Additional): {addrs[2]}")
        except:
            pass
    except Exception as e:
        print(f"❌ Failed: {e}")

def system_67_whois_lookup():
    """Perform WHOIS lookup"""
    print("\n\033[1;36m📋 WHOIS Lookup\033[0m")
    domain = input("Enter domain: ").strip()
    print("⚠️ WHOIS lookup requires external library 'whois'")
    print("💡 Using fallback: web-based WHOIS")
    print(f"🌐 Check: https://whois.icann.org/en/lookup?name={domain}")
    try:
        import socket
        print(f"✅ Domain: {domain}")
        print(f"✅ IP: {socket.gethostbyname(domain)}")
    except:
        print("❌ WHOIS lookup failed!")

def system_68_subdomain_finder():
    """Find subdomains (simple version)"""
    print("\n\033[1;36m🔍 Subdomain Finder\033[0m")
    domain = input("Enter domain: ").strip()
    common_subdomains = ['www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk', 
                         'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'm', 'imap', 'test', 
                         'ns', 'blog', 'pop3', 'dev', 'www2', 'admin', 'forum', 'news', 'vpn']
    print(f"\n✅ Common subdomains for {domain}:")
    found = []
    for sub in common_subdomains:
        try:
            import socket
            socket.gethostbyname(f"{sub}.{domain}")
            found.append(sub)
            print(f"✅ {sub}.{domain} - Found!")
        except:
            pass
    if not found:
        print("❌ No common subdomains found!")

def system_69_port_scanner():
    """Simple port scanner for websites"""
    print("\n\033[1;36m🔌 Port Scanner\033[0m")
    host = input("Enter host: ").strip()
    print("⚠️ Scanning common ports (80, 443, 21, 22, 25, 3306, 8080)")
    common_ports = [80, 443, 21, 22, 25, 3306, 8080]
    try:
        import socket
        print(f"\n✅ Scanning {host}:")
        for port in common_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"✅ Port {port} - OPEN")
            else:
                print(f"❌ Port {port} - CLOSED")
            sock.close()
    except Exception as e:
        print(f"❌ Failed: {e}")

def system_70_website_screenshot():
    """Generate website screenshot (URL only)"""
    print("\n\033[1;36m📸 Website Screenshot\033[0m")
    url = input("Enter website URL: ").strip()
    print(f"🌐 Screenshot available at: https://www.screenshotmachine.com/")
    print(f"🔗 Use: https://www.screenshotmachine.com/?url={url}")
    print(f"💡 Or use: https://api.screenshotmachine.com/")

def system_71_url_shortener():
    """Shorten URL (uses built-in redirect checker)"""
    print("\n\033[1;36m🔗 URL Shortener\033[0m")
    url = input("Enter URL to shorten: ").strip()
    print("💡 Use online services:")
    print(f"📌 https://tinyurl.com/create.php?url={url}")
    print(f"📌 https://bitly.com/")
    print(f"📌 https://is.gd/")

def system_72_qr_code():
    """Generate QR code for URL"""
    print("\n\033[1;36m📱 QR Code Generator\033[0m")
    url = input("Enter URL for QR code: ").strip()
    print(f"\n✅ QR Code available at:")
    print(f"🌐 https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={url}")
    print(f"📱 Or use: https://www.qr-code-generator.com/")

def system_73_xml_to_json():
    """Convert XML to JSON (simplified)"""
    print("\n\033[1;36m🔄 XML to JSON Converter\033[0m")
    xml_input = input("Enter XML data (or path to XML file): ").strip()
    if os.path.exists(xml_input):
        with open(xml_input, 'r') as f:
            xml_input = f.read()
    print("⚠️ Full XML to JSON requires 'xmltodict' library")
    print("💡 Converting simple XML tags...")
    # Simple tag extraction
    tags = re.findall(r'<([^>]+)>([^<]+)</\1>', xml_input)
    if tags:
        result = {}
        for tag, value in tags:
            result[tag] = value.strip()
        print(f"\n✅ Converted:\n{json.dumps(result, indent=2)}")
    else:
        print("❌ No XML tags found!")

def system_74_json_to_xml():
    """Convert JSON to XML (simplified)"""
    print("\n\033[1;36m🔄 JSON to XML Converter\033[0m")
    json_input = input("Enter JSON data: ").strip()
    try:
        data = json.loads(json_input)
        xml_output = "<?xml version='1.0' encoding='UTF-8'?>\n<root>\n"
        for key, value in data.items():
            xml_output += f"  <{key}>{value}</{key}>\n"
        xml_output += "</root>"
        print(f"\n✅ Converted:\n{xml_output}")
    except:
        print("❌ Invalid JSON!")

def system_75_csv_to_json():
    """Convert CSV to JSON"""
    print("\n\033[1;36m🔄 CSV to JSON Converter\033[0m")
    csv_input = input("Enter CSV file path or data: ").strip()
    if os.path.exists(csv_input):
        with open(csv_input, 'r') as f:
            csv_input = f.read()
    lines = csv_input.strip().split('\n')
    if len(lines) < 2:
        print("❌ Invalid CSV format!")
        return
    headers = [h.strip() for h in lines[0].split(',')]
    result = []
    for line in lines[1:]:
        values = [v.strip() for v in line.split(',')]
        if len(values) == len(headers):
            result.append(dict(zip(headers, values)))
    print(f"\n✅ Converted:\n{json.dumps(result, indent=2)}")

def system_76_json_to_csv():
    """Convert JSON to CSV"""
    print("\n\033[1;36m🔄 JSON to CSV Converter\033[0m")
    json_input = input("Enter JSON data: ").strip()
    try:
        data = json.loads(json_input)
        if isinstance(data, list) and len(data) > 0:
            headers = list(data[0].keys())
            csv_output = ','.join(headers) + '\n'
            for item in data:
                csv_output += ','.join([str(item.get(h, '')) for h in headers]) + '\n'
            print(f"\n✅ Converted:\n{csv_output}")
        else:
            print("❌ Invalid JSON array!")
    except:
        print("❌ Invalid JSON!")

def system_77_html_minify():
    """Minify HTML code"""
    print("\n\033[1;36m📦 HTML Minifier\033[0m")
    html_input = input("Enter HTML file path or code: ").strip()
    if os.path.exists(html_input):
        with open(html_input, 'r') as f:
            html_input = f.read()
    # Remove comments and extra whitespace
    minified = re.sub(r'<!--.*?-->', '', html_input, flags=re.DOTALL)
    minified = re.sub(r'\s+', ' ', minified)
    minified = re.sub(r'>\s+<', '><', minified)
    print(f"\n✅ Minified HTML:\n{'-' * 40}")
    print(minified[:500] + "..." if len(minified) > 500 else minified)

def system_78_html_beautify():
    """Beautify HTML code"""
    print("\n\033[1;36m✨ HTML Beautifier\033[0m")
    html_input = input("Enter HTML file path or code: ").strip()
    if os.path.exists(html_input):
        with open(html_input, 'r') as f:
            html_input = f.read()
    # Simple beautification - add line breaks
    beautified = html_input.replace('>', '>\n').replace('</', '\n</')
    # Remove empty lines
    beautified = '\n'.join([line.strip() for line in beautified.split('\n') if line.strip()])
    print(f"\n✅ Beautified HTML:\n{'-' * 40}")
    print(beautified[:1000] + "..." if len(beautified) > 1000 else beautified)

def system_79_css_minify():
    """Minify CSS code"""
    print("\n\033[1;36m📦 CSS Minifier\033[0m")
    css_input = input("Enter CSS file path or code: ").strip()
    if os.path.exists(css_input):
        with open(css_input, 'r') as f:
            css_input = f.read()
    # Remove comments and extra whitespace
    minified = re.sub(r'/\*.*?\*/', '', css_input, flags=re.DOTALL)
    minified = re.sub(r'\s+', ' ', minified)
    minified = re.sub(r'}\s*{', '}{', minified)
    minified = re.sub(r';\s*}', ';}', minified)
    print(f"\n✅ Minified CSS:\n{'-' * 40}")
    print(minified[:500] + "..." if len(minified) > 500 else minified)

def system_80_js_minify():
    """Minify JavaScript code (basic)"""
    print("\n\033[1;36m📦 JavaScript Minifier\033[0m")
    js_input = input("Enter JS file path or code: ").strip()
    if os.path.exists(js_input):
        with open(js_input, 'r') as f:
            js_input = f.read()
    # Remove comments and extra whitespace
    minified = re.sub(r'//.*?$', '', js_input, flags=re.MULTILINE)
    minified = re.sub(r'/\*.*?\*/', '', minified, flags=re.DOTALL)
    minified = re.sub(r'\s+', ' ', minified)
    minified = re.sub(r';\s+', ';', minified)
    minified = re.sub(r'{\s+', '{', minified)
    minified = re.sub(r'}\s+', '}', minified)
    print(f"\n✅ Minified JS:\n{'-' * 40}")
    print(minified[:500] + "..." if len(minified) > 500 else minified)

# ============================================
#  MAIN PROGRAM - SYSTEM DISPATCHER
#  Design Pattern: Dictionary-based Router
#  Now supports 80 systems
# ============================================

def main():
    systems = {
        # Systems 1-50: File & Crypto
        '1': system_1_jsc_decrypt, '2': system_2_file_lock, '3': system_3_file_unlock,
        '4': system_4_text_encrypt, '5': system_5_text_decrypt, '6': system_6_hash_generate,
        '7': system_7_base64_encode, '8': system_8_base64_decode, '9': system_9_json_format,
        '10': system_10_file_reader, '11': system_11_file_writer, '12': system_12_file_copy,
        '13': system_13_file_move, '14': system_14_file_delete, '15': system_15_create_folder,
        '16': system_16_file_size, '17': system_17_file_exists, '18': system_18_random_string,
        '19': system_19_password_generate, '20': system_20_url_encode, '21': system_21_url_decode,
        '22': system_22_hex_encode, '23': system_23_hex_decode, '24': system_24_rot13,
        '25': system_25_rot47, '26': system_26_xor_cipher, '27': system_27_calculator,
        '28': system_28_datetime, '29': system_29_timer, '30': system_30_stopwatch,
        '31': system_31_file_rename, '32': system_32_file_attribute, '33': system_33_directory_list,
        '34': system_34_duplicate_finder, '35': system_35_file_compare, '36': system_36_line_count,
        '37': system_37_word_count, '38': system_38_character_count, '39': system_39_reverse_string,
        '40': system_40_reverse_file, '41': system_41_file_embed, '42': system_42_file_extract,
        '43': system_43_zip_file, '44': system_44_unzip_file, '45': system_45_file_merge,
        '46': system_46_file_split, '47': system_47_file_patch, '48': system_48_backup_create,
        '49': system_49_restore_backup, '50': system_50_system_info,
        
        # Systems 51-80: Web Tools
        '51': system_51_website_http, '52': system_52_website_https,
        '53': system_53_website_status, '54': system_54_website_headers,
        '55': system_55_website_title, '56': system_56_meta_tags,
        '57': system_57_extract_links, '58': system_58_extract_images,
        '59': system_59_extract_emails, '60': system_60_extract_phone,
        '61': system_61_extract_css, '62': system_62_extract_js,
        '63': system_63_domain_info, '64': system_64_ip_lookup,
        '65': system_65_ssl_check, '66': system_66_dns_lookup,
        '67': system_67_whois_lookup, '68': system_68_subdomain_finder,
        '69': system_69_port_scanner, '70': system_70_website_screenshot,
        '71': system_71_url_shortener, '72': system_72_qr_code,
        '73': system_73_xml_to_json, '74': system_74_json_to_xml,
        '75': system_75_csv_to_json, '76': system_76_json_to_csv,
        '77': system_77_html_minify, '78': system_78_html_beautify,
        '79': system_79_css_minify, '80': system_80_js_minify
    }
    
    while True:
        print_header()
        print_menu()
        choice = input("\n\033[1;33m👉 Enter system number (0 to exit): \033[0m").strip()
        
        if choice == '0':
            print("\n\033[1;32m👋 Goodbye! See you again!\033[0m")
            break
        
        if choice in systems:
            systems[choice]()
            input("\n\nPress Enter to return to menu...")
        else:
            print("\n❌ Invalid number! Please enter 0-80.")
            input("Press Enter...")

if __name__ == "__main__":
    main()
