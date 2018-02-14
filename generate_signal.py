import xml.etree.ElementTree as etree
import xml.dom.minidom as doc
import numpy as np
import string,re,os



if __name__ == '__main__':
	sgsfile = doc.Document()
	sgs = sgsfile.createElement('sgs')
	sgsfile.appendChild(sgs)

	sigfile = etree.parse('D:\Journal_paper\STPM\Caohejing_vissim\Caohejing_STPM1.sig')
	sgs0 = sigfile.findall('sgs/sg')

	for sg0 in sgs0:
		sg = sgsfile.createElement('sg')
		sg.setAttribute('id',sg0.attrib['id'])
		sg.setAttribute('name',sg0.attrib['name'])
		sg.setAttribute('defaultSignalSequence',sg0.attrib['defaultSignalSequence'])
		sg.setAttribute('underEPICSControl','true')
		defaultDurations = sgsfile.createElement('defaultDurations')
		duration = [1000,1000,5000,3000]
		for i in np.arange(0,4):
			defaultDuration = sgsfile.createElement('defaultDuration')
			defaultDuration.setAttribute('display',str(i+1))
			defaultDuration.setAttribute('duration',str(duration[i]))
			defaultDurations.appendChild(defaultDuration)
		sg.appendChild(defaultDurations)
		EPICSTrafficDemands = sgsfile.createElement('EPICSTrafficDemands')
		sg.appendChild(EPICSTrafficDemands)
		sgs.appendChild(sg)


		
	fp = open('E:\CHJ_V7\sgs.xml','w')
	sgsfile.writexml(fp,indent='\t', addindent='\t',newl='\n',encoding="utf-8")