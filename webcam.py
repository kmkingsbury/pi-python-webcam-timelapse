import datetime
import os
import time
import sys

#a = datetime.datetime.now().time()
#b = addSecs(a, 300)
#print(a)
#print(b)
delay = 10
count = 0
pics2take = 6

now = datetime.datetime.now()
eventtime =  now + datetime.timedelta(seconds = -int(delay))
print ("Now:    " + now.strftime('%Y-%m-%d %H:%M:%S.%f'))
print ("Next: " + eventtime.strftime('%Y-%m-%d %H:%M:%S.%f'))

# datetime object containing current date and time
while 1==1 :
  now = datetime.datetime.now()
  #print("now =", now)
    
  if now >= eventtime:  
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%Y-%m-%d_%H%M%S")
    print("date and time =", dt_string)
    
    cmd = "/usr/bin/fswebcam -r 1920x1080 --rotate 90  --no-banner /mnt/pi/plants/"+ dt_string + ".jpg"
    returned_value = os.system(cmd) 
    eventtime =  now + datetime.timedelta(seconds = int(delay))
    count += 1
    print ("Next: " + eventtime.strftime('%Y-%m-%d %H:%M:%S.%f'))

  else:
    time.sleep(.2);

  if count >= pics2take:
    sys.exit()

