import xml.etree.ElementTree as etree
import xml.dom.minidom as doc
import numpy as np
import string,re,os



if __name__ == '__main__':
	SC = doc.Document()	
	SCroot = SC.createElement('signalControllers')
	SC.appendChild(SCroot)
	signalController = SC.createElement('signalController')
	signalController.setAttribute('active','true')
	signalController.setAttribute('cycTm','0.000000')
	signalController.setAttribute('cycTmIsVar','true')
	signalController.setAttribute('debug','false')
	signalController.setAttribute('guiFile','VISSIG_GUI.dll')
	signalController.setAttribute('name','')
	signalController.setAttribute('no','1')
	signalController.setAttribute('offset','0.000000')
	signalController.setAttribute('progNo','1')
	signalController.setAttribute('scDetRecFile','Caohejing_1.ldp')
	signalController.setAttribute('scDetRecShortNam','false')
	signalController.setAttribute('sigTmsTabAutoConfig','true')
	signalController.setAttribute('supplyFile1','#exe#vissig.config')
	signalController.setAttribute('supplyFile2','#data#Caohejing_STPM1.sig')
	signalController.setAttribute('supplyFile3','')
	signalController.setAttribute('type','FIXEDTIME')
	SCroot.appendChild(signalController)
	
	SH = doc.Document()
	SHroot = SH.createElement('signalHeads')
	SH.appendChild(SHroot)

	inp = open(r"D:\Journal_paper\STPM\Caohejing_vissim\Caohejing_STPM.inp",'r')  
	sGs = SC.createElement('sGs')
	for line in inp.readlines():
		if line.startswith('SIGNAL_GROUP'):
			line0 = line.split()
			signalGroupnumber = line0[1]
			signalGroup = SC.createElement('signalGroup')
			signalGroup.setAttribute('amber','3.000000')
			signalGroup.setAttribute('greenFlsh','0.000000')
			signalGroup.setAttribute('minGreen','5.000000')
			signalGroup.setAttribute('minRed','0.000000')
			signalGroup.setAttribute('name',line0[3][1:]+' '+line0[4]+' '+line0[1])
			signalGroup.setAttribute('no',signalGroupnumber)
			signalGroup.setAttribute('redAmber','0.000000')
			signalGroup.setAttribute('type','NORMAL')
			sGs.appendChild(signalGroup)
		if line.startswith('  SIGNAL_HEAD'):
			line0 = line.split()
			signalHead = SH.createElement('signalHead')
			signalHead.setAttribute('allPedTypes','true')
			signalHead.setAttribute('allVehTypes','true')
			signalHead.setAttribute('complRate','1.000000')
			signalHead.setAttribute('dischRecAct','false')
			signalHead.setAttribute('isBlockSig','false')
			signalHead.setAttribute('lane',line0[13]+' '+line0[15])
			signalHead.setAttribute('localNo','0')
			signalHead.setAttribute('name',line0[3][1:len(line0[3])-1])
			signalHead.setAttribute('no',line0[1])
			signalHead.setAttribute('pos',line0[17])
			signalHead.setAttribute('sg',line0[8]+' '+line0[10])
			signalHead.setAttribute('slowDownDist','3.000000')
			signalHead.setAttribute('type','CIRCULAR')
			signalHead.setAttribute('vAmberBlock','0.000000')
			SHroot.appendChild(signalHead)
	signalController.appendChild(sGs)
	
	wttFiles = SC.createElement('wttFiles')
	intObjectRef = SC.createElement('intObjectRef')
	intObjectRef.setAttribute('key','1')
	wttFiles.appendChild(intObjectRef)
	signalController.appendChild(wttFiles)
		
		
	fp1 = open('E:\CHJ_V7\signalController.xml','w')
	SC.writexml(fp1,indent='\t', addindent='\t',newl='\n',encoding="utf-8")
	fp2 = open('E:\CHJ_V7\signalHead.xml','w')
	SH.writexml(fp2,indent='\t', addindent='\t',newl='\n',encoding="utf-8")