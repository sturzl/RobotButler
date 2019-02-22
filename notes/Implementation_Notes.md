# Raspi
- hostname is butler-1.local to ssh
- install arduino ide with
  - sudo apt-get update
  - sudo apt-get install ubuntu-make
  - umake ide arduino
  - sudo usermod -a -G dialout $USER
  - sudo apt-get install arduino
- sudo pip3 install pyserial flask
- Run the script: python3 Butler.py '/dev/ttyUSB______'


# Arduino
- use the 328p (old bootloader) option


# TODO
Find the cup and target the arm


# References/Tutorials
- [Serving website from raspi](https://www.hackster.io/bportaluri/web-controlled-led-animations-with-raspberry-pi-and-arduino-112025)
- [Communicating to arduino](https://www.meccanismocomplesso.org/en/controlling-arduino-raspberry-pi/)
