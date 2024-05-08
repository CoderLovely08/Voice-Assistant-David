import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "davidvoiceassistant7@gmail.com"
password = "kvpe bluh srlf xxcb"
receiver_email = "lovelysharmaas0812@gmail.com"

# Create message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = "Subject of the email"

# Email body
body = "This is the body of the email."
message.attach(MIMEText(body, 'plain'))

# SMTP server setup for Gmail
smtp_server = "smtp.gmail.com"
port = 587  # Gmail SMTP port

# Start TLS connection
context = smtplib.SMTP(smtp_server, port)
context.starttls()

# Login to Gmail
context.login(sender_email, password)

# Send email
text = message.as_string()
context.sendmail(sender_email, receiver_email, text)

# Close connection
context.quit()

def preprocess_email(email):
    # Reverse the email address and replace the first occurrence of "ta" with "@"
    processed_email = email[::-1].replace("ta", "@", 1)[::-1].replace(" ", "")
    
    return processed_email.lower()

email = input()
processed_email = preprocess_email(email)
print(processed_email)