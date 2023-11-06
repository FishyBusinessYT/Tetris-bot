from win32api import mouse_event, SetCursorPos

def click(normalizedpos, left):
    SetCursorPos((int(259*normalizedpos) + 843, 945))
    if left:
        mouse_event(2, 0, 0); mouse_event(4, 0, 0)
    else:
        mouse_event(8, 0, 0); mouse_event(16, 0, 0)

def move(normalizedpos):
    SetCursorPos((int(259*normalizedpos) + 843, 945))