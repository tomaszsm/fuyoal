#!/usr/bin/python3

from core import *

import argparse
import gettext

class VersionedHelp(argparse.HelpFormatter):
    def _format_usage(self, usage, actions, groups, prefix=None):
        if prefix is None:
            prefix = gettext.gettext("fuyoal 1.0 Deniale encryption software. http://tsmolen.eu/fuyoal\n\nusage:")
        return argparse.HelpFormatter._format_usage(self, usage, actions, groups, prefix)

class program():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            formatter_class=VersionedHelp,usage="\n  fuyoal -h\n  fuyoal -e FILE1 KEY1 [-s SIZE | -a FILE2 KEY2] [-o FILE]\n  fuyoal -d FILE1 KEY1 [-o FILE]")
        self.grsa = self.parser.add_mutually_exclusive_group()
        self.gred = self.parser.add_mutually_exclusive_group(required=True)
        self.parser.add_argument("FILE1",         nargs=1, help="input file for encryption or decryption")
        self.parser.add_argument("KEY1",          nargs=1, help="key for encryption or decryption")
        self.gred.add_argument("-e", "--encrypt", help="encrypt FILE1 with KEY1", action="store_true")
        self.gred.add_argument("-d", "--decrypt", help="decrypt FILE1 with KEY1", action="store_true")
        self.grsa.add_argument("-s", "--size",    nargs=1, help="size of phony volume added to ane encrypted file", type=self.positive_int, default=[False])
        self.grsa.add_argument("-a", "--add",     nargs=2, metavar=("FILE2","KEY2"), help="second file, key pair for encryption", default=[False])
        self.parser.add_argument("-o", "--output",nargs=1, metavar=("FILE"), help="write output to FILE", default=[False])
        self.args = self.parser.parse_args()
        
    def main(self,argv):
        edc = edcr()
        if(self.args.encrypt):
            if(self.args.add[0]):
                self.ret = edc.encrypt_file2(self.args.FILE1[0],bytes(self.args.KEY1[0],"utf8"),
                                             self.args.add[0],bytes(self.args.add[1],"utf8"),self.args.output[0])
                if(self.ret==-2):
                    print("fuyoal: Could not write to file!")
            else:
                self.ret = edc.encrypt_file1(self.args.FILE1[0],bytes(self.args.KEY1[0],"utf8"),self.args.size[0],self.args.output[0])
                if(self.ret==-2):
                    print("fuyoal: Could not write to file!")
        else:
            self.ret = edc.decrypt_file(self.args.FILE1[0],bytes(self.args.KEY1[0],"utf8"),self.args.output[0])
            if(self.ret==-2):
                print("fuyoal: Wrong key!")
            if(self.ret==-3):
                print("fuyoal: Input error!")

    def positive_int(self,string):
        value = int(string)
        if value < 1:
            msg = "%r is not a positive integer" % string
            raise argparse.ArgumentTypeError(msg)
        return value

    
if __name__ == "__main__":
    prg = program()
    prg.main(sys.argv[1:])
   
