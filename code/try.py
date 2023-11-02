import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os


def send_email(links, lines):
    lines_list = '\n'.join([f'<li>{line}</li>' for line in lines])
    links_list = '\n'.join([f'<li>{link}</li>' for link in links])

    html = f'''
        <h2>All Links:</h2>
        <ul>
            {lines_list}
        </ul>

        <h2>Interested Links:</h2>
        <ul>
            {links_list}
        </ul>
    '''

    sender_email = "hammadirshad305@outlook.com"
    receiver_emails = maillist

    message = MIMEMultipart()
    message['From'] = 'hammad irshad <hammadirshad305@outlook.com>'
    message['To'] = ', '.join(receiver_emails)
    message['Subject'] = 'Udemy coupon sender python'

    message.attach(MIMEText(html, 'html'))

    try:
        smtp_server = smtplib.SMTP('smtp.office365.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, 'tgyfajllloxuuuim')
        smtp_server.sendmail(sender_email, receiver_emails, message.as_string())
        smtp_server.quit()
        print("Message sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")


# Initialize an empty list to store links
links = []
# Initialize an empty list to store lines
lines = []
temp = []

# Define the list of email addresses
maillist = [
    'hammadirshad300@gmail.com',
    'hammadirshad23@gmail.com',
    'iqna2018@gmail.com',
]

# Read the contents of text.txt
with open('code/text.txt', 'r') as file:
    data = file.read()

    with open('code/temp.txt', 'r') as word_file:
        word = word_file.read()
        temp = word.split('\n')

        # Split the file content into an array of lines
        lines = data.split('\n')

        # Iterate through the lines
        for line in lines:
            if any(keyword in line for keyword in ['php', 'python', 'google', 'aws', 'azure', 'scrap', 'bootcamp', 'js', 'language', 'microsoft', 'learn', 'react', 'gcp', 'project', 'learning']):
                links.append(line.strip())  # Strip to remove any extra spaces
        print(word)
        print(data)
        # If there are links, send an email
        if word != data:
            send_email(links, lines)

        with open('code/temp.txt', 'w') as temp_file:
            temp_file.write('\n'.join(lines))
            print("Data written to file successfully.")


# def send_email(links, lines):
#     lines_list = '\n'.join([f'<li>{line}</li>' for line in lines])
#     links_list = '\n'.join([f'<li>{link}</li>' for link in links])

#     html = f'''
#         <h2>All Links:</h2>
#         <ul>
#             {lines_list}
#         </ul>

#         <h2>Interested Links:</h2>
#         <ul>
#             {links_list}
#         </ul>
#     '''

#     sender_email = "hammadirshad305@outlook.com"
#     receiver_emails = maillist

#     message = MIMEMultipart()
#     message['From'] = 'hammad irshad <hammadirshad305@outlook.com>'
#     message['To'] = ', '.join(receiver_emails)
#     message['Subject'] = 'Udemy coupon sender'

#     message.attach(MIMEText(html, 'html'))

#     try:
#         smtp_server = smtplib.SMTP('smtp.office365.com', 587)
#         smtp_server.starttls()
#         smtp_server.login(sender_email, 'tgyfajllloxuuuim')
#         smtp_server.sendmail(sender_email, receiver_emails, message.as_string())
#         smtp_server.quit()
#         print("Message sent successfully")
#     except Exception as e:
#         print(f"Error sending email: {e}")
