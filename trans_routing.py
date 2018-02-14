import linecache
import xml.etree.ElementTree as etree
import xml.dom.minidom as doc
import numpy as np
import string,re,os

	

if __name__ == '__main__':
	vehicleRoutingDecisionsStatic = doc.Document()
	root = vehicleRoutingDecisionsStatic.createElement('vehicleRoutingDecisionsStatic')
	vehicleRoutingDecisionsStatic.appendChild(root)


	os.chdir("D:\Journal_paper\STPM\Caohejing_vissim")
	inproute = linecache.getlines("Caohejing_STPM.inp")[2142:2299]
	startline = 0
	endline = 0
	flag = 0
	destLinks = []
	for i in np.arange(0,len(inproute)):
		if inproute[i].startswith('ROUTING_DECISION'):
			startline = i
			flag = 1
		if inproute[i].startswith('     ROUTE') and flag==1:		
		    destLinks = destLinks + [i-startline]
		if inproute[i]=='\n' and flag==1:
			endline = i
			routing = inproute[startline:endline]			
			vehicleRoutingDecisionStatic = vehicleRoutingDecisionsStatic.createElement('vehicleRoutingDecisionStatic')
			vehicleRoutingDecisionStatic.setAttribute('allVehTypes','true')
			vehicleRoutingDecisionStatic.setAttribute('anmFlag','false')
			vehicleRoutingDecisionStatic.setAttribute('combineStaRoutDec','false')
			line1 = routing[1].split()
			line0 = routing[0].split()
			vehicleRoutingDecisionStatic.setAttribute('link',line1[1])
			vehicleRoutingDecisionStatic.setAttribute('name',line0[3][1:len(line0[3])-1])
			vehicleRoutingDecisionStatic.setAttribute('no',line0[1])
			vehicleRoutingDecisionStatic.setAttribute('pos',line1[3])
			vehRoutSta = vehicleRoutingDecisionsStatic.createElement('vehRoutSta')

			for j in np.arange(0,len(destLinks)):
				num = destLinks[j]
				print num
				line = routing[num].split()
				vehicleRouteStatic = vehicleRoutingDecisionsStatic.createElement('vehicleRouteStatic')
				vehicleRouteStatic.setAttribute('destLink',line[4])
				vehicleRouteStatic.setAttribute('destPos',line[6])
				vehicleRouteStatic.setAttribute('name','')
				vehicleRouteStatic.setAttribute('no',line[1])
				vehicleRouteStatic.setAttribute('relFlow','')
				linkSeq = vehicleRoutingDecisionsStatic.createElement('linkSeq')
				routingnode = []
				if j < len(destLinks)-1:
					for k in np.arange(num+2,destLinks[j+1]):
						routingnode = routingnode + routing[k].split()
				elif j == len(destLinks)-1:
					for k in np.arange(num+2,endline-startline):
						routingnode = routingnode + routing[k].split()
				routingnodenum = len(routingnode)-1
				linkSeq = vehicleRoutingDecisionsStatic.createElement('linkSeq')
				for k in np.arange(0,routingnodenum):
					intObjectRef = vehicleRoutingDecisionsStatic.createElement('intObjectRef')
					intObjectRef.setAttribute('key',routingnode[k+1])
					linkSeq.appendChild(intObjectRef)
					vehicleRouteStatic.appendChild(linkSeq)
				vehRoutSta.appendChild(vehicleRouteStatic)
			vehicleRoutingDecisionStatic.appendChild(vehRoutSta)
			root.appendChild(vehicleRoutingDecisionStatic)

			flag = 0
			destLinks = []

	fp = open('E:\CHJ_V7\staticroute.xml','w')
	vehicleRoutingDecisionsStatic.writexml(fp,indent='\t', addindent='\t',newl='\n',encoding="utf-8")









	
