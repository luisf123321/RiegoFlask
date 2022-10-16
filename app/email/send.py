import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

class SendEmail:

    @classmethod
    def send(cls, body, email, title):
        try:
            message = MIMEMultipart()
            message['From'] = 'u20162151531@usco.edu.co'
            message['To'] = email
            message['Subject'] = title
            message.attach(MIMEText(body, 'html'))
            server = smtplib.SMTP('smtp.gmail.com', 587)            
            fp = open('app/email/Logo_Riego.svg', 'rb')
            msgImage = MIMEImage(fp.read(),_subtype="svg+xml")
            fp.close()
            msgImage.add_header('Content-ID', '<image1>')
            message.attach(msgImage)
            msg_full = message.as_string()
            server.starttls()
            server.login('u20162151531@usco.edu.co', 'ioapechsxnfjfanw')
            server.sendmail(from_addr='u20162151531@usco.edu.co',
                            to_addrs="encisolf901@gmail.com", msg=msg_full)
            server.quit()
        except Exception as e:
            print(e)
            print('Something went wrong...')
