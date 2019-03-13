from flask import Flask, render_template, request

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
