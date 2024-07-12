from celery import Celery
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Celery
celery = Celery('tasks', broker=os.getenv('CELERY_BROKER_URL', 'amqp://guest:guest@localhost:5672//'))

@celery.task
def send_email(recipient):
    # This is a mock email sending function
    print(f"Sending email to {recipient}")
    return f"Email sent to {recipient}"