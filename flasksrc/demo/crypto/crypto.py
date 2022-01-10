from flask import request


# safe
def pycryptodome_aes():
    text = request.args.get('text', '')
    from Crypto.Cipher import AES
    cipher = AES.new(b'1234567812345678', AES.MODE_OFB)
    msg = cipher.iv + cipher.encrypt(bytes(text, 'utf-8'))
    return msg


def pycryptodome_blowfish():
    text = request.args.get('text', '')
    from Crypto.Cipher import Blowfish
    cipher = Blowfish.new(b'1234', Blowfish.MODE_OFB)
    msg = cipher.iv + cipher.encrypt(bytes(text, 'utf-8'))
    return msg


def pycryptodome_des():
    text = request.args.get('text', '')
    from Crypto.Cipher import DES
    cipher = DES.new(b'12345678', DES.MODE_OFB)
    msg = cipher.iv + cipher.encrypt(bytes(text, 'utf-8'))
    return msg


def pycryptodomex_blowfish():
    text = request.args.get('text', '')
    from Cryptodome.Cipher import Blowfish
    cipher = Blowfish.new(b'1234', Blowfish.MODE_OFB)
    msg = cipher.iv + cipher.encrypt(bytes(text, 'utf-8'))
    return msg


def pycryptodomex_des():
    text = request.args.get('text', '')
    from Cryptodome.Cipher import DES
    cipher = DES.new(b'12345678', DES.MODE_OFB)
    msg = cipher.iv + cipher.encrypt(bytes(text, 'utf-8'))
    return msg
