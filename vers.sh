#!/bin/bash
cd d:/projekty/python/fuyoal

echo fuyoal_source.tar.gz
fsize=$(stat -c%s "fuyoal_source.tar.gz")
echo "scale=2; $fsize / 1024" | bc
echo `sha256sum "fuyoal_source.tar.gz"`
echo
echo fuyoal.exe
fsize=$(stat -c%s "fuyoal.exe")
echo "scale=2; $fsize / 1024 / 1024" | bc
echo `sha256sum "fuyoal.exe"`
echo
echo guifuyoal.exe
fsize=$(stat -c%s "guifuyoal.exe")
echo "scale=2; $fsize / 1024 / 1024" | bc
echo `sha256sum "guifuyoal.exe"`

# read -p "Press [Enter] key to start exit..."
