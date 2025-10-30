from wtforms import Form 
from wtforms import StringField, FloatField, EmailField, PasswordField, IntegerField, RadioField
from wtforms import validators

class UserForm(Form):
    matricula = IntegerField('Matricula', [validators.DataRequired(message="La matricula es obligatoria")])
    nombre = StringField('Nombre', [validators.DataRequired(message="El campo es requerido")])
    apellido = StringField('Apellido', [validators.DataRequired(message="El campo es requerido")])
    correo = EmailField('Correo', [validators.DataRequired(message="Ingrese Correo Valido")])



class FigForm(Form):

    figura = RadioField('Selecciona la figura', choices=[('triangulo', 'Triangulo'), ('rectangulo', 'Rectangulo'), ('circulo', 'Circulo'), ('pentagono', 'Pentagono')], validators=[validators.DataRequired(message="Seleccione una figura.")])
    val1 = FloatField('Base / Radio / Lado', [validators.DataRequired(message="El campo es requerido.")])
    val2 = FloatField('Altura')
   