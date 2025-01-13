import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

fromaddr = "use_your_from_email"
toaddr = "use_your_to_email"
mypass = "your_from_email_SMTP_service_password"
report_name = "report.html"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test report - 4 seminar"

with open(report_name, 'rb') as f:
    part = MIMEApplication(f.read(), Name=basename(report_name))
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(report_name)
    msg.attach(part)

body = "This test message"
msg.attach(MIMEText(body, "plain"))

server = smtplib.SMTP_SSL('smtp.mail.ru', 465) #for example mail.ru
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
