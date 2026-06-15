from flask import Flask,render_template,url_for,redirect,request,flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
load_dotenv()
app= Flask(__name__, template_folder= 'templates', static_folder='static', static_url_path='/')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cont')
def cont():
    return render_template('contact.html')
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config[ 'MAIL_SERVER'] ='smtp.gmail.com'
app.config['MAIL_PORT'] = 465

app.config[ 'MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config[ 'MAIL_USE_TLS'] = False
app.config[ 'MAIL_USE_SSL'] = True
app.config[ 'MAIL_USERNAME'] = 'tasco263@gmail.com'
mail = Mail(app)

@app.route('/send_email', methods=["POST"])
def send_email():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    
    msg = Message(
        subject=f"Contact Form: {subject}",
        sender=app.config['MAIL_USERNAME'],
        recipients=['tasco263@gmail.com'],
        reply_to=email
    )

    msg.body = f"""
Name: {name}
Email: {email}

Message:
{message}
"""

    mail.send(msg)

    flash('Email sent successfully!')
    return redirect(url_for('cont'))


@app.route('/proj')
def proj():
    return render_template('projects.html')
    
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team():
    return render_template('team.html')
    
    

if __name__ == '__main__':

    
    

    app.run(host='0.0.0.0', port=8080, debug=True)


