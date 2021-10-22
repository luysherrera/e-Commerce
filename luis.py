from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import bcrypt

app = Flask(__name__)
app.secret_key="inventarioMazda"

#config Database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inventario_mazda'
mysqldb = MySQL(app)

semilla = bcrypt.gensalt()

@app.route('/')
def main():
    if 'nombre' in session:
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html')


@app.route('/signin', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if 'nombre' in session:
            cur = mysqldb.connection.cursor()
            sql = "SELECT u.codigo, u.nombre, u.apellidos, u.email, u.rol FROM usuarios u"
            cur.execute(sql)
            data = cur.fetchall()
            return render_template('signin.html', datas = data)
    else:
        return "render_template('signin.html')"
        

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        if 'nombre' in session:
            return render_template('index.html')
        else:
            return render_template('login.html')
    else:
        nombre1 = request.form['name1']
        nombre2 = request.form['name2']
        name = nombre1 + ' ' + nombre2
        apellido1 = request.form['lastName1']
        apellido2 = request.form['lastName2']
        lastname = apellido1 + ' ' + apellido2
        email = request.form['email']
        rol = 'FinalUser'
        password = request.form['passs']
        password_encode = password.encode("utf-8")
        password_encrypted = bcrypt.hashpw(password_encode, semilla)

        cur = mysqldb.connection.cursor()
        cur.execute('INSERT INTO usuarios (nombre, apellidos, email, rol, contraseña, created) VALUES (%s, %s, %s, %s, %s, %s)', (name.upper(), lastname.upper(), email.upper(), rol.upper(), password_encrypted, 'NOW()'))
        mysqldb.connection.commit()

#error sin resolver
        if session['nombre'] != None:
            return render_template('dashboard.html')
        else:
            session['nombre'] = name.upper()
            session['apellidos'] = lastname.upper()
            session['email'] = email.upper()
            session['rol'] = rol.upper()

            flash('Usuario Agregado satisfactoriamente')
            return render_template('productos.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
            if 'nombre' in session:
                return render_template('login.html')
            else:
                return render_template('login.html')
    else:
        #Obtener datos de ususario de base de datos
        usuario = request.form['email']
        contraseña = request.form['contraseña']
        password_encrypted = contraseña.encode('utf8')
        cur = mysqldb.connection.cursor()
        sql = "SELECT * FROM usuarios WHERE email = %s"
        cur.execute(sql,[usuario])


        usuario = cur.fetchone()
        cur.close()
        if usuario != None:
            password_encrypted_encode = usuario[5].encode()
            if bcrypt.checkpw(password_encrypted, password_encrypted_encode):
                session['nombre'] = usuario[1]
                session['apellidos'] = usuario[2]
                session['email'] = usuario[3]
                session['rol'] = usuario[4]
                #return render_template('productos.html')
                return  redirect(url_for('dashboard'))
                
                

            else:
                flash("Congtraseña incorrecta", "alert-warning")
                return render_template('login.html')
        else:
            flash("El usuario no existe")
            print("El usuario no existe")
            return redirect(url_for('login'))
            


@app.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'nombre' in session:
        return render_template('dashboard.html')
    else:
        return render_template('login.html')

    

@app.route('/admin', methods=['GET'])
def admin():
    #Si ya inicio session y tipo de usuario es admin o superAdmin -> dashboard administrativo
    #sino si inicio session y tipo de usuario es usuario final -> dashboard
    #sino index
    if usuario != '':
        if rol == 'finalUser':
            return "render_template('dashboard')"
        else:
            return "render_template('admin.html')"
    else:
        return index()

@app.route('/editusuario', methods=['GET','POST'])
def editusuario():
    if usuario != '':
        if rol == 'finalUser':
            return "render_template('dashboard.html')"
        else:
            return "render_template('editarusuario.html')"
    else:
        return index()


@app.route('/eliminarusuario', methods=['GET','POST'])
def eliminarusuario():
    if usuario != '':
        if rol == 'finalUser':
            return "render_template('dashboard.html')"
        else:
            return "render_template('eliminarusuario.html')"
    else:
        return index()

@app.route('/verusuarios', methods=['GET'])
def verusuarios():
    if usuario != '':
        if rol == 'finalUser':
            return "render_template('dashboard.html')"
        else:
            return "render_template('verusuarios.html')"
    else:
        return index()

@app.route('/editarrol', methods=['GET','POST'])
def edititarrol():
    if usuario != '':
        if rol == 'superAdmin':
            return "render_template('editarrol.html')"
        else:
            return index()
    else:
        return index()

@app.route('/addProducto', methods=['GET','POST'])
def addProducto():
    if usuario != '':
        if rol == 'finalUser':
            flash('No tiene permisos de añadir productos')
            return "render_template('dashboard')"
        else:
            return "render_template('addproductos.html')"
    else:
        return index()


@app.route('/editProducto', methods=['GET','POST'])
def editProducto():
    if usuario != '':
        return "render_template('editarProductos.html')"
    else:
        return index()


@app.route('/eliminarProducto', methods=['GET','POST'])
def eliminarProducto():
    if usuario != '':
        if rol == 'finalUser':
            flash('No tiene permisos de eliminar productos')
            return "render_template('dashboard')"
        else:
            return "render_template('eliminarproducto.html')"
    else:
        return index()


@app.route('/buscarproducto', methods=['GET','POST'])
def buscar_producto():
    if usuario != '':
        return "render_template('buscarproducto.html')"
    else:
        return index()

@app.route('/listarproductos', methods=['GET'])
def listar_productos():
    if usuario != '':
        return render_template('inventory.html', data = usuario)
    else:
        return index()

@app.route('/productosdisponibles')
def productDisponibles():
    usuario = 'as'
    if usuario != '':
        cur = mysqldb.connection.cursor()
        sql = "SELECT * FROM productos WHERE cant_disp_bodega > 0"
        cur.execute(sql)
        data = cur.fetchall()
        return render_template('productos.html', datas = data )
    else:
        return index()

if __name__ == '__main__':
    app.run(port=3000, debug=True)