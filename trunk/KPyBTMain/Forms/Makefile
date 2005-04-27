PYUIC=kdepyuic
PY = 	KPyBTTorrentBase.py \
	KPyBTTorrentListBase.py \
	KPyBTCfgPageGlobalsBase.py \
	KPyBTCfgPageNetworkBase.py 






PYC =	KPyBTTorrentBase.pyc \
	KPyBTTorrentListBase.pyc \
	KPyBTCfgPageGlobalsBase.pyc \
	KPyBTCfgPageNetworkBase.pyc \






	
%.py : %.ui
	$(PYUIC) $< > $@


ALL: $(PY)

clean: 
	rm -f $(PY)
	rm -f $(PYC)

