#!/usr/bin/python3
# horrible python script to set time and date  on the IC7300
# or other Icom radios that use the same protocol.
# I made this script because the IC7300 has a faulty RTC battery and it does not have
# ethernet connection and NTP client like the 7610, 705, 9700, R8600, etc.
# This script sets the time slightly wrong because you cannot set seconds, only minutes.

# I'm a sysadmin and not a programmer and this script violates ALL the programming
# best practices. ALL of them. Feel free to make it much better.
# IZ4UFQ


civaddress="0x94" #this is the default IC7300 address. Change to match your radio config.
baudrate = 19200  #change to match your radio serial speed
serialport = "/dev/ttyUSB0"  # Serial port of your radios serial interface. See comment below

# you can set a serial port by id so that it always connect to the correct radio, usefeul if you have more than
# one usb serial port connected (I have 8 of them)
#serialport = "/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_IC-7300_03005669-if00-port0"


#Import libraries we'll need to use
import time
import serial
import struct

# Get time in GMT. If you want local time change to "t = time.localtime()"
t = time.gmtime()


# extract strings for year, day, month, hour, minute 
# with a leading zero if needed
year = str(t.tm_year)
month = str(t.tm_mon).rjust(2,'0')
day = str(t.tm_mday).rjust(2,'0')
hour = str(t.tm_hour).rjust(2,'0')
minute = str(t.tm_min).rjust(2,'0')


# set date, ci-v command is 0x94
command = ["0xFE", "0xFE", civaddress, "0xE0", "0x1A", "0x05", "0x00" ]
command.append("0x94")
command.append("0x"+year[0:2])
command.append("0x"+year[2:])
command.append("0x"+month)
command.append("0x"+day)
command.append("0xFD")

ser = serial.Serial(serialport, baudrate)
count = 0
while(count < 13):
    senddata = int(bytes(command[count], 'UTF-8'), 16)
    ser.write(struct.pack('>B', senddata))
    count = count +1
ser.close()

# set time, ci-v command is 0x95
# you CANNOT set seconds, so unless you want to wait for the minute mark
# you'll end up with a time that is set incorrectly by less than one minute
# I prefer to set time incorrectly than to wait for up to 59 seconds 

command = ["0xFE", "0xFE", civaddress, "0xE0", "0x1A", "0x05", "0x00" ]
command.append("0x95")
command.append("0x"+hour)
command.append("0x"+minute)
command.append("0xFD")

ser = serial.Serial(serialport, baudrate)
count = 0
while(count < 11):
    senddata = int(bytes(command[count], 'UTF-8'), 16)
    ser.write(struct.pack('>B', senddata))
    count = count +1
ser.close()

