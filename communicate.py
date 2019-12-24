# https://realpython.com/python-send-email/
# https://myaccount.google.com/lesssecureapps

import socket
import sys
import os
import time
import smtplib, ssl

from datetime import datetime

stream = os.popen("curl ipecho.net/plain")
message = stream.read()

user = input("Username in gmail (without <@gmail.com>? ")
password = input("Password in gmail? ")

sender_email = user + "@gmail.com"
receiver_email = user + "@gmail.com"

while True:
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        sys.stdout.write(f"{dt_string}: Sending \"{message}\" ... "); sys.stdout.flush()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        sys.stdout.write("done\n");
    time.sleep(3600)

quit()

from datetime import datetime

port = 4552

user = input("Username in gmail (without <@gmail.com>? ")
password = input("Password in gmail? ")

sender_email = user + "@gmail.com"
receiver_email = user + "@gmail.com"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(3600)
s.bind(("0.0.0.0", port))

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print(f"{dt_string}: Listening on {port}")

def send_email(message):

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        sys.stdout.write(f"{dt_string}: Sending \"{message}\" ... "); sys.stdout.flush()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        sys.stdout.write("done\n");

prev_client = None
while True:
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    try:
        _, client = s.recvfrom(4096)
        sys.stdout.write(f"{client}\n")
        
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        if client != prev_client:
            sys.stdout.write("{dt_string}: The client has changed its IP address\n")
            send_email(str(client))
            
        prev_client = client

    except socket.timeout:
        sys.stdout.write("{dt_string}: Client disconnected\n")
        send_email("Client disconnected")
