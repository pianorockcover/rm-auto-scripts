import pyautogui
import time
import tkinter.messagebox

# Close ALL Windows exept AT
# Put autotune tanspose input to coordinates 1022, 145

time.sleep(5)

class WavNote(object):
    def __init__(self, transpose, name):
        self.transpose = transpose
        self.name = name

def transposeAndExport(note):
    pyautogui.click(1022, 145)
    time.sleep(1)
    pyautogui.write(note.transpose)

    time.sleep(1)

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.keyDown('r')

    time.sleep(1)

    pyautogui.keyUp('r')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')

    time.sleep(1)

    pyautogui.write(note.name)
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('enter')

    time.sleep(2)

files = [WavNote('0', 'E2.mp3'),
         WavNote('1', 'F2.mp3'),
         WavNote('2', 'Fs2.mp3'),
         WavNote('3', 'G2.mp3'),
         WavNote('4', 'Gs2.mp3'),
         WavNote('5', 'A2.mp3'),
         WavNote('6', 'As2.mp3'),
         WavNote('-5', 'B2.mp3'),
         WavNote('-4', 'C2.mp3'),
         WavNote('-3', 'Cs2.mp3'),
         WavNote('-2', 'D2.mp3'),
         WavNote('-1', 'Ds2.mp3'),
         WavNote('0', 'E3.mp3')]

for file in files:
    transposeAndExport(file)
    print(file.name, file.transpose)

tkinter.messagebox.showinfo(title='Autotune Done!!!',message='Eeeee, done!')