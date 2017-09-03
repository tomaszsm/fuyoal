import binascii
import hashlib
import os
import shutil
import sys
from Crypto import Random
from Crypto.Cipher import AES
from random import gauss


def encrypt_file1(filein,key,sizealt):
    if(not os.path.isfile(filein)):
        print("fuyoal: File " + filein + " does not exist!")
        return(-1)
    if(sizealt):
        phonyfsize = sizealt
    else:
        orginfsize = os.path.getsize(filein)
        phonyfsize = randomsize(orginfsize, orginfsize*.1, orginfsize*.3)
    iterator = 0
    while(os.path.isfile("fuyoaltemp"+str(iterator))):
        iterator += 1
    phonyfile = "fuyoaltemp"+str(iterator)
    with open(phonyfile, 'wb') as outfile:
        for i in xrange(phonyfsize):
            outfile.write("0")
    ret = encrypt_file2(filein,key,phonyfile,binascii.b2a_base64(Random.get_random_bytes(32))[:32])
    os.remove(phonyfile)
    if(os.path.isfile(phonyfile)):
        return(-1)
    else:
        return(ret)
    
    
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
    with open(outfile, 'wb') as destination:
        destination.write(f1size)
        shutil.copyfileobj(open(fileout1,'rb'), destination)
        shutil.copyfileobj(open(fileout2,'rb'), destination)
    os.remove(fileout1)
    os.remove(fileout2)

    return(0)
    
def decrypt_file(filein,key):
    if(not os.path.isfile(filein)):
        print("fuyoal: File " + filein + " does not exist!")
        return(-1)
    if(filein[-4:]==".fya"):
        fileout = filein[:-4]
    else:
        fileout = filein+".dec"
    ret = decrypt(filein, fileout, key, 32)
    return(ret)


def randomsize(size,par1,par2):
    ret = gauss(size,par1)
    while(abs(ret-size) > par2):
        ret = gauss(size,par1)
    return(int(round(ret)))
    
    
def pad(s,bs):
    return(s + (bs - len(s) % bs) * chr(bs - len(s) % bs))

def unpad(s):
    return(s[0:-ord(s[-1])])
    
def encrypt(filein, fileout, key, bs):
    key = hashlib.sha256(key.encode()).digest()
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(filein)
    breakafter = False
    with open(filein, 'rb') as infile:
        with open(fileout, 'wb') as outfile:
            outfile.write(iv)
            outfile.write(cipher.encrypt("Arguing that you don't care abou"))
            blockcounter = 0
            while True:
                chunk = infile.read(bs)
                if(len(chunk) == 0):
                    breakafter = True
                    chunk = pad("",bs)
                elif(len(chunk) % bs != 0):
                    breakafter = True
                    chunk = pad(chunk,bs)
                blockcounter += 1
                outfile.write(cipher.encrypt(chunk))
                if(breakafter):
                    break
    return(blockcounter)

                
def decrypt(filein, fileout, keya, bs):
    key = hashlib.sha256(keya.encode()).digest()
    with open(filein, 'rb') as infile:
        try:
            f1size = int(infile.read(32))
        except:
            return(-3)
            
        iv = infile.read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        if(cipher.decrypt(infile.read(32))=="Arguing that you don't care abou"):
            decryptfile = 0
        else:
            infile.seek(32 + AES.block_size + (f1size+1)*bs, 0)
            iv = infile.read(AES.block_size)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            if(cipher.decrypt(infile.read(32))=="Arguing that you don't care abou"):
                decryptfile = 1
            else:
                return(-2)
        
        with open(fileout, 'wb') as outfile:
            chunk = infile.read(bs)
            iterator = 0
            while True:
                iterator += 1
                nextchunk = infile.read(bs)
                if(len(nextchunk)==0 or (decryptfile==0 and iterator>=f1size)):
                    outfile.write(unpad(cipher.decrypt(chunk)))
                    return(0)
                else:
                    outfile.write(cipher.decrypt(chunk))
                    chunk = nextchunk
