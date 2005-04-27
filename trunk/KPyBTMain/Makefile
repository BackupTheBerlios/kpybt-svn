MAKE=make
SUBDIRS = Forms

all: GenerateSource

GenerateSource: $(SUBDIRS)
	cd $< ; make 

clean: $(SUBDIRS)
	cd $< ; make clean
