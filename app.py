from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Email configuration
    sender_email = 'mycheelly@gmail.com'
    sender_password = 'sua-senha'
    receiver_email = 'mycheelly@gmail.com'
    subject = 'Novo formulário de contato'

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    body = f"Nome: {name}\nEmail: {email}\nMensagem: {message}"
    msg.attach(MIMEText(body, 'plain'))

    # Send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    return 'Formulário enviado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
