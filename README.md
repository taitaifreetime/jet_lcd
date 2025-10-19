# LCD display using Jetson GPIO
Use of LCD1602A display on Jetson.
See main.py as a sample. 
Tested on Jetson Orin Nano Super, python 3.10, Jetpack 36.4.4.

## Pin distribution
- VSS: gnd
- VDD: 5V
- V0 : voltage for adjusting contrast
- RS : LOW for commands, High for data
- RW : read / write
- E  : LOW unables any activity, HIGH enable activity
- D0-D7: 8bit data
- A/K: Anode and Kathode for adjusting backlight

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
- If you see ```/usr/local/lib/python3.10/dist-packages/Jetson/GPIO/gpio_cdev.py:373: UserWarning: Could not open /dev/mem for pinmux check. If you want pinmux checks, make sure your user has permissions to read /dev/mem and that it exists. Error: [Errno 13] Permission denied: '/dev/mem' warnings.warn('Could not open /dev/mem for pinmux check. If you want pinmux checks, make sure your user has permissions to read /dev/mem and that it exists. Error: ' +```, try ```sudo python main.py```