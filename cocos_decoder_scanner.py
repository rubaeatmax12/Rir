import os
import re
import base64

# নির্দিষ্ট ডিকোড করা প্যাটার্ন সনাক্ত করার জন্য Regex
UID_PATTERN = re.compile(
    r'\b(?:uid|userid|user_id|player_id|playerid)\b\s*[:=]\s*["\'`]?([a-zA-Z0-9_\-\@\.]+)(?:["\'`]?)', 
    re.IGNORECASE
)

TOKEN_PATTERN = re.compile(
    r'\b(?:token|access_token|auth_token|session_token|jwt|sessionid|session_id)\b\s*[:=]\s*["\'`]?([a-zA-Z0-9\.\-_\=\+\/]+)(?:["\'`]?)', 
    re.IGNORECASE
)

URL_PATTERN = re.compile(r'https?://[^\s"\'`<>]+')
IP_PATTERN = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

# ১. হেক্স কোড (\x75) ডিকোড করার ফাংশন
def decode_hex_escapes(text):
    hex_pattern = re.compile(r'\\x([0-9a-fA-F]{2})')
    return hex_pattern.sub(lambda m: chr(int(m.group(1), 16)), text)

# ২. ইউনিকোড (\u0074) ডিকোড করার ফাংশন
def decode_unicode_escapes(text):
    unicode_pattern = re.compile(r'\\u([0-9a-fA-F]{4})')
    return unicode_pattern.sub(lambda m: chr(int(m.group(1), 16)), text)

# ৩. সম্ভাব্য Base64 স্ট্রিং খুঁজে ডিকোড করার ফাংশন
def try_decode_base64(text):
    # কোটেশনের ভেতরের সম্ভাব্য Base64 টেক্সট খোঁজা (দৈর্ঘ্য ৮ থেকে ২০০ ক্যারেক্টার)
    b64_pattern = re.compile(r'["\']([A-Za-z0-9\+\/]{8,200}={0,2})["\']')
    decoded_results = []
    
    for match in b64_pattern.finditer(text):
        candidate = match.group(1)
        try:
            # বেইস৬৪ ডিকোড করার চেষ্টা
            decoded_bytes = base64.b64decode(candidate)
            decoded_str = decoded_bytes.decode('utf-8', errors='ignore')
            
            # ডিকোড করা লেখাটি পড়ার যোগ্য (Readable ASCII) কি না পরীক্ষা
            if len(decoded_str) > 3 and all(32 <= ord(c) < 127 for c in decoded_str):
                decoded_results.append((candidate, decoded_str))
        except Exception:
            pass
    return decoded_results

