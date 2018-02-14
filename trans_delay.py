import linecache
import xml.etree.ElementTree as etree
import xml.dom.minidom as doc
import numpy as np
import string,re,os

	

if __name__ == '__main__':
	delayMeasurements = doc.Document()
	root = delayMeasurements.createElement('delayMeasurements')
	delayMeasurements.appendChild(root)

	os.chdir("D:\Journal_paper\STPM\Caohejing_vissim")
	inpdelay = linecache.getlines("Caohejing_STPM.inp")[3218:3266]
	

	for i in np.arange(0,len(inpdelay)/3):
		line1 = inpdelay[i*3].split()
		line2 = inpdelay[i*3+1].split()
		delayMeasurement = delayMeasurements.createElement('delayMeasurement')
		delayMeasurement.setAttribute('name','')
		delayMeasurement.setAttribute('no',line1[1])
		vehTravTmMeas = delayMeasurements.createElement('vehTravTmMeas')
		intObjectRef = delayMeasurements.createElement('intObjectRef')
		intObjectRef.setAttribute('key',line2[1])
		vehTravTmMeas.appendChild(intObjectRef)
		delayMeasurement.appendChild(vehTravTmMeas)
		root.appendChild(delayMeasurement)
	
	fp = open('E:\CHJ_V7\delaymeasurements.xml','w')
	delayMeasurements.writexml(fp,indent='\t', addindent='\t',newl='\n',encoding="utf-8")

