import Jetson.GPIO as GPIO
import threading
import time

class JetLCD:
    def __init__(self, width, height, gpio_RS, gpio_E, gpio_D4, gpio_D5, gpio_D6, gpio_D7):
        self.width_ = width
        self.height_ = height
        self.gpio_RS_ = gpio_RS
        self.gpio_E_  = gpio_E
        self.gpio_D4_ = gpio_D4
        self.gpio_D5_ = gpio_D5
        self.gpio_D6_ = gpio_D6
        self.gpio_D7_ = gpio_D7
        self.flag_loading_ = False
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup([self.gpio_RS_, self.gpio_E_, self.gpio_D4_, self.gpio_D5_, self.gpio_D6_, self.gpio_D7_], GPIO.OUT)
        self.init_display()

    def init_display(self):
        GPIO.output(self.gpio_RS_, False)
        self.send_nibble(0x30)
        time.sleep(0.005)
        self.send_nibble(0x30)
        time.sleep(0.001)
        self.send_nibble(0x30)
        self.send_nibble(0x20)  # 4-bit mode
        self.send_byte(0x28, False)  # function set: 4bit, 2 lines, 5x8 dots
        self.send_byte(0x0C, False)  # display on, cursor off
        self.send_byte(0x06, False)  # entry mode
        self.send_byte(0x01, False)  # clear display
        time.sleep(0.002)

    def pulse_enable(self):
        GPIO.output(self.gpio_E_, False)
        time.sleep(0.000001)
        GPIO.output(self.gpio_E_, True)
        time.sleep(0.000001)
        GPIO.output(self.gpio_E_, False)
        time.sleep(0.0001)

    def send_nibble(self, nibble):
        GPIO.output(self.gpio_D4_, bool(nibble & 0x10))
        GPIO.output(self.gpio_D5_, bool(nibble & 0x20))
        GPIO.output(self.gpio_D6_, bool(nibble & 0x40))
        GPIO.output(self.gpio_D7_, bool(nibble & 0x80))
        self.pulse_enable()

    def send_byte(self, byte, mode):
        GPIO.output(self.gpio_RS_, mode)
        # high nibble
        self.send_nibble(byte)
        # low nibble
        self.send_nibble(byte << 4)

    def clear_display(self):
        self.send_byte(0x01, False)
        time.sleep(0.002) # >=0.002

    def start_loading(self):
        def threading_loading():
            self.clear_display()
            self.flag_loading_ = True
            while (True):
                for i in range(self.height_):
                    for j in range(self.width_ + 1):
                        if not self.flag_loading_: return
                        self.lcd_write(" "*(j-1)+"*", i)
                        time.sleep(0.2)
                    self.clear_display()
        t = threading.Thread(target=threading_loading, daemon=True)
        t.start()
        return t

    def stop_loading(self):
        self.flag_loading_ = False

    def lcd_write(self, message, line):
        if line == 0:
            self.send_byte(0x80, False)
        elif line == 1:
            self.send_byte(0xC0, False)
        for char in message:
            self.send_byte(ord(char), True)