# fuyoal
Deniable encryption software

## Table of Contents
1. [About Fuyoal](#about-fuyoal)
1. [Working](#working)
1. [License and Warranty](#license-and-warranty)
1. [Known Liabilities](#known-liabilities)
1. [Usage](#usage)
	1. [Command Line Interface](#command-line-interface)
		1.  [Details:](#details)
	1.  [Graphical User Interface](#graphical-user-interface)
1. [Screenshots](#screenshots)
1. [Dependencies](#dependencies)
1. [Download Windows Binnaries](#download-windows-binnaries)
1. [Contact](#contact)


## About Fuyoal

In many countries [key disclosure](https://en.wikipedia.org/wiki/Key_disclosure_law) law requires individuals to reveal their encryption keys to police and other law enforcement agencies. Non-compliance may result in serious repercussions. One way to handle this intrusion is to conceal some content in a way preventing any proof of its existence.

[Deniable encryption](https://en.wikipedia.org/wiki/Deniable_encryption) refers to a situation when an adversary cannot prove that concealed content exists. The most commonly discussed form of deniable encryption is steganography. It is a technique fit for some purposes, but inadequate for general use. Firstly, because it usually takes much larger content to hide the target one. Secondly, because pure steganography dos not fulfill [Kerckhoffs's principle](https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle).

Alternative approach consist in hiding secret content along with evident albeit encrypted content. In an ideal situation the concealed content is hidden perfectly i.e., an adversary has no means of finding out that the secret part exists. However there is generally no way of decrypting one ciphertext into two sets of plain content if the key is shorter than the content. The strategy adopted by Fuyoal is a little different. If it is impossible to make single file and facade-concealed pair indistinguishable by making them look like single file, let us make them indistinguishable by making everything look like facade-concealed pairs. Thus Fuyoal transforms each single file and each facade-concealed pair of files into one encrypted file that reveals no information whether the second of its two volumes is real message or random blather.

Most of versatile deniable encryption tools include low level hiding techniques like creating multiple encrypted disk volumes within a container volume. These tools are difficult to use in portable form or in general without deep integration with computer operational system. Fuyoal encrypts and decrypts selected files without any demanding system dependencies. It also does not leave any tracks in operational system other than the ones left by ordinary file manipulation.

## Working

Fuyoal encrypts two volumes of data (using AES-256) with two keys and concatenates them together. The encrypted file contains information about the size of the first volume in order make it possible to separate one of the volumes. The first volume is always the real file to be encrypted, the second one can be either another file or a block of zeros encrypted with a random key. The output file has the following structure:

| Size of first volume (8 B) | IV 1 (16 B) | Key verification constant 1 (32 B) | Encrypted file 1 | Padding 1 (1-32 B) | IV 2 (16 B) | Key verification constant 2 (32 B) | Encrypted file 2 | Padding 2 (1-32 B) |
|----------------------------|-------------|------------------------------------|------------------|--------------------|-------------|------------------------------------|------------------|--------------------|

When decrypting, provided key is tested on the first key verification constant. If its validity is proven the key is used to decrypt the first volume. If the key does not fit, it is tested on the second key verification constant. If it appears to be valid, the second volume is decrypted. If it does not, the decryption fails.

Each key is hashed (using SHA-256) one milion times before aplying to hinder possible bruteforce attack on a key.

## License and Warranty

The program and this documentation is available under [GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0).

Fuyoal comes with absolutely no warranty.

## Known Liabilities

In the case of encryption of one (real) file the size of the second (phony) file is drawn from truncated normal distribution. The mean of the distribution equals the size of the real file, the standard deviation equals 10% of the size of the real file, and boundaries are set 30% of the size of the real file below and above the mean. This strategy should work fine when encrypting several files and when both the real and the facade files are similarly sized. However with a large number of files (both single ones and facade-concealed pairs), the difference between the distribution mentioned above and that of the sizes of the concealed files may become noticeable. This could give an adversary a (probabilistic) knowledge as to which encrypted files contain a hidden partition.

This problem can be solved by replacing the automatic generation of the phony files’ size with a process that would result in indistinguishable distributions of second partitions' sizes in both groups of files. This would require the following steps. First, encryption of all (or a large representative sample of) facade-concealed pairs. Second, estimation of the distribution of the second partition's size (conditionaly on the size of the first partition). Third, encryption of the single files using explicit setup of the second partition's size (also conditionaly on the size of the first one) to mimic the previously estimated distribution. This strategy reduces chances of an adversary to distinguish between single and double encrypted files.

Also:

![xkcd.com/538/](https://imgs.xkcd.com/comics/security.png)

(https://xkcd.com/538/)

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

## Download Windows Binnaries
Windows precompiled binnaries can be download from here:

| Resource               | File                                                             | Size     | Version |
|------------------------|------------------------------------------------------------------|----------|---------|
| Windows binaries (CLI) | [fuyoal.exe](http://tsmolen.eu/fuyoal/download/fuyoal.exe)       | 10.27 MB | 1.1     |
| Windows binaries (GUI) | [guifuyoal.exe](http://tsmolen.eu/fuyoal/download/guifuyoal.exe) | 15.87 MB | 1.1     |

## Contact
Contact the author via his [web page](http://tsmolen.eu/).
