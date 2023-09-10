import time
import hashlib
chars = ["~","!","@","#","$","%","^","&","*","-","_","=","+","|","\\","/",",",";",":",""]

def calculate_sha1_hash(input_string):

    sha1_hash = hashlib.sha1()
    sha1_hash.update(input_string.encode('utf-8'))
    hash_hex = sha1_hash.hexdigest()
    return hash_hex


with open('hash_sha1.txt', 'w') as file:
    while True:
        current_utc_timestamp = int(time.time())
        for i in chars:
                text0 = f"test@test.com{i}{current_utc_timestamp}"
                text1 = f"{current_utc_timestamp}{i}test@test.com"
                # print(text0)
                # print(text1)
                # file.write(f"{text0}\n{text1}\n")

                sha1_hash0 = calculate_sha1_hash(text0)
                sha1_hash1 = calculate_sha1_hash(text1)
                print(f"{sha1_hash0}\n{sha1_hash1}\n")

                file.write(f"{sha1_hash0}\n{sha1_hash1}\n")
        time.sleep(0.8)




