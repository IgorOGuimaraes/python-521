
import os
import sys
import time

if len(sys.argv) < 2:
	print('Diretório não especificado')
	sys.exit(1)

dirname = sys.argv[1]

done = False

while not done:
	for filename in os.listdir(dirname):
		with open(dirname + '/' + filename, 'r') as f:
			pass

		os.remove(dirname + '/' + filename)
		print('{} apagado'.format(filename))
	time.sleep(1)