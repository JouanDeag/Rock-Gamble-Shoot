import os
import random


random_number = random.randint(0, 5)

current_path = os.getcwd()

# Select path based on random number
if (random_number == 0):
    os.system("start chrome https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if (random_number == 1):
    os.system("taskkill /f /im discord.exe")
    
if (random_number == 3):
    pass

if (random_number == 4):
    os.system("start chrome https://www.youtube.com/watch?v=9bZkp7q19f0")
    
if (random_number == 5):
    os.system(f"del {current_path}/main.exe")