import yaml, os

# checks.txt
#checks:
#     ping:
#          google: google.com:443
#          mysite: mytest.test:443

dict=yaml.load(open('checks.txt'))

ping=dict['checks']['ping']

for key in ping:
	value=ping[key]
	host, port=value.split(':')
	
	try:
		s = socket.socket()
		s.connect((host, port)) 
		s.send("some more data")
		print ('✔ %s' % key)
	except:
		print ('✗ %s' % key)
