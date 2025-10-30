from flask import Flask, render_template, request
import forms
import math

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

@app.route("/Alumnos", methods=['GET', 'POST'])
def alumnos():
    mat=0
    nom="" 
    ape=""
    em=""
    alumnos_clase=forms.UserForm(request.form)
    if request.method=='POST' and alumnos_clase.validate():
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        ape=alumnos_clase.apellido.data
        em=alumnos_clase.correo.data
    return render_template('alumnos.html', form=alumnos_clase, mat=mat, nom=nom, ape=ape, em=em)

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