#!/usr/bin/python
#
#Fix Permisos Cpanel
#
#
#=======================================================================

import optparse
import subprocess
import os

def fixPerm(userName, userHome):
	flag = False
	
	print "Chmod 755 Directories in: " + userHome
	chmodDirectory = subprocess.Popen("find "+ userHome +" -type d -exec chmod 755 {} \;", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	print "\n"
	
	print "Chmod 655 Files in: " + userHome
	chmodFile = subprocess.Popen("find "+userHome+" -type f -exec chmod 644 {} \;", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	print "\n"

	print "Chown everything"
	chown = subprocess.Popen("chown -R " + userName + ":" + userName + " " + userHome + "/*", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	chownOutput = chown.stdout.read()
	
	if 'chown' in chownOutput:
		flag = True
		print chownOutput
		
	print "\n"
	return flag
	
def main():
	#Menu String	
	menuParser = optparse.OptionParser(
	"Fix Permisos Cpanel"
	"\nuso: fixpermisoscpanel.py [opciones]"
	"\n"
	"\n	-u <usuario> : Usuario Cpanel"
	)

	#Listado de Argumentos
	menuParser.add_option("-u", "--user", dest="userName", type="string", help="Especificar usuario Cpanel")
	
	(opciones, args) = menuParser.parse_args()
	
	#Capturando argumentos
	#if(opciones.userName == None or opciones.phpHandler == None):
	if(opciones.userName == None):
		print menuParser.usage
	else:
		if(os.path.isdir("/home/"+opciones.userName)):
			userName = opciones.userName
			userHome = "/home/"+userName+"/public_html"
			flag = fixPerm(userName, userHome)
		else:
			print 'No existe el usuario cpanel'
			exit(0)
	
	if (flag == True):
		print "Fix Permisos Fail!"
	else:
		print "Fix Permisos Success"
				
if __name__ == '__main__':
	main()