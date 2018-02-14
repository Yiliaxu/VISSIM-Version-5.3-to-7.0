import linecache
import xml.etree.ElementTree as etree
import xml.dom.minidom as doc
import numpy as np
import string,re,os

	

if __name__ == '__main__':
	vehicleInputs = doc.Document()
	root = vehicleInputs.createElement('vehicleInputs')
	vehicleInputs.appendChild(root)

	os.chdir("D:\Journal_paper\STPM\Caohejing_vissim")
	inpinput = linecache.getlines("Caohejing_STPM.inp")[2311:2396]


	for i in np.arange(0,len(inpinput)/5):
		line0 = inpinput[i*5+0].split()
		line1 = inpinput[i*5+1].split()
		line2 = inpinput[i*5+2].split()
		vehicleInput = vehicleInputs.createElement('vehicleInput')
		vehicleInput.setAttribute('anmFlag','false')
		vehicleInput.setAttribute('link',line2[1])
		vehicleInput.setAttribute('name',line1[1][1:len(line1[1])-1])
		vehicleInput.setAttribute('no',line0[1])
		timeIntVehVols = vehicleInputs.createElement('timeIntVehVols')
		timeIntervalVehVolume = vehicleInputs.createElement('timeIntervalVehVolume')
		timeIntervalVehVolume.setAttribute('cont','false')
		timeIntervalVehVolume.setAttribute('timeInt','1 0')
		timeIntervalVehVolume.setAttribute('vehComp','1')
		timeIntervalVehVolume.setAttribute('volType','STOCHASTIC')
		timeIntervalVehVolume.setAttribute('volume',line2[3])
		timeIntVehVols.appendChild(timeIntervalVehVolume)
		vehicleInput.appendChild(timeIntVehVols)
		root.appendChild(vehicleInput)


	
	fp = open('E:\CHJ_V7\input.xml','w')
	vehicleInputs.writexml(fp,indent='\t', addindent='\t',newl='\n',encoding="utf-8")

