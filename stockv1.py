# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 00:53:09 2019

@author: Tejas
"""

import datetime as dt
from datetime import date
import pandas as pd
import pandas_datareader.data as web

import smtplib
import config


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Some Issue you need to check the code bro!!!")


current_date = []
today = date.today()

tdy = (today.strftime('%Y,%m,%d')).split(',')

for i in tdy:
    current_date.append(int(i))

start = dt.datetime(2000,1,1)
end = dt.datetime(current_date[0],current_date[1],current_date[2])

df = web.DataReader('ADANIPOWER.NS' , 'yahoo' , start , end)

latest_data = ((df['Adj Close'].tail(1).to_string(index=False)).split('\n'))[1]
latest_data = float(latest_data)

if latest_data < 65:
    subject = "Share Buy Request"
    msg = "Hello there, the ADANIPOWERS share price are at buying position with %f per share price"%latest_data  
    send_email(subject, msg)
    
else:
    pass



