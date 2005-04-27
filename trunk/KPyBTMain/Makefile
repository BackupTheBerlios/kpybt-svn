MAKE=make
SUBDIRS = Forms KPyBTWidgets

all: GenerateSource

GenerateSource: $(SUBDIRS)
	cd $< ; make 

clean: $(SUBDIRS)
	rm -f *.pyc
	for i in $(SUBDIRS) ; do cd $$i ; make $@ ; cd .. ; done

