from wtforms import Form 
from wtforms import StringField, FloatField, EmailField, PasswordField, IntegerField, RadioField
from wtforms import validators
import datetime

class UserForm(Form):
    matricula = IntegerField('Matricula', [validators.DataRequired(message="La matricula es obligatoria")])
    nombre = StringField('Nombre', [validators.DataRequired(message="El campo es requerido")])
    apellido = StringField('Apellido', [validators.DataRequired(message="El campo es requerido")])
    correo = EmailField('Correo', [validators.DataRequired(message="Ingrese Correo Valido")])



class FigForm(Form):

    figura = RadioField('Selecciona la figura', choices=[('triangulo', 'Triangulo'), ('rectangulo', 'Rectangulo'), ('circulo', 'Circulo'), ('pentagono', 'Pentagono')], validators=[validators.DataRequired(message="Seleccione una figura.")])
    val1 = FloatField('Base / Radio / Lado', [validators.DataRequired(message="El campo es requerido.")])
    val2 = FloatField('Altura')

class PizzasForm(Form):
    Nombre = StringField("Nombre",
            [validators.DataRequired(message="El nombre es obligatorio")])
    Direccion = StringField("Dirección",
            [validators.DataRequired(message="La dirección es obligatoria")])
    Telefono = StringField("Teléfono",
            [validators.DataRequired(message="El teléfono es obligatorio")])
 
    Fecha = StringField("Fecha",
            default=datetime.date.today().strftime('%Y-%m-%d'))
 
    NumPizzas = IntegerField("Numero de Pizzas",
            [validators.Optional(), validators.NumberRange(min=1, message="Debe ser al menos 1")],
            default=1)
   