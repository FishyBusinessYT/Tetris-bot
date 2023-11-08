from win32api import mouse_event, SetCursorPos

from time import sleep

def click(normalizedpos, left):
    SetCursorPos((int(259*normalizedpos) + 843, 945))
    if left:
        mouse_event(2, 0, 0); mouse_event(4, 0, 0)
    else:
        mouse_event(8, 0, 0); mouse_event(16, 0, 0)

def move(normalizedpos):
    SetCursorPos((int(259*normalizedpos) + 855, 945))

def restart():
    for i in range(40):
        click(0.5, 1)
        sleep(0.05)
    SetCursorPos((960, 800))
    mouse_event(2, 0, 0); mouse_event(4, 0, 0)
