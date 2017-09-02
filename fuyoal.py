import hashlib
import os
import struct
import sys
from Crypto import Random
from Crypto.Cipher import AES

def main(argv):
    if("-e" in argv):
        if(len(argv)==3):
            encrypt_file1(argv[1],argv[2])
        elif(len(argv)==5):
            encrypt_file2(argv[1],argv[2],argv[3],argv[4])
        else:
            usage()
    elif("-d" in argv):
        if(len(argv)==3):
            decrypt_file(argv[1],argv[2])
        else:
            usage()
    else:
        usage()


def usage():
    print("Usage:")
    print("  fuyoal -h")
    print("  fuyoal -e file1 key1 [file2 key2]")
    print("  fuyoal -d file key1 | key2")
    print("")
    print("Options:")
    print("  -h        Shows help message")
    print("  -e        Ensrypts file1 with key1 and possibly file2 with key2")
    print("  -d        Decrypts file with key")


def encrypt_file1(filein,key):
    encrypt(filein, filein+".fya", key, 32)


def decrypt_file(filein,key):
    if(filein[-4:]==".fya"):
        fileout = filein[:-4]
    else:
        fileout = filein+".dec"
    decrypt(filein, fileout, key, 32)


def encrypt(filein, fileout, key, bs):
    key2 = hashlib.sha256(key.encode()).digest()
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key2, AES.MODE_CBC, iv)
    filesize = os.path.getsize(filein)
    with open(filein, 'rb') as infile:
        with open(fileout, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)
            outfile.write(cipher.encrypt("Arguing that you don't care abou"))
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
        if(cipher.decrypt(infile.read(32))!="Arguing that you don't care abou"):
            print("fuyoal: Wrong key!")
            return(-1)
        with open(fileout, 'wb') as outfile:
            while True:
                chunk = infile.read(bs)
                if len(chunk) == 0:
                    break
                outfile.write(cipher.decrypt(chunk))
            outfile.truncate(origsize)

            
if __name__ == "__main__":
   main(sys.argv[1:])
