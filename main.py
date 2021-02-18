#wenn auf desktop ausgeführt; Module 'qrcode' und 'pandas' über 'pip install' installieren 
#excel sheet als CSV mit kommata getrennt exportieren und in selben Ordner des Scripts einfügen
#img Ordner anlegen wenn keiner Existiert

import qrcode
import pandas
import os
#from os import path

'''
userDesktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
print("{}\img".format(userDesktop))

def checkDirectory(): 
	if (path.exists("{}\img".format(userDesktop)) != True):
		os.mkdir("{}\img".format(userDesktop))
'''

#checkDirectory()

def swapSemicolon(input):
	#austauschen von Semikolons zu kommas
	text = open(input,"r")
	text = ''.join([i for i in text]) \
    .replace(";", ",")
	x = open("temp.csv","w")
	x.writelines(text)
	x.close()


def generateQRCodes(input):
	
	swapSemicolon(input)
	#checkDirectory()

	input = pandas.read_csv("temp.csv")

	#Iteration über die Zeilen der CSV und auslesung der Links mit pandas
	for index, values in input.iterrows():
		#temp = "{}\img\{}.png".format(userDesktop,values["Names"])
		temp = "img\{}.png".format(values["Names"])
		#Prüfen ob Link Feld leer ist
		if(str(values["Links"]) != "nan"):
			#generieren der QR codes im img ordner in der selben directory
			img = qrcode.make(values["Links"])
			img.save(temp)
	os.remove("temp.csv")