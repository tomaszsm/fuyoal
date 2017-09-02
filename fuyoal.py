import hashlib
import os
import shutil
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
    if(not os.path.isfile(filein)):
        print("fuyoal: File " + filein + " does not exist!")
        return(-1)
    encrypt(filein, filein+".fya", key, 32)

    
def encrypt_file2(filein1,key1,filein2,key2):
    if(not os.path.isfile(filein1)):
        print("fuyoal: File " + filein1 + " does not exist!")
        return(-1)
    if(not os.path.isfile(filein2)):
        print("fuyoal: File " + filein2 + " does not exist!")
        return(-1)
    
    iterator1 = 0
    while(os.path.isfile(filein1+str(iterator1))):
        iterator1 += 1
    fileout1 = filein1+str(iterator1)
    iterator2 = 0
    while(os.path.isfile(filein2+str(iterator2))):
        iterator2 += 1
    fileout2 = filein2+str(iterator2)
    
    f1size = str(encrypt(filein1, fileout1, key1, 32))
    encrypt(filein2, fileout2, key2, 32)
    
    f1size = "0"*(32-len(f1size)) + f1size

    outfile = filein1+".fya"
    destination = open(outfile,'wb')
    destination.write(f1size)
    shutil.copyfileobj(open(fileout1,'rb'), destination)
    shutil.copyfileobj(open(fileout2,'rb'), destination)
    destination.close()
    # os.remove(fileout1)
    # os.remove(fileout2)
    
def decrypt_file(filein,key):
    if(not os.path.isfile(filein)):
        print("fuyoal: File " + filein + " does not exist!")
        return(-1)
    if(filein[-4:]==".fya"):
        fileout = filein[:-4]
    else:
        fileout = filein+".dec"
    print(decrypt(filein, fileout, key, 32, True))


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
            blockcounter = 0
            while True:
                chunk = infile.read(bs)
                if(len(chunk) == 0):
                    break
                elif(len(chunk) % bs != 0):
                    chunk += ' ' * (bs - len(chunk) % bs)
                blockcounter += 1
                outfile.write(cipher.encrypt(chunk))
    return(blockcounter)

                
def decrypt(filein, fileout, key, bs, oneblock):
    key2 = hashlib.sha256(key.encode()).digest()
    with open(filein, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)    # AES.block_size ?
        cipher = AES.new(key2, AES.MODE_CBC, iv)
        f1size = infile.read(32)
        if(cipher.decrypt(infile.read(32))!="Arguing that you don't care abou"):
            print("fuyoal: Wrong key!")
            return(-1)
        with open(fileout, 'wb') as outfile:
            while True:
                chunk = infile.read(bs)
                if(oneblock):
                    return(cipher.decrypt(chunk))
                if(len(chunk)==0):
                    break
                outfile.write(cipher.decrypt(chunk))
            outfile.truncate(origsize)

            
if __name__ == "__main__":
   main(sys.argv[1:])
