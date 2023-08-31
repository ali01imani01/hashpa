import time
import hashlib
chars = ["~","!","@","#","$","%","^","&","*","-","_","=","+","|","\\","/",",",";",":",""]

def calculate_sha256_hash(input_string):

    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    hash_hex = sha256_hash.hexdigest()
    return hash_hex


with open('hash_sha256.txt', 'w') as file:
    while True:
        current_utc_timestamp = int(time.time())
        for i in chars:
                text0 = f"test@test.com{i}{current_utc_timestamp}"
                text1 = f"{current_utc_timestamp}{i}test@test.com"
                # print(text0)
                # print(text1)
                # file.write(f"{text0}\n{text1}\n")
                sha256_hash0 = calculate_sha256_hash(text0)
                sha256_hash1 = calculate_sha256_hash(text1)
                print(f"{sha256_hash0}\n{sha256_hash1}\n")

                file.write(f"{sha256_hash0}\n{sha256_hash1}\n")
        time.sleep(0.8)
