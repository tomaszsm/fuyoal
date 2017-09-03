from core import *

def main(argv):
    if("-h" in argv):
        usage()
    elif(argv[0] == "-e"):
        if(len(argv)==3):
            encrypt_file1(argv[1],argv[2],False)
        elif(len(argv)==5):
            if(argv[3]=="-s"):
                try:
                    sizealt = int(argv[4])
                except:
                    print("fuyoal: Wrong size (-s) parameter!")
                    return(-1)
                encrypt_file1(argv[1],argv[2],sizealt)
            else:
                encrypt_file2(argv[1],argv[2],argv[3],argv[4])
        else:
            usage()
    elif(argv[0] == "-d"):
        if(len(argv)==3):
            ret = decrypt_file(argv[1],argv[2])
            if(ret==-2):
                print("fuyoal: Wrong key!")
            if(ret==-3):
                print("fuyoal: Input error!")
        else:
            usage()
    else:
        usage()


def usage():
    print("Usage:")
    print("  fuyoal -h")
    print("  fuyoal -e file1 key1 [-s size] | [file2 key2]")
    print("  fuyoal -d file key1 | key2")
    print("")
    print("Options:")
    print("  -h        Shows help message")
    print("  -e        Ensrypts file1 with key1 and possibly file2 with key2")
    print("  -s        Specify size of phony second file (in bytes)")
    print("  -d        Decrypts file with key")


if __name__ == "__main__":
   main(sys.argv[1:])
