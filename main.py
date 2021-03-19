import csv
from flask import Flask, render_template, url_for, session, flash
from werkzeug.utils import redirect
from forms import ContactForm, LoginForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = 'supersecretsecretkey'


@app.route("/")
def home():
    return render_template('home.html', username=session.get('username'))


@app.route("/Contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        with open('messages.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([form.firstname.data, form.lastname.data, form.region.data,
                             form.email.data, form.message.data])
        return redirect(
            url_for('contact_response', fname=form.firstname.data, lastname=form.lastname.data, region=form.region.data,
                    email=form.email.data, message=form.message.data))
    return render_template('contactus.html', form=form, username=session.get('username'))


@app.route('/contact_response/<fname>/<lastname>/<region>/<email>/<message>', methods=['GET', 'POST'])
def contact_response(fname, lastname, region, email, message):
    return render_template('contact_response.html', fname=fname, lastname=lastname, region=region,
                           email=email, message=message)


@app.route("/FAQ")
def faq():
    with open('data/questions.csv') as f:
        faq_list = list(csv.reader(f))
    return render_template('faq.html', faq_list=faq_list, username=session.get('username'))


@app.route("/AboutUs")
def aboutus():
    return render_template('aboutus.html', username=session.get('username'))


@app.route("/Projects")
def projects():
    with open('data/projects.csv') as f:
        proj_list = list(csv.reader(f))
    return render_template('projects.html', proj_list=proj_list, username=session.get('username'))


@app.route('/Login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if check_password(form.username.data, form.password.data):
            session['username'] = form.username.data
            return redirect(url_for('home'))
        else:
            flash('Incorrect username/password!')
    return render_template('login.html', form=form)


def check_password(username, password):
    with open('data/passwords.csv') as f:
        for user in csv.reader(f):
            if username == user[0] and password == user[1]:
                return True
    return False


@app.route('/Logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
