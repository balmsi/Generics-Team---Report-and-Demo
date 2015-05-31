Python 2.7.3 (default, Mar 18 2014, 05:13:23) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> import time
>>> os.system('modprobe wl-gpio')
256
>>> os.system('modprobe wl-therm')
256
>>> temp_sensor='sys/bus/wl/devices/28-000005e2fdc3/wl_slave'
>>> def temp_raw():
	f=open(temp_sensor,'r')
	lines=f.readlines()
	f.close()
	return lines
def read_temp():
	
SyntaxError: invalid syntax
>>> defread_temp():
	
SyntaxError: invalid syntax
>>> 
defread_temp():
lines=temp_raw()
while lines[0].strip()[-3:] !='YES':
    TIME.SLEEP(0.2)
    lines=temp_r0aw()
    temp_output=lines[1].find('t=')
    if temp_output!=-1:
        temp_string=lines[1].strip()[temp_output+2:]
        temp_c=float(temp_string)/1000.0
        temp_f=temp_c*9.0/5.0+32.0
        return temp_c,temp_f
    while True:
        print(read_temp())
        time.sleep(1)
        def read_temp_raw():
            catdata=subproccess.Popen(['cat',device_file],stdout=subprocess.PIPE,stderr=subprocess.PIPE
            out,err=catdata.communicate()
            out_decode=out.decode('utf-8')
            lines=out_decode.split('\n')
            return lines
        deg_c,deg_f=read_temp()
        nano thermometer.py
        