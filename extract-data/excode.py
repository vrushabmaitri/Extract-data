import email
import os
import json
from cStringIO import StringIO
from email.generator import Generator
path='/home/vrushab/Desktop/'
str1="/home/vrushab/Desktop/beck-s"
for file1 in os.listdir(str1):
	st=str1+"/"+file1
	#print(file1)
	#print(st)
	putr=path+file1+"."+'json'
	
	file2=open(putr,'a')
	file2.close()
	mails=[]
	for fl1 in os.listdir(st):
		pt=st+"/"+fl1
		fp=open(pt,"r");
		ph=[]
		mob=[]
		for line in fp:
			if 'Phone:' in line or 'Phone :' in line:
				li=line.split(':')
				ph=li[1]
			if 'Mobile:'in line or 'Mobile :' in line:
				mi=line.split(':')
				mob=mi[1]
		fp.close()
		fp=open(pt,"r");	
		str2=fp.read()
		msg=email.message_from_string(str2)
		frommail=msg.get("From")
		fromname=msg.get("X-From")
		tm=str(msg.get("To"))
		tnm=str(msg.get("X-To"))
		if(tm!='None'):
			tomail=msg.get("To").split(',')
		else:
			tomail=[]
		if(tnm!='None'):
			toname=msg.get("X-To").split(',')
		else:
			toname=[]
		fromccmail=str(msg.get("Cc"))
		fromccname=str(msg.get("X-cc"))
		if(fromccmail!='None'):
			fromccm=msg.get("Cc").split(',')
		else:
			fromccm=[]
		if(fromccname!='None'):
			fromccnm=msg.get("X-cc").split(',')
		else:
			fromccnm=[]

		with open(putr,'a') as f:
			names=fromname.split(' ')
			ml=frommail.lstrip()
			if(ml not in mails):			
				if(len(names)==1):
					data={'First Name':names[0],'Email':frommail.lstrip(),'additional':{'Last Name':"",'Mobile':mob,'Phone':ph}}
				elif(len(names)==2):
					data={'First Name':names[0],'Email':frommail.lstrip(),'additional':{'Last Name':names[1],'Mobile':mob,'Phone':ph}}
				elif(len(names)==3):
					data={'First Name':names[0],'Email':frommail.strip(),'additional':{'Last Name':names[2],'Mobile':mob,'Phone':ph}}
				json_str=json.dumps(data)
				data=json.loads(json_str)	
				json.dump(data,f,indent=4)
				mails.append(ml)
			
			for i in range(0,len(tomail)):
				nm=toname[i].lstrip()
				names=nm.split(' ')
				ml=tomail[i].lstrip()
				if(tomail[i].lstrip() not in  mails):
					if(len(names)==1):
						data={'First Name':names[0],'Email':tomail[i].lstrip(),'additional':{'Last Name':""}}
					elif(len(names)==2):
						data={'First Name':names[0],'Email':tomail[i].lstrip(),'additional':{'Last Name':names[1]}}
					elif(len(names)==3):
						data={'First Name':names[0],'Email':tomail[i].lstrip(),'additional':{'Last Name':names[2]}}
					json_str=json.dumps(data)
					data=json.loads(json_str)	
					json.dump(data,f,indent=4)
					mails.append(ml)
			length=min(len(fromccm),len(fromccnm))
			for i in range(0,length):
				nm=fromccnm[i].lstrip()
				names=nm.split(' ')
				ml=fromccm[i].lstrip()
				if(fromccm[i].lstrip() not in mails):
					if(len(names)==1):
						data={'First Name':names[0],'Email':fromccm[i].lstrip(),'additional':{'Last Name':""}}
					elif(len(names)==2):
						data={'First Name':names[0],'Email':fromccm[i].lstrip(),'additional':{'Last Name':names[1]}}
					elif(len(names)==3):
						data={'First Name':names[0],'Email':fromccm[i].lstrip(),'additional':{'Last Name':names[2]}}
					json_str=json.dumps(data)
					data=json.loads(json_str)	
					json.dump(data,f,indent=4)
					mails.append(ml)
