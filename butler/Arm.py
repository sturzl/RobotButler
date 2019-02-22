import serial, serial.tools.list_ports, time, socket

class Arm:

	def set_blink_speed(self, blink_speed):
		self.__send_command(blink_speed)

	def aim_arm(self):
	    print('Aiming arm')

	def pour_selection(self, selection):
	    print('Pouring selection: ', selection)

	def reset_arm(self):
	    print('Resetting arm')

	def __send_command(self, command):
	    print('Sending command: ', command)
	    self.arduino.flush()
	    self.arduino.write(command.encode())
	    self.__read_response()
	    time.sleep(.1)
	    self.arduino.flush()

	def __read_response(self):
	    time.sleep(1)
	    while (self.arduino.in_waiting > 0):
	        print('Arduino response: ')
	        print(self.arduino.readline().decode(), end="")

	def __init__(self, port):
		self.arduino = serial.Serial(port, 115200, timeout=1)
		time.sleep(.5)