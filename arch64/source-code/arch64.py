# Coding by emirix7 from Arch4ea all rights reserved

import base64
from art import tprint
import sys

tprint("Arch4ea")
print("----------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------")
print("\n")

encode = "e"
decode = "d"

def decoder_base64():
    base64_str = input("Enter The Base64 -->  ")
    base64_bayt = base64_str.encode("ascii")
  
    string_bayt = base64.b64decode(base64_bayt)
    emir_string = string_bayt.decode("ascii")
    
    print("\n")
    print("Decoded String --> {0}".format(emir_string))

def encoder_base64():
    base64_st = input("Enter The String -->  ")
    
    encodedBayts = base64.b64encode(base64_st.encode("utf-8"))
    encodedSt = str(encodedBayts, "utf-8")
    
    print("\n")
    print("Encoded String --> {0}".format(encodedSt))

# Coding by emirix7 from Arch4ea all rights reserved
    
while(True):    
 soru = input("Encode Or Decode ? (e,d) -->  ")

 if(soru == decode):
    decoder_base64()
    break
    
 elif(soru == encode):
    encoder_base64()
    break
   
 else:
    print("No Such Option")
        
input("\n\tPress Enter To Exit")

# Coding by emirix7 from Arch4ea all rights reserved       