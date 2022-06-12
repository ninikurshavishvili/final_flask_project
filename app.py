from flask import Flask, redirect,render_template, url_for, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "ninidfsdjfsjd"
app.permanent_session_lifetime = timedelta(minutes=3)


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        user = request.form['nameuser']
        session['client'] = user
        return redirect(url_for('lastname'))
    elif request.method == "POST":
        lastname = request.form['lastname']
        return redirect(url_for())
    elif request.method == "POST":
        password = request.form['password']
    else:
        if 'client' in session:
            return render_template('base.html')


@app.route("/home")
def home():
    if 'client' in session:
        username = session['client']
        return {username}
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
