import platform
import os
import sys

def ResizeScreen(x,y):
		clientos = platform.system()
		if clientos == 'Windows':
			os.system("mode {rows},{columns}".format(rows=x,columns=y))
		elif clientos == 'Linux' or clientos == 'Darwin' or clientos.startswith('CYGWIN'):
			sys.stdout.write("\x1b[8;{columns};{rows}t".format(rows=x,columns=y))