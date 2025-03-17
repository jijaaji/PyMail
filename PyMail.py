import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Gmail account credentials (replace with your actual credentials)
sender_email = "example@gmail.com"  # Your Gmail address
sender_password = "xxxx xxxx xxxx xxxx"  # Your Gmail app password (see instructions below)

# Recipient information (list of dictionaries with name and email)
recipients = [
    {"name": "Meagan", "email": "mbehm@kforce.com"},
    {"name": "April", "email": "areed@kforce.com"},
    {"name": "Kaeleigh", "email": "kdorgan@apexsystems.com"}
]

# Email subject and body
subject = "Python Automated Email"
body = """
Hi {name},

Hope this email finds you awesome.
We're the approved vendor of your company.

I'm reaching out to discuss any open position with you, where we can help.
If yes, do let me know because we help staffing companies to find Top Tier Tech Talents on a C2C & W2 basis with hourly or one time referral fees.

Looking forward to your response.

Thanks & Regards,
Your Name

"""

# SMTP server details (for Gmail)
smtp_server = "smtp.gmail.com"
port = 465  # For SSL

def send_email(recipient_name, recipient_email, email_subject, email_body):
    """Sends an email to a single recipient."""

    # Create the email message
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = email_subject

    # Format the email body with the recipient's name
    formatted_body = email_body.format(name=recipient_name)

    # Attach the formatted body to the email
    message.attach(MIMEText(formatted_body, "plain"))  # You can also use "html" for HTML email

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
            print(f"Email sent successfully to {recipient_name} ({recipient_email})")

    except Exception as e:
        print(f"Error sending email to {recipient_name} ({recipient_email}): {e}")


# Main loop to send emails to all recipients
if __name__ == "__main__":
    for recipient in recipients:
        send_email(recipient["name"], recipient["email"], subject, body)

    print("All emails sent (or attempted).")


# IMPORTANT NOTES:
# 1.  Gmail App Password:  You need to enable "less secure app access" OR, ideally,
#     create an "App Password" in your Gmail account settings to use with Python.
#     -  Less Secure App Access (less recommended):  Go to your Google account settings
#        (https://myaccount.google.com/), then "Security", and turn on "Less secure app access".
#        Google is phasing this out, so the next method is preferred.
#     -  App Password (recommended):
#        a. Enable 2-Step Verification on your Google account.
#        b. Go to your Google account settings (https://myaccount.google.com/), then "Security".
#        c. Under "How you sign in to Google", click "App Passwords".
#        d. Select "Mail" and "Other (Custom name)".
#        e. Give it a name (e.g., "Python Script").
#        f. Click "Generate".  This will give you a 16-character password.  **Use this
#           password** in the `sender_password` variable in your script. Store this password
#           securely.

# 2.  Security Considerations:  Storing your email credentials directly in the script is
#     generally not recommended for production environments.  Consider using environment variables
#     or a configuration file to store these credentials securely.

# 3.  Rate Limiting:  Gmail has rate limits on sending emails.  If you send too many emails too
#     quickly, your account might be temporarily blocked.  Consider adding delays between emails
#     if you're sending to a large list.

# 4.  Error Handling: The `try...except` block in the `send_email` function catches potential
#     errors during the email sending process. You can customize the error handling to log
#     errors, retry sending, or take other appropriate actions.

# 5.  HTML Emails:  To send HTML emails, change `MIMEText(formatted_body, "plain")` to
#     `MIMEText(formatted_body, "html")` and make sure your `body` variable contains HTML markup.