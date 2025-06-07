
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(df):
    sender_email = "your_email@gmail.com"   
    receiver_email = "receiver_email@gmail.com"
    app_password = "your_app_password"  # For Gmail, use App Passwords

    # Email subject & content
    subject = "SLA Violations Detected"
    body = "Hi,\n\nThe following services violated SLA thresholds:\n\n"
    body += df.to_string(index=False)
    body += "\n\nRegards,\nSLA Monitoring System"

    # Create email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Send
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email alert sent successfully.")
    except Exception as e:
        print("Failed to send email:", str(e))
