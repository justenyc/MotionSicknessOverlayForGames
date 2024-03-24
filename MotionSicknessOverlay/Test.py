"""Simple example showing how to get gamepad events."""

from __future__ import print_function


from inputs import get_gamepad
import time

def main():
    try:
        gamepad = get_gamepad()
        print(gamepad)
    except:
        print("No gamepad found")
    '''
    while True:
        events = get_gamepad()
        for event in events:
            if event.code == "ABS_RX" or event.code == "ABS_RY":
                #32767
                print(event.code, float(event.state)/32766)
    '''

if __name__ == "__main__":
    main()