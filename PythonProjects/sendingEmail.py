#!python3

import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587) #port 587 for gmail SMTP traffic commonly

type(conn) #returns <class 'smtplib.SMTP'>

conn.ehlo() #hello function used to start the connection
conn.starttls() # encrypts traffic with tls

conn.login('username@gmail.com', 'password') #Google restricts this due to new security rules that are to protect user information

conn.sendmail('username@gmail.com', 'destination@gmail.com', 'Subject: This is the Subject Format\n\nDear Brycen,\nThanks for your hard work.\nHave a great day!\n\n-Brycen') # format includes new lines twice to change from Subject, to Body, to signature.

conn.quit()
