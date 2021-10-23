from flask import Flask, render_template
app= Flask(__name__)

@app.route('/login', methods=['GET','POST'] )
def iniciarSesion():
    return render_template('login.html')

@app.route('/Registro', methods=['GET','POST'])
def Registro():
    return render_template('Register.html')

@app.route('/principal', methods=['GET', 'POST'])
def principal():
    return render_template('PaginaPrincipal.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/ListaDeseos', methods=['GET', 'POST'])
def ListaDeseos():
    return render_template('ListaDeDeseos.html')

@app.route('/EliminarProductos',methods=['GET', 'POST'])
def EliminarProductos():
    return render_template('eliminarProducto.html')

@app.route('/Comentarios', methods=['GET', 'POST'])
def Comentarios():
    return render_template('Comentarios.html')