# Load environment variables
load_dotenv()

# Configure Celery
app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//')

@app.task
def send_email(recipient):
    # SMTP Configuration
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))
    smtp_username = os.getenv('SMTP_USERNAME')
    smtp_password = os.getenv('SMTP_PASSWORD')

    # Email content
    subject = "Test Email"
    body = "This is a test email sent from the Python application."
    sender = "sender@example.com"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
        return f"Email sent to {recipient}"
    except Exception as e:
        return f"Failed to send email: {str(e)}"