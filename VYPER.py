import os, platform, time, sys
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x vyp')
    os.system('./vyp')
elif bit == '32bit':exit('not support your device')
