import os
import threading
def openFile():
    os.system("notepad.exe Functionalities.txt")
t1 = threading.Thread(target=openFile).start()
print("Done")