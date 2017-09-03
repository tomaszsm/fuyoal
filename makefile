BASENAME=fuyoal

.PHONY: all clean

all: $(BASENAME).exe clean

clean:
	-rm -r build
	-rm $(BASENAME).spec

$(BASENAME).exe: $(BASENAME).py
	-rm -r dist
	-rm -r $(BASENAME)
	pyinstaller --onefile $(BASENAME).py # --windowed --icon=icon.ico
	mv dist/$(BASENAME).exe $(BASENAME).exe
	-rm -r dist

