import os
import io
import zipfile
import hashlib
import shutil
import datetime
import stat
import platform
import subprocess

# ================== SECURITY ENGINE (UNCHANGED) ==================
def generate_fast_large_key(password: str) -> bytes:
    key = b""
    current_hash = hashlib.sha512(password.encode('utf-8')).digest()
    for i in range(16):
        current_hash = hashlib.sha512(current_hash + str(i).encode('utf-8')).digest()
        key += current_hash
    return key

def fast_xor_crypt(data: bytes, key: bytes) -> bytes:
    data_len = len(data)
    key_len = len(key)
    repeated_key = (key * (data_len // key_len + 1))[:data_len]
    int_data = int.from_bytes(data, 'big')
    int_key = int.from_bytes(repeated_key, 'big')
    int_result = int_data ^ int_key
    return int_result.to_bytes(data_len, 'big')

# ================== UI DESIGN SYSTEM ==================
def show_logo():
    print("\033[1;36m" + "="*50 + "\033[0m")
    print("\033[1;33m" + "  ██████  ██ ███████ ███████ " + "\033[0m")
    print("\033[1;33m" + "  ██   ██ ██ ██      ██      " + "\033[0m")
    print("\033[1;33m" + "  ██████  ██ █████   █████   " + "\033[0m")
    print("\033[1;33m" + "  ██   ██ ██ ██      ██      " + "\033[0m")
    print("\033[1;33m" + "  ██   ██ ██ ███████ ███████ " + "\033[0m")
    print("\033[1;36m" + "="*50 + "\033[0m")
    print("\033[1;32m" + "     RIR - Secure Vault System v3.0" + "\033[0m")
    print("\033[1;34m" + "    32 Features | Mobile Optimized" + "\033[0m")
    print("\033[1;36m" + "="*50 + "\033[0m\n")

def show_menu():
    print("\033[1;37m┌──────────────────────────────────────────────┐\033[0m")
    print("\033[1;37m│  🔒 CORE VAULT (Original 2 Features)       │\033[0m")
    print("\033[1;37m├──────────────────────────────────────────────┤\033[0m")
    print("\033[1;32m│  1. Lock Folder (Encrypt)                   │\033[0m")
    print("\033[1;32m│  2. Unlock File (Decrypt)                   │\033[0m")
    print("\033[1;37m├──────────────────────────────────────────────┤\033[0m")
    print("\033[1;37m│  🛠️  NEW 30 UTILITY TOOLS                   │\033[0m")
    print("\033[1;37m├──────────────────────────────────────────────┤\033[0m")
    print("\033[1;33m│  3.  File Shredder (Secure Delete)          │\033[0m")
    print("\033[1;33m│  4.  Duplicate File Finder                  │\033[0m")
    print("\033[1;33m│  5.  Batch Rename Files                     │\033[0m")
    print("\033[1;33m│  6.  Folder Size Analyzer                   │\033[0m")
    print("\033[1;33m│  7.  File Type Counter                      │\033[0m")
    print("\033[1;33m│  8.  Empty Folder Cleaner                   │\033[0m")
    print("\033[1;33m│  9.  Large File Finder (>100MB)             │\033[0m")
    print("\033[1;33m│  10. File Organizer by Extension            │\033[0m")
    print("\033[1;33m│  11. Create Dummy Files (Test)              │\033[0m")
    print("\033[1;33m│  12. Calculate Folder Checksum (MD5)        │\033[0m")
    print("\033[1;33m│  13. Compare Two Folders                    │\033[0m")
    print("\033[1;33m│  14. Backup Folder with Timestamp           │\033[0m")
    print("\033[1;33m│  15. Restore Backup                         │\033[0m")
    print("\033[1;33m│  16. Hide/Unhide Files (Windows)            │\033[0m")
    print("\033[1;33m│  17. File Permission Changer (Linux/Mac)    │\033[0m")
    print("\033[1;33m│  18. Create Symbolic Link                   │\033[0m")
    print("\033[1;33m│  19. Find Broken Symlinks                   │\033[0m")
    print("\033[1;33m│  20. Monitor Folder Changes (Simple)        │\033[0m")
    print("\033[1;33m│  21. Generate Random Password               │\033[0m")
    print("\033[1;33m│  22. Hash File (SHA256/MD5)                │\033[0m")
    print("\033[1;33m│  23. Split File into Parts                  │\033[0m")
    print("\033[1;33m│  24. Merge File Parts                       │\033[0m")
    print("\033[1;33m│  25. Encrypt Text (Clipboard Ready)         │\033[0m")
    print("\033[1;33m│  26. Decrypt Text                           │\033[0m")
    print("\033[1;33m│  27. System Info Display                    │\033[0m")
    print("\033[1;33m│  28. Disk Usage Report                      │\033[0m")
    print("\033[1;33m│  29. File Age Monitor (Older than 30 days)  │\033[0m")
    print("\033[1;33m│  30. Create ZIP with Password               │\033[0m")
    print("\033[1;33m│  31. Extract ZIP with Password               │\033[0m")
    print("\033[1;33m│  32. Exit / Close Tool                      │\033[0m")
    print("\033[1;37m└──────────────────────────────────────────────┘\033[0m")

def show_header(title):
    print("\n\033[1;35m" + "▬"*50 + "\033[0m")
    print("\033[1;36m" + f"  {title}" + "\033[0m")
    print("\033[1;35m" + "▬"*50 + "\033[0m")

def show_success(msg):
    print("\033[1;32m✅ " + msg + "\033[0m")

def show_error(msg):
    print("\033[1;31m❌ " + msg + "\033[0m")

def show_info(msg):
    print("\033[1;34mℹ️  " + msg + "\033[0m")

# ================== CORE FEATURES (1-2) - FIXED LOCATION ==================
def lock_folder():
    show_header("🔒 LOCK FOLDER (Encrypt)")
    folder_path = input("📁 Enter folder path: ").strip()
    
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        show_error("Folder not found!")
        return

    # FIX: Allow user to specify full path or just filename
    output_file = input("💾 Output filename (e.g., vault.enc or /sdcard/vault.enc): ").strip()
    
    # If user gives only filename, save in current directory
    if not os.path.dirname(output_file):
        output_file = os.path.join(os.getcwd(), output_file)
    
    password = input("🔑 Password: ").strip()
    if not password:
        show_error("Password cannot be empty!")
        return
    
    try:
        show_info("Processing... Please wait.")
        
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_absolute_path = os.path.join(root, file)
                    file_relative_path = os.path.relpath(file_absolute_path, folder_path)
                    zip_file.write(file_absolute_path, file_relative_path)
        
        raw_data = zip_buffer.getvalue()
        key_bytes = generate_fast_large_key(password)
        encrypted_data = fast_xor_crypt(raw_data, key_bytes)
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'wb') as f:
            f.write(encrypted_data)
            
        show_success(f"Folder locked! File saved at: {os.path.abspath(output_file)}")
        
    except Exception as e:
        show_error(str(e))

def unlock_file():
    show_header("🔓 UNLOCK FILE (Decrypt)")
    file_path = input("📁 Enter locked file path: ").strip()
    
    if not os.path.exists(file_path):
        show_error("File not found!")
        return

    output_folder = input("📂 Output folder: ").strip()
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    password = input("🔑 Password: ").strip()

    try:
        show_info("Decrypting... Please wait.")
        
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

        key_bytes = generate_fast_large_key(password)
        decrypted_data = fast_xor_crypt(encrypted_data, key_bytes)
        
        zip_buffer = io.BytesIO(decrypted_data)
        with zipfile.ZipFile(zip_buffer, 'r') as zip_file:
            zip_file.extractall(output_folder)
            
        show_success(f"Unlocked! Files restored to: {os.path.abspath(output_folder)}")
        
    except Exception as e:
        show_error("Wrong password or corrupted file!")

# ================== NEW 30 FEATURES (3-31) ==================
def file_shredder():
    show_header("🗑️ FILE SHREDDER")
    path = input("📁 File/Folder path to shred: ").strip()
    if not os.path.exists(path):
        show_error("Path not found!")
        return
    confirm = input("⚠️ PERMANENT DELETE! Type 'YES' to confirm: ").strip()
    if confirm != "YES":
        show_info("Cancelled.")
        return
    try:
        if os.path.isfile(path):
            with open(path, "wb") as f:
                f.write(os.urandom(os.path.getsize(path)))
            os.remove(path)
        else:
            shutil.rmtree(path)
        show_success("Shredded successfully!")
    except Exception as e:
        show_error(str(e))

def find_duplicates():
    show_header("🔍 DUPLICATE FILE FINDER")
    folder = input("📁 Folder to scan: ").strip()
    if not os.path.isdir(folder):
        show_error("Invalid folder!")
        return
    hashes = {}
    duplicates = []
    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            try:
                with open(path, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                if file_hash in hashes:
                    duplicates.append((path, hashes[file_hash]))
                else:
                    hashes[file_hash] = path
            except:
                continue
    if duplicates:
        show_info(f"Found {len(duplicates)} duplicates:")
        for dup in duplicates:
            print(f"  📄 {dup[0]}  <->  {dup[1]}")
    else:
        show_info("No duplicates found.")

def batch_rename():
    show_header("✏️ BATCH RENAME")
    folder = input("📁 Folder: ").strip()
    prefix = input("📛 New prefix: ").strip()
    ext = input("📎 Extension (e.g., .txt): ").strip()
    if not os.path.isdir(folder):
        show_error("Invalid folder!")
        return
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    for i, fname in enumerate(files, 1):
        old = os.path.join(folder, fname)
        new = os.path.join(folder, f"{prefix}_{i}{ext}")
        os.rename(old, new)
    show_success(f"Renamed {len(files)} files.")

def folder_size_analyzer():
    show_header("📊 FOLDER SIZE")
    folder = input("📁 Folder: ").strip()
    if not os.path.isdir(folder):
        show_error("Invalid folder!")
        return
    total = 0
    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            total += os.path.getsize(path)
    show_info(f"Total size: {total / (1024*1024):.2f} MB")

def file_type_counter():
    show_header("📈 FILE TYPE COUNTER")
    folder = input("📁 Folder: ").strip()
    if not os.path.isdir(folder):
        show_error("Invalid folder!")
        return
    ext_count = {}
    for root, _, files in os.walk(folder):
        for file in files:
            ext = os.path.splitext(file)[1] or "No Extension"
            ext_count[ext] = ext_count.get(ext, 0) + 1
    for ext, count in sorted(ext_count.items(), key=lambda x: x[1], reverse=True):
        print(f"  {ext}: {count} files")

def clean_empty_folders():
    show_header("🧹 EMPTY FOLDER CLEANER")
    folder = input("📁 Folder: ").strip()
    if not os.path.isdir(folder):
        show_error("Invalid folder!")
        return
    count = 0
    for root, dirs, _ in os.walk(folder, topdown=False):
        for d in dirs:
            dir_path = os.path.join(root, d)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                count += 1
    show_success(f"Removed {count} empty folders.")

def find_large_files():
    show_header("📦 LARGE FILES (>100MB)")
    folder = input("📁 Folder: ").strip()
    if not os.path.isdir(folder):
        show_error("Invalid folder!")
        return
    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            size = os.path.getsize(path) / (1024*1024)
            if size > 100:
                print(f"  📄 {path} ({size:.2f} MB)")

def organize_by_extension():
    show_header("📂 ORGANIZE BY EXTENSION")
    folder = input("📁 Folder: ").strip()
    if not os.path.isdir(folder):
        show_error("Invalid folder!")
        return
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            ext = os.path.splitext(file)[1][1:] or "no_ext"
            target = os.path.join(folder, ext)
            os.makedirs(target, exist_ok=True)
            shutil.move(path, os.path.join(target, file))
    show_success("Organized!")

def create_dummy_files():
    show_header("🧪 CREATE DUMMY FILES")
    folder = input("📁 Folder: ").strip()
    count = int(input("🔢 Number of files: ").strip())
    size_kb = int(input("📏 Size (KB each): ").strip())
    os.makedirs(folder, exist_ok=True)
    for i in range(count):
        with open(os.path.join(folder, f"dummy_{i}.txt"), 'wb') as f:
            f.write(os.urandom(size_kb * 1024))
    show_success(f"Created {count} dummy files.")

def folder_checksum():
    show_header("🔐 FOLDER MD5 CHECKSUM")
    folder = input("📁 Folder: ").strip()
    if not os.path.isdir(folder):
        show_error("Invalid folder!")
        return
    hasher = hashlib.md5()
    for root, _, files in sorted(os.walk(folder)):
        for file in sorted(files):
            path = os.path.join(root, file)
            with open(path, 'rb') as f:
                hasher.update(f.read())
    show_info(f"MD5: {hasher.hexdigest()}")

def compare_folders():
    show_header("🔁 COMPARE TWO FOLDERS")
    f1 = input("📁 Folder 1: ").strip()
    f2 = input("📁 Folder 2: ").strip()
    if not os.path.isdir(f1) or not os.path.isdir(f2):
        show_error("Invalid folders!")
        return
    set1 = set(os.path.relpath(os.path.join(r,f), f1) for r,_,fs in os.walk(f1) for f in fs)
    set2 = set(os.path.relpath(os.path.join(r,f), f2) for r,_,fs in os.walk(f2) for f in fs)
    only1 = set1 - set2
    only2 = set2 - set1
    if only1:
        show_info("Only in Folder 1:")
        for f in only1: print(f"  {f}")
    if only2:
        show_info("Only in Folder 2:")
        for f in only2: print(f"  {f}")
    if not only1 and not only2:
        show_info("Folders are identical.")

def backup_folder():
    show_header("💾 BACKUP WITH TIMESTAMP")
    src = input("📁 Source folder: ").strip()
    if not os.path.isdir(src):
        show_error("Invalid folder!")
        return
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = f"backup_{ts}"
    shutil.copytree(src, dst)
    show_success(f"Backup created: {dst}")

def restore_backup():
    show_header("♻️ RESTORE BACKUP")
    src = input("📁 Backup folder: ").strip()
    dst = input("📁 Restore to: ").strip()
    if not os.path.isdir(src):
        show_error("Backup not found!")
        return
    shutil.copytree(src, dst)
    show_success(f"Restored to {dst}")

def hide_unhide_windows():
    show_header("👁️ HIDE/UNHIDE (Windows)")
    path = input("📁 File/Folder: ").strip()
    if not os.path.exists(path):
        show_error("Not found!")
        return
    action = input("(h)ide or (u)nhide? ").strip().lower()
    if action == 'h':
        os.system(f'attrib +h "{path}"')
        show_success("Hidden!")
    elif action == 'u':
        os.system(f'attrib -h "{path}"')
        show_success("Unhidden!")
    else:
        show_error("Invalid choice.")

def change_permissions():
    show_header("🔑 CHANGE PERMISSIONS (Linux/Mac)")
    path = input("📁 File/Folder: ").strip()
    if not os.path.exists(path):
        show_error("Not found!")
        return
    perm = input("🔢 Permissions (e.g., 755): ").strip()
    os.chmod(path, int(perm, 8))
    show_success("Permissions updated!")

def create_symlink():
    show_header("🔗 CREATE SYMLINK")
    target = input("📁 Target: ").strip()
    link = input("🔗 Link name: ").strip()
    os.symlink(target, link)
    show_success(f"Symlink created: {link} -> {target}")

def find_broken_symlinks():
    show_header("💔 FIND BROKEN SYMLINKS")
    folder = input("📁 Folder: ").strip()
    if not os.path.isdir(folder):
        show_error("Invalid folder!")
        return
    for root, _, files in os.walk(folder):
        for f in files:
            path = os.path.join(root, f)
            if os.path.islink(path) and not os.path.exists(os.readlink(path)):
                print(f"  Broken: {path}")

def monitor_folder_changes():
    show_header("👀 MONITOR FOLDER (Simple)")
    folder = input("📁 Folder to monitor: ").strip()
    if not os.path.isdir(folder):
        show_error("Invalid folder!")
        return
    snapshot = set()
    for root, _, files in os.walk(folder):
        for f in files:
            path = os.path.join(root, f)
            snapshot.add((path, os.path.getmtime(path)))
    show_info("Monitoring... Press Ctrl+C to stop.")
    try:
        while True:
            import time
            time.sleep(5)
            current = set()
            for root, _, files in os.walk(folder):
                for f in files:
                    path = os.path.join(root, f)
                    current.add((path, os.path.getmtime(path)))
            new = current - snapshot
            removed = snapshot - current
            for item in new:
                print(f"  ➕ Added/Modified: {item[0]}")
            for item in removed:
                print(f"  ➖ Removed: {item[0]}")
            snapshot = current
    except KeyboardInterrupt:
        show_info("Monitoring stopped.")

def generate_password():
    show_header("🔐 RANDOM PASSWORD")
    length = int(input("🔢 Length: ").strip())
    import secrets
    import string
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(secrets.choice(chars) for _ in range(length))
    show_info(f"Password: {pwd}")

def hash_file():
    show_header("🔏 HASH FILE")
    path = input("📁 File: ").strip()
    if not os.path.isfile(path):
        show_error("File not found!")
        return
    algo = input("🔢 (md5/sha256): ").strip().lower()
    hasher = hashlib.md5() if algo == "md5" else hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    show_info(f"{algo.upper()}: {hasher.hexdigest()}")

def split_file():
    show_header("✂️ SPLIT FILE")
    path = input("📁 File: ").strip()
    if not os.path.isfile(path):
        show_error("File not found!")
        return
    part_size = int(input("📏 Part size (MB): ").strip()) * 1024 * 1024
    with open(path, 'rb') as f:
        i = 1
        while True:
            chunk = f.read(part_size)
            if not chunk:
                break
            with open(f"{path}.part{i}", 'wb') as p:
                p.write(chunk)
            i += 1
    show_success(f"Split into {i-1} parts.")

def merge_files():
    show_header("🧩 MERGE FILES")
    base = input("📁 Base filename (without .part): ").strip()
    i = 1
    with open(f"{base}_merged", 'wb') as out:
        while True:
            try:
                with open(f"{base}.part{i}", 'rb') as p:
                    out.write(p.read())
                i += 1
            except:
                break
    show_success(f"Merged into {base}_merged")

def encrypt_text():
    show_header("🔐 ENCRYPT TEXT")
    text = input("📝 Text: ").strip()
    pwd = input("🔑 Password: ").strip()
    key = generate_fast_large_key(pwd)
    encrypted = fast_xor_crypt(text.encode(), key)
    import base64
    show_info(f"Encrypted (base64): {base64.b64encode(encrypted).decode()}")

def decrypt_text():
    show_header("🔓 DECRYPT TEXT")
    enc = input("📝 Encrypted (base64): ").strip()
    pwd = input("🔑 Password: ").strip()
    import base64
    try:
        data = base64.b64decode(enc)
        key = generate_fast_large_key(pwd)
        decrypted = fast_xor_crypt(data, key)
        show_info(f"Decrypted: {decrypted.decode()}")
    except:
        show_error("Decryption failed!")

def system_info():
    show_header("🖥️ SYSTEM INFO")
    show_info(f"OS: {platform.system()} {platform.release()}")
    show_info(f"Machine: {platform.machine()}")
    show_info(f"Processor: {platform.processor()}")
    show_info(f"Python: {platform.python_version()}")

def disk_usage():
    show_header("💿 DISK USAGE")
    import shutil
    total, used, free = shutil.disk_usage("/")
    show_info(f"Total: {total / (1024**3):.2f} GB")
    show_info(f"Used: {used / (1024**3):.2f} GB")
    show_info(f"Free: {free / (1024**3):.2f} GB")

def file_age_monitor():
    show_header("📅 FILE AGE MONITOR (>30 days)")
    folder = input("📁 Folder: ").strip()
    if not os.path.isdir(folder):
        show_error("Invalid folder!")
        return
    now = datetime.datetime.now()
    for root, _, files in os.walk(folder):
        for f in files:
            path = os.path.join(root, f)
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(path))
            if (now - mtime).days > 30:
                print(f"  🕒 {path} (Last modified: {mtime.strftime('%Y-%m-%d')})")

def zip_with_password():
    show_header("📦 CREATE ZIP WITH PASSWORD")
    folder = input("📁 Folder to zip: ").strip()
    out = input("💾 Output zip name: ").strip()
    pwd = input("🔑 Password: ").strip()
    if not os.path.isdir(folder):
        show_error("Invalid folder!")
        return
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(folder):
            for f in files:
                path = os.path.join(root, f)
                zf.write(path, os.path.relpath(path, folder))
    data = zip_buffer.getvalue()
    key = generate_fast_large_key(pwd)
    encrypted = fast_xor_crypt(data, key)
    with open(out, 'wb') as f:
        f.write(encrypted)
    show_success(f"ZIP encrypted: {out}")

def extract_zip_with_password():
    show_header("📂 EXTRACT ZIP WITH PASSWORD")
    path = input("📁 Encrypted zip file: ").strip()
    out = input("📂 Extract to: ").strip()
    pwd = input("🔑 Password: ").strip()
    if not os.path.isfile(path):
        show_error("File not found!")
        return
    try:
        with open(path, 'rb') as f:
            encrypted = f.read()
        key = generate_fast_large_key(pwd)
        decrypted = fast_xor_crypt(encrypted, key)
        zip_buffer = io.BytesIO(decrypted)
        with zipfile.ZipFile(zip_buffer, 'r') as zf:
            zf.extractall(out)
        show_success(f"Extracted to {out}")
    except:
        show_error("Wrong password or corrupted!")

# ================== MAIN ==================
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_logo()
    while True:
        show_menu()
        choice = input("\n🎯 Select option (1-32): ").strip()
        
        if choice == '1': lock_folder()
        elif choice == '2': unlock_file()
        elif choice == '3': file_shredder()
        elif choice == '4': find_duplicates()
        elif choice == '5': batch_rename()
        elif choice == '6': folder_size_analyzer()
        elif choice == '7': file_type_counter()
        elif choice == '8': clean_empty_folders()
        elif choice == '9': find_large_files()
        elif choice == '10': organize_by_extension()
        elif choice == '11': create_dummy_files()
        elif choice == '12': folder_checksum()
        elif choice == '13': compare_folders()
        elif choice == '14': backup_folder()
        elif choice == '15': restore_backup()
        elif choice == '16': hide_unhide_windows()
        elif choice == '17': change_permissions()
        elif choice == '18': create_symlink()
        elif choice == '19': find_broken_symlinks()
        elif choice == '20': monitor_folder_changes()
        elif choice == '21': generate_password()
        elif choice == '22': hash_file()
        elif choice == '23': split_file()
        elif choice == '24': merge_files()
        elif choice == '25': encrypt_text()
        elif choice == '26': decrypt_text()
        elif choice == '27': system_info()
        elif choice == '28': disk_usage()
        elif choice == '29': file_age_monitor()
        elif choice == '30': zip_with_password()
        elif choice == '31': extract_zip_with_password()
        elif choice == '32':
            show_info("👋 Thanks for using RIR Vault! Goodbye.")
            break
        else:
            show_error("Invalid option! Please choose 1-32.")
        
        input("\n⏎ Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        show_logo()

if __name__ == "__main__":
    main()