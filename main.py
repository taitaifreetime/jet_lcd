# sample code

from jet_lcd import JetLCD
import time

RS = 7 
E  = 15
D4 = 29
D5 = 31
D6 = 33
D7 = 32
width = 16
height = 2
lcd_device = JetLCD(width, height, RS, E, D4, D5, D6, D7)
lcd_device.lcd_write("Init Dsply Done", 0)
lcd_device.lcd_write("True", 1)
time.sleep(5)
lcd_device.clear_display()

lcd_device.start_loading()
time.sleep(6)
lcd_device.stop_loading()
lcd_device.clear_display()

lcd_device.lcd_write("Loading Done", 0)
lcd_device.lcd_write("True", 1)
time.sleep(5)
lcd_device.clear_display()

lcd_device.lcd_write("Sample Code Done", 0)
lcd_device.lcd_write("True", 1)