import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime as dt


def sendmail(to_email, letter):
    """
    Function to send an email.

    Parameters:
    - to_email: The recipient's email address.
    - letter: The body of the email.
    """
    # SMTP server configuration
    smtp_server = "smtp.example.com"
    port = 587  # For STARTTLS
    from_email = "johndoe@example.com"  # Sender's email address
    password = "password"  # Sender's email password

    # Create a MIMEText message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Happy Birthday!"
    body = letter
    msg.attach(MIMEText(body, 'plain'))

    # Convert the message to a string
    message_string = msg.as_string()

    # Create an SMTP connection
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()  # Upgrade the connection to secure
        server.login(from_email, password)  # Log in to the SMTP server
        # Send the email
        server.sendmail(from_email, to_email, message_string)


with open("quotes.txt", "r") as file:
    quotes = [line.strip() for line in file]

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    sendmail(random.choice(quotes))
