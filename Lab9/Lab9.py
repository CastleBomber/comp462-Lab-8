#!/usr/bin/env python
import RPi_I2C_driver, time

mylcd = RPi_I2C_driver.lcd()
mylcd.lcd_display_string("Time: ", 1)
mylcd.lcd_display_string(time, 1)
mylcd.lcd_display_string("Temp: ", 2)
time.sleep(3)
mylcd.lcd_clear()
mylcd.backlight(0)
