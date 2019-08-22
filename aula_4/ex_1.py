
import os
import sys
import subprocess
import tempfile
import datetime
import time

#print(os.path.devnull)

#with open('nome.txt', 'a') as f:
#	f.write('hello, world\n')




### Gerador de Log
#for i in range(10 ** 6):
#	now = datetime.datetime.now().strftime('%d-%m-%Y | %H-%M-%S')
#	print(
#		'{} | log {}'.format(now, i)	
#	)


with open('log', 'r') as f:
	for line in f.readlines():
		date, hour, log = line.split('|')

		log_n = log.lstrip().split(' ')[-1]	
		log_n = int(log_n)

		args = sys.argv
		if len(args) >  1:
			for log in args[1::]:
				if log_n == int(log):
					print(line)
		elif log_n % 7 != 0:
			print(line)