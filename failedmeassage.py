import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls()   
# Authentication 
s.login("shaileshchoudhary1999@gmail.com", "19101996") 
# message to be sent 
message = "Hey Developer,Website is not working. please check the code and push again"
# sending the mail 
s.sendmail("shaileshchoudhary1999@gmail.com", "shaileshchoudhary1999@gmail.com", message) 
# terminating the session 
s.quit()
