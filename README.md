# pi-python-webcam-timelapse


A Python script that use the fswebcam utility to take a series of pictures from a USB webcam connected to a Raspberry Pi. Not the standard Pi Camera.

Run as Cronjob every minute, the script will take 6 photos then exit, effectively making a continuous timelapse every 10 seconds.

The way I have it setup is to write the photos to a mounted dir, and also to rotate 90 degrees since I have the camera longways to get a particular shot/angle.

Cron:
* * * * * /usr/bin/python3 /home/pi/pi-python-webcam-timelapse/webcam.py  2>&1 >> /tmp/cron 


