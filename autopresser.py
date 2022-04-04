from pynput.keyboard import Key, Controller
import keyboard
import time
import keyboard
time.sleep(10)
keyboardd = Controller()
cheese = True
while True:
    while cheese:
        if keyboard.is_pressed("q") and keyboard.is_pressed("p"):
            cheese = False
        keyboardd.press('f')
        keyboardd.release('f')
    if keyboard.is_pressed("q") and keyboard.is_pressed("o"):
        cheese = True

