import os
dn = ".villagerLoader"
config = None
def read(fn):
	try:
		h = open(fn)
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
			co[2] = inp
	tw = ""
	for o in co:
		tw+=o[0]+"]["+o[2]+"\n"
	os.mkdir('.villagerLoader')
	h = open(dn+"/config.txt",'w+')
	h.write(tw)
	h.close()
	config = read(dn+"/config.txt")
