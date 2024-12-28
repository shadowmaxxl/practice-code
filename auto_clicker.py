from pynput.keyboard import Key, Controller
import time 

# Create a keyboard controller
def create_Keyboard():
    return Controller()
keyboard = create_Keyboard()
    # Press and release space
    #""" it is a function that uses the module to simulate typing and sending messages automatically
    #it is used to automate the process of typing and sending messages on the keyboard
#"""
message = "i hate you"

for num in range(15):
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(0.3)
    create_Keyboard()