def start_decoder_scan():
    print("=== COCOS2D JS ডিকোডার ও সিক্রেট স্ক্যানার ===\n")
    
    file_path = input("ফাইলটির পাথ (Path) দাও (যেমন: /sdcard/Project.js): ").strip()
    
    if not os.path.exists(file_path):
        print(f"\n[ত্রুটি] ফাইলটি পাওয়া যায়নি: '{file_path}'")
        return
        
    base_name = os.path.basename(file_path)
    dir_name = os.path.dirname(file_path)
    report_path = os.path.join(dir_name, f"decoded_report_{base_name}.txt") if dir_name else f"decoded_report_{base_name}.txt"

    print(f"\nডিকোডিং স্ক্যান শুরু হচ্ছে: {base_name}")
    print("এটি হেক্স, ইউনিকোড এবং বেইস-৬৪ ডিকোড করে স্ক্যান করবে। একটু সময় লাগতে পারে...")

    uids = set()
    tokens = set()
    urls = set()
    ips = set()
    decoded_b64_list = []
    total_lines = 0

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                total_lines = line_num
                clean_line = line.strip()
                if not clean_line:
                    continue

                # --- ডিকোডিং প্রসেস ---
                # ক. হেক্স ডিকোড (\x41 -> A)
                decoded_line = decode_hex_escapes(clean_line)
                # খ. ইউনিকোড ডিকোড (\u0041 -> A)
                decoded_line = decode_unicode_escapes(decoded_line)
                
                # গ. Base64 ডিকোড করার চেষ্টা
                b64_matches = try_decode_base64(clean_line)
                for original, decoded in b64_matches:
                    decoded_b64_list.append((line_num, original, decoded))
                    # ডিকোড করা টেক্সট মূল লাইনের সাথে যুক্ত করা যাতে নিচে সার্চে ধরা পড়ে
                    decoded_line += " " + decoded

                # --- আসল সার্চ প্রসেস (ডিকোড করা লাইনের ওপর) ---
                # ১. UID খোঁজা
                uid_matches = UID_PATTERN.findall(decoded_line)
                for uid in uid_matches:
                    if len(uid) > 2 and uid.lower() not in ["null", "undefined", "true", "false"]:
                        uids.add((uid, line_num))

                # ২. Token খোঁজা
                token_matches = TOKEN_PATTERN.findall(decoded_line)
                for token in token_matches:
                    if len(token) > 4 and token.lower() not in ["null", "undefined", "true", "false"]:
                        tokens.add((token, line_num))

                # ৩. URLs খোঁজা
                url_matches = URL_PATTERN.findall(decoded_line)
                for url in url_matches:
                    urls.add((url, line_num))

                # ৪. IPs খোঁজা
                ip_matches = IP_PATTERN.findall(decoded_line)
                for ip in ip_matches:
                    ips.add((ip, line_num))

        # রিপোর্ট ফাইল তৈরি
        with open(report_path, 'w', encoding='utf-8') as rep:
            rep.write(f"==================================================\n")
            rep.write(f"   DECODER & EXTRATOR REPORT: {base_name}\n")
            rep.write(f"==================================================\n")
            rep.write(f"মোট স্ক্যান করা লাইন সংখ্যা: {total_lines}\n\n")

            # ডিকোড হওয়া বেইস-৬৪ টেক্সটসমূহ
            rep.write(f"--- [ ডিকোড করা Base64 টেক্সটসমূহ ({len(decoded_b64_list)} টি) ] ---\n")
            if decoded_b64_list:
                for line, orig, dec in decoded_b64_list[:500]: # প্রথম ৫০০টি রেজাল্ট
                    rep.write(f"[Line {line}] En: {orig} => De: {dec}\n")
                if len(decoded_b64_list) > 500:
                    rep.write(f"... আরও {len(decoded_b64_list) - 500} টি Base64 ম্যাচ স্কিপ করা হয়েছে।\n")
            else:
                rep.write("কোনো ডিকোডযোগ্য Base64 স্ট্রিং পাওয়া যায়নি।\n")
            rep.write("\n" + "="*50 + "\n\n")

            # UIDs
            rep.write(f"--- [ এনক্রিপশন ভেঙে পাওয়া UIDs ({len(uids)} টি) ] ---\n")
            if uids:
                for uid, line in sorted(uids):
                    rep.write(f"[Line {line}] UID: {uid}\n")
            else:
                rep.write("কোনো UID পাওয়া যায়নি।\n")
            rep.write("\n" + "="*50 + "\n\n")

            # Tokens
            rep.write(f"--- [ এনক্রিপশন ভেঙে পাওয়া TOKENS ({len(tokens)} টি) ] ---\n")
            if tokens:
                for token, line in sorted(tokens):
                    display_token = token[:80] + "..." if len(token) > 80 else token
                    rep.write(f"[Line {line}] Token: {display_token}\n")
            else:
                rep.write("কোনো Token পাওয়া যায়নি।\n")
            rep.write("\n" + "="*50 + "\n\n")

            # URLs/সার্ভার
            rep.write(f"--- [ এনক্রিপশন ভেঙে পাওয়া URLs/সার্ভার ({len(urls)} টি) ] ---\n")
            if urls:
                for url, line in sorted(urls):
                    rep.write(f"[Line {line}] URL: {url}\n")
            else:
                rep.write("কোনো URL পাওয়া যায়নি।\n")

        print("\n" + "="*45)
        print("ডিকোডিং ও তথ্য নিষ্কাশন সফলভাবে সম্পন্ন হয়েছে!")
        print(f"সংরক্ষিত ফাইল: {report_path}")
        print(f"লোকেশন: {os.path.abspath(report_path)}")
        print("="*45)

    except Exception as e:
        print(f"\n[ত্রুটি] স্ক্যান করার সময় সমস্যা হয়েছে: {str(e)}")

if __name__ == "__main__":
    start_decoder_scan()
