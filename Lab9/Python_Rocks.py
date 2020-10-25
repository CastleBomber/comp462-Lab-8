#!/usr/bin/env python
import RPi_I2C_driver, time

mylcd = RPi_I2C_driver.lcd(addr = 0x27)
mylcd.lcd_display_string("Python3 rocks...", 1)
time.sleep(3)
mylcd.lcd_clear()
mylcd.backlight(0)
