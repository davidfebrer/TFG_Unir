
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, DateField, ValidationError
from wtforms.validators import DataRequired

class Form (FlaskForm):
    tipos_alojamiento = SelectField('Tipo de Alojamiento', choices=[('hotel', 'Hotel'), ('apartamento', 'Apartamento'), ('casa', 'Casa')], validators=[DataRequired()])
    fecha1 = DateField('Inicio', validators=[DataRequired()], id="fecha1")
    fecha2 = DateField('Final', validators=[DataRequired()], id="fecha2")
    personas = SelectField('Personas', choices=[('1', '1 Adulto'), ('2', '2 Adultos'), ('1_1', '1 Adulto, 1 Niño'), ('2_1', '2 Adultos, 1 Niño'), ('2_2', '2 Adultos, 2 Niños')], validators=[DataRequired()])
    submit = SubmitField('Buscar')  