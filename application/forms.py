from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo, ValidationError
from application.tables import User

class InputForm(FlaskForm):

    name = StringField('nome', validators = [DataRequired(), Length(max = 70)], render_kw={"placeholder": "Nos diga seu nome completo", "class": "form-control"})
    email = StringField('email', validators = [DataRequired(), Email(), Length(max = 120)], render_kw={"placeholder": "Insira um email válido", "class": "form-control"})
    password = PasswordField('pass', validators = [DataRequired()], render_kw={"class": "form-control"})
    password_confirm = PasswordField('confirmPass', validators = [DataRequired(), EqualTo('password', message = 'As senhas não batem!')], render_kw={"class": "form-control", "oninput" : "verificaSenha()"})

    debtype = StringField('Tpdivida', validators = [DataRequired(), Length(max = 30)], render_kw={"class": "form-control"})
    income = StringField('salario', validators = [DataRequired(), Length(max = 12)], render_kw={"class": "form-control"})
    savings = StringField('poupanca', validators = [InputRequired(), Length(max = 12)], render_kw={"class": "form-control"})
    interestrate = StringField('juros', validators = [InputRequired(), Length(max = 12)], render_kw={"class": "form-control"})
    savingsyield = StringField('rendimento', validators =[InputRequired(), Length(max = 12)], render_kw={"class": "form-control"})
    debt = StringField('divida', validators = [InputRequired(), Length(max = 12)], render_kw={"class": "form-control"})
    objective = StringField('objetivo', validators = [InputRequired(), Length(max = 12)], render_kw={"palceholder" : "Quanto você deseja acumular?", "class": "form-control"})
    rent = StringField('aluguel', validators = [InputRequired(), Length(max = 12)], render_kw={"class": "form-control"})
    transport = StringField('transporte', validators = [InputRequired(), Length(max = 12)], render_kw={"class": "form-control"})
    food = StringField('alimentacao', validators = [InputRequired(), Length(max = 12)], render_kw={"class": "form-control"})
    bills = StringField('contas', validators = [InputRequired(), Length(max = 12)], render_kw={"class": "form-control", "placeholder" : "Média das contas mensais"})
    shopping = StringField('compras', validators = [InputRequired(), Length(max = 12)], render_kw={"class": "form-control"})
    extra = StringField('outros', validators = [InputRequired(), Length(max = 12)], render_kw={"class": "form-control"})
    submit = SubmitField('Enviar') # , kwargs={"class" : "btn btn-success"}

class LoginForm(FlaskForm):

    email = StringField('email', validators = [DataRequired(), Email(), Length(max = 50)], render_kw={"placeholder": "Seu Email...", "class": "form-control"})
    password = PasswordField('senha', validators = [DataRequired()], render_kw={"placeholder": "Sua senha...", "class": "form-control"})
    submit = SubmitField('Entrar') # , kwargs={"class" : "btn btn-success"}
