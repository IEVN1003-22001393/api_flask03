from flask import Flask, render_template, request
from flask import make_response, jsonify
import json
import forms
import math

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

@app.route('/pizza', methods=['GET','POST'])
def pizza():
    mostrarVen = False
# ---------------------------------------- Cargado del formulario y cookies
    form = forms.PizzasForm(request.form)
    pedido_actual_str = request.cookies.get('pedido_actual', '[]')
    pedido_actual = json.loads(pedido_actual_str)
   
    ventas_str = request.cookies.get('ventas_dia', '[]')
    ventas = json.loads(ventas_str)
   
    ventasAgrupadas = {}
    total_dia = 0
    for venta in ventas:
        nombre = venta.get('nombre')
        total = venta.get('total')
        total_dia += total
        ventasAgrupadas[nombre] = ventasAgrupadas.get(nombre, 0) + total
   
# ---------------------------------------- Formulario
    if request.method == 'POST':
     
        action = request.form.get("action")
        if action == 'agregar':
            precios_tamanio = {'chica': 40, 'mediana': 80, 'grande': 120}
           
            tamanio = request.form.get('Tamanio')
            ingredientesLista = request.form.getlist('Ingredientes')
            num_pizzas = form.NumPizzas.data
           
            if tamanio and num_pizzas:
                costTmnio = precios_tamanio.get(tamanio)
                costIngre = len(ingredientesLista) * 10
                subtotal = (costTmnio + costIngre) * num_pizzas
                pizzaOrdenada = {"tamanio": tamanio, "ingredientes": ingredientesLista, "num_pizzas": num_pizzas, "subtotal": subtotal}
                pedido_actual.append(pizzaOrdenada)
        elif action == 'terminar':
            total_pedido = 0
            for item in pedido_actual:
                total_pedido += item.get('subtotal')
            newVenta = {"nombre": form.Nombre.data, "direccion": form.Direccion.data, "telefono": form.Telefono.data, "fecha": form.Fecha.data, "total": total_pedido}
            ventas.append(newVenta)
            ventasAgrupadas = {}
            total_dia = 0
            for venta in ventas:
                nombre = venta.get('nombre')
                total = venta.get('total')
                total_dia += total
                ventasAgrupadas[nombre] = ventasAgrupadas.get(nombre, 0) + total
           
            pedido_actual = []
            form = forms.PizzasForm()
        elif action == 'quitar_ultimo':
            if pedido_actual:
                pedido_actual.pop()
 
        elif action == 'mostrarVen':
            mostrarVen = True
            
        elif action == 'borrarVen':
            ventas = []
            ventasAgrupadas = {}
            total_dia = 0
            mostrarVen = False
   
    response = make_response(render_template('pizza.html', form=form, pedido=pedido_actual, ventas_agrupadas=ventasAgrupadas, total_dia=total_dia, mostrarVen=mostrarVen))
   
    response.set_cookie('pedido_actual', json.dumps(pedido_actual))
    response.set_cookie('ventas_dia', json.dumps(ventas))
 
    return response

@app.route("/Alumnos", methods=['GET', 'POST'])
def alumnos():
    mat=0
    nom="" 
    ape=""
    em=""
    estudiantes=[]
    datos={}

    alumnos_clase=forms.UserForm(request.form)
    if request.method=='POST' and alumnos_clase.validate():
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        ape=alumnos_clase.apellido.data
        em=alumnos_clase.correo.data
        datos={"matricula":mat, "nombre":nom, "apellido":ape, "correo":em}

        datos_str=request.cookies.get('estudiante')
        if not datos_str:
            return"No hay cookies"
        tem=json.loads(datos_str)
        estudiantes=tem
        estudiantes=json.loads(datos_str)
        print(type(estudiantes))
        estudiantes.append(datos)
 
    response=make_response(render_template('alumnos.html', form=alumnos_clase,mat=mat,nom=nom,ape=ape,em=em))
   
    response.set_cookie('estudiante', json.dumps(estudiantes))
    return response
 

@app.route("/get_cookie")
def get_cookie():
    datos_str=request.cookies.get('estudiante')
    if not datos_str:
        return"No hay cookies"
    datos=json.loads(datos_str)
    
    return jsonify(datos)



@app.route('/figuras', methods=['GET', 'POST'])
def figuras():
    area = 0.0 

    figuras_clase = forms.FigForm(request.form)
    
    if request.method == 'POST' and figuras_clase.validate():
        figura = figuras_clase.figura.data
        val1 = figuras_clase.val1.data
        val2 = figuras_clase.val2.data 

        if figura == 'triangulo':
            area = (val1 * val2) / 2
        
        elif figura == 'rectangulo':
            area = val1 * val2

        elif figura == 'circulo':
            area = math.pi * (val1 ** 2)
        
        elif figura == 'pentagono':

            apotema = val1 / (2 * math.tan(math.radians(36)))
            area = (5/2) * val1 * apotema
    
    return render_template('figuras.html', area=area, form=figuras_clase)

@app.route('/index')
def index():

    titulo="IEVN1003 - PWA"
    listado=["Opera 1", "Opera2 ","Opera 3", "Opera 4"]
    return render_template('index.html', titulo=titulo, listado=listado)

@app.route('/operas', methods=['GET', 'POST'])
def operas():

    if request.method=='POST':
        x1=request.form.get('n1')
        x2=request.form.get('n2')
        resultado=x1+x2
        return render_template('operas.html', resultado=resultado)

    return render_template('operas.html')

@app.route('/distancia')
def distancia():
    return render_template('distancia.html')


@app.route('/about')
def about():
    return "<h1>This is the about page <h1/>"

@app.route("/user/<string:user>")
def use(user):
    return "Hola" + user 

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "ID {} nombre: {}".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>")
def func(n1,n2):
    return "la suma: {}".format(n1+n2)

@app.route("/prueba")
def prueba():
    return """
    <h1>Prueba de HTML</h1>
    <p>Esto es una prueba</p>
    <ul>
        <li>Elemento 1</li>
        <li>Elemento 2</li>
        <li>Elemento 3</li>
    </ul>
    """

if __name__ == '__main__':
    app.run(debug=True)