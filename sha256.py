import time
import hashlib

def calculate_sha256_hash(input_string):

    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    hash_hex = sha256_hash.hexdigest()
    return hash_hex


with open('sha256_hash.txt', 'w') as file:

    while True:
        current_utc_timestamp = int(time.time())

        input_string = f"test@test.com-{current_utc_timestamp}"
        sha256_hash = calculate_sha256_hash(input_string)
        print(sha256_hash)
        file.write(f"{sha256_hash}\n")
        time.sleep(1)