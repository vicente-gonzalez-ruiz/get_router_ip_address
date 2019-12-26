# https://realpython.com/python-send-email/
# https://myaccount.google.com/lesssecureapps

import socket
import sys
import os
import time
import smtplib, ssl

from datetime import datetime

user = input("Username in gmail (without <@gmail.com>? ")
password = input("Password in gmail? ")

sender_email = user + "@gmail.com"
receiver_email = user + "@gmail.com"

old = ""
while True:
    stream = os.popen("curl ipecho.net/plain")
    message = stream.read()
    if old != message:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            #sys.stdout.write(f"{dt_string}: Sending \"{message}\" ... "); sys.stdout.flush()
            sys.stdout.write("{}: : Sending \"{}\" ... ".format(dt_string,message))
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            sys.stdout.write("done\n");
    old = message
    time.sleep(60)
