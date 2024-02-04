# icom-set-time
Set time on ICOM IC7300 (and others)

This simple and definitely not polished python script sets time and date on the Icom IC7300 ham radio transceiver using CI-V protocol over USB. 

It can be made compatible with more or less every CI-V Icom radios like the 7100, 7610, 705, 9700, R8600, etc by simply changing the radio CI-V address (and the serial port address and speed). Beware: it seems (it has been reported to me) that the CI-V command for setting time is not the same on all of the aforementioned radios, so while it can be made compatible with all of these radios, maybe you'll also have to change the CI-V commands, so baiscally you'll have to tweak more or less the whole thing (serial port, speed, CI-V address, CI-V commands)

I made this script because my 7300 has a faulty RTC clock battery and loses time when the power supply is switched off. This issue exists also on other models, but more modern ones have ethernet or wifi and an NTP client in them, so there is no need to set the time via USB.

This script requires python 3 and it should run on every recent Linux installation, I tested it on Mint.

If you need a windows one, check https://kb3hha.com/Set7300Clock (not mine)
