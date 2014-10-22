from HTMLParser import HTMLParser
import RPi.GPIO as GPIO
import time
import sys 
import urllib2

class GetAccess(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.flag = False
		self.flag2 = False
		self.flag3 = False
		self.cnt   = 2 
		self.data  = ''

	def handle_starttag(self, tag, attrs):
		if tag == 'strong' and self.flag == True and self.flag3 == False:
			if self.cnt > 1 :
				self.cnt -= 1
			else :
				self.flag2 = True
				self.flag  = False
		else :
			self.flag2 = False
		if tag == 'table':
			for name,value in attrs:
				if value == 'totalcount':
					self.flag = True

	def handle_data(self, data):
		if self.flag2 == True:
			self.data  = data
			self.flag2 = False
			self.flag3 = True


class PrintLed: 
	degit1  = 22
	degit2  = 37
	degit3  = 32
	degit4  = 29
	led_A   = 31
	led_B   = 36
	led_C   = 16
	led_D   = 12
	led_E   = 7
	led_F   = 33
	led_G   = 15
	led_DP  = 11
	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.degit1, GPIO.OUT)
		GPIO.setup(self.degit2, GPIO.OUT)
		GPIO.setup(self.degit3, GPIO.OUT)
		GPIO.setup(self.degit4, GPIO.OUT)
		GPIO.setup(self.led_A , GPIO.OUT)
		GPIO.setup(self.led_B,  GPIO.OUT)
		GPIO.setup(self.led_C,  GPIO.OUT)
		GPIO.setup(self.led_D,  GPIO.OUT)
		GPIO.setup(self.led_E,  GPIO.OUT)
		GPIO.setup(self.led_F,  GPIO.OUT)
		GPIO.setup(self.led_G,  GPIO.OUT)
		GPIO.setup(self.led_DP, GPIO.OUT)

	def show(self, degit, value):
		if value == '1' : self.show_1(degit);
		elif value == '2' : self.show_2(degit);
		elif value == '3' : self.show_3(degit);
		elif value == '4' : self.show_4(degit);
		elif value == '5' : self.show_5(degit);
		elif value == '6' : self.show_6(degit);
		elif value == '7' : self.show_7(degit);
		elif value == '8' : self.show_8(degit);
		elif value == '9' : self.show_9(degit);
		elif value == '0' : self.show_0(degit);
		else : self.print_off(degit);

	def show_0(self, degit):
		self.set_degit(degit)
		GPIO.output(self.led_A,  0)
		GPIO.output(self.led_B,  0)
		GPIO.output(self.led_C,  0)
		GPIO.output(self.led_D,  0)
		GPIO.output(self.led_E,  0)
		GPIO.output(self.led_F,  0)
		GPIO.output(self.led_G,  1)
		GPIO.output(self.led_DP, 1)
		
		
	def show_1(self, degit):
		self.set_degit(degit)
		GPIO.output(self.led_A,  1)
		GPIO.output(self.led_B,  0)
		GPIO.output(self.led_C,  0)
		GPIO.output(self.led_D,  1)
		GPIO.output(self.led_E,  1)
		GPIO.output(self.led_F,  1)
		GPIO.output(self.led_G,  1)
		GPIO.output(self.led_DP, 1)
		
	def show_2(self, degit):
		self.set_degit(degit)
		GPIO.output(self.led_A,  0)
		GPIO.output(self.led_B,  0)
		GPIO.output(self.led_C,  1)
		GPIO.output(self.led_D,  0)
		GPIO.output(self.led_E,  0)
		GPIO.output(self.led_F,  1)
		GPIO.output(self.led_G,  0)
		GPIO.output(self.led_DP, 1)
		
	def show_3(self, degit):
		self.set_degit(degit)
		GPIO.output(self.led_A,  0)
		GPIO.output(self.led_B,  0)
		GPIO.output(self.led_C,  0)
		GPIO.output(self.led_D,  0)
		GPIO.output(self.led_E,  1)
		GPIO.output(self.led_F,  1)
		GPIO.output(self.led_G,  0)
		GPIO.output(self.led_DP, 1)
		
	def show_4(self, degit):
		self.set_degit(degit)
		GPIO.output(self.led_A,  1)
		GPIO.output(self.led_B,  0)
		GPIO.output(self.led_C,  0)
		GPIO.output(self.led_D,  1)
		GPIO.output(self.led_E,  1)
		GPIO.output(self.led_F,  0)
		GPIO.output(self.led_G,  0)
		GPIO.output(self.led_DP, 1)
		
	def show_5(self, degit):
		self.set_degit(degit)
		GPIO.output(self.led_A,  0)
		GPIO.output(self.led_B,  1)
		GPIO.output(self.led_C,  0)
		GPIO.output(self.led_D,  0)
		GPIO.output(self.led_E,  1)
		GPIO.output(self.led_F,  0)
		GPIO.output(self.led_G,  0)
		GPIO.output(self.led_DP, 1)
		
	def show_6(self, degit):
		self.set_degit(degit)
		GPIO.output(self.led_A,  0)
		GPIO.output(self.led_B,  1)
		GPIO.output(self.led_C,  0)
		GPIO.output(self.led_D,  0)
		GPIO.output(self.led_E,  0)
		GPIO.output(self.led_F,  0)
		GPIO.output(self.led_G,  0)
		GPIO.output(self.led_DP, 1)
		
	def show_7(self, degit):
		self.set_degit(degit)
		GPIO.output(self.led_A,  0)
		GPIO.output(self.led_B,  0)
		GPIO.output(self.led_C,  0)
		GPIO.output(self.led_D,  1)
		GPIO.output(self.led_E,  1)
		GPIO.output(self.led_F,  0)
		GPIO.output(self.led_G,  1)
		GPIO.output(self.led_DP, 1)
		
	def show_8(self, degit):
		self.set_degit(degit)
		GPIO.output(self.led_A,  0)
		GPIO.output(self.led_B,  0)
		GPIO.output(self.led_C,  0)
		GPIO.output(self.led_D,  0)
		GPIO.output(self.led_E,  0)
		GPIO.output(self.led_F,  0)
		GPIO.output(self.led_G,  0)
		GPIO.output(self.led_DP, 1)
		
	def show_9(self, degit):
		self.set_degit(degit)
		GPIO.output(self.led_A,  0)
		GPIO.output(self.led_B,  0)
		GPIO.output(self.led_C,  0)
		GPIO.output(self.led_D,  0)
		GPIO.output(self.led_E,  1)
		GPIO.output(self.led_F,  0)
		GPIO.output(self.led_G,  0)
		GPIO.output(self.led_DP, 1)
		
	def print_off(self, degit):
		GPIO.output(self.degit1, 0)
		GPIO.output(self.degit2, 0)
		GPIO.output(self.degit3, 0)
		GPIO.output(self.degit4, 0)
		GPIO.output(self.led_A,  0)
		GPIO.output(self.led_B,  0)
		GPIO.output(self.led_C,  0)
		GPIO.output(self.led_D,  0)
		GPIO.output(self.led_E,  0)
		GPIO.output(self.led_F,  0)
		GPIO.output(self.led_G,  0)
		GPIO.output(self.led_DP, 0)

	def set_degit(self, degit):
		if degit == 1 : GPIO.output(self.degit1, 1);
		else: GPIO.output(self.degit1, 0);
		if degit == 2 : GPIO.output(self.degit2, 1);
		else: GPIO.output(self.degit2, 0);
		if degit == 3 : GPIO.output(self.degit3, 1);
		else: GPIO.output(self.degit3, 0);
		if degit == 4 : GPIO.output(self.degit4, 1);
		else: GPIO.output(self.degit4, 0);
		
	def __del__(self):
		GPIO.cleanup()

url = 'http://counter.hatena.ne.jp/katashiyo515/?cid=101'
response = urllib2.urlopen(url)
ga = GetAccess()
ga.feed(response.read())
access_data = ga.data
print access_data
ga.close()

degit1_value = access_data[4];
degit2_value = access_data[3];
degit3_value = access_data[2];
degit4_value = access_data[0];

p = PrintLed();
for num in range(0, 1000):
	p.show(1, degit1_value);
	time.sleep(0.001)
	p.show(2, degit2_value);
	time.sleep(0.001)
	p.show(3, degit3_value);
	time.sleep(0.001)
	p.show(4, degit4_value);
	time.sleep(0.001)

del p
