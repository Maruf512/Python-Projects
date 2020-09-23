import smtplib


a = input("Enter your email address: ")
b = input("Enter the password: ")
c = input("Where do you want to sent the email: ")
d = input("Enter the Massage you want to send: ")


server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(a, b)
server.sendmail(a, c, d)
server.quit()
print("Your email has been successfully sended")
