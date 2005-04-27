MAKE=make
SUBDIRS = KPyBTMain

all: GenerateSource

GenerateSource: $(SUBDIRS)
	cd $< ; make 

clean: $(SUBDIRS)
	cd $< ; make $@
	
