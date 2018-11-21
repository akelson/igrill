# Grill Probe Extender

Web server that runs on a Raspberry Pi Zero W and connects to an iGrill so that
temperatures can be monitored when your phone is not within Bluetooth range.

##Installation notes for headless Raspberry Pi Zero W

1. Obtain a copy of Rasbian Stretch Lite. Don't extract it.

https://www.raspberrypi.org/downloads/raspbian/

2. Write the image to an SD card.

3. Configure the Pi to connect to a wireless network by adding a wpa_supplicant.conf to boot partition.

4. Configure the Pi to start ssh by adding empty ssh.txt to boot partion.

5. Connect to the Pi with ssh. It should advertise itself with Avahi as rasberrypi.local.

default user: pi
default pass: rasberry



