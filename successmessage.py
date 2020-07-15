import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls()   
# Authentication 
s.login("shaileshchoudhary1999@gmail.com", "password") 
# message to be sent 
message = "Server running"
# sending the mail 
s.sendmail("sender", "reciever", message) 
# terminating the session 
s.quit()
