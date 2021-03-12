import sys
import emoji
import random

name = "Sam"

WISE_COMPILER = [
    "According to the compiler, there is a",
    "In all its wisdom, the compiler informs me that there is a",
    "Unfortunately, the compiler has found a",
    ]
    
def get_filename(string):
    for i in range(len(string)):
        if string[i] == '.':
            for j in range(i, len(string)):
                if string[j] == ':':
                    return j
    return 0

def get_last_colon(string):
    last_colon = 0
    for i in range(len(string)):
        if string[i] == ':':
            last_colon = i
    return last_colon

def print_random_emoji():
    r = random.randint(0, 80)
    s = 128516
    print(chr(s + r))
    
    
print(f"Hey {name}, I'm sorry, I have some bad news.")
print()
errl = 0
for line in sys.stdin:
    if errl == 0:
        errl = 1
        continue
    errl += 1
    filename_end = get_filename(line)
    last_colon = get_last_colon(line)
    if filename_end != 0:
        n = random.randint(0, len(WISE_COMPILER) - 1)
        print(WISE_COMPILER[n] + line[last_colon + 1:-1] + " in " + line[:filename_end], end=" ")
        
    else:
        print("Oh, and the compiler also said this: " + line[:-1], end=" ")
    # print(emoji.emojize(' :blue_heart:'))
    print_random_emoji()
    print()

print("This must be difficult to hear. But don't worry. You'll debug it, I'm sure.", end= " ")
print(u'\U0001F4AA')
print()
print("All the best,")
print()
print("Your friendly compiler messenger.")
