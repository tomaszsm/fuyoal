import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import struct

def encrypt(filein, fileout, key, bs):
    key2 = hashlib.sha256(key.encode()).digest()
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key2, AES.MODE_CBC, iv)
    filesize = os.path.getsize(filein)
    
    with open(filein, 'rb') as infile:
        with open(fileout, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(bs)
                if len(chunk) == 0:
                    break
                elif len(chunk) % bs != 0:
                    chunk += ' ' * (bs - len(chunk) % bs)
                    
                outfile.write(cipher.encrypt(chunk))
                
def decrypt(filein, fileout, key, bs):
    key2 = hashlib.sha256(key.encode()).digest()

    with open(filein, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)        
        cipher = AES.new(key2, AES.MODE_CBC, iv)

        with open(fileout, 'wb') as outfile:
            while True:
                chunk = infile.read(bs)
                if len(chunk) == 0:
                    break
                outfile.write(cipher.decrypt(chunk))

            outfile.truncate(origsize)

