import linecache
import xml.etree.ElementTree as etree
import xml.dom.minidom as doc
import numpy as np
import string,re,os

	

if __name__ == '__main__':
	vehicleTravelTimeMeasurements = doc.Document()
	root = vehicleTravelTimeMeasurements.createElement('vehicleTravelTimeMeasurements')
	vehicleTravelTimeMeasurements.appendChild(root)

	os.chdir("D:\Journal_paper\STPM\Caohejing_vissim")
	inptrveltime = linecache.getlines("Caohejing_STPM.inp")[3173:3211]
	for i in np.arange(0,len(inptrveltime)/2):
		line1 = inptrveltime[i*2].split()
		line2 = inptrveltime[i*2+1].split()
		vehicleTravelTimeMeasurement = vehicleTravelTimeMeasurements.createElement('vehicleTravelTimeMeasurement')
		vehicleTravelTimeMeasurement.setAttribute('name',line1[3][1:len(line1[3])-1])
		vehicleTravelTimeMeasurement.setAttribute('no',line1[1])
		start = vehicleTravelTimeMeasurements.createElement('start')
		start.setAttribute('link',line2[2])
		start.setAttribute('pos',line2[4])
		vehicleTravelTimeMeasurement.appendChild(start)
		end = vehicleTravelTimeMeasurements.createElement('end')
		end.setAttribute('link',line2[7])
		end.setAttribute('pos',line2[9])
		vehicleTravelTimeMeasurement.appendChild(end)
		root.appendChild(vehicleTravelTimeMeasurement)
	
	fp = open('E:\CHJ_V7\TravelTimeMeasurement.xml','w')
	vehicleTravelTimeMeasurements.writexml(fp,indent='\t', addindent='\t',newl='\n',encoding="utf-8")









	
