import time
import hashlib
chars = ["~","!","@","#","$","%","^","&","*","-","_","=","+","|","\\","/",",",";",":",""]

def calculate_md5_hash(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()


with open('hash_sha256.txt', 'w') as file:
    while True:
        current_utc_timestamp = int(time.time())
        for i in chars:
                text0 = f"test@test.com{i}{current_utc_timestamp}"
                text1 = f"{current_utc_timestamp}{i}test@test.com"
                # print(text0)
                # print(text1)
                # file.write(f"{text0}\n{text1}\n")
                sha256_hash0 = calculate_md5_hash(text0)
                sha256_hash1 = calculate_md5_hash(text1)
                print(f"{sha256_hash0}\n{sha256_hash1}\n")

                file.write(f"{sha256_hash0}\n{sha256_hash1}\n")
        time.sleep(0.8)
