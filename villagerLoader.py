import os
import urllib2
import urllib
import sys
import shutil
dn = ".villagerLoader"
config = None
def read(fn):
	try:
		if 'str' in str(type(fn)):
			h = open(fn)
		else:
			h = fn
		l = h.readlines()
		h.close()
		r = {}
		for L in l:
			spl = L.replace("\n", "").split('][')
			r[spl[0]] = spl[1:]
		return r
	except Exception as e:
		print "An error occured."
		print e
		exit(-1)
	return None
if os.path.isdir(dn):
	if os.path.isfile(dn+"/config.txt"):
		config = read(dn+"/config.txt")
if config == None:
	print "Welcome to Villager Loader!"
	print "First, a few questions."
	print "To use the default value, just press enter."
	co = [["src", "Pack URL", "http://colin.reederhome.net/villagerPack2.txt"], ["dir", "Install Directory", "."]]
	for o in co:
		inp = raw_input(o[1]+" ["+o[2]+"]:")
		if len(inp.strip())>0:
			o[2] = inp
	tw = ""
	for o in co:
		tw+=o[0]+"]["+o[2]+"\n"
	if not os.path.isdir(dn):
		os.mkdir('.villagerLoader')
	h = open(dn+"/config.txt",'w+')
	h.write(tw)
	h.close()
	config = read(dn+"/config.txt")
url = config["src"][0]
urllib.urlretrieve(url, dn+"/newThing.txt")
nd = read(dn+"/newThing.txt")
if not os.path.isdir(config["dir"][0]):
	os.mkdir(config["dir"][0])
ofn = dn+"/lastUpdated.txt"
od = None
if os.path.isfile(ofn):
	od = read(ofn)
	for d in od:
		tr = False
		if d in nd:
			if nd[d] != od[d]:
				tr = True
		else:
			tr = True
		if tr:
			print "Removing "+od[d][0]
			os.remove(config["dir"][0]+"/"+od[d][0])
shutil.move(dn+"/newThing.txt", ofn)
dat1 = False
for d in nd:
	td = False
	if od != None:
		if d not in od:
			td = True
		else:
			if od[d] != nd[d]:
				td = True
	else:
		td = True
	if td:
		print "Downloading "+nd[d][0]
		dat1 = True
		sys.stdout.flush()
		urllib.urlretrieve(nd[d][1], config["dir"][0]+"/"+nd[d][0])
if not dat1:
	print "Up to date!"
