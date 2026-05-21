import os

try:
    import xxtea
except ImportError:
    print("ভুল: 'xxtea' লাইব্রেরিটি ইনস্টল করা নেই।")
    print("দয়া করে টার্মিনালে এই কমান্ডটি রান করো: pip install xxtea-py")
    exit(1)

def lock_file_with_xxtea():
    print("--- Cocos2d JS to JSC এনক্রিপশন টুল --- \n")

    # ১. ইনপুট ফাইলের লোকেশন নেওয়া
    while True:
        js_path = input("১. তোমার JS ফাইলের লোকেশন দাও (যেমন: main.js): ").strip()
        if os.path.exists(js_path):
            break
        print("ভুল: এই লোকেশনে কোনো ফাইল পাওয়া যায়নি! আবার চেষ্টা করো।\n")

    # ২. সেভ করার ফাইলের লোকেশন নেওয়া
    jsc_path = input("২. নতুন JSC ফাইলটি কোথায় সেভ করতে চাও (যেমন: main.jsc): ").strip()
    if not jsc_path:
        jsc_path = "output.jsc"  # ডিফল্ট নাম

    # ৩. Key ইনপুট নেওয়া
    while True:
        key = input("৩. তোমার XXTEA Key টি দাও: ").strip()
        if key:
            break
        print("ভুল: Key খালি রাখা যাবে না!\n")

    # ৪. Signature (Sign) ইনপুট নেওয়া (ঐচ্ছিক)
    sign = input("৪. ফাইলের Signature থাকলে দাও (না থাকলে Enter চাপো): ").strip()

    try:
        # JS ফাইল থেকে ডেটা পড়া
        with open(js_path, 'rb') as f:
            js_data = f.read()

        # Key-কে বাইট-এ রূপান্তর করা
        key_bytes = key.encode('utf-8')

        # XXTEA লাইব্রেরি দিয়ে এনক্রিপশন করা
        # xxtea.encrypt সাধারণত bytes ইনপুট নেয় এবং bytes আউটপুট দেয়
        encrypted_data = xxtea.encrypt(js_data, key_bytes)

        # যদি কোনো Signature থাকে তবে তা এনক্রিপ্টেড ডেটার শুরুতে যোগ করা
        if sign:
            final_data = sign.encode('utf-8') + encrypted_data
        else:
            final_data = encrypted_data

        # নতুন JSC ফাইলে ডেটা সেভ করা
        with open(jsc_path, 'wb') as f:
            f.write(final_data)

        print("\n" + "="*40)
        print("অভিনন্দন! ফাইলটি সফলভাবে লক করা হয়েছে।")
        print(f"সংরক্ষিত ফাইলের লোকেশন: {os.path.abspath(jsc_path)}")
        print("="*40)

    except Exception as e:
        print(f"\nএনক্রিপ্ট করার সময় একটি সমস্যা হয়েছে: {str(e)}")

if __name__ == "__main__":
    lock_file_with_xxtea()
