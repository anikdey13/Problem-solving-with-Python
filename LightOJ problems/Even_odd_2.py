# একটি পূর্ণসংখ্যা দেওয়া থাকবে, সেটি জোড় না বিজোড় তা বের করতে হবে।

# ইনপুট:
# প্রথম লাইনে একটি সংখ্যা T (1 ≤ T ≤ 100) দেওয়া থাকবে। পরবর্তীতে T-এর মান যত, ততটি লাইন থাকবে। প্রতিটি লাইনে একটি করে পূর্ণসংখ্যা N দেওয়া থাকবে। একটি সংখ্যায় সর্বোচ্চ 100টি অঙ্ক (digit) থাকতে পারে।

# আউটপুট:
# প্রতিটি পূর্ণসংখ্যার জন্য, সংখ্যাটি জোড় হলে even, আর বিজোড় হলে odd কথাটি প্রিন্ট করতে হবে।

# নমুনা:
# ইনপুট	            আউটপুট
# 4
# 0                 even
# -22               even
# 5                 odd
# 1267818768111166  even


T = int(input())
for i in range(T):
    N = int(input())
    if N%2 == 0:
        print('even')
    else:
        print('odd')