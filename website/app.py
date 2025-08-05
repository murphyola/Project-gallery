from flask import Flask,render_template,url_for,redirect,request
from flask_mail import Mail, Message
app= Flask(__name__, template_folder= 'templates', static_folder='static', static_url_path='/')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cont')
def cont():
    return render_template('contact.html')

app.config[ 'MAIL_SERVER'] ='smtp.gmail.com'
app.config[ 'MAIL_PORT'] = 465
app.config[ 'MAIL_USERNAME'] = 'murphyola112@gmail.com'
app.config[ 'MAIL_PASSWORD'] = 'hsizqjahmiogdgfw'
app.config[ 'MAIL_USE_TLS'] = False
app.config[ 'MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/send_email', methods=["POST"])
def send_email():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    
    msg = Message(subject=subject, sender=email, recipients=['murphyola112@gmail.com'])
    msg.body = message
    mail.send(msg)
    return 'Email sent successfully'


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
    app.run(host='0.0.0.0', debug=True)

