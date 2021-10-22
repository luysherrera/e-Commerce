from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def iniciarSesion():
    return render_template('login.html')
@app.route('/Dashboard')
def dashboard():
    return render_template('dashboard.html')