from core import *

import argparse

def main(argv):
    parser = argparse.ArgumentParser(usage="\n  fuyoal -h\n  fuyoal -e FILE1 KEY1 [-s SIZE | -a FILE2 KEY2] [-o FILE]\n  fuyoal -d FILE1 KEY1 [-o FILE]")
    grsa = parser.add_mutually_exclusive_group()
    gred = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument("FILE1",         nargs=1, help="Input file for encryption or decryption")
    parser.add_argument("KEY1",          nargs=1, help="Key for encryption or decryption")
    gred.add_argument("-e", "--encrypt", help="Encrypts FILE1 with KEY1", action="store_true")
    gred.add_argument("-d", "--decrypt", help="Decrypts FILE1 with KEY1", action="store_true")
    grsa.add_argument("-s", "--size",    nargs=1, help="Size of phony volume added to ane encrypted file", type=int, default=[False])
    grsa.add_argument("-a", "--add",     nargs=2, metavar=("FILE2","KEY2"), help="Second file, key pair for encryption", default=[False])
    parser.add_argument("-o", "--output",nargs=1, metavar=("FILE"), help="Writes output to FILE", default=[False])
    args = parser.parse_args()
    if(args.encrypt):
        if(args.add[0]):
            ret = encrypt_file2(args.FILE1[0],args.KEY1[0],args.add[0],args.add[1],args.output[0])
            if(ret==-2):
                print("fuyoal: Could not write to file!")
        else:
            ret = encrypt_file1(args.FILE1[0],args.KEY1[0],args.size[0],args.output[0])
            if(ret==-2):
                print("fuyoal: Could not write to file!")
    else:
        ret = decrypt_file(args.FILE1[0],args.KEY1[0],args.output[0])
        if(ret==-2):
            print("fuyoal: Wrong key!")
        if(ret==-3):
            print("fuyoal: Input error!")


if __name__ == "__main__":
   main(sys.argv[1:])
