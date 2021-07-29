import subprocess
import keyboard
import time
from tkinter.font import Font
from breezypythongui import EasyFrame

class SleepTimer(EasyFrame):
    
    def __init__(self):
        # Build GUI
        EasyFrame.__init__(self, width = 250, height = 200, title = "Sleep Timer")
        # Label
        mainLabel = self.addLabel(text = "SELECT INTERVAL", row = 1, column = 0)
        timerLabel = self.addLabel(text = "00:00", row = 2, column = 0)
        # Select buttons
        # 30 min
        self.addButton(text = "30 min.", row = 1, column = 1, command = self.sleep30)
        # 45 min
        self.addButton(text = "45 min.", row = 2, column = 1, command = self.sleep45)
        # 60 min
        self.addButton(text = "60 min.", row = 3, column = 1, command = self.sleep60)
        # 120 min
        self.addButton(text = "120 min.", row = 4, column = 1, command = self.sleep120)
        # Abort
        self.addButton(text = "Abort", row = 5, column = 0, command = self.abort)
        
        # Design
        self.setResizable(False)
        font = Font(family = "Verdana", size = 12, slant = "italic")
        mainLabel["font"] = font
        mainLabel["foreground"] = "blue"
        #self.setBackground("blue")
        # image        
        
    # Sleep funtions
    def sleep30(self):
        subprocess.call([r'C:\Users\awilmes\Scripts\Python\sleep30.bat'])
        countdown(int(1201))       
        
    def sleep45(self):
        subprocess.call([r'C:\Users\awilmes\Scripts\Python\sleep45.bat'])
        countdown(int(2101))
        
    def sleep60(self):
        subprocess.call([r'C:\Users\awilmes\Scripts\Python\sleep60.bat'])
        countdown(int(3001))
        
    def sleep120(self):
        subprocess.call([r'C:\Users\awilmes\Scripts\Python\sleep120.bat'])
        countdown(int(6601))
        
    def abort(self):
        subprocess.call([r'C:\Users\awilmes\Scripts\Python\sleepAbort.bat'])

        
def countdown(t):    
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        keyboard.press_and_release('enter')
        
def main():
    SleepTimer().mainloop()
    
if __name__ == "__main__":
    main()