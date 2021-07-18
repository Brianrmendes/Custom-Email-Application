# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# import pandas as pd
# from tkinter import *
#
# root = Tk()
# root.title("Gmail")
# e = Entry(root, width=35, borderwidth=5)
# e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#
# my_label = Label(root, text="Enter your email", padx=5, pady=5)
#
# '''
# email_list = pd.read_excel("test1.xlsx")
#
#
# # Get all the Names, Email Addreses, Subjects and Messages
# all_names = email_list['Name']
# all_emails = email_list['Email']
# tw = email_list['TW']
# th = email_list['THPA']
# seat = email_list['Seat']
#
#
# your_name = 'Brian'
# sender_address = 'brian.testemail007@gmail.com'
# sender_pass = 'Applepie123'
#
# session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
# session.starttls()  # enable security
# session.login(sender_address, sender_pass)  # login with mail_id and password
#
# for idx in range(len(all_emails)):
#     name = "Your PWP MARKS"
#     email = all_emails[idx]
#
#     subject = "PWP TW AND TH-PA MARKS"
#     mail_content = "Seat No : " + str(seat[idx]) + "  PWP Term Work : " + str(tw[idx]) + "  TH-PA [Average of (PT1 & PT2) plus MicroProject] : " + str(th[idx])
#
#     full_email = ("From: {0} <{1}>\n"
#                   "To: {2} <{3}>\n"
#                   "Subject: {4}\n\n"
#                   "{5}"
#                   .format(your_name, sender_address, name, email, subject, mail_content))
#
#     session.sendmail(sender_address, [email], full_email)
#
#
# receiver_address = 'mendesbrianr@gmail.com'
# #Setup the MIME
# message = MIMEMultipart()
# message['From'] = sender_address
# message['To'] = receiver_address
# message['Subject'] = 'A test mail sent by Python'
#
#
#
# # The body and the attachments for the mail
# message.attach(MIMEText(mail_content, 'plain'))
# filename = "test1.xlsx"
# attachment = open("E:/FrAgnel/Internship_stuff/Discover_Technologies/Projects/Gmail/test1.xlsx", "rb")
# p = MIMEBase('application', 'octet-stream')
# p.set_payload((attachment).read())
# encoders.encode_base64(p)
# p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
# message.attach(p)
#
# # Create SMTP session for sending the mail
# text = message.as_string()
# session.sendmail(sender_address, receiver_address, text)
# session.quit()
# print('Mail Sent')
# '''
# root.mainloop()