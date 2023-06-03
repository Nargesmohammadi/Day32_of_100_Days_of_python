# Automated birthday wisher

# Send Email Using smtplib

This repository provides a simple Python script (`send_email.py`) that demonstrates how to send an email using the `smtplib` library in Python.

## Methods

The `send_email.py` script provides a single function, `send_email`, which takes in several parameters and sends an email using the `smtplib` library. Here are the parameters required by the function:
- `sender`: The email address of the sender.
- `password`: The password for the sender's email account.
- `recipient`: The email address of the recipient.
- `subject`: The subject line of the email.
- `body`: The body text of the email.
- `attachment_path` (optional): The file path of any attachments to be included in the email.

The `send_email` function uses the SMTP protocol to connect to the email provider's server and authenticate the sender's credentials. It then creates an email message with the provided subject and body text, sets the sender and recipient addresses, and attaches any specified files. Finally, it sends the email message using the `smtplib` `sendmail` method.

## Customization

The `send_email.py` script can be customized to include additional functionality or handle different types of emails. For example, you could modify the script to send HTML-formatted emails or handle multiple recipients.

## Dependencies

The send_email.py script requires the smtplib, email, and os libraries in Python.

    The smtplib library is used to establish a connection to the SMTP server of your email provider and send the email.
    The email library is used to create and format the email message with the specified subject and body text.
    The os library is used to handle any attachments that are included in the email.

In addition to these libraries, the send_email.py script also makes use of the following methods:

    The getpass method from the getpass library is used to securely prompt the user for their email password without displaying it on the terminal.
    The basename method from the os.path library is used to extract the filename of any attachments, which is then added to the email message.



Overall, this repository provides a simple example of how to send emails using `smtplib` in Python. Developers can use the `send_email` function as a starting point to add similar functionality to their own projects and customize it to suit their specific needs.
