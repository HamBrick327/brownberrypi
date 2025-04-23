## TODO test this
from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

rowPins = [0, 1, 2, 3]
colPins = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

outputPins = []
inputPins = []
liveCols = []
liveRows = []
''' EXAMPLE PIN CODE
pin_led = Pin(16, mode=Pin.OUT, value=1)
pin_led = Pin(16, mode=Pin.OUT, value=0)
pin_14 = Pin(14, mode=Pin.IN)
'''

## check columns
for pin in rowPins:
    outputPins.append(Pin(pin, mode=Pin.OUT, value=1))
for index, pin in enumerate(colPins):
    inputPins.append(Pin(pin, mode=Pin.IN, pull=Pin.PULL_DOWN))
    if inputPins[index].value():
        liveCols.append(pin)
## check rows
for pin in colPins:
    outputPins.append(Pin(pin, mode=Pin.OUT, value=1))
for index, pin in enumerate(rowPins):
    inputPins.append(Pin(pin, mode=Pin.IN, pull=Pin.PULL_DOWN))
    if inputPins[index].value():
        liveRows.append(pin)

'''TODO add keybind logic'''
keybinds = [[['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'],
            ['ctrl', 'alt', 'meta', 'shift', 'space', 'fn1', 'fn2', 'home', 'end', 'backspace']]]

''' begin pseudocode
if fn1 is pressed:
    keyboard.press(keybinds[1][row][col])
elif fn2 is pressed:
    keyboard.press(keybinds[2][row][col])
*insert optional if fn1 and fn2 are pressed*
elif not (fn1 or fn2):
    keyboard.press(keybinds[0][row][col])
end pseudocode'''