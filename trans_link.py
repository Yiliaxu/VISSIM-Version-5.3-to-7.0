import xml.etree.ElementTree as etree
import xml.dom.minidom as doc
import numpy as np
import string,re,os



if __name__ == '__main__':
	links = doc.Document()
	root = links.createElement('links')
	links.appendChild(root)

	inp = open(r"D:\Journal_paper\STPM\Caohejing_vissim\Caohejing_STPM.inp",'r')
	IsThisLink = 0
	IsThisConnector = 0
	for line in inp.readlines():
		if line.startswith('LINK'):
			IsThisLink = 1
			link = links.createElement('link')
			link.setAttribute('costPerKm','0.000000')
			link.setAttribute('direction','ALL')
			link.setAttribute('displayType','1')
			link.setAttribute('emegStopDist','5.000000')
			link.setAttribute('gradient','0.000000')
			link.setAttribute('isPedArea','false')
			link.setAttribute('level','1')
			link.setAttribute('linkBehavType','1')
			link.setAttribute('linkEvalAct','true')
			link.setAttribute('linkEvalSegLen','10.000000')
			link.setAttribute('lnChgDist','200.000000')
			link.setAttribute('lnChgDistIsPerLn','false')
			link.setAttribute('lnChgEvalAct','true')
			line0 = line.split()
			link.setAttribute('name',line0[3][1:len(line0[3])-1])
			link.setAttribute('no',line0[1])
			link.setAttribute('onlyOvtBus','false')
			link.setAttribute('showClsfValues','true')
			link.setAttribute('showVeh','true')
			link.setAttribute('surch1','0.000000')
			link.setAttribute('surch2','0.000000')
			link.setAttribute('thickness','0.000000')
			link.setAttribute('vehRecAct','true')
		if line.startswith('  LENGTH') and IsThisLink==1:
			lanes = links.createElement('lanes')
			line0 = line.split()
			lane_num = int(line0[3])
			for i in np.arange(0,lane_num):
				lane = links.createElement('lane')
				lane.setAttribute('width','3.500000')
				lanes.appendChild(lane)
			link.appendChild(lanes)
		if line.startswith('  FROM') and IsThisLink==1:
			geometry = links.createElement('geometry')
			line0 = line.split()
			points3D = links.createElement('points3D')
			point3D = links.createElement('point3D')
			point3D.setAttribute('x',line0[1])
			point3D.setAttribute('y',line0[2])
			point3D.setAttribute('zOffset','0.000000')
			points3D.appendChild(point3D)
		if line.startswith('  OVER') and IsThisLink==1:
			line0 = line.split()
			over_num = len(line0)/4
			for i in np.arange(0,over_num):
				point3D = links.createElement('point3D')
				point3D.setAttribute('x',line0[i*4+1])
				point3D.setAttribute('y',line0[i*4+2])
				point3D.setAttribute('zOffset','0.000000')
				points3D.appendChild(point3D)
		if line.startswith('  TO') and IsThisLink==1:
			line0 = line.split()
			point3D = links.createElement('point3D')
			point3D.setAttribute('x',line0[1])
			point3D.setAttribute('y',line0[2])
			point3D.setAttribute('zOffset','0.000000')
			points3D.appendChild(point3D)
			geometry.appendChild(points3D)
			link.appendChild(geometry)
			root.appendChild(link)
			IsThisLink=0
#####################################################################
##############################CONNECTOR##############################
		if line.startswith('CONNECTOR'):
			IsThisConnector=1
			connector = links.createElement('link')
			connector.setAttribute('costPerKm','0.000000')
			connector.setAttribute('direction','ALL')
			connector.setAttribute('displayType','1')
			connector.setAttribute('emegStopDist','5.000000')
			connector.setAttribute('gradient','0.000000')
			connector.setAttribute('isPedArea','false')
			connector.setAttribute('linkBehavType','1')
			connector.setAttribute('linkEvalAct','true')
			connector.setAttribute('linkEvalSegLen','10.000000')
			connector.setAttribute('lnChgDist','200.000000')
			connector.setAttribute('lnChgDistIsPerLn','false')
			connector.setAttribute('lnChgEvalAct','true')
			line0 = line.split()
			connector.setAttribute('name','')
			connector.setAttribute('no',line0[1])
			connector.setAttribute('onlyOvtBus','false')
			connector.setAttribute('showClsfValues','true')
			connector.setAttribute('showVeh','true')
			connector.setAttribute('surch1','0.000000')
			connector.setAttribute('surch2','0.000000')
			connector.setAttribute('thickness','0.000000')
			connector.setAttribute('vehRecAct','true')

		if line.startswith('  FROM') and IsThisConnector==1:
			line0 = line.split()
			lane_num = len(line0)-6
			lanes = links.createElement('lanes')
			geometry = links.createElement('geometry')
			points3D = links.createElement('points3D')
			for i in np.arange(0,lane_num):
				lane = links.createElement('lane')
				lanes.appendChild(lane)
			connector.appendChild(lanes)
			fromlinkendpt = links.createElement('fromLinkEndPt')
			fromlinkendpt.setAttribute('lane',line0[2]+' '+line0[4])
			fromlinkendpt.setAttribute('pos',line0[len(line0)-1])
			connector.appendChild(fromlinkendpt)

		if line.startswith('  OVER') and IsThisConnector==1:
			line0 = line.split()
			over_num = len(line0)/4
			for i in np.arange(0,over_num):
				point3D = links.createElement('point3D')
				point3D.setAttribute('x',line0[i*4+1])
				point3D.setAttribute('y',line0[i*4+2])
				point3D.setAttribute('zOffset','0.000000')
				points3D.appendChild(point3D)

		if line.startswith('  TO') and IsThisConnector==1:
			line0 = line.split()
			tolinkendpt = links.createElement('toLinkEndPt')
			tolinkendpt.setAttribute('lane',line0[2]+' '+line0[4])
			tolinkendpt.setAttribute('pos',line0[len(line0)-6])
			connector.appendChild(tolinkendpt)
			geometry.appendChild(points3D)
			connector.appendChild(geometry)
			root.appendChild(connector)
			IsThisConnector = 0




	fp = open('E:\CHJ_V7\links.xml','w')
	links.writexml(fp,indent='\t', addindent='\t',newl='\n',encoding="utf-8")