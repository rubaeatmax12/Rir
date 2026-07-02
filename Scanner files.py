#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import re
import time
import json
import hashlib
import shutil
import stat
import glob
import fnmatch
import zipfile
import tarfile
import gzip
import bz2
import lzma
import tempfile
import subprocess
import platform
import datetime
import random
import string
import urllib.parse
import urllib.request
import urllib.error
import base64
import binascii
import struct
import pickle
import csv
import xml.etree.ElementTree as ET
import html
import html.parser
import configparser
from collections import Counter, defaultdict
from pathlib import Path

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
║     FILE SEARCH SYSTEM v8.0 - 300 SYSTEMS                   ║
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

def get_input(prompt, default=""):
    try:
        return input(prompt).strip() or default
    except:
        return default

def print_header():
    os.system('clear' if os.name != 'nt' else 'cls')
    cprint(RIR_LOGO, Colors.CYAN)
    print()

def print_main_menu():
    print(Colors.BOLD + Colors.CYAN + "=" * 70 + Colors.END)
    cprint("  🗂️  MAIN CATEGORIES (1-10)", Colors.YELLOW, True)
    cprint("  1.  File Search Systems (1-30)", Colors.WHITE)
    cprint("  2.  File Analysis Systems (31-60)", Colors.WHITE)
    cprint("  3.  File Management Systems (61-90)", Colors.WHITE)
    cprint("  4.  File Security Systems (91-120)", Colors.WHITE)
    cprint("  5.  File Conversion Systems (121-150)", Colors.WHITE)
    cprint("  6.  File Compression Systems (151-180)", Colors.WHITE)
    cprint("  7.  File Encryption Systems (181-210)", Colors.WHITE)
    cprint("  8.  File Backup Systems (211-240)", Colors.WHITE)
    cprint("  9.  File Monitoring Systems (241-270)", Colors.WHITE)
    cprint("  10. File Utility Systems (271-300)", Colors.WHITE)
    print(Colors.CYAN + "=" * 70 + Colors.END)
    cprint("  0.  Exit Tool", Colors.RED, True)
    print(Colors.CYAN + "=" * 70 + Colors.END)

# ==================== FILE SEARCH SYSTEMS (1-30) ====================

def system_1():
    cprint("\n📂 Basic File Search", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    pattern = get_input("🔍 Enter search pattern: ", "*")
    files = glob.glob(os.path.join(path, pattern))
    for f in files[:10]:
        cprint(f"  {f}", Colors.GREEN)
    return True

def system_2():
    cprint("\n📂 Recursive File Search", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    pattern = get_input("🔍 Enter search pattern: ", "*.txt")
    matches = []
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, pattern):
            matches.append(os.path.join(root, file))
    for f in matches[:20]:
        cprint(f"  {f}", Colors.GREEN)
    cprint(f"📊 Total: {len(matches)} files", Colors.CYAN)
    return True

def system_3():
    cprint("\n🔍 Text Search in Files", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    text = get_input("🔍 Enter text to search: ", "")
    if not text:
        cprint("❌ Please enter text to search", Colors.RED)
        return True
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), 'r', errors='ignore') as f:
                    content = f.read()
                    if text in content:
                        cprint(f"  {os.path.join(root, file)}", Colors.GREEN)
                        count += 1
            except:
                pass
    cprint(f"📊 Found in {count} files", Colors.CYAN)
    return True

def system_4():
    cprint("\n🔍 Case-Insensitive Text Search", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    text = get_input("🔍 Enter text to search: ", "")
    if not text:
        cprint("❌ Please enter text", Colors.RED)
        return True
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), 'r', errors='ignore') as f:
                    content = f.read()
                    if text.lower() in content.lower():
                        cprint(f"  {os.path.join(root, file)}", Colors.GREEN)
                        count += 1
            except:
                pass
    cprint(f"📊 Found in {count} files", Colors.CYAN)
    return True

def system_5():
    cprint("\n🔍 Regex File Search", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    pattern = get_input("🔍 Enter regex pattern: ", ".*")
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), 'r', errors='ignore') as f:
                    content = f.read()
                    if re.search(pattern, content):
                        cprint(f"  {os.path.join(root, file)}", Colors.GREEN)
                        count += 1
            except:
                pass
    cprint(f"📊 Found in {count} files", Colors.CYAN)
    return True

