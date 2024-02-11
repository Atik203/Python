import pyautogui
import time
def print_pyramid(rows):
    pyramid_text = ""
    for i in range(1, rows + 1):
        hash = '# ' * i
        spaces = ' ' * (rows - i)
        line =   hash +spaces+ '\n'
        pyramid_text += line
    pyautogui.typewrite(pyramid_text)
    
        
rows = int(input())
time.sleep(5)
print_pyramid(rows)
