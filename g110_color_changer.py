import usb.core
import usb.util
import time
import sys
 
# find our device
# this may be specific to your keyboard so please make sure to find yours
dev = usb.core.find(idVendor=0x046D, idProduct=0xC22B)
 
# was it found?
if dev is None:
    raise ValueError('Device not found')
 
# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

#  Brightness, 255 - bright, 0 - off
b=255

# Here I just loop forever through all the colors. 
while True: 
	#loop forwards through colors
	for i in range(255):
		try:
			# data i is color, b is brightness
			data = [0x07, i, 0, 0, b]
			#crazy usb sniffed codes here
			ret = dev.ctrl_transfer(0x22, 0x9, 0x307, 0, data)
			print ret
			time.sleep(.005)
		except:
			pass
	#loop backwards through colors
	for i in range(255,-1,-1):
		try:
			data = [0x07, i, 0, 0, b]
			ret = dev.ctrl_transfer(0x22, 0x9, 0x307, 0, data)
			print ret
			time.sleep(.005)
		except:
			pass