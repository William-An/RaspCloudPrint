import web
import os
import sys
import subprocess
import datetime
# Log page! 
urls = ('/upload', 'Upload',
		'/error','Err',
		'/log','Log')
 
class Upload:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        render = web.template.render('static/')
        return render.index()

    def POST(self):
        x = web.input(printjob={})
        filedir = 'file'                                 	# change this to the directory you want to store the file in.
        if 'printjob' in x:                                   # to check if the file-object is created
            filepath=x.printjob.filename    # replaces the windows-style slashes with linux ones.
            filename=filepath.split('/')[-1]               # splits the and chooses the last part (the filename with extension)
            fout = open(filedir+'/'+filename,'wb')       # creates the file where the uploaded file should be stored
            fout.write(x.printjob.file.read())                # writes the uploaded file to the newly created file.
            fout.close()                                    # closes the file, upload complete.
        filename = filedir+"/"+filename
        if 'pdf' in filename[-4:]:                
            printer(filename)
        else:
            raise web.seeother('/error')
class Err:
	def GET(self):
		web.header("Content-Type","text/html; charset=utf-8")
		render = web.template.render('static/')
		return render.error()

class Log:
	def GET(self):
		with open("static/log","rb") as logfile:
			return "<a href=\"static/log\">Download Log</a><br>"+"<br>".join([i.decode() for i in logfile.readlines()]);
def notfound():
	raise web.seeother('/error')

def printer(filename):
	with open('static/log','a+') as logfile:
		logfile.write("[*] Start printjob "+filename+" "+str(datetime.datetime.now())+"\n")
		try:
			subprocess.call(['lp',filename],timeout=10)
			subprocess.call(["rm",filename],timeout=10)
			logfile.write("[+] Finish printjob "+filename+" "+str(datetime.datetime.now())+"\n")
			raise web.seeother('/upload')
		except Exception as err:
			if str(err) == "303 See Other":
                            raise web.seeother('/upload')
			subprocess.call(["rm",filename],timeout=10)
			logfile.write("[-] Error in printing "+filename+" "+str(datetime.datetime.now())+" | Error:"+str(err)+"\n")   
			# print(str(err))
			raise web.seeother('/error')

if __name__ == "__main__":
    app = web.application(urls, globals()) 
    app.notfound = notfound
    app.internalerror = notfound
    app.run()



                        

