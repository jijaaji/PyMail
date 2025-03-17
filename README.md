# Python Automated Email Script

This Python script sends automated emails to a list of recipients using Gmail. It utilizes the `smtplib`, `ssl`, and `email` modules to construct and send emails securely.

## Prerequisites

*   **Python 3.x:** Ensure you have Python 3.x installed on your system.
*   **Gmail Account:** You'll need a Gmail account to send emails from.
*   **App Password (Recommended):** You **must** generate an App Password for your Gmail account.  Using your regular Gmail password directly is highly discouraged and may not work due to security policies.  See instructions below.

## Setup

1.  **Install Required Modules:** (Not strictly necessary, as these are built-in Python modules, but good practice to mention).

    ```bash
    # No modules to install. All modules are built-in.
    # Example if there were modules: pip install <module_name>
    ```

2.  **Configure Credentials:**

    *   Open the `your_script_name.py` file (replace `your_script_name.py` with the actual name of your script).

    *   **Important:** Replace the placeholder values for `sender_email` and `sender_password` with your actual Gmail address and **App Password**, respectively.

        ```python
        sender_email = "your_email@gmail.com"  # Your Gmail address
        sender_password = "xxxx xxxx xxxx xxxx"  # Your Gmail App Password
        ```

    *   **Gmail App Password Instructions:**

        1.  Enable 2-Step Verification on your Google account if you haven't already.
        2.  Go to your Google account settings: [https://myaccount.google.com/](https://myaccount.google.com/)
        3.  Navigate to "Security".
        4.  Under "How you sign in to Google," click "App Passwords".
        5.  Select "Mail" and "Other (Custom name)".
        6.  Give it a descriptive name (e.g., "Python Script").
        7.  Click "Generate".  This will provide a 16-character password. **This is the password you should use** for `sender_password`.
        8.  **Store the App Password securely.**

3.  **Configure Recipients:**

    *   Modify the `recipients` list to include the names and email addresses of the people you want to send emails to.

        ```python
        recipients = [
            {"name": "Meagan", "email": "mbehm@kforce.com"},
            {"name": "April", "email": "areed@kforce.com"},
            {"name": "Kaeleigh", "email": "kdorgan@apexsystems.com"}
        ]
        ```

4.  **Customize Email Content:**

    *   Modify the `subject` and `body` variables to change the email subject and body content.  The `body` uses a placeholder `{name}` that will be replaced with each recipient's name.

        ```python
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
        ```

## Usage

1.  **Run the Script:**  Execute the Python script from your terminal:

    ```bash
    python your_script_name.py
    ```
Open your terminal like CMD please locate the folder where you've saved the Python script. Once, you've located the directory/ location type python "python your_script_name.py" 

    Replace `your_script_name.py` with the actual name of your script file.

1.  **Check Output:** The script will print messages to the console indicating the status of each email sent.  It will also catch and print any errors that occur.

## Important Considerations

*   **Security:** Storing your email credentials directly in the script is **not recommended** for production environments.  Consider using environment variables, configuration files, or a secrets management system to store these credentials securely.

*   **Rate Limiting:** Gmail has rate limits on sending emails. Sending too many emails in a short period may result in your account being temporarily blocked.  If sending to a large list, add delays between emails (e.g., using `time.sleep()`).

*   **Error Handling:** The `try...except` block in the `send_email` function catches potential errors.  Customize the error handling to log errors, retry sending, or implement other appropriate actions.

*   **HTML Emails:**  To send HTML emails, change `MIMEText(formatted_body, "plain")` to `MIMEText(formatted_body, "html")` in the `send_email` function, and ensure your `body` variable contains valid HTML markup. For example:

    ```python
    message.attach(MIMEText(formatted_body, "html"))
    body = """
    <html>
      <body>
        <p>Hi {name},</p>
        <p>This is an <b>HTML email</b>.</p>
      </body>
    </html>
    """
    ```

*   **Sender Name:**  To specify a sender name in addition to the sender email, modify the `message["From"]` line to include the name like this:

    ```python
    from email.utils import formataddr
    message["From"] = formataddr(("Your Name", sender_email))
    ```

*   **Attachments:** To add attachments, you'll need to use the `email.mime.base` and `email.encoders` modules.  Search online for "Python send email with attachment" for examples.

*   **Dependencies:** The `smtplib`, `ssl` and `email` modules are built-in Python modules. You shouldn't need to install anything explicitly using `pip`.
