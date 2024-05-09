import calendar
import datetime
import random
from Crypto.Cipher import AES
import binascii
import time
import calendar
# from datetime import datetime, timezone, timedelta
import time


plaintext = binascii.unhexlify("255044462d312e350a25d0d4c5d80a34")
ciphertext = binascii.unhexlify("d06bf9d0dab8e8ef880660d2af65aa82")
iv = binascii.unhexlify("09080706050403020100A2B2C2D2E2F2")

output_file ="text.txt"

with open(output_file, 'r') as file:
    for line in file:
        line, timeStamp = line.split(",")
        keyinHex = line
        clean_input_string = ''.join(filter(lambda x: x in '0123456789ABCDEFabcdef', line))
        line = binascii.unhexlify(clean_input_string)
        aes_cipher = AES.new(line, AES.MODE_CBC, iv)
        myoutput = aes_cipher.decrypt(ciphertext)
        if myoutput == plaintext:
            print("Key Succesfully found")
            print("The Key is:", keyinHex)
            normal_date = datetime.datetime.utcfromtimestamp(int(timeStamp))
            print("The Time that the document was encrypted was:", normal_date)
            break

print(datetime.datetime.utcfromtimestamp(1524020929))