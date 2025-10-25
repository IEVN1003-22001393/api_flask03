from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

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