import ctypes
from ctypes import wintypes
import psutil
import time
from datetime import datetime
import keyboard 

while True:
    if keyboard.is_pressed("p"):
        break
    active_old = ctypes.windll.user32.GetForegroundWindow()
    time.sleep(3)
    active_new = ctypes.windll.user32.GetForegroundWindow()
    if active_old != active_new:
        pid = wintypes.DWORD()
        active_window = ctypes.windll.user32.GetWindowThreadProcessId(active_new,ctypes.byref(pid))
        pid = pid.value
        for item in psutil.process_iter():
            if pid == item.pid:
                file = open("log.txt", "a")
                current_datetime = datetime.now()
                file.write(str(current_datetime)[:-7]+" ")
                file.write(item.name()+"\n")
                file.close()