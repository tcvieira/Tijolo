'''
This program is free software: you can redistribute it and/or modify
t under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
	    
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
			    
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

#SERIAL_PORT = '/dev/tty.usbserial-A700ez9w'
SERIAL_PORT = '/dev/ttyS0'
#SERIAL_PORT = '/dev/ttyUSB0'
#SERIAL_PORT = '/dev/ttyUSB1'

SERIAL_BAUD_RATE = 115200

ADDR_LIST = [0x04,0x61,0x03,0x65]

WIDTH = 16
HEIGHT = 32

DEAD = 255
LIVE = 0