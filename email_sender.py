import smtplib
from email.message import EmailMessage 

email=EmailMessage()
email['from']='Abeer'
email['to']='saptarshiabeer2004@gmail.com'
email['subject']='TEST'
email.set_content('I am sending my first mail for test...')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('saptarshiabeerwork2004@gmail.com' , 'bxnr ekhe vqwu zssw')
    smtp.send_message(email)
    print("Email sent!!!")