from flask import Flask,render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Step 2: Configure Flask-Mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Your email server (Gmail in this case)
app.config['MAIL_PORT'] = 587  # Port for Gmail's SMTP server
app.config['MAIL_USE_TLS'] = True  # Use TLS (Transport Layer Security)
app.config['MAIL_USERNAME'] = 'zuruel.kamande@student.moringaschool.com'  # Your email address
app.config['MAIL_PASSWORD'] = 'vwba cbyj ibwv ztnf'  # Your email password
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']  # Default sender email

mail = Mail(app)

# Define a route to send email
@app.route('/')
def send_email():
    try:
        msg = Message(
            subject='Hello from the other side!',
            sender=app.config['MAIL_USERNAME'],  # Explicit sender
            recipients=['zurueladrian@gmail.com']
        )
        msg.body = "Hey Zuruel, sending you this email from my Flask app, asking if Maxwell is a legit Arsenal fan."
        mail.send(msg)
        return render_template("index.html")
    except Exception as e:
        return f"An error occurred: {e}"
    

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run("127.0.0.1", 5006, debug=True)
