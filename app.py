from flask import Flask, render_template, session, redirect, url_for, request
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'clave_secreta'
app.permanent_session_lifetime = timedelta(minutes=10)

# Catálogo de productos
productos = [
    {'id': 1, 'nombre': 'Mouse Gamer', 'precio': 59.90, 'imagen': 'producto1.jpg'},
    {'id': 2, 'nombre': 'Teclado Mecánico', 'precio': 99.90, 'imagen': 'producto2.jpg'},
    {'id': 3, 'nombre': 'Audífonos Bluetooth', 'precio': 149.90, 'imagen': 'producto3.jpg'}
]

@app.route('/')
def catalogo():
    return render_template('catalogo.html', productos=productos)

@app.route('/agregar/<int:id>')
def agregar(id):
    producto = next((p for p in productos if p['id'] == id), None)
    if producto:
        if 'carrito' not in session:
            session['carrito'] = []
        carrito = session['carrito']
        carrito.append(producto)
        session['carrito'] = carrito
    return redirect(url_for('catalogo'))

@app.route('/carrito')
def ver_carrito():
    carrito = session.get('carrito', [])
    total = sum(p['precio'] for p in carrito)
    return render_template('carrito.html', carrito=carrito, total=total)

if __name__ == '__main__':
    app.run(debug=True)
