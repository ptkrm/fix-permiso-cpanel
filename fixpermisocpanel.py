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
	subprocess.Popen("ls")
	return '1'
	
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
	if(opciones.userName == None):
		print menuParser.usage
	else:
		if(os.path.isdir("/home/"+opciones.userName)):
			userName = opciones.userName
			userHome = "/home/"+userName
			fixPerm(userName, userHome)
		else:
			print 'No existe el usuario cpanel'
			exit(0)
	
	print 'Fini'
				
if __name__ == '__main__':
	main()