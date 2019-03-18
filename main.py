from flask import Flask, render_template, request
# import mail
import google.appengine.api.mail as mail

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dev-jordan')
def dev_jordan():
    return render_template('dev_jordan.html')

@app.route('/my-dev-work')
def my_dev_work():
    return render_template('my_dev_work.html')

@app.route('/sax-jordan')
def sax_jordan():
    return render_template('sax_jordan.html')

@app.route('/my-sax-work')
def my_sax_work():
    return render_template('my_sax_work.html')

@app.route('/va-jordan')
def va_jordan():
    return render_template('va_jordan.html')

@app.route('/my-visual-work')
def my_visual_work():
    return render_template('my_visual_work.html')

@app.route('/bike-jordan')
def bike_jordan():
    return render_template('bike_jordan.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        contact_email = ''
        with file('contact_email.txt') as f:
            contact_email = f.read().strip('\n')
        mail.send_mail(sender=email,
                to=contact_email,
                subject="Message from the website :)",
                body=message)
        return render_template('thanks_for_contacting.html')
    elif request.method == 'GET':
        return render_template('contact.html')


