from flask import Flask, request
from celery_app import send_email
import logging
from datetime import datetime

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='/var/log/messaging_system.log', level=logging.INFO)

@app.route('/')
def index():
    return "Welcome to the messaging system. Use '?sendmail=' or '?talktome' parameters."

@app.route('/sendmail')
def sendmail():
    recipient = request.args.get('sendmail', 'example@example.com')
    send_email.delay(recipient)
    return f"Email sending task queued for {recipient}"

@app.route('/talktome')
def talktome():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Talktome request received at {current_time}")
    return f"Current time logged: {current_time}"

if __name__ == '__main__':
    app.run(debug=True)