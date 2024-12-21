# fuyoal

Each key is hashed (using SHA-256) one milion times before aplying to hinder possible bruteforce attack on a key.

## License and Warranty

The program and this documentation is available under [GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0).

Fuyoal comes with absolutely no warranty.

## Known Liabilities

In the case of encryption of one (real) file the size of the second (phony) file is drawn from truncated normal distribution. The mean of the distribution equals the size of the real file, the standard deviation equals 10% of the size of the real file, and boundaries are set 30% of the size of the real file below and above the mean. This strategy should work fine when encrypting several files and when both the real and the facade files are similarly sized. However with a large number of files (both single ones and facade-concealed pairs), the difference between the distribution mentioned above and that of the sizes of the concealed files may become noticeable. This could give an adversary a (probabilistic) knowledge as to which encrypted files contain a hidden partition.

This problem can be solved by replacing the automatic generation of the phony files’ size with a process that would result in indistinguishable distributions of second partitions' sizes in both groups of files. This would require the following steps. First, encryption of all (or a large representative sample of) facade-concealed pairs. Second, estimation of the distribution of the second partition's size (conditionaly on the size of the first partition). Third, encryption of the single files using explicit setup of the second partition's size (also conditionaly on the size of the first one) to mimic the previously estimated distribution. This strategy reduces chances of an adversary to distinguish between single and double encrypted files.

Also:

![xkcd.com/538/](https://imgs.xkcd.com/comics/security.png)

## Usage
### Command Line Interface

Fuyoal is to be used as follows:
```
usage: 
    fuyoal -h
    fuyoal -e FILE1 KEY1 [-s SIZE | -a FILE2 KEY2] [-o FILE]
    fuyoal -d FILE1 KEY1 [-o FILE]

positional arguments:
    FILE1                 input file for encryption or decryption
    KEY1                  key for encryption or decryption

optional arguments:
    -h, --help            show this help message and exit
    -e, --encrypt         encrypt FILE1 with KEY1
    -d, --decrypt         decrypt FILE1 with KEY1
    -s SIZE, --size SIZE  size of phony volume added to ane encrypted file
    -a FILE2 KEY2, --add FILE2 KEY2
			  second file, key pair for encryption
    -o FILE, --output FILE
			  write output to FILE
```
#### Details:
```
fuyoal -h
```
displays information about program and help message presented above.
```
fuyoal -e FILE1 KEY1
```
encrypts FILE1 with KEY1 and adds random part to make it impossible to discriminate this case from the case when two files are encrypted together. The size of the phony part is drawn from truncated normal distribution (see Known Liabilities for details). The output is saved to file FILE1.fya.
```
fuyoal -e FILE1 KEY1 -s SIZE
```
encrypts FILE1 with KEY1 and adds random part to make it impossible to discriminate this case from the case when two files are encrypted together. The size of the phony part is specified by SIZE parameter in bytes. The output is saved to file FILE1.fya.
```
fuyoal -e FILE1 KEY1 -a FILE2 KEY2
```
encrypts FILE1 with KEY1 and FILE2 with KEY2 and saves them together to file FILE1.fya.
```
fuyoal -d FILE1 KEY1
```
depending on KEY1 either decrypts the first (when two files were encrypted together) or the only file (when just one file was encrypted), or decrypts the second (hidden) file (when two files were encrypted together). The input is encrypted FILE1.
```
fuyoal (-e | -d) FILE1 KEY1 [options] -o FILE
```
encrypts or decrypts files according to options and saves output to FILE.

### Graphical User Interface
Using GUI version of the program is pretty self-explanatory (see screen).

## Screenshots
![Screenshot](http://tsmolen.eu/fuyoal/screen.png)

## Dependencies
Running the program from source requires Python 3.x with [Cryptodome](https://pycryptodome.readthedocs.io/en/latest/) package. Besides that GUI version requires [wxPython](https://www.wxpython.org/) package.

Windows binaries require Microsoft Windows operating system or emulator of it.

## Contact
Contact the author via his [web page](http://tsmolen.eu/).
