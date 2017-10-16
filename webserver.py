import requests
import os

from flask import Flask, render_template


app = Flask(__name__,static_url_path="/static")

@app.route('/')
def homepage():
	return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about')
def aboutus():
    return render_template("aboutus.html")

@app.route('/contact')
def contactus():
    return render_template("contactus.html")

@app.route('/blog/8-experiments-in-motivation')
def blog1():
    return render_template("/blog/8_Experiments_in_Motivation.html")

@app.route('/blog/a-mindful-shift-of-focus')
def blog2():
    return render_template("blog/A_Mindful_Shift_of_Focus.html")

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def blog3():
    return render_template("/blog/How_to_Develop_an_Awesome_Sense_of_Direction.html")

@app.route('/blog/training-to-be-a-good-writer')
def blog4():
    return render_template("/blog/Training_to_Be_a_Good_Writer.html")

@app.route('/blog/what-productivity-systems-wont-solve')
def blog5():
    return render_template("/blog/What_Productivity_Systems_Won't_Solve.html")

@app.route('/contact', methods = ['GET'])
def contact():
	return render_template("contactus.html", notifications=[])

@app.route('/contact', methods=['POST'])
def send_email():
    message = request.form.get("message")
    subject = request.form.get("subject")
    firstname = request.form.get("fisrtname")
    lastname = request.form.get("lastname")
    notifications = []

    auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])

    data = {
        'from': os.environ["INFO253_MAILGUN_FROM_EMAIL"],
        'to': os.environ["INFO253_MAILGUN_TO_EMAIL"],
        'subject': subject,
        'text': "Subject = " + subject + "\n" + "Firstname = " + firstname + "\n" + "Last name = " + lastname + "\n" + "Message = " + message
        }

    r = requests.post(
        'https://api.mailgun.net/v3/{}/messages'.format(os.environ["INFO253_MAILGUN_DOMAIN"]),
        auth=auth,
        data=data)
    
    if r.status_code == requests.codes.ok:
        notifications.append("Your email was sent")
    else:
        notifications.append("You email was not sent. Please try again later")



    return render_template("contact.html", notifications=notifications)


