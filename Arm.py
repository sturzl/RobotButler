import serial, serial.tools.list_ports, time, socket

class Arm:
	def aim_arm(self):
	    print('Aiming arm')

	def pour_selection(self, selection):
	    print('Pouring selection: ', selection)

	def reset_arm(self):
	    print('Resetting arm')

	def arduino_send_cmd(self, command):
	    print('Sending command: ')
	    self.arduino.flush()
	    command = command + '\n'
	    self.arduino.write(command.encode())
	    arduino_get_resp()
	    time.sleep(.1)
	    self.arduino.flush()

	def arduino_get_resp(self):
	    time.sleep(.1)
	    while (self.arduino.in_waiting > 0):
	        print('Arduino response: ')
	        print(self.arduino.readline().decode(), end="")

	def __init__(self, port):
		self.arduino = serial.Serial(port, 9600, timeout=1)
		time.sleep(.5)