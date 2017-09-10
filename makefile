.PHONY: all clean

all: fuyoal.exe guifuyoal.exe fuyoal_source.tar.gz clean

clean:
	-rm -r build
	-rm fuyoal.spec
	-rm core.pyc
	-rm guifuyoal.spec

fuyoal.exe: fuyoal.py core.py
	-rm -r dist
	pyinstaller --onefile --console fuyoal.py
	mv dist/fuyoal.exe fuyoal.exe
	-rm -r dist

guifuyoal.exe: guifuyoal.py core.py icon.ico
	-rm -r dist
	pyinstaller --onefile --windowed --icon=icon.ico guifuyoal.py
	mv dist/guifuyoal.exe guifuyoal.exe
	-rm -r dist

fuyoal_source.tar.gz: fuyoal.py guifuyoal.py core.py
	-rm fuyoal_source.tar
	-rm fuyoal_source.tar.gz
	tar -cf fuyoal_source.tar fuyoal.py guifuyoal.py core.py
	gzip fuyoal_source.tar
