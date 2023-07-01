password = "admin"

# sha1加密
def sha1_secret_str(s: str):
    import hashlib
    sha = hashlib.sha1(s.encode('utf-8'))
    encrypts = sha.hexdigest()
    return encrypts

value = sha1_secret_str(password)

# sha1解密



print(value)