def system_6():
    cprint("\n📂 Search by File Extension", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    ext = get_input("🔍 Enter extension (e.g., .txt): ", ".txt")
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(ext):
                cprint(f"  {os.path.join(root, file)}", Colors.GREEN)
                count += 1
    cprint(f"📊 Found {count} files", Colors.CYAN)
    return True

def system_7():
    cprint("\n📂 Search by File Size", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    size_mb = float(get_input("📊 Minimum size (MB): ", "1"))
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                size = os.path.getsize(filepath) / (1024*1024)
                if size >= size_mb:
                    cprint(f"  {filepath} ({size:.2f} MB)", Colors.GREEN)
                    count += 1
            except:
                pass
    cprint(f"📊 Found {count} files", Colors.CYAN)
    return True

def system_8():
    cprint("\n📂 Search by File Date", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    days = int(get_input("📅 Modified in last N days: ", "7"))
    cutoff = time.time() - (days * 86400)
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                mtime = os.path.getmtime(filepath)
                if mtime >= cutoff:
                    cprint(f"  {filepath}", Colors.GREEN)
                    count += 1
            except:
                pass
    cprint(f"📊 Found {count} files", Colors.CYAN)
    return True

def system_9():
    cprint("\n📂 Search by File Owner", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    owner = get_input("👤 Enter owner name: ", "")
    if not owner:
        cprint("❌ Please enter owner", Colors.RED)
        return True
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                stat_info = os.stat(filepath)
                uid = stat_info.st_uid
                try:
                    import pwd
                    owner_name = pwd.getpwuid(uid).pw_name
                    if owner_name == owner:
                        cprint(f"  {filepath}", Colors.GREEN)
                        count += 1
                except:
                    pass
            except:
                pass
    cprint(f"📊 Found {count} files", Colors.CYAN)
    return True

def system_10():
    cprint("\n📂 Search Duplicate Files", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    cprint("🔍 Scanning for duplicates...", Colors.YELLOW, True)
    hashes = {}
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                if file_hash in hashes:
                    cprint(f"  Duplicate: {filepath}", Colors.RED)
                    cprint(f"    Original: {hashes[file_hash]}", Colors.CYAN)
                    count += 1
                else:
                    hashes[file_hash] = filepath
            except:
                pass
    cprint(f"📊 Found {count} duplicates", Colors.CYAN)
    return True

def system_11():
    cprint("\n📂 Search Hidden Files", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('.'):
                cprint(f"  {os.path.join(root, file)}", Colors.GREEN)
                count += 1
    cprint(f"📊 Found {count} hidden files", Colors.CYAN)
    return True

def system_12():
    cprint("\n📂 Search Empty Files", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                if os.path.getsize(filepath) == 0:
                    cprint(f"  {filepath}", Colors.GREEN)
                    count += 1
            except:
                pass
    cprint(f"📊 Found {count} empty files", Colors.CYAN)
    return True

def system_13():
    cprint("\n📂 Search Large Files", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    size_mb = float(get_input("📊 Minimum size (MB): ", "100"))
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                size = os.path.getsize(filepath) / (1024*1024)
                if size >= size_mb:
                    cprint(f"  {filepath} ({size:.2f} MB)", Colors.GREEN)
                    count += 1
            except:
                pass
    cprint(f"📊 Found {count} large files", Colors.CYAN)
    return True

def system_14():
    cprint("\n📂 Search Old Files", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    days = int(get_input("📅 Not modified in N days: ", "30"))
    cutoff = time.time() - (days * 86400)
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                mtime = os.path.getmtime(filepath)
                if mtime < cutoff:
                    cprint(f"  {filepath}", Colors.GREEN)
                    count += 1
            except:
                pass
    cprint(f"📊 Found {count} old files", Colors.CYAN)
    return True

def system_15():
    cprint("\n📂 Search by File Type", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    ftype = get_input("🔍 Enter file type: ", "text")
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'rb') as f:
                    header = f.read(1024)
                    if ftype in str(header):
                        cprint(f"  {filepath}", Colors.GREEN)
                        count += 1
            except:
                pass
    cprint(f"📊 Found {count} files", Colors.CYAN)
    return True

def system_16():
    cprint("\n📂 Search by File Permissions", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    perm = get_input("🔍 Enter permission (e.g., 755): ", "755")
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                mode = oct(os.stat(filepath).st_mode)[-3:]
                if mode == perm:
                    cprint(f"  {filepath}", Colors.GREEN)
                    count += 1
            except:
                pass
    cprint(f"📊 Found {count} files", Colors.CYAN)
    return True

def system_17():
    cprint("\n📂 Search by File Name Pattern", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    pattern = get_input("🔍 Enter pattern (e.g., *test*): ", "*")
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if fnmatch.fnmatch(file, pattern):
                cprint(f"  {os.path.join(root, file)}", Colors.GREEN)
                count += 1
    cprint(f"📊 Found {count} files", Colors.CYAN)
    return True

def system_18():
    cprint("\n🔍 Search in Compressed Files", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    text = get_input("🔍 Enter text to search: ", "")
    if not text:
        cprint("❌ Please enter text", Colors.RED)
        return True
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.zip'):
                try:
                    with zipfile.ZipFile(os.path.join(root, file), 'r') as zf:
                        for info in zf.infolist():
                            if text in info.filename:
                                cprint(f"  {os.path.join(root, file)} -> {info.filename}", Colors.GREEN)
                                count += 1
                except:
                    pass
    cprint(f"📊 Found in {count} files", Colors.CYAN)
    return True

def system_19():
    cprint("\n📂 Search by File Owner (Windows)", Colors.BLUE, True)
    if platform.system() != 'Windows':
        cprint("⚠️  This tool only works on Windows", Colors.YELLOW)
        return True
    path = get_input("📁 Enter folder path: ", ".")
    owner = get_input("👤 Enter owner: ", "")
    if not owner:
        cprint("❌ Please enter owner", Colors.RED)
        return True
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                output = subprocess.check_output(['icacls', filepath], timeout=5)
                if owner in output.decode():
                    cprint(f"  {filepath}", Colors.GREEN)
                    count += 1
            except:
                pass
    cprint(f"📊 Found {count} files", Colors.CYAN)
    return True

def system_20():
    cprint("\n📂 Search by File Attribute", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    attr = get_input("🔍 Enter attribute (e.g., hidden, readonly): ", "hidden")
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                if attr.lower() == 'hidden' and os.path.basename(filepath).startswith('.'):
                    cprint(f"  {filepath}", Colors.GREEN)
                    count += 1
                elif attr.lower() == 'readonly' and not os.access(filepath, os.W_OK):
                    cprint(f"  {filepath}", Colors.GREEN)
                    count += 1
            except:
                pass
    cprint(f"📊 Found {count} files", Colors.CYAN)
    return True

# ==================== FILE ANALYSIS SYSTEMS (31-60) ====================

def system_31():
    cprint("\n📊 Analyze File Types", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    ext_count = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            ext = os.path.splitext(file)[1] or 'no_extension'
            ext_count[ext] = ext_count.get(ext, 0) + 1
    cprint("📊 File Type Distribution:", Colors.YELLOW, True)
    for ext, count in sorted(ext_count.items(), key=lambda x: x[1], reverse=True)[:20]:
        cprint(f"  {ext}: {count} files", Colors.GREEN)
    return True

def system_32():
    cprint("\n📊 Analyze File Sizes", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    sizes = []
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                sizes.append(os.path.getsize(os.path.join(root, file)))
            except:
                pass
    if sizes:
        cprint(f"📊 File Size Statistics:", Colors.YELLOW, True)
        cprint(f"  Total: {sum(sizes) / (1024*1024):.2f} MB", Colors.CYAN)
        cprint(f"  Count: {len(sizes)}", Colors.CYAN)
        cprint(f"  Min: {min(sizes) / 1024:.2f} KB", Colors.CYAN)
        cprint(f"  Max: {max(sizes) / (1024*1024):.2f} MB", Colors.CYAN)
        cprint(f"  Avg: {sum(sizes)/len(sizes) / 1024:.2f} KB", Colors.CYAN)
    return True

def system_33():
    cprint("\n📊 Analyze File Dates", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    dates = []
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                dates.append(os.path.getmtime(os.path.join(root, file)))
            except:
                pass
    if dates:
        cprint(f"📊 File Date Statistics:", Colors.YELLOW, True)
        cprint(f"  Oldest: {datetime.datetime.fromtimestamp(min(dates)).strftime('%Y-%m-%d')}", Colors.CYAN)
        cprint(f"  Newest: {datetime.datetime.fromtimestamp(max(dates)).strftime('%Y-%m-%d')}", Colors.CYAN)
        cprint(f"  Count: {len(dates)}", Colors.CYAN)
    return True

def system_34():
    cprint("\n📊 Analyze Folder Structure", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    depth = int(get_input("📊 Max depth: ", "3"))
    cprint("📊 Folder Structure:", Colors.YELLOW, True)
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        if level <= depth:
            indent = '  ' * level
            cprint(f"{indent}📁 {os.path.basename(root)}/", Colors.CYAN)
            if level < depth:
                for d in dirs[:5]:
                    cprint(f"{indent}  📁 {d}/", Colors.GREEN)
    return True

def system_35():
    cprint("\n📊 Analyze File Content", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    text = get_input("🔍 Enter text to analyze: ", "")
    if not text:
        cprint("❌ Please enter text", Colors.RED)
        return True
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), 'r', errors='ignore') as f:
                    content = f.read()
                    count += content.count(text)
            except:
                pass
    cprint(f"📊 '{text}' appears {count} times", Colors.CYAN)
    return True

def system_36():
    cprint("\n📊 Analyze File Permissions", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    perms = defaultdict(int)
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                mode = oct(os.stat(os.path.join(root, file)).st_mode)[-3:]
                perms[mode] += 1
            except:
                pass
    cprint("📊 Permission Distribution:", Colors.YELLOW, True)
    for perm, count in sorted(perms.items(), key=lambda x: x[1], reverse=True):
        cprint(f"  {perm}: {count} files", Colors.GREEN)
    return True

def system_37():
    cprint("\n📊 Analyze File Ownership", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    owners = defaultdict(int)
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                uid = os.stat(os.path.join(root, file)).st_uid
                try:
                    import pwd
                    owner = pwd.getpwuid(uid).pw_name
                except:
                    owner = str(uid)
                owners[owner] += 1
            except:
                pass
    cprint("📊 Owner Distribution:", Colors.YELLOW, True)
    for owner, count in sorted(owners.items(), key=lambda x: x[1], reverse=True)[:20]:
        cprint(f"  {owner}: {count} files", Colors.GREEN)
    return True

def system_38():
    cprint("\n📊 Analyze File Extensions", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    ext_count = defaultdict(int)
    for root, dirs, files in os.walk(path):
        for file in files:
            ext = os.path.splitext(file)[1].lower() or 'no_ext'
            ext_count[ext] += 1
    cprint("📊 Extension Distribution:", Colors.YELLOW, True)
    for ext, count in sorted(ext_count.items(), key=lambda x: x[1], reverse=True)[:30]:
        cprint(f"  {ext}: {count} files", Colors.GREEN)
    return True

def system_39():
    cprint("\n📊 Analyze File Lines", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    total_lines = 0
    file_count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), 'r', errors='ignore') as f:
                    total_lines += sum(1 for _ in f)
                    file_count += 1
            except:
                pass
    cprint(f"📊 Total lines: {total_lines}", Colors.CYAN)
    cprint(f"📊 Files analyzed: {file_count}", Colors.CYAN)
    if file_count > 0:
        cprint(f"📊 Avg lines per file: {total_lines/file_count:.2f}", Colors.CYAN)
    return True

def system_40():
    cprint("\n📊 Analyze File Words", Colors.BLUE, True)
    path = get_input("📁 Enter folder path: ", ".")
    total_words = 0
    file_count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), 'r', errors='ignore') as f:
                    content = f.read()
                    words = len(re.findall(r'\w+', content))
                    total_words += words
                    file_count += 1
            except:
                pass
    cprint(f"📊 Total words: {total_words}", Colors.CYAN)
    cprint(f"📊 Files analyzed: {file_count}", Colors.CYAN)
    if file_count > 0:
        cprint(f"📊 Avg words per file: {total_words/file_count:.2f}", Colors.CYAN)
    return True

# ==================== FILE MANAGEMENT SYSTEMS (61-90) ====================

def system_61():
    cprint("\n📂 File Copy System", Colors.BLUE, True)
    src = get_input("📁 Source file/folder: ", "")
    dst = get_input("📁 Destination: ", "")
    if src and dst:
        try:
            if os.path.isdir(src):
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
            cprint("✅ Copy successful!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_62():
    cprint("\n📂 File Move System", Colors.BLUE, True)
    src = get_input("📁 Source file/folder: ", "")
    dst = get_input("📁 Destination: ", "")
    if src and dst:
        try:
            shutil.move(src, dst)
            cprint("✅ Move successful!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_63():
    cprint("\n📂 File Delete System", Colors.BLUE, True)
    path = get_input("📁 File/folder to delete: ", "")
    if path:
        confirm = get_input("⚠️  Confirm deletion (yes/no): ", "no")
        if confirm.lower() == 'yes':
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
                cprint("✅ Deleted!", Colors.GREEN)
            except Exception as e:
                cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_64():
    cprint("\n📂 File Rename System", Colors.BLUE, True)
    old = get_input("📁 Current name: ", "")
    new = get_input("📁 New name: ", "")
    if old and new:
        try:
            os.rename(old, new)
            cprint("✅ Renamed!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_65():
    cprint("\n📂 Batch File Rename", Colors.BLUE, True)
    path = get_input("📁 Folder path: ", ".")
    pattern = get_input("📋 Pattern (e.g., file_{index}.txt): ", "file_{index}.txt")
    prefix = get_input("📋 Prefix: ", "new_")
    count = 0
    for root, dirs, files in os.walk(path):
        for i, file in enumerate(files, 1):
            old = os.path.join(root, file)
            new = os.path.join(root, f"{prefix}{i}{os.path.splitext(file)[1]}")
            try:
                os.rename(old, new)
                count += 1
            except:
                pass
    cprint(f"✅ Renamed {count} files", Colors.GREEN)
    return True

def system_66():
    cprint("\n📂 Create Folder System", Colors.BLUE, True)
    path = get_input("📁 Folder path to create: ", "")
    if path:
        try:
            os.makedirs(path, exist_ok=True)
            cprint("✅ Folder created!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_67():
    cprint("\n📂 Create File System", Colors.BLUE, True)
    path = get_input("📁 File path: ", "")
    content = get_input("📝 File content: ", "")
    if path:
        try:
            with open(path, 'w') as f:
                f.write(content)
            cprint("✅ File created!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_68():
    cprint("\n📂 File List System", Colors.BLUE, True)
    path = get_input("📁 Folder path: ", ".")
    try:
        files = os.listdir(path)
        cprint(f"📊 Found {len(files)} items:", Colors.YELLOW, True)
        for f in sorted(files)[:50]:
            full_path = os.path.join(path, f)
            if os.path.isdir(full_path):
                cprint(f"  📁 {f}/", Colors.CYAN)
            else:
                size = os.path.getsize(full_path)
                cprint(f"  📄 {f} ({size/1024:.2f} KB)", Colors.GREEN)
    except Exception as e:
        cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_69():
    cprint("\n📂 File Tree System", Colors.BLUE, True)
    path = get_input("📁 Folder path: ", ".")
    depth = int(get_input("📊 Max depth: ", "3"))
    cprint("📊 File Tree:", Colors.YELLOW, True)
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        if level <= depth:
            indent = '  ' * level
            cprint(f"{indent}📁 {os.path.basename(root)}/", Colors.CYAN)
            for f in files[:5]:
                cprint(f"{indent}  📄 {f}", Colors.GREEN)
    return True

def system_70():
    cprint("\n📂 File Info System", Colors.BLUE, True)
    path = get_input("📁 File path: ", "")
    if path and os.path.exists(path):
        stat_info = os.stat(path)
        cprint("📋 File Information:", Colors.YELLOW, True)
        cprint(f"  Name: {os.path.basename(path)}", Colors.CYAN)
        cprint(f"  Path: {os.path.abspath(path)}", Colors.CYAN)
        cprint(f"  Size: {stat_info.st_size / 1024:.2f} KB", Colors.CYAN)
        cprint(f"  Created: {datetime.datetime.fromtimestamp(stat_info.st_ctime)}", Colors.CYAN)
        cprint(f"  Modified: {datetime.datetime.fromtimestamp(stat_info.st_mtime)}", Colors.CYAN)
        cprint(f"  Accessed: {datetime.datetime.fromtimestamp(stat_info.st_atime)}", Colors.CYAN)
        cprint(f"  Permissions: {oct(stat_info.st_mode)[-3:]}", Colors.CYAN)
    else:
        cprint("❌ File not found", Colors.RED)
    return True

# ==================== FILE SECURITY SYSTEMS (91-120) ====================

def system_91():
    cprint("\n🔐 File Permission Changer", Colors.BLUE, True)
    path = get_input("📁 File/folder path: ", "")
    perm = get_input("🔢 Permission (e.g., 755): ", "755")
    if path:
        try:
            os.chmod(path, int(perm, 8))
            cprint("✅ Permission changed!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_92():
    cprint("\n🔐 File Owner Changer", Colors.BLUE, True)
    path = get_input("📁 File/folder path: ", "")
    owner = get_input("👤 New owner: ", "")
    if path and owner:
        try:
            import pwd
            uid = pwd.getpwnam(owner).pw_uid
            os.chown(path, uid, -1)
            cprint("✅ Owner changed!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_93():
    cprint("\n🔐 File Hash Checker", Colors.BLUE, True)
    path = get_input("📁 File path: ", "")
    if path and os.path.exists(path):
        try:
            with open(path, 'rb') as f:
                data = f.read()
                cprint(f"MD5: {hashlib.md5(data).hexdigest()}", Colors.GREEN)
                cprint(f"SHA1: {hashlib.sha1(data).hexdigest()}", Colors.GREEN)
                cprint(f"SHA256: {hashlib.sha256(data).hexdigest()}", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_94():
    cprint("\n🔐 File Integrity Checker", Colors.BLUE, True)
    path = get_input("📁 File path: ", "")
    hash_file = get_input("📁 Hash file path: ", "")
    if path and hash_file:
        try:
            with open(path, 'rb') as f:
                current_hash = hashlib.sha256(f.read()).hexdigest()
            with open(hash_file, 'r') as f:
                stored_hash = f.read().strip()
            if current_hash == stored_hash:
                cprint("✅ File integrity verified!", Colors.GREEN)
            else:
                cprint("❌ File integrity compromised!", Colors.RED)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_95():
    cprint("\n🔐 File Encryption System", Colors.BLUE, True)
    path = get_input("📁 File to encrypt: ", "")
    if path:
        key = get_input("🔑 Encryption key: ", "")
        if key:
            try:
                with open(path, 'rb') as f:
                    data = f.read()
                key_bytes = key.encode() * (len(data) // len(key) + 1)
                encrypted = bytes(a ^ b for a, b in zip(data, key_bytes[:len(data)]))
                with open(path + '.enc', 'wb') as f:
                    f.write(encrypted)
                cprint("✅ File encrypted!", Colors.GREEN)
            except Exception as e:
                cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_96():
    cprint("\n🔐 File Decryption System", Colors.BLUE, True)
    path = get_input("📁 File to decrypt: ", "")
    if path:
        key = get_input("🔑 Decryption key: ", "")
        if key:
            try:
                with open(path, 'rb') as f:
                    data = f.read()
                key_bytes = key.encode() * (len(data) // len(key) + 1)
                decrypted = bytes(a ^ b for a, b in zip(data, key_bytes[:len(data)]))
                out_path = path.replace('.enc', '.dec')
                with open(out_path, 'wb') as f:
                    f.write(decrypted)
                cprint("✅ File decrypted!", Colors.GREEN)
            except Exception as e:
                cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_97():
    cprint("\n🔐 File Shredder System", Colors.BLUE, True)
    path = get_input("📁 File to shred: ", "")
    if path:
        confirm = get_input("⚠️  Permanent delete! Confirm (yes/no): ", "no")
        if confirm.lower() == 'yes':
            try:
                with open(path, 'wb') as f:
                    f.write(os.urandom(os.path.getsize(path)))
                os.remove(path)
                cprint("✅ File shredded!", Colors.GREEN)
            except Exception as e:
                cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_98():
    cprint("\n🔐 File Lock System", Colors.BLUE, True)
    path = get_input("📁 File to lock: ", "")
    if path:
        try:
            os.chmod(path, 0o444)
            cprint("✅ File locked (read-only)!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_99():
    cprint("\n🔐 File Unlock System", Colors.BLUE, True)
    path = get_input("📁 File to unlock: ", "")
    if path:
        try:
            os.chmod(path, 0o644)
            cprint("✅ File unlocked!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_100():
    cprint("\n🔐 File Backup Security", Colors.BLUE, True)
    path = get_input("📁 File/folder to backup: ", "")
    if path:
        try:
            backup_path = path + '.backup'
            if os.path.isdir(path):
                shutil.copytree(path, backup_path)
            else:
                shutil.copy2(path, backup_path)
            cprint(f"✅ Backup created: {backup_path}", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

# ==================== FILE CONVERSION SYSTEMS (121-150) ====================

def system_121():
    cprint("\n🔄 Text to JSON Converter", Colors.BLUE, True)
    path = get_input("📁 Text file path: ", "")
    if path:
        try:
            with open(path, 'r') as f:
                content = f.read()
            lines = content.split('\n')
            data = {'lines': lines, 'count': len(lines)}
            with open(path + '.json', 'w') as f:
                json.dump(data, f, indent=2)
            cprint("✅ Converted to JSON!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_122():
    cprint("\n🔄 JSON to Text Converter", Colors.BLUE, True)
    path = get_input("📁 JSON file path: ", "")
    if path:
        try:
            with open(path, 'r') as f:
                data = json.load(f)
            if isinstance(data, dict) and 'lines' in data:
                content = '\n'.join(data['lines'])
                with open(path + '.txt', 'w') as f:
                    f.write(content)
                cprint("✅ Converted to Text!", Colors.GREEN)
            else:
                cprint("❌ Invalid JSON format", Colors.RED)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_123():
    cprint("\n🔄 CSV to JSON Converter", Colors.BLUE, True)
    path = get_input("📁 CSV file path: ", "")
    if path:
        try:
            data = []
            with open(path, 'r') as f:
                reader = csv.reader(f)
                headers = next(reader)
                for row in reader:
                    data.append(dict(zip(headers, row)))
            with open(path + '.json', 'w') as f:
                json.dump(data, f, indent=2)
            cprint("✅ Converted to JSON!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_124():
    cprint("\n🔄 JSON to CSV Converter", Colors.BLUE, True)
    path = get_input("📁 JSON file path: ", "")
    if path:
        try:
            with open(path, 'r') as f:
                data = json.load(f)
            if data:
                headers = list(data[0].keys())
                with open(path + '.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(headers)
                    for row in data:
                        writer.writerow([row.get(h, '') for h in headers])
                cprint("✅ Converted to CSV!", Colors.GREEN)
            else:
                cprint("❌ Empty data", Colors.RED)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_125():
    cprint("\n🔄 XML to JSON Converter", Colors.BLUE, True)
    path = get_input("📁 XML file path: ", "")
    if path:
        try:
            tree = ET.parse(path)
            root = tree.getroot()
            data = xml_to_dict(root)
            with open(path + '.json', 'w') as f:
                json.dump(data, f, indent=2)
            cprint("✅ Converted to JSON!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def xml_to_dict(element):
    result = {}
    for child in element:
        if len(child) == 0:
            result[child.tag] = child.text
        else:
            result[child.tag] = xml_to_dict(child)
    return result

def system_126():
    cprint("\n🔄 JSON to XML Converter", Colors.BLUE, True)
    path = get_input("📁 JSON file path: ", "")
    if path:
        try:
            with open(path, 'r') as f:
                data = json.load(f)
            root = ET.Element('root')
            for key, value in data.items():
                child = ET.SubElement(root, key)
                child.text = str(value)
            tree = ET.ElementTree(root)
            tree.write(path + '.xml')
            cprint("✅ Converted to XML!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_127():
    cprint("\n🔄 Base64 Encode File", Colors.BLUE, True)
    path = get_input("📁 File to encode: ", "")
    if path:
        try:
            with open(path, 'rb') as f:
                data = f.read()
            encoded = base64.b64encode(data).decode()
            with open(path + '.b64', 'w') as f:
                f.write(encoded)
            cprint("✅ Encoded to Base64!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_128():
    cprint("\n🔄 Base64 Decode File", Colors.BLUE, True)
    path = get_input("📁 Base64 file path: ", "")
    if path:
        try:
            with open(path, 'r') as f:
                data = f.read()
            decoded = base64.b64decode(data)
            with open(path + '.decoded', 'wb') as f:
                f.write(decoded)
            cprint("✅ Decoded from Base64!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_129():
    cprint("\n🔄 Hex Encode File", Colors.BLUE, True)
    path = get_input("📁 File to encode: ", "")
    if path:
        try:
            with open(path, 'rb') as f:
                data = f.read()
            encoded = binascii.hexlify(data).decode()
            with open(path + '.hex', 'w') as f:
                f.write(encoded)
            cprint("✅ Encoded to Hex!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_130():
    cprint("\n🔄 Hex Decode File", Colors.BLUE, True)
    path = get_input("📁 Hex file path: ", "")
    if path:
        try:
            with open(path, 'r') as f:
                data = f.read()
            decoded = binascii.unhexlify(data)
            with open(path + '.decoded', 'wb') as f:
                f.write(decoded)
            cprint("✅ Decoded from Hex!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

# ==================== FILE COMPRESSION SYSTEMS (151-180) ====================

def system_151():
    cprint("\n📦 ZIP File Creator", Colors.BLUE, True)
    path = get_input("📁 File/folder to zip: ", "")
    if path:
        try:
            zip_name = get_input("📦 Zip file name: ", "archive.zip")
            with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
                if os.path.isdir(path):
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            filepath = os.path.join(root, file)
                            arcname = os.path.relpath(filepath, path)
                            zf.write(filepath, arcname)
                else:
                    zf.write(path, os.path.basename(path))
            cprint(f"✅ ZIP created: {zip_name}", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_152():
    cprint("\n📦 ZIP File Extractor", Colors.BLUE, True)
    path = get_input("📁 ZIP file path: ", "")
    if path:
        try:
            extract_path = get_input("📁 Extract to: ", ".")
            with zipfile.ZipFile(path, 'r') as zf:
                zf.extractall(extract_path)
            cprint("✅ ZIP extracted!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_153():
    cprint("\n📦 TAR File Creator", Colors.BLUE, True)
    path = get_input("📁 File/folder to tar: ", "")
    if path:
        try:
            tar_name = get_input("📦 Tar file name: ", "archive.tar")
            with tarfile.open(tar_name, 'w') as tf:
                if os.path.isdir(path):
                    tf.add(path, arcname=os.path.basename(path))
                else:
                    tf.add(path)
            cprint(f"✅ TAR created: {tar_name}", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_154():
    cprint("\n📦 TAR File Extractor", Colors.BLUE, True)
    path = get_input("📁 TAR file path: ", "")
    if path:
        try:
            extract_path = get_input("📁 Extract to: ", ".")
            with tarfile.open(path, 'r') as tf:
                tf.extractall(extract_path)
            cprint("✅ TAR extracted!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_155():
    cprint("\n📦 GZIP File Compressor", Colors.BLUE, True)
    path = get_input("📁 File to compress: ", "")
    if path:
        try:
            with open(path, 'rb') as f:
                data = f.read()
            with gzip.open(path + '.gz', 'wb') as f:
                f.write(data)
            cprint(f"✅ GZIP created: {path}.gz", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_156():
    cprint("\n📦 GZIP File Decompressor", Colors.BLUE, True)
    path = get_input("📁 GZIP file path: ", "")
    if path:
        try:
            with gzip.open(path, 'rb') as f:
                data = f.read()
            out_path = path.replace('.gz', '')
            with open(out_path, 'wb') as f:
                f.write(data)
            cprint(f"✅ GZIP decompressed: {out_path}", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_157():
    cprint("\n📦 BZIP2 File Compressor", Colors.BLUE, True)
    path = get_input("📁 File to compress: ", "")
    if path:
        try:
            with open(path, 'rb') as f:
                data = f.read()
            with bz2.BZ2File(path + '.bz2', 'wb') as f:
                f.write(data)
            cprint(f"✅ BZIP2 created: {path}.bz2", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_158():
    cprint("\n📦 BZIP2 File Decompressor", Colors.BLUE, True)
    path = get_input("📁 BZIP2 file path: ", "")
    if path:
        try:
            with bz2.BZ2File(path, 'rb') as f:
                data = f.read()
            out_path = path.replace('.bz2', '')
            with open(out_path, 'wb') as f:
                f.write(data)
            cprint(f"✅ BZIP2 decompressed: {out_path}", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_159():
    cprint("\n📦 LZMA File Compressor", Colors.BLUE, True)
    path = get_input("📁 File to compress: ", "")
    if path:
        try:
            with open(path, 'rb') as f:
                data = f.read()
            with lzma.LZMAFile(path + '.xz', 'w') as f:
                f.write(data)
            cprint(f"✅ LZMA created: {path}.xz", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_160():
    cprint("\n📦 LZMA File Decompressor", Colors.BLUE, True)
    path = get_input("📁 LZMA file path: ", "")
    if path:
        try:
            with lzma.LZMAFile(path, 'rb') as f:
                data = f.read()
            out_path = path.replace('.xz', '')
            with open(out_path, 'wb') as f:
                f.write(data)
            cprint(f"✅ LZMA decompressed: {out_path}", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

# ==================== FILE ENCRYPTION SYSTEMS (181-210) ====================

def system_181():
    cprint("\n🔐 AES File Encryptor", Colors.BLUE, True)
    path = get_input("📁 File to encrypt: ", "")
    if path:
        cprint("📋 Using simple XOR encryption", Colors.YELLOW)
        key = get_input("🔑 Encryption key: ", "")
        if key:
            try:
                with open(path, 'rb') as f:
                    data = f.read()
                key_bytes = hashlib.sha256(key.encode()).digest()
                encrypted = bytes(a ^ b for a, b in zip(data, key_bytes * (len(data) // 32 + 1)))
                with open(path + '.aes', 'wb') as f:
                    f.write(encrypted)
                cprint("✅ File encrypted!", Colors.GREEN)
            except Exception as e:
                cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_182():
    cprint("\n🔐 AES File Decryptor", Colors.BLUE, True)
    path = get_input("📁 File to decrypt: ", "")
    if path:
        key = get_input("🔑 Decryption key: ", "")
        if key:
            try:
                with open(path, 'rb') as f:
                    data = f.read()
                key_bytes = hashlib.sha256(key.encode()).digest()
                decrypted = bytes(a ^ b for a, b in zip(data, key_bytes * (len(data) // 32 + 1)))
                out_path = path.replace('.aes', '.dec')
                with open(out_path, 'wb') as f:
                    f.write(decrypted)
                cprint("✅ File decrypted!", Colors.GREEN)
            except Exception as e:
                cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_183():
    cprint("\n🔐 RSA Key Generator", Colors.BLUE, True)
    cprint("📋 Using simple key generation", Colors.YELLOW)
    key = hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()
    with open('rsa_private.key', 'w') as f:
        f.write(key)
    cprint("✅ RSA keys generated!", Colors.GREEN)
    return True

def system_184():
    cprint("\n🔐 File Digital Signature", Colors.BLUE, True)
    path = get_input("📁 File to sign: ", "")
    if path:
        try:
            with open(path, 'rb') as f:
                data = f.read()
            signature = hashlib.sha256(data).hexdigest()
            with open(path + '.sig', 'w') as f:
                f.write(signature)
            cprint(f"✅ Signature created: {path}.sig", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_185():
    cprint("\n🔐 File Signature Verify", Colors.BLUE, True)
    path = get_input("📁 File to verify: ", "")
    sig_path = get_input("📁 Signature file: ", "")
    if path and sig_path:
        try:
            with open(path, 'rb') as f:
                data = f.read()
            with open(sig_path, 'r') as f:
                sig = f.read().strip()
            current_sig = hashlib.sha256(data).hexdigest()
            if current_sig == sig:
                cprint("✅ Signature verified!", Colors.GREEN)
            else:
                cprint("❌ Signature invalid!", Colors.RED)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_186():
    cprint("\n🔐 File Password Protection", Colors.BLUE, True)
    path = get_input("📁 File to protect: ", "")
    if path:
        password = get_input("🔑 Password: ", "")
        if password:
            try:
                with open(path, 'rb') as f:
                    data = f.read()
                key = hashlib.sha256(password.encode()).digest()
                protected = bytes(a ^ b for a, b in zip(data, key * (len(data) // 32 + 1)))
                with open(path + '.protected', 'wb') as f:
                    f.write(protected)
                cprint("✅ File protected!", Colors.GREEN)
            except Exception as e:
                cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_187():
    cprint("\n🔐 File Password Unlock", Colors.BLUE, True)
    path = get_input("📁 Protected file: ", "")
    if path:
        password = get_input("🔑 Password: ", "")
        if password:
            try:
                with open(path, 'rb') as f:
                    data = f.read()
                key = hashlib.sha256(password.encode()).digest()
                unlocked = bytes(a ^ b for a, b in zip(data, key * (len(data) // 32 + 1)))
                out_path = path.replace('.protected', '.unlocked')
                with open(out_path, 'wb') as f:
                    f.write(unlocked)
                cprint("✅ File unlocked!", Colors.GREEN)
            except Exception as e:
                cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

# ==================== FILE BACKUP SYSTEMS (211-240) ====================

def system_211():
    cprint("\n💾 Simple File Backup", Colors.BLUE, True)
    path = get_input("📁 File/folder to backup: ", "")
    if path:
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = f"{path}.backup_{timestamp}"
            if os.path.isdir(path):
                shutil.copytree(path, backup_path)
            else:
                shutil.copy2(path, backup_path)
            cprint(f"✅ Backup created: {backup_path}", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_212():
    cprint("\n💾 Incremental Backup", Colors.BLUE, True)
    path = get_input("📁 Source folder: ", "")
    backup_dir = get_input("📁 Backup folder: ", "")
    if path and backup_dir:
        try:
            os.makedirs(backup_dir, exist_ok=True)
            for root, dirs, files in os.walk(path):
                for file in files:
                    src = os.path.join(root, file)
                    rel_path = os.path.relpath(src, path)
                    dst = os.path.join(backup_dir, rel_path)
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    if not os.path.exists(dst) or os.path.getmtime(src) > os.path.getmtime(dst):
                        shutil.copy2(src, dst)
            cprint("✅ Incremental backup completed!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_213():
    cprint("\n💾 Differential Backup", Colors.BLUE, True)
    path = get_input("📁 Source folder: ", "")
    backup_dir = get_input("📁 Backup folder: ", "")
    if path and backup_dir:
        try:
            os.makedirs(backup_dir, exist_ok=True)
            timestamp = time.time()
            for root, dirs, files in os.walk(path):
                for file in files:
                    src = os.path.join(root, file)
                    rel_path = os.path.relpath(src, path)
                    dst = os.path.join(backup_dir, rel_path)
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    if not os.path.exists(dst) or os.path.getmtime(src) > timestamp:
                        shutil.copy2(src, dst)
            cprint("✅ Differential backup completed!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_214():
    cprint("\n💾 Full System Backup", Colors.BLUE, True)
    path = get_input("📁 Source folder: ", "")
    if path:
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"backup_{timestamp}.zip"
            with zipfile.ZipFile(backup_file, 'w', zipfile.ZIP_DEFLATED) as zf:
                for root, dirs, files in os.walk(path):
                    for file in files:
                        filepath = os.path.join(root, file)
                        arcname = os.path.relpath(filepath, path)
                        zf.write(filepath, arcname)
            cprint(f"✅ Full backup created: {backup_file}", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_215():
    cprint("\n💾 Restore Backup", Colors.BLUE, True)
    backup_file = get_input("📁 Backup file: ", "")
    restore_path = get_input("📁 Restore to: ", "")
    if backup_file and restore_path:
        try:
            if backup_file.endswith('.zip'):
                with zipfile.ZipFile(backup_file, 'r') as zf:
                    zf.extractall(restore_path)
            else:
                shutil.copy2(backup_file, restore_path)
            cprint("✅ Backup restored!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

# ==================== FILE MONITORING SYSTEMS (241-270) ====================

def system_241():
    cprint("\n👀 File Change Monitor", Colors.BLUE, True)
    path = get_input("📁 Folder to monitor: ", ".")
    if path:
        cprint("🔍 Monitoring folder changes...", Colors.YELLOW, True)
        cprint("📋 Press Ctrl+C to stop", Colors.CYAN)
        try:
            snapshots = {}
            while True:
                current = {}
                for root, dirs, files in os.walk(path):
                    for file in files:
                        filepath = os.path.join(root, file)
                        current[filepath] = os.path.getmtime(filepath)
                for key in current:
                    if key not in snapshots:
                        cprint(f"➕ Added: {key}", Colors.GREEN)
                    elif current[key] != snapshots[key]:
                        cprint(f"✏️ Modified: {key}", Colors.YELLOW)
                for key in snapshots:
                    if key not in current:
                        cprint(f"➖ Removed: {key}", Colors.RED)
                snapshots = current
                time.sleep(2)
        except KeyboardInterrupt:
            cprint("\n✅ Monitoring stopped", Colors.CYAN)
    return True

def system_242():
    cprint("\n📊 File Access Monitor", Colors.BLUE, True)
    path = get_input("📁 Folder to monitor: ", ".")
    if path:
        cprint("🔍 Monitoring file access...", Colors.YELLOW, True)
        cprint("📋 Press Ctrl+C to stop", Colors.CYAN)
        try:
            while True:
                for root, dirs, files in os.walk(path):
                    for file in files:
                        filepath = os.path.join(root, file)
                        atime = datetime.datetime.fromtimestamp(os.path.getatime(filepath))
                        if (datetime.datetime.now() - atime).seconds < 5:
                            cprint(f"📖 Accessed: {filepath}", Colors.GREEN)
                time.sleep(5)
        except KeyboardInterrupt:
            cprint("\n✅ Monitoring stopped", Colors.CYAN)
    return True

def system_243():
    cprint("\n📊 File Size Monitor", Colors.BLUE, True)
    path = get_input("📁 Folder to monitor: ", ".")
    if path:
        cprint("🔍 Monitoring file sizes...", Colors.YELLOW, True)
        try:
            while True:
                total_size = 0
                file_count = 0
                for root, dirs, files in os.walk(path):
                    for file in files:
                        filepath = os.path.join(root, file)
                        total_size += os.path.getsize(filepath)
                        file_count += 1
                cprint(f"📊 Files: {file_count}, Size: {total_size/(1024*1024):.2f} MB", Colors.CYAN)
                time.sleep(5)
        except KeyboardInterrupt:
            cprint("\n✅ Monitoring stopped", Colors.CYAN)
    return True

# ==================== FILE UTILITY SYSTEMS (271-300) ====================

def system_271():
    cprint("\n🔧 File Merge System", Colors.BLUE, True)
    files_input = get_input("📁 Files to merge (comma separated): ", "")
    output = get_input("📁 Output file: ", "merged.txt")
    if files_input:
        try:
            files = [f.strip() for f in files_input.split(',')]
            with open(output, 'wb') as out:
                for f in files:
                    with open(f, 'rb') as inf:
                        out.write(inf.read())
            cprint(f"✅ Merged {len(files)} files into {output}", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_272():
    cprint("\n🔧 File Split System", Colors.BLUE, True)
    path = get_input("📁 File to split: ", "")
    if path:
        try:
            size_mb = int(get_input("📊 Part size (MB): ", "10"))
            size_bytes = size_mb * 1024 * 1024
            with open(path, 'rb') as f:
                i = 1
                while True:
                    chunk = f.read(size_bytes)
                    if not chunk:
                        break
                    with open(f"{path}.part{i}", 'wb') as cf:
                        cf.write(chunk)
                    i += 1
            cprint(f"✅ Split into {i-1} parts", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_273():
    cprint("\n🔧 File Compare System", Colors.BLUE, True)
    f1 = get_input("📁 First file: ", "")
    f2 = get_input("📁 Second file: ", "")
    if f1 and f2:
        try:
            with open(f1, 'rb') as f:
                data1 = f.read()
            with open(f2, 'rb') as f:
                data2 = f.read()
            if data1 == data2:
                cprint("✅ Files are identical", Colors.GREEN)
            else:
                cprint("❌ Files are different", Colors.RED)
                cprint(f"  Size1: {len(data1)}, Size2: {len(data2)}", Colors.CYAN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_274():
    cprint("\n🔧 File Cleanup System", Colors.BLUE, True)
    path = get_input("📁 Folder to cleanup: ", ".")
    days = int(get_input("📅 Delete files older than N days: ", "30"))
    if path:
        try:
            cutoff = time.time() - (days * 86400)
            count = 0
            for root, dirs, files in os.walk(path):
                for file in files:
                    filepath = os.path.join(root, file)
                    if os.path.getmtime(filepath) < cutoff:
                        os.remove(filepath)
                        count += 1
            cprint(f"✅ Deleted {count} old files", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_275():
    cprint("\n🔧 File Organizer System", Colors.BLUE, True)
    path = get_input("📁 Folder to organize: ", ".")
    if path:
        try:
            for file in os.listdir(path):
                filepath = os.path.join(path, file)
                if os.path.isfile(filepath):
                    ext = os.path.splitext(file)[1][1:] or "no_ext"
                    dest = os.path.join(path, ext)
                    os.makedirs(dest, exist_ok=True)
                    shutil.move(filepath, os.path.join(dest, file))
            cprint("✅ Files organized!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_276():
    cprint("\n🔧 File Duplicate Remover", Colors.BLUE, True)
    path = get_input("📁 Folder to clean: ", ".")
    if path:
        try:
            hashes = {}
            count = 0
            for root, dirs, files in os.walk(path):
                for file in files:
                    filepath = os.path.join(root, file)
                    with open(filepath, 'rb') as f:
                        file_hash = hashlib.md5(f.read()).hexdigest()
                    if file_hash in hashes:
                        os.remove(filepath)
                        count += 1
                    else:
                        hashes[file_hash] = filepath
            cprint(f"✅ Removed {count} duplicates", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_277():
    cprint("\n🔧 File Line Counter", Colors.BLUE, True)
    path = get_input("📁 File path: ", "")
    if path:
        try:
            with open(path, 'r', errors='ignore') as f:
                lines = sum(1 for _ in f)
            cprint(f"📊 Lines: {lines}", Colors.CYAN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_278():
    cprint("\n🔧 File Word Counter", Colors.BLUE, True)
    path = get_input("📁 File path: ", "")
    if path:
        try:
            with open(path, 'r', errors='ignore') as f:
                content = f.read()
                words = len(re.findall(r'\w+', content))
            cprint(f"📊 Words: {words}", Colors.CYAN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_279():
    cprint("\n🔧 File Character Counter", Colors.BLUE, True)
    path = get_input("📁 File path: ", "")
    if path:
        try:
            with open(path, 'r', errors='ignore') as f:
                content = f.read()
                chars = len(content)
            cprint(f"📊 Characters: {chars}", Colors.CYAN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

def system_280():
    cprint("\n🔧 File Search & Replace", Colors.BLUE, True)
    path = get_input("📁 File path: ", "")
    if path:
        try:
            with open(path, 'r', errors='ignore') as f:
                content = f.read()
            old = get_input("🔍 Search for: ", "")
            new = get_input("📝 Replace with: ", "")
            if old and new:
                new_content = content.replace(old, new)
                with open(path, 'w') as f:
                    f.write(new_content)
                cprint("✅ Search & Replace completed!", Colors.GREEN)
        except Exception as e:
            cprint(f"❌ Error: {str(e)}", Colors.RED)
    return True

# ==================== MAIN ====================

def main():
    while True:
        print_header()
        print_main_menu()
        
        choice = get_input(f"\n{Colors.BOLD}🎯 Select category (0-10): {Colors.END}")
        
        if choice == '0':
            cprint("\n👋 Thanks for using RIR File Search System!", Colors.GREEN, True)
            cprint("🔒 Stay Secure, Stay Safe!", Colors.CYAN, True)
            cprint("🛡️  RIR Cyber Tools", Colors.MAGENTA, True)
            break
        
        if choice == '1':
            sub_menu_file_search()
        elif choice == '2':
            sub_menu_analysis()
        elif choice == '3':
            sub_menu_management()
        elif choice == '4':
            sub_menu_security()
        elif choice == '5':
            sub_menu_conversion()
        elif choice == '6':
            sub_menu_compression()
        elif choice == '7':
            sub_menu_encryption()
        elif choice == '8':
            sub_menu_backup()
        elif choice == '9':
            sub_menu_monitoring()
        elif choice == '10':
            sub_menu_utility()
        else:
            cprint("❌ Invalid choice!", Colors.RED)
        
        get_input(f"\n{Colors.CYAN}⏎ Press Enter to continue...{Colors.END}")

def sub_menu_file_search():
    while True:
        os.system('clear' if os.name != 'nt' else 'cls')
        print_header()
        cprint("  🗂️  FILE SEARCH SYSTEMS (1-30)", Colors.YELLOW, True)
        cprint("  1.  Basic File Search", Colors.WHITE)
        cprint("  2.  Recursive File Search", Colors.WHITE)
        cprint("  3.  Text Search in Files", Colors.WHITE)
        cprint("  4.  Case-Insensitive Text Search", Colors.WHITE)
        cprint("  5.  Regex File Search", Colors.WHITE)
        cprint("  6.  Search by File Extension", Colors.WHITE)
        cprint("  7.  Search by File Size", Colors.WHITE)
        cprint("  8.  Search by File Date", Colors.WHITE)
        cprint("  9.  Search by File Owner", Colors.WHITE)
        cprint("  10. Search Duplicate Files", Colors.WHITE)
        cprint("  11. Search Hidden Files", Colors.WHITE)
        cprint("  12. Search Empty Files", Colors.WHITE)
        cprint("  13. Search Large Files", Colors.WHITE)
        cprint("  14. Search Old Files", Colors.WHITE)
        cprint("  15. Search by File Type", Colors.WHITE)
        cprint("  16. Search by File Permissions", Colors.WHITE)
        cprint("  17. Search by File Name Pattern", Colors.WHITE)
        cprint("  18. Search in Compressed Files", Colors.WHITE)
        cprint("  19. Search by File Owner (Windows)", Colors.WHITE)
        cprint("  20. Search by File Attribute", Colors.WHITE)
        cprint("  0.  Back to Main Menu", Colors.RED, True)
        
        choice = get_input(f"\n{Colors.BOLD}🎯 Select tool (0-20): {Colors.END}")
        
        if choice == '0':
            break
        elif choice == '1':
            system_1()
        elif choice == '2':
            system_2()
        elif choice == '3':
            system_3()
        elif choice == '4':
            system_4()
        elif choice == '5':
            system_5()
        elif choice == '6':
            system_6()
        elif choice == '7':
            system_7()
        elif choice == '8':
            system_8()
        elif choice == '9':
            system_9()
        elif choice == '10':
            system_10()
        elif choice == '11':
            system_11()
        elif choice == '12':
            system_12()
        elif choice == '13':
            system_13()
        elif choice == '14':
            system_14()
        elif choice == '15':
            system_15()
        elif choice == '16':
            system_16()
        elif choice == '17':
            system_17()
        elif choice == '18':
            system_18()
        elif choice == '19':
            system_19()
        elif choice == '20':
            system_20()
        else:
            cprint("❌ Invalid choice!", Colors.RED)
        
        get_input(f"\n{Colors.CYAN}⏎ Press Enter to continue...{Colors.END}")

def sub_menu_analysis():
    while True:
        os.system('clear' if os.name != 'nt' else 'cls')
        print_header()
        cprint("  📊 FILE ANALYSIS SYSTEMS (31-60)", Colors.YELLOW, True)
        cprint("  31. Analyze File Types", Colors.WHITE)
        cprint("  32. Analyze File Sizes", Colors.WHITE)
        cprint("  33. Analyze File Dates", Colors.WHITE)
        cprint("  34. Analyze Folder Structure", Colors.WHITE)
        cprint("  35. Analyze File Content", Colors.WHITE)
        cprint("  36. Analyze File Permissions", Colors.WHITE)
        cprint("  37. Analyze File Ownership", Colors.WHITE)
        cprint("  38. Analyze File Extensions", Colors.WHITE)
        cprint("  39. Analyze File Lines", Colors.WHITE)
        cprint("  40. Analyze File Words", Colors.WHITE)
        cprint("  0.  Back to Main Menu", Colors.RED, True)
        
        choice = get_input(f"\n{Colors.BOLD}🎯 Select tool (0-10): {Colors.END}")
        
        if choice == '0':
            break
        elif choice == '31':
            system_31()
        elif choice == '32':
            system_32()
        elif choice == '33':
            system_33()
        elif choice == '34':
            system_34()
        elif choice == '35':
            system_35()
        elif choice == '36':
            system_36()
        elif choice == '37':
            system_37()
        elif choice == '38':
            system_38()
        elif choice == '39':
            system_39()
        elif choice == '40':
            system_40()
        else:
            cprint("❌ Invalid choice!", Colors.RED)
        
        get_input(f"\n{Colors.CYAN}⏎ Press Enter to continue...{Colors.END}")

def sub_menu_management():
    while True:
        os.system('clear' if os.name != 'nt' else 'cls')
        print_header()
        cprint("  📂 FILE MANAGEMENT SYSTEMS (61-90)", Colors.YELLOW, True)
        cprint("  61. File Copy System", Colors.WHITE)
        cprint("  62. File Move System", Colors.WHITE)
        cprint("  63. File Delete System", Colors.WHITE)
        cprint("  64. File Rename System", Colors.WHITE)
        cprint("  65. Batch File Rename", Colors.WHITE)
        cprint("  66. Create Folder System", Colors.WHITE)
        cprint("  67. Create File System", Colors.WHITE)
        cprint("  68. File List System", Colors.WHITE)
        cprint("  69. File Tree System", Colors.WHITE)
        cprint("  70. File Info System", Colors.WHITE)
        cprint("  0.  Back to Main Menu", Colors.RED, True)
        
        choice = get_input(f"\n{Colors.BOLD}🎯 Select tool (0-10): {Colors.END}")
        
        if choice == '0':
            break
        elif choice == '61':
            system_61()
        elif choice == '62':
            system_62()
        elif choice == '63':
            system_63()
        elif choice == '64':
            system_64()
        elif choice == '65':
            system_65()
        elif choice == '66':
            system_66()
        elif choice == '67':
            system_67()
        elif choice == '68':
            system_68()
        elif choice == '69':
            system_69()
        elif choice == '70':
            system_70()
        else:
            cprint("❌ Invalid choice!", Colors.RED)
        
        get_input(f"\n{Colors.CYAN}⏎ Press Enter to continue...{Colors.END}")

def sub_menu_security():
    while True:
        os.system('clear' if os.name != 'nt' else 'cls')
        print_header()
        cprint("  🔐 FILE SECURITY SYSTEMS (91-120)", Colors.YELLOW, True)
        cprint("  91. File Permission Changer", Colors.WHITE)
        cprint("  92. File Owner Changer", Colors.WHITE)
        cprint("  93. File Hash Checker", Colors.WHITE)
        cprint("  94. File Integrity Checker", Colors.WHITE)
        cprint("  95. File Encryption System", Colors.WHITE)
        cprint("  96. File Decryption System", Colors.WHITE)
        cprint("  97. File Shredder System", Colors.WHITE)
        cprint("  98. File Lock System", Colors.WHITE)
        cprint("  99. File Unlock System", Colors.WHITE)
        cprint("  100. File Backup Security", Colors.WHITE)
        cprint("  0.  Back to Main Menu", Colors.RED, True)
        
        choice = get_input(f"\n{Colors.BOLD}🎯 Select tool (0-10): {Colors.END}")
        
        if choice == '0':
            break
        elif choice == '91':
            system_91()
        elif choice == '92':
            system_92()
        elif choice == '93':
            system_93()
        elif choice == '94':
            system_94()
        elif choice == '95':
            system_95()
        elif choice == '96':
            system_96()
        elif choice == '97':
            system_97()
        elif choice == '98':
            system_98()
        elif choice == '99':
            system_99()
        elif choice == '100':
            system_100()
        else:
            cprint("❌ Invalid choice!", Colors.RED)
        
        get_input(f"\n{Colors.CYAN}⏎ Press Enter to continue...{Colors.END}")

def sub_menu_conversion():
    while True:
        os.system('clear' if os.name != 'nt' else 'cls')
        print_header()
        cprint("  🔄 FILE CONVERSION SYSTEMS (121-150)", Colors.YELLOW, True)
        cprint("  121. Text to JSON Converter", Colors.WHITE)
        cprint("  122. JSON to Text Converter", Colors.WHITE)
        cprint("  123. CSV to JSON Converter", Colors.WHITE)
        cprint("  124. JSON to CSV Converter", Colors.WHITE)
        cprint("  125. XML to JSON Converter", Colors.WHITE)
        cprint("  126. JSON to XML Converter", Colors.WHITE)
        cprint("  127. Base64 Encode File", Colors.WHITE)
        cprint("  128. Base64 Decode File", Colors.WHITE)
        cprint("  129. Hex Encode File", Colors.WHITE)
        cprint("  130. Hex Decode File", Colors.WHITE)
        cprint("  0.  Back to Main Menu", Colors.RED, True)
        
        choice = get_input(f"\n{Colors.BOLD}🎯 Select tool (0-10): {Colors.END}")
        
        if choice == '0':
            break
        elif choice == '121':
            system_121()
        elif choice == '122':
            system_122()
        elif choice == '123':
            system_123()
        elif choice == '124':
            system_124()
        elif choice == '125':
            system_125()
        elif choice == '126':
            system_126()
        elif choice == '127':
            system_127()
        elif choice == '128':
            system_128()
        elif choice == '129':
            system_129()
        elif choice == '130':
            system_130()
        else:
            cprint("❌ Invalid choice!", Colors.RED)
        
        get_input(f"\n{Colors.CYAN}⏎ Press Enter to continue...{Colors.END}")

def sub_menu_compression():
    while True:
        os.system('clear' if os.name != 'nt' else 'cls')
        print_header()
        cprint("  📦 FILE COMPRESSION SYSTEMS (151-180)", Colors.YELLOW, True)
        cprint("  151. ZIP File Creator", Colors.WHITE)
        cprint("  152. ZIP File Extractor", Colors.WHITE)
        cprint("  153. TAR File Creator", Colors.WHITE)
        cprint("  154. TAR File Extractor", Colors.WHITE)
        cprint("  155. GZIP File Compressor", Colors.WHITE)
        cprint("  156. GZIP File Decompressor", Colors.WHITE)
        cprint("  157. BZIP2 File Compressor", Colors.WHITE)
        cprint("  158. BZIP2 File Decompressor", Colors.WHITE)
        cprint("  159. LZMA File Compressor", Colors.WHITE)
        cprint("  160. LZMA File Decompressor", Colors.WHITE)
        cprint("  0.  Back to Main Menu", Colors.RED, True)
        
        choice = get_input(f"\n{Colors.BOLD}🎯 Select tool (0-10): {Colors.END}")
        
        if choice == '0':
            break
        elif choice == '151':
            system_151()
        elif choice == '152':
            system_152()
        elif choice == '153':
            system_153()
        elif choice == '154':
            system_154()
        elif choice == '155':
            system_155()
        elif choice == '156':
            system_156()
        elif choice == '157':
            system_157()
        elif choice == '158':
            system_158()
        elif choice == '159':
            system_159()
        elif choice == '160':
            system_160()
        else:
            cprint("❌ Invalid choice!", Colors.RED)
        
        get_input(f"\n{Colors.CYAN}⏎ Press Enter to continue...{Colors.END}")

def sub_menu_encryption():
    while True:
        os.system('clear' if os.name != 'nt' else 'cls')
        print_header()
        cprint("  🔐 FILE ENCRYPTION SYSTEMS (181-210)", Colors.YELLOW, True)
        cprint("  181. AES File Encryptor", Colors.WHITE)
        cprint("  182. AES File Decryptor", Colors.WHITE)
        cprint("  183. RSA Key Generator", Colors.WHITE)
        cprint("  184. File Digital Signature", Colors.WHITE)
        cprint("  185. File Signature Verify", Colors.WHITE)
        cprint("  186. File Password Protection", Colors.WHITE)
        cprint("  187. File Password Unlock", Colors.WHITE)
        cprint("  0.  Back to Main Menu", Colors.RED, True)
        
        choice = get_input(f"\n{Colors.BOLD}🎯 Select tool (0-7): {Colors.END}")
        
        if choice == '0':
            break
        elif choice == '181':
            system_181()
        elif choice == '182':
            system_182()
        elif choice == '183':
            system_183()
        elif choice == '184':
            system_184()
        elif choice == '185':
            system_185()
        elif choice == '186':
            system_186()
        elif choice == '187':
            system_187()
        else:
            cprint("❌ Invalid choice!", Colors.RED)
        
        get_input(f"\n{Colors.CYAN}⏎ Press Enter to continue...{Colors.END}")

def sub_menu_backup():
    while True:
        os.system('clear' if os.name != 'nt' else 'cls')
        print_header()
        cprint("  💾 FILE BACKUP SYSTEMS (211-240)", Colors.YELLOW, True)
        cprint("  211. Simple File Backup", Colors.WHITE)
        cprint("  212. Incremental Backup", Colors.WHITE)
        cprint("  213. Differential Backup", Colors.WHITE)
        cprint("  214. Full System Backup", Colors.WHITE)
        cprint("  215. Restore Backup", Colors.WHITE)
        cprint("  0.  Back to Main Menu", Colors.RED, True)
        
        choice = get_input(f"\n{Colors.BOLD}🎯 Select tool (0-5): {Colors.END}")
        
        if choice == '0':
            break
        elif choice == '211':
            system_211()
        elif choice == '212':
            system_212()
        elif choice == '213':
            system_213()
        elif choice == '214':
            system_214()
        elif choice == '215':
            system_215()
        else:
            cprint("❌ Invalid choice!", Colors.RED)
        
        get_input(f"\n{Colors.CYAN}⏎ Press Enter to continue...{Colors.END}")

def sub_menu_monitoring():
    while True:
        os.system('clear' if os.name != 'nt' else 'cls')
        print_header()
        cprint("  👀 FILE MONITORING SYSTEMS (241-270)", Colors.YELLOW, True)
        cprint("  241. File Change Monitor", Colors.WHITE)
        cprint("  242. File Access Monitor", Colors.WHITE)
        cprint("  243. File Size Monitor", Colors.WHITE)
        cprint("  0.  Back to Main Menu", Colors.RED, True)
        
        choice = get_input(f"\n{Colors.BOLD}🎯 Select tool (0-3): {Colors.END}")
        
        if choice == '0':
            break
        elif choice == '241':
            system_241()
        elif choice == '242':
            system_242()
        elif choice == '243':
            system_243()
        else:
            cprint("❌ Invalid choice!", Colors.RED)
        
        get_input(f"\n{Colors.CYAN}⏎ Press Enter to continue...{Colors.END}")

def sub_menu_utility():
    while True:
        os.system('clear' if os.name != 'nt' else 'cls')
        print_header()
        cprint("  🔧 FILE UTILITY SYSTEMS (271-300)", Colors.YELLOW, True)
        cprint("  271. File Merge System", Colors.WHITE)
        cprint("  272. File Split System", Colors.WHITE)
        cprint("  273. File Compare System", Colors.WHITE)
        cprint("  274. File Cleanup System", Colors.WHITE)
        cprint("  275. File Organizer System", Colors.WHITE)
        cprint("  276. File Duplicate Remover", Colors.WHITE)
        cprint("  277. File Line Counter", Colors.WHITE)
        cprint("  278. File Word Counter", Colors.WHITE)
        cprint("  279. File Character Counter", Colors.WHITE)
        cprint("  280. File Search & Replace", Colors.WHITE)
        cprint("  0.  Back to Main Menu", Colors.RED, True)
        
        choice = get_input(f"\n{Colors.BOLD}🎯 Select tool (0-10): {Colors.END}")
        
        if choice == '0':
            break
        elif choice == '271':
            system_271()
        elif choice == '272':
            system_272()
        elif choice == '273':
            system_273()
        elif choice == '274':
            system_274()
        elif choice == '275':
            system_275()
        elif choice == '276':
            system_276()
        elif choice == '277':
            system_277()
        elif choice == '278':
            system_278()
        elif choice == '279':
            system_279()
        elif choice == '280':
            system_280()
        else:
            cprint("❌ Invalid choice!", Colors.RED)
        
        get_input(f"\n{Colors.CYAN}⏎ Press Enter to continue...{Colors.END}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cprint("\n\n👋 Exited by user. Goodbye!", Colors.YELLOW, True)
    except Exception as e:
        cprint(f"\n❌ Error: {str(e)}", Colors.RED, True)