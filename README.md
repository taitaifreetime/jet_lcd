# LCD display using Jetson GPIO
Use of LCD1602A display on Jetson.
See main.py as a sample. 
Tested on Jetson Orin Nano Super, python 3.10, Jetpack 36.4.4.

## Tips
- Default all GPIO pins are input. To output messages, the GPIOs need to change to output.
```
sudo busybox devmem 0x2430068 w 0x8
```
- Install and upgrade Jetson.GPIO.
```
sudo pip3 install Jetson.GPIO
sudo pip3 install --upgrade Jetson.GPIO
```