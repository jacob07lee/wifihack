import os
import urllib2
from wireless import Wireless
def internet_on():
	try:
		urllib2.urlopen('http://google.com', timeout=1)
		print ("Connected")
		return True
	except urllib2.URLError as err:
		print("Not Connected")
		return False

while(internet_on()==False):
	f=open("/boot/wifiinfo.txt", "r")
	data =f.read().splitlines()
	print(data[1])
	os.system('sudo ifconfig wlan0 up')
	wireless = Wireless()
	wireless.connect(ssid=data[0], password=data[1])
	os.system('sudo dhclient wlan0')