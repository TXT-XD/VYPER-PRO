import os, platform, time, sys
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('git pull')
    if os.path.isfile('/data/data/com.termux/files/home/VYPER-PRO/domat64.so'):
    	os.system('mv domat64.so /data/data/com.termux/files/usr/lib/python3.11')
    import vyp
elif bit == '32bit':exit('not support your device')
