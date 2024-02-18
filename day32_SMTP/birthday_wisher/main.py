import random
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime as dt


def sendmail(to_email, letter_name):
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
    body = letter_name
    msg.attach(MIMEText(body, 'plain'))

    # Convert the message to a string
    message_string = msg.as_string()

    # Create an SMTP connection
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()  # Upgrade the connection to secure
        server.login(from_email, password)  # Log in to the SMTP server
        # Send the email
        server.sendmail(from_email, to_email, message_string)


# Load birthdays from a CSV file into a Pandas DataFrame
birthdays = pd.read_csv("birthdays.csv")

# Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month

# Filter the DataFrame for rows where the month and day match today's date
matching_birthdays = birthdays[(birthdays['month'] == month) & (birthdays['day'] == day)]

# Iterate through the filtered DataFrame
for index, row in matching_birthdays.iterrows():
    # Randomly select a letter template
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as ltr_data:
        letter = ltr_data.read()
        # Replace placeholder with the recipient's name
        letter_name = letter.replace("[NAME]", row['name'])  # Ensure 'name' is correct column name
        # Send the customized email
        sendmail(row['email'], letter_name)  # Ensure 'email' is correct column name
