import pynput
from inputs import get_gamepad
import threading
import math
import FileHelper as fh

def on_move(x, y):
    global currentVector
    #print('Pointer moved to {0}'.format((x, y)))
    currentVector = (x, y)

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format( 
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == pynput.keyboard.Key.end:
        # Stop listener
        mouseListener.stop()
        return False

def force_mouse_position(x, y):
    mouse.position = (x, y)
    return

def calculate_delta(target, root):
    global mouseMagnitude
    delta = (target[0] - root[0], target[1] - root[1])
    mouseMagnitude = math.sqrt(math.pow(delta[0],2) + math.pow(delta[1], 2))
    #print("{0} * {1} = {2}".format(mouseMagnitude, AppProperties.app_sensitivity, mouseMagnitude * AppProperties.app_sensitivity))
    mouseMagnitude = mouseMagnitude/100 * sensitivity

def attach_listeners():
    mouseListener.start()
    kbListener.start()
    #mouseListener.join()
    #kbListener.join()

def update_mouse_position():
    global lastVector
    global currentVector
    calculate_delta(currentVector, lastVector)
    #print("LastVector: {0}, CurrentVector: {1}".format(lastVector, currentVector))
    lastVector = currentVector

def gamepad_input():
    try:
        global gamepadMagnitude
        events = get_gamepad()
        for event in events:
            if event.code == "ABS_RX": 
                rightStickValue[0] = float(event.state)/32766
            if event.code == "ABS_RY":
                rightStickValue[1] = float(event.state)/32766
            #print(rightStickValue)
            gamepadMagnitude = math.sqrt(math.pow(rightStickValue[0],2) + math.pow(rightStickValue[1], 2))
            gamepadMagnitude = gamepadMagnitude * sensitivity
        return True
    except Exception as e:
        print(e)

mouse = pynput.mouse.Controller()
lastVector = (0,0)
currentVector = (0,0)
mouseMagnitude = 0
gamepadMagnitude = 0
rightStickValue = [0,0]
savedProperties = fh.get_saved_data()
sensitivity = savedProperties["sensitivity"]

mouseListener = pynput.mouse.Listener(on_move=on_move)

kbListener = pynput.keyboard.Listener(
    on_press=on_press,
    on_release=on_release)