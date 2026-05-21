"""
JSC Decryptor Tool - 2025
Original Logic by: Bartłomiej Duda
Modified for Interactive Use
"""

import gzip
import io
import os
import xxtea
from zipfile import BadZipFile, ZipFile

def run_tool():
    print("====================================")
    print("   JSC PYDECRYPT INTERACTIVE TOOL   ")
    print("====================================")

    # ১. ফাইল লোকেশন ইনপুট
    jsc_file_path = input("\n[?] তোর .jsc ফাইলের ফুল পাথ বা নাম লেখ: ").strip()

    # ফাইল আছে কিনা চেক
    if not os.path.exists(jsc_file_path):
        print(f"❌ এরর: '{jsc_file_path}' ফাইলটি খুঁজে পাওয়া যায়নি!")
        return

    print(f"✅ ফাইল পাওয়া গেছে: {os.path.basename(jsc_file_path)}")

    # ২. চাবি (Key) ইনপুট
    encryption_key = input("[?] এনক্রিপশন কি (Key) দে: ").strip()
    
    if not encryption_key:
        print("❌ এরর: কি (Key) ছাড়া ডিক্রিপ্ট করা সম্ভব না!")
        return

    # ৩. আউটপুট ফাইলের নাম
    output_file_path = input("[?] আউটপুট ফাইলের নাম কী দিবি? (যেমন: code.js): ").strip()
    if not output_file_path:
        output_file_path = "decrypted_output.js"

    print("\n[*] প্রসেসিং শুরু হচ্ছে...")

    try:
        # ফাইল রিড করা
        with open(jsc_file_path, "rb") as f:
            jsc_file_data = f.read()

        # ডিক্রিপশন (XXTEA)
        output_data = xxtea.decrypt(jsc_file_data, encryption_key)

        if not output_data or len(output_data) == 0:
            print("❌ এরর: ডিক্রিপশন ব্যর্থ! কি (Key) ভুল হতে পারে।")
            return

        # GZIP চেক ও ডিকম্প্রেস
        is_gzip_file = True
        try:
            output_data = gzip.decompress(output_data)
            print("[+] এটি একটি GZIP আর্কাইভ ছিল।")
        except Exception:
            print("[!] এটি GZIP আর্কাইভ নয়।")
            is_gzip_file = False

        # ZIP চেক (যদি GZIP না হয়)
        if not is_gzip_file:
            try:
                zip_check = io.BytesIO(output_data)
                ZipFile(zip_check)
                if not output_file_path.endswith(".zip"):
                    output_file_path += ".zip"
                print("[+] এটি একটি ZIP আর্কাইভ ছিল।")
            except BadZipFile:
                print("[!] এটি কোনো পরিচিত জিপ ফরম্যাট নয়, সরাসরি টেক্সট হিসেবে সেভ হচ্ছে।")

        # ফাইল রাইট করা
        with open(output_file_path, "wb") as js_file:
            js_file.write(output_data)

        print(f"\n✅ কাজ শেষ! তোর ফাইল এখানে সেভ হয়েছে: {os.path.abspath(output_file_path)}")
        print("====================================")

    except Exception as e:
        print(f"❌ হঠাৎ একটা সমস্যা হয়েছে: {str(e)}")

if __name__ == "__main__":
    run_tool()