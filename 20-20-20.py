from time import sleep
import pyttsx3
from win10toast import ToastNotifier
from configparser import ConfigParser
import os

# Creating Default 'config.ini' File (In Case File Not Exit)
if os.path.exists('config.ini'):
    pass
else:
    print("'Config.ini' file Has Created")
    with open ('config.ini','w') as f:
        f.write('[Work]\nMinutes = 20\n\n[Rest]\nMinutes = 0\nSeconds = 20')

# Audio Reminder Function (Time to Rest)
def rest_voice():
    program=pyttsx3.init()
    voices = program.getProperty('voices')
    program.setProperty('rate',160)
    program.setProperty('voice', voices[1].id)
    program.say('Time to Rest')
    program.runAndWait()

# Audio Reminder Function (Time to Work)
def work_voice():
    program=pyttsx3.init()
    voices = program.getProperty('voices')
    program.setProperty('rate',160)
    program.setProperty('voice', voices[1].id)
    program.say('Time to Work')
    program.runAndWait()

# Shows Windows notification (Rest Reminder)
def rest_notification():
    toaster = ToastNotifier()
    toaster.show_toast("20-20-20 Rule", 
                       "Time to Rest\nLook at 20 Feet away",
                       duration=1,threaded=False)
    
# Shows Windows notification (Work Reminder)
def work_notification():
    toaster = ToastNotifier()
    toaster.show_toast("20-20-20 Rule", 
                       "Time to work",
                       duration=1,threaded=False)

# Extracting 'config.ini' Data
config=ConfigParser()
config.read('config.ini')
work_time=config['Work']['Minutes']
print('Work Time :',work_time, ' Minutes')
rest_time = config ['Rest']['Minutes']

# Using 'config.ini' Second Or Minute For Rest Time
if float(rest_time) > 0:
    print('Rest Time :',rest_time,'Minutes\n')
    rest_time = float(rest_time) * 60
else :
    rest_time = int(config ['Rest']['Seconds']) 
    print('Rest Time :',rest_time, 'Seconds\n')

# Using "config.ini" Work Time And Starting The Reminder Loop
work_time=float(work_time)*60
work_voice()
work_notification()

# Extra Decoration
print('\nDevloper: Ignore "TypeError"')
print('Work in Progress...')

# Main Reminder Loop Body
while True:
    sleep(work_time)
    rest_voice()
    rest_notification()
    print('Rest in Progress...')
    print('')
    sleep(rest_time)
    work_voice()
    work_notification()
    print('Work in Progress...')
    print('')