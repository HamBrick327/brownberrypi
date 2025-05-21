## TODO test this
import board
import digitalio
from time import sleep

# pin = Pin("LED", Pin.OUT)

keybinds = [[['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'],
            ['ctrl', 'alt', 'meta', 'shift', 'space', 'fn1', 'fn2', 'home', 'end', 'backspace']],
            [['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10'], ## fn1 layer
             ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
             ['', '', '', '', '', '', '', '', '', '']
            ]]

## setup
rowPins = [0, 1, 2, 3]
temp = []
for pin in rowPins:
    #temp = digitalio.DigitalInOut((board.GP0))
    #temp.append(digitalio.DigitalInOut(board.{pin}))
    exec(f'temp.append(digitalio.DigitalInOut(board.GP{pin}))')
    rowPins = temp

colPins = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
temp = []
for pin in colPins:
    exec(f'temp.append(digitalio.DigitalInOut(board.GP{pin}))')
    colPins = temp


outputPins = []
inputPins = []
liveCols = []
liveRows = []

## end setup
while True:
    liveCols = []
    liveRows = []   ## check for live columns
    ## set the rows as outputs
    for pin in rowPins:
        pin.direction = digitalio.Direction.OUTPUT
        pin.value = True ## this should have the same functionality

    ## set the columns as inputs
    for index, pin in enumerate(colPins):
        inputPins = colPins
        pin.direction = digitalio.Direction.INPUT
        pin.pull = digitalio.Pull.DOWN
        # for every pin, define it as an input with a default low value

        if inputPins[index].value:
            liveCols.append(index)

    sleep(.02)
    ##check rows
    ## set columns as outputs
    for pin in colPins:
        outputPins = colPins
        pin.direction = digitalio.Direction.OUTPUT
        pin.value = True ## this should have the same functionality

    ## set the rowPins as inputs
    for index, pin in enumerate(rowPins):
        inputPins = rowPins
        pin.direction = digitalio.Direction.INPUT
        pin.pull = digitalio.Pull.DOWN
 
        if inputPins[index].value:
            liveRows.append(index)
            
    print('row', liveRows)
    print('col', liveCols)

    sleep(.02)
## TODO add keybind logic
## TODO add shift logic
## TODO add shift + fn1 logic for shift + numkeys


''' begin seudocode
if fn1 is pressed:
    keyboard.press(keybinds[1][row][col])
elif fn2 is pressed:
    keyboard.press(keybinds[2][row][col])
*insert optional if fn1 and fn2 are pressed*
elif not (fn1 or fn2):
    keyboard.press(keybinds[0][row][col])
end pseudocode'''
