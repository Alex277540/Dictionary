import json
import time
import os
import sys
from difflib import get_close_matches


print("""
                 ==> Simple Dictionary Of Words
                    ==> Created By: Mohamed Dief
                       ==> Enter (-exit) For Exit The Program

""")

print("[1]Start")
print("[2]Contact Me")
print("[3]Exit")

c = input("\n==> ")

if c == '1':
    pass
elif c == '2':
    print("Wait...")
    time.sleep(4)
    print("\n[+]Github: github.com/DEMON1A")                    
    print("[+]Facebook: facebook.com/mohamed.dief.1029")      
    print("[+]Twitter: twitter.com/Demon77098812")            
    print("[+]Email: mdaif1332@gmail.com")
    start = input("\nDo You Want Start? Y For Start. N for stop..!: ")
    if start == "Y":
        pass
    else:
        sys.exit()
        
else:
    sys.exit()

data = json.load(open("data.json"))
#Load data from json file , Do not download script without it! 

def words(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w , data.keys())) > 0:
        y_or_n = input("Did You Mean {0}? If Yes Put Y If No Put N: " .format(get_close_matches(w , data.keys())[0]))
        if y_or_n == "Y":
            return data[get_close_matches(w , data.keys())[0]]
        elif y_or_n == "N":
            return "Sorry This Word Does Not Exist, Check it again..."
        else:
            return "Sorry We Did't Understand Your Entry..."

    else:
        return "Sorry This Word Does Not Exist, Check it again..." 
#Check The Word on data file or not and return the Definition of the word...

word = input("\nEnter Word: ")
#Ask the user for the word he wants to define

if word == "-exit":
    sys.exit()

output = words(word)

if type(output) == list:
    for item in output:
        print(item)


