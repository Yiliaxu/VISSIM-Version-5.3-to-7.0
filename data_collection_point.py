import xml.etree.ElementTree as etree
import xml.dom.minidom as doc
import numpy as np
import string,re,os



if __name__ == '__main__':
	dataCollectionPoints = doc.Document()
	root = dataCollectionPoints.createElement('dataCollectionPoints')
	dataCollectionPoints.appendChild(root)

	dataCollectionMeasurements = doc.Document()
	rootMeasurement = dataCollectionMeasurements.createElement('dataCollectionMeasurements')
	dataCollectionMeasurements.appendChild(rootMeasurement)

	inp = open(r"D:\Journal_paper\STPM\Caohejing_vissim\Caohejing_STPM.inp",'r')  
	IsThisPoint = 0
	counter = 0
	for line in inp.readlines():
		if line.startswith('COLLECTION_POINT'):
			IsThisPoint = 1
			line0 = line.split()
			dataCollectionPoint = dataCollectionPoints.createElement('dataCollectionPoint')
			dataCollectionPoint.setAttribute('name',line0[3][1:len(line0[3])-1])
			dataCollectionPoint.setAttribute('no',line0[1])

		if line.startswith('     POSITION LINK') and IsThisPoint==1:
			line0 = line.split()
			dataCollectionPoint.setAttribute('lane',line0[2]+' '+line0[4])
			dataCollectionPoint.setAttribute('pos',line0[6])
			IsThisPoint = 0
			root.appendChild(dataCollectionPoint)

		if line.startswith('CROSS_SEC_MEASUREMENT'):
			counter = counter + 1
			if counter>1:
				line0 = line.split()
				dataCollectionMeasurement = dataCollectionMeasurements.createElement('dataCollectionMeasurement')
				dataCollectionMeasurement.setAttribute('name','')
				dataCollectionMeasurement.setAttribute('no',line0[1])
				dataCollectionPoints0 = dataCollectionMeasurements.createElement('dataCollectionPoints')
				for i in np.arange(0,len(line0)-3):
					intObjectRef = dataCollectionMeasurements.createElement('intObjectRef')
					intObjectRef.setAttribute('key',line0[3+i])
					dataCollectionPoints0.appendChild(intObjectRef)
				dataCollectionMeasurement.appendChild(dataCollectionPoints0)
				rootMeasurement.appendChild(dataCollectionMeasurement)


	fp = open('E:\CHJ_V7\datapoint.xml','w')
	dataCollectionPoints.writexml(fp,indent='\t', addindent='\t',newl='\n',encoding="utf-8")
	fp1 = open('E:\CHJ_V7\datameasurement.xml','w')
	dataCollectionMeasurements.writexml(fp1,indent='\t', addindent='\t',newl='\n',encoding="utf-8")





	