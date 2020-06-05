import base64
import json

from Crypto.Cipher import AES


def decrypt(encryptedData,session_key,iv,appid):
    try:
        session_key = base64.b64decode(session_key)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.decode(iv)
        cipher = AES.new(session_key,AES.MODE_CBC,iv)
        de = cipher.decrypt(encryptedData)
        decrypted = de[:-ord(de[len(de)-1:])]
        decrypted = json.load(decrypted)
        if decrypted['watermark']['appid'] != appid :
            return None

        return decrypted

    except:
        #todo
        return None
