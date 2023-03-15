from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        with open('users.txt', 'r') as f:
            if email in f.read():
                return redirect(url_for('login'))

        with open('users.txt', 'a') as f:
            f.write(f"{email}:{password}\n")

        return redirect(url_for('login'))

    return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        with open('users.txt', 'r') as f:
            for line in f:
                line_email, line_password = line.strip().split(':')
                if line_email == email and line_password == password:
                    return "You are logged in!"

            return "Wrong email or password"

    return render_template('login.html')
