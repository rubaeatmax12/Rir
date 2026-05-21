import os

def search_token_in_file(file_path, search_term):
    # ফাইলটি আসলেই ওই লোকেশনে আছে কি না তা পরীক্ষা করা
    if not os.path.exists(file_path):
        print("ভুল ফাইল লোকেশন! দয়া করে সঠিক পথটি দিন।")
        return

    count = 0
    found_lines = []

    try:
        # ফাইলটি পড়া হচ্ছে (বড় ফাইলের জন্য লাইন-বাই-লাইন পড়া হচ্ছে)
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line_number, line in enumerate(file, 1):
                # আপনি যে শব্দটি খুঁজছেন (যেমন: token) তা লাইনে আছে কি না পরীক্ষা করা হচ্ছে
                # এখানে case-insensitive search করা হয়েছে (ছোট-বড় হাতের অক্ষরের পার্থক্য ধরা হবে না)
                if search_term.lower() in line.lower():
                    clean_line = line.strip()
                    found_lines.append((line_number, clean_line))
                    count += 1

        # ফলাফল প্রদর্শন
        print("\n" + "="*40)
        print(f"অনুসন্ধানের ফলাফল:")
        print(f"মোট '{search_term}' পাওয়া গেছে: {count} বার")
        print("="*40)

        if count > 0:
            print("\nখুঁজে পাওয়া লাইনগুলো নিচে দেওয়া হলো:\n")
            for num, content in found_lines:
                print(f"[লাইন {num}]: {content}")
        else:
            print(f"ফাইলটিতে '{search_term}' শব্দটি খুঁজে পাওয়া যায়নি।")

    except Exception as e:
        print(f"ফাইলটি পড়ার সময় একটি সমস্যা হয়েছে: {e}")

if __name__ == "__main__":
    print("--- ফাইল টোকেন সার্চার টুল ---")
    
    # ব্যবহারকারীর কাছ থেকে ফাইল লোকেশন নেওয়া
    file_location = input("ফাইল লোকেশন (যেমন: C:/folder/file.txt) দিন: ").strip()
    
    # ব্যবহারকারীর কাছ থেকে কী শব্দ খুঁজবেন তা নেওয়া
    token_to_search = input("যে শব্দটি খুঁজতে চান (যেমন: token) লিখুন: ").strip()
    
    if file_location and token_to_search:
        search_token_in_file(file_location, token_to_search)
    else:
        print("ফাইল লোকেশন এবং শব্দ দুটিই দেওয়া আবশ্যক।")
