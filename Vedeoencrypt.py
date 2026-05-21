import os
import io
import zipfile
import hashlib

# পাসওয়ার্ড থেকে অত্যন্ত শক্তিশালী এবং বড় ১০২৪ বাইটের কি (Key) তৈরি করার ফাস্ট ফাংশন
def generate_fast_large_key(password: str) -> bytes:
    key = b""
    # পাসওয়ার্ডকে হ্যাশ করে ১০২৪ বাইটের অত্যন্ত সুরক্ষিত কি তৈরি করা
    current_hash = hashlib.sha512(password.encode('utf-8')).digest()
    for i in range(16):  # ১৬ বার হ্যাশ করে ১৬ * ৬৪ = ১০২৪ বাইট তৈরি করা
        current_hash = hashlib.sha512(current_hash + str(i).encode('utf-8')).digest()
        key += current_hash
    return key

# সুপার-ফাস্ট এনক্রিপশন ট্রিক (মিলি-সেকেন্ডে কাজ করবে)
def fast_xor_crypt(data: bytes, key: bytes) -> bytes:
    data_len = len(data)
    key_len = len(key)
    
    # কি-কে ডেটার সমান সাইজে বড় করা
    repeated_key = (key * (data_len // key_len + 1))[:data_len]
    
    # পাইথন ইন্টিজার ম্যাজিক (C-Speed এ কাজ করে)
    int_data = int.from_bytes(data, 'big')
    int_key = int.from_bytes(repeated_key, 'big')
    
    int_result = int_data ^ int_key
    return int_result.to_bytes(data_len, 'big')

# ১. ফোল্ডার লক করার ফাংশন
def lock_folder():
    print("\n--- ফোল্ডার লক করার প্রক্রিয়া (সুপার-ফাস্ট) ---")
    folder_path = input("লক করার ফোল্ডারের পথ (Path) দাও: ").strip()
    
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print("ভুল: এই নামে কোনো ফোল্ডার পাওয়া যায়নি!")
        return

    output_file = input("লক করা ফাইলটি কী নামে সেভ করতে চাও (যেমন: Raja.enc): ").strip()
    password = input("লক করার পাসওয়ার্ড (Key) দাও: ").strip()
    
    if not password:
        print("ভুল: পাসওয়ার্ড খালি রাখা যাবে না!")
        return

    try:
        print("প্রসেস করা হচ্ছে, দয়া করে অপেক্ষা করো...")
        
        # ফোল্ডারের ফাইলগুলো মেমোরিতে জিপ করা (খুব দ্রুত হবে)
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_absolute_path = os.path.join(root, file)
                    file_relative_path = os.path.relpath(file_absolute_path, folder_path)
                    zip_file.write(file_absolute_path, file_relative_path)
        
        raw_data = zip_buffer.getvalue()
        key_bytes = generate_fast_large_key(password)
        
        # সুপার-ফাস্ট এনক্রিপ্ট
        encrypted_data = fast_xor_crypt(raw_data, key_bytes)
        
        # ফাইলে সেভ করা
        with open(output_file, 'wb') as f:
            f.write(encrypted_data)
            
        print("\n" + "="*45)
        print("কাজ শেষ! ফাইলটি সফলভাবে লক করা হয়েছে।")
        print(f"লক করা ফাইলের লোকেশন: {os.path.abspath(output_file)}")
        print("="*45)

    except Exception as e:
        print(f"সমস্যা হয়েছে: {str(e)}")

# ২. ফাইল আনলক করার ফাংশন
def unlock_file():
    print("\n--- ফাইল আনলক করার প্রক্রিয়া ---")
    file_path = input("লক করা ফাইলের পথ (Path) দাও: ").strip()
    
    if not os.path.exists(file_path):
        print("ভুল: এই ফাইলটি খুঁজে পাওয়া যায়নি!")
        return

    output_folder = input("ফাইলগুলো কোন ফোল্ডারে আনলক করতে চাও: ").strip()
    password = input("পাসওয়ার্ড (Key) টি দাও: ").strip()

    try:
        print("আনলক করা হচ্ছে, দয়া করে অপেক্ষা করো...")
        
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

        key_bytes = generate_fast_large_key(password)
        
        # সুপার-ফাস্ট ডিক্রিপ্ট
        decrypted_data = fast_xor_crypt(encrypted_data, key_bytes)
        
        # জিপ ফাইলটি আনজিপ করা
        zip_buffer = io.BytesIO(decrypted_data)
        with zipfile.ZipFile(zip_buffer, 'r') as zip_file:
            zip_file.extractall(output_folder)
            
        print("\n" + "="*45)
        print("কাজ শেষ! ফাইলটি সফলভাবে আনলক করা হয়েছে।")
        print(f"সব ফাইল এখানে ফেরত এসেছে: {os.path.abspath(output_folder)}")
        print("="*45)

    except Exception as e:
        print("\nভুল: পাসওয়ার্ড সঠিক নয় অথবা ফাইলটি ক্ষতিগ্রস্ত হয়েছে!")

# মেইন ইন্টারফেস
def main():
    while True:
        print("\n======= FAST FOLDER VAULT =======")
        print("[১] ফোল্ডার লক করুন (Folder Lock)")
        print("[২] ফাইল আনলক করুন (File Unlock)")
        print("[৩] বন্ধ করুন (Exit)")
        
        choice = input("\nঅপশন সিলেক্ট করো (১/২/৩): ").strip()
        
        if choice == '1':
            lock_folder()
        elif choice == '2':
            unlock_file()
        elif choice == '3':
            print("ধন্যবাদ! টুলটি বন্ধ করা হচ্ছে।")
            break
        else:
            print("ভুল অপশন! দয়া করে সঠিক সংখ্যাটি চাপো।")

if __name__ == "__main__":
    main()
