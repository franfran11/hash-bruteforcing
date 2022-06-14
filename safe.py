import hashlib
import sys
import time

template = """                                                                                                       
   .                                .                         .                             .          
 .'|                              .'|                       .'|                           .'|          
<  |                             <  |                     .'  |       .-,.--.           .'  |          
 | |             __               | |                    <    |       |  .-. |    __   <    |          
 | | .'''-.   .:--.'.         _   | | .'''-.              |   | ____  | |  | | .:--.'.  |   | ____     
 | |/.'''. \ / |   \ |      .' |  | |/.'''. \             |   | \ .'  | |  | |/ |   \ | |   | \ .'     
 |  /    | | `" __ | |     .   | /|  /    | |             |   |/  .   | |  '- `" __ | | |   |/  .      
 | |     | |  .'.''| |   .'.'| |//| |     | |             |    /\  \  | |      .'.''| | |    /\  \     
 | |     | | / /   | |_.'.'.-'  / | |     | |             |   |  \  \ | |     / /   | |_|   |  \  \    
 | '.    | '.\ \._,\ '/.'   \_.'  | '.    | '.            '    \  \  \|_|     \ \._,\ '/'    \  \  \   
 '---'   '---'`--'  `"            '---'   '---'          '------'  '---'       `--'  `"'------'  '---' 
 Help options: -w:wordlists.txt
                hash_file
 example : crack.py -w:wordlists.txt hashes.txt 
"""


if "-h" in sys.argv[1]:
    print(template)
    exit()

if "-w" in sys.argv[1]:
    wordlists = sys.argv[1].strip("-w:")
    try:
        with open(wordlists, "r", encoding="latin-1") as file:
            content = file.readlines()
    except FileNotFoundError:
        print("FileNotFound")
        exit()

hashes = sys.argv[2]
try:
    with open(hashes, "r") as file:
        encrypted = file.readlines()
except FileNotFoundError:
    print("FileNotFound")
    exit()
passlist = [i.strip("\n") for i in content]
hashes = [crypted.strip("\n") for crypted in encrypted]
cracked = 0

start = time.time()
for has in hashes:
    for i in passlist:
        v = i.encode('utf-8')
        guess = hashlib.md5(v).hexdigest()
        if guess == has:
            print(f"Password for {has} is {i}")
            cracked += 1

        if len(hashes) == cracked:
            print("No more hashes to crack")
            end = time.time()
            print(f"cracked in {round(end-start)}")
            exit()
        else:
            pass


print(f"password not found, hashes cracked : {cracked}/{len(hashes)}")
