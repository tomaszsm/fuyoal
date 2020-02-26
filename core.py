import os
import random as regran
import shutil
import struct
import sys
from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA256


class edcr():
    def __init__(self):
        self.testconstant = bytes("Arguing that you don't care abou","ascii")
        self.hashfactor = 1000000


    def encrypt_file1(self,filein,key,sizealt,output):
        if(not os.path.isfile(filein)):
            print("fuyoal: File " + filein + " does not exist!")
            return(-1)
        if(sizealt):
            phonyfsize = sizealt
        else:
            orginfsize = os.path.getsize(filein)
            phonyfsize = self.randomsize(orginfsize, orginfsize*.1, orginfsize*.3)
        iterator = 0
        while(os.path.isfile("fuyoaltemp" + str(iterator))):
            iterator += 1
        phonyfile = "fuyoaltemp" + str(iterator)
        with open(phonyfile, 'wb') as outfile:
            outfile.seek(phonyfsize-1)
            outfile.write(b"\0")
        randomkey = Random.get_random_bytes(32)
        ret = self.encrypt_file2(filein,key,phonyfile,randomkey,output)
        os.remove(phonyfile)
        if(os.path.isfile(phonyfile)):
            return(-1)
        else:
            return(ret)


    def encrypt_file2(self,filein1,key1,filein2,key2,output):
        if(not os.path.isfile(filein1)):
            print("fuyoal: File " + filein1 + " does not exist!")
            return(-1)
        if(not os.path.isfile(filein2)):
            print("fuyoal: File " + filein2 + " does not exist!")
            return(-1)

        iterator1 = 0
        while(os.path.isfile(filein1 + str(iterator1))):
            iterator1 += 1
        fileout1 = filein1 + str(iterator1)
        iterator2 = 0
        while(os.path.isfile(filein2 + str(iterator2))):
            iterator2 += 1
        fileout2 = filein2  +str(iterator2)

        f1size = self.encrypt(filein1, fileout1, key1, 32)
        self.encrypt(filein2, fileout2, key2, 32)

        f1size_s = struct.pack("Q",f1size)

        if(output):
            outfile = output
        else:
            outfile = filein1+".fya"
        try:
            with open(outfile, 'wb') as destination:
                destination.write(f1size_s)
                shutil.copyfileobj(open(fileout1,'rb'), destination)
                shutil.copyfileobj(open(fileout2,'rb'), destination)
            os.remove(fileout1)
            os.remove(fileout2)
        except IOError:
            os.remove(fileout1)
            os.remove(fileout2)
            return(-2)

        return(0)


    def decrypt_file(self,filein,key,output):
        if(not os.path.isfile(filein)):
            print("fuyoal: File " + filein + " does not exist!")
            return(-1)
        if(output):
            fileout = output
        elif(filein[-4:]==".fya"):
            fileout = filein[:-4]
        else:
            fileout = filein+".dec"
        ret = self.decrypt(filein, fileout, key, 32)
        return(ret)


    def randomsize(self,size,par1,par2):
        regran.seed(os.urandom(64))
        ret = regran.gauss(size,par1)
        while(abs(ret-size) > par2):
            ret = regran.gauss(size,par1)
        return(int(round(ret)))


    def pad(self,s,bs):
        return(s + bytes((bs - len(s) % bs) * chr(bs - len(s) % bs),"ascii"))


    def unpad(self,s):
        return(s[0:-s[-1]])


    def encrypt(self,filein, fileout, keya, bs):
        key = self.hash_key(keya,self.hashfactor)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        filesize = os.path.getsize(filein)
        breakafter = False
        with open(filein, 'rb') as infile:
            with open(fileout, 'wb') as outfile:
                outfile.write(iv)
                outfile.write(cipher.encrypt(self.testconstant))
                blockcounter = 0
                while True:
                    chunk = infile.read(bs)
                    if(len(chunk) == 0):
                        breakafter = True
                        chunk = self.pad(b"",bs)
                    elif(len(chunk) % bs != 0):
                        breakafter = True
                        chunk = self.pad(chunk,bs)
                    blockcounter += 1
                    outfile.write(cipher.encrypt(chunk))
                    if(breakafter):
                        break
        return(blockcounter)


    def decrypt(self,filein, fileout, keya, bs):
        key = self.hash_key(keya,self.hashfactor)
        with open(filein, 'rb') as infile:
            try:
                f1size_s = infile.read(8)
                f1size = struct.unpack("Q",f1size_s)[0]
            except:
                return(-3)

            iv = infile.read(AES.block_size)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            if(cipher.decrypt(infile.read(32)) == self.testconstant):
                decryptfile = 0
            else:
                infile.seek(8 + AES.block_size + (f1size+1)*bs, 0)
                iv = infile.read(AES.block_size)
                cipher = AES.new(key, AES.MODE_CBC, iv)
                if(cipher.decrypt(infile.read(32)) == self.testconstant):
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
                        outfile.write(self.unpad(cipher.decrypt(chunk)))
                        return(0)
                    else:
                        outfile.write(cipher.decrypt(chunk))
                        chunk = nextchunk


    def hash_key(self,key,rep):
        h = SHA256.new()
        for i in range(rep):
            h.update(key)
        return(h.digest())
