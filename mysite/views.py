from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from subprocess import call
import pyrebase, json, requests

@csrf_exempt 
def echo(req):
	fileUrl = str(req.POST['fileUrl'])
	config = {
  		"apiKey": "AIzaSyDCUr8ng_lqfuwHEzOTE-yF2mbarPpBm5M",
  		"authDomain": "boba-eecca.firebaseapp.com",
  		"databaseURL": "https://boba-eecca.firebaseio.com",
  		"storageBucket": "boba-eecca.appspot.com",
		}
	firebase = pyrebase.initialize_app(config)
	auth = firebase.auth()
	user = auth.sign_in_with_email_and_password('leem@plz.com', 'qweqwe')
	storage = firebase.storage()

	url=fileUrl.split('?')
	fileName=url[0].split('/')
	hwpName=fileName[len(fileName)-1]			#hwpName=lecture.hwp
	fileN=fileName[len(fileName)-1].split('.')		#fileN[0]=lecture
	pdfName=fileN[0]+'.pdf'					#pdfName=lecture.pdf
	storage.child(hwpName).download( hwpName , user['idToken'])

	call('/home/jh/HWPtoPDF_Django/home/jh/.local/bin/hwp5html '+hwpName, shell=True)			#transformation


	cssFile = fileN[0] + '/styles.css'
	f = open(cssFile,"a")
	modifyCss = ".Paper { border: 1px solid white;} body { padding: 0px; white-space:pre-wrap; }"
	f.write(modifyCss)
	f.close()

	call('wkhtmltopdf -s A5 ./'+fileN[0]+'/index.xhtml '+pdfName, shell=True)
	call('rm -rf '+fileN[0]+' '+hwpName, shell=True)		#remove files in server

	uploadfile = "./"+pdfName
	storage.child(pdfName).put(uploadfile)
	
	fileUrl = str(storage.child(pdfName).get_url(1))		#get pdf's new url
	call('rm '+pdfName, shell=True)				#remove pdf file in server

	return HttpResponse(fileUrl)
