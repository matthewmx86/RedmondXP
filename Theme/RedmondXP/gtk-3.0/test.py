import os,sys
searchstr = "alpha(shade(@selected_bg_color,0.8),0.8)"

def file(i,searchstr):
	fo = open(i,'r')
	strline = 0
	mute = False
	for line in fo:
		strline = strline + 1
		if "/*" in line:
			mute = True
		elif "*/" in line:
			mute = False

		if searchstr in line and mute == False:
			print(i+":"+str(strline)+">"\
			+line.replace("\n",""))
	fo.close()
	return(0)

for x in os.listdir():
	if ".css" in x:
		file(x,searchstr)

