import pyautogui
import time
import tkinter.messagebox
import sys

# Disable CapsLock Or NumLock Before start!!!
# Close All Windows Except Piano Roll
# Select D#2 note!!!
# ./main.bat bass 2

time.sleep(5)

instrument = sys.argv[1]
number = sys.argv[2]


def exportNote(name):
    pyautogui.keyDown('shift')
    pyautogui.press('up')
    pyautogui.keyUp('shift')

    time.sleep(1)

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.keyDown('r')

    time.sleep(1)

    pyautogui.keyUp('r')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')

    time.sleep(1)

    pyautogui.write('C:\\Users\\Nikitos\\Documents\\rapme\\source\\api\\samples\\{}\\{}\\{}'.format(
        instrument, number, note))
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('enter')

    time.sleep(2)


# notes = ['E2.mp3',
#          'F2.mp3',
#          'Fs2.mp3',
#          'G2.mp3',
#          'Gs2.mp3',
#          'A2.mp3',
#          'As2.mp3',
#          'B2.mp3',
#          'C2.mp3',
#          'Cs2.mp3',
#          'D2.mp3',
#          'Ds2.mp3',
#          'E3.mp3']

#  For BASS
notes = [
    'A2.mp3',
    'As2.mp3',
    'B2.mp3',
    'C2.mp3',
    'Cs2.mp3',
    'D2.mp3',
    'Ds2.mp3',
    'E2.mp3',
    'F2.mp3',
    'Fs2.mp3',
    'G2.mp3',
    'Gs2.mp3']

for note in notes:
    exportNote(note)
    print(note)

tkinter.messagebox.showinfo(title='Export Done!!!', message='Eeeee, done!')
