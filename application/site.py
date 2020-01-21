import os
from flask import Flask, render_template, redirect, request, url_for, g, session
from application import app, db, pwcrypt
from application.forms import InputForm, LoginForm
from application.tables import User
from flask_login import login_user, current_user, logout_user, login_required
import matplotlib.pyplot as plt
from io import BytesIO

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

# application pages
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def homepage():

        if not session.new:
                redirect(url_for('chart'))

        form = InputForm()
        entry = LoginForm()

        if request.method == 'POST' and form.is_submitted():
                try:
                        name = request.form.get('nome')
                        email = request.form.get('email')
                        password = request.form.get('pass')
                        vpass = request.form.get('confirmPass')
                        income = request.form.get('salario')
                        savings = request.form.get('poupanca')
                        debt = request.form.get('divida')
                        dtype = request.form.get('tpDivida')
                        interestrate = request.form.get('juros')
                        obj = request.form.get('objetivo')
                        rent = request.form.get('aluguel')
                        transport = request.form.get('transporte')
                        food = request.form.get('alimentacao')
                        bills = request.form.get('contas')
                        shopping = request.form.get('compras')
                        extra = request.form.get('outros')

                        if password != vpass:
                                raise ValueError("Os campos senha e confirmação de senha não batem.")

                        hashed_password = pwcrypt.generate_password_hash(password).decode('utf-8')

                        newuser = User(username=name,email=email,password=hashed_password,income=income,savings=savings,debt=debt,debttype=dtype,interestrate=interestrate,objective=obj,rent=rent,transport=transport,food=food,bills=bills,shopping=shopping,extra=extra)
                        
                        db.session.add(newuser)
                        db.session.commit()
                        redirect(url_for('chart'))

                except Exception:
                        pass

                finally:
                        return render_template("homepage.html", form = form, entry = entry)

        elif request.method == 'POST' and entry.is_submitted():
                try:
                        uname = request.entry.get('nome')
                        pwcheck = request.entry.get('pass')
                        user = User.query.filter_by(email=form.email.data).first()
                        dbpass = User.query.filter_by(username=uname).password
        
                        if user and pwcrypt.check_password_hash(dbpass, pwcheck):
                                login_user(user)
                                redirect(url_for('handle_form'))
                        else: return render_template("homepage.html", form = form, entry = entry)
                                
                except Exception:
                        pass
                        
        return render_template("homepage.html", form = form, entry = entry)

@login_required
@app.route('/chart', methods=['GET', 'POST'])
def chart():
        return render_template('userpage.html')

@app.route("/handle_form", methods=['POST'])
def handle_form():
        if request.method == "POST":
                fields = [k for k in request.form]
                values = [request.form[k] for k in request.form]
                data = dict(zip(fields, values))

        salario = float(data['income'])
        poupanca = float(data['savings'])
        # taxa = data['taxa']
        taxa = float(0.05)
        divida = float(data['debt'])
        # juros = data['juros']
        juros =  float(0.14)
        objetivo = float(data['objective'])
        aluguel = float(data['rent'])
        transporte = float(data['transport'])
        alimentacao = float(data['food'])
        contas = float(data['bills'])
        compras = float(data['shopping'])
        outros = float(data['extra'])

        i = 1
        xaxis = list()
        yaxis = list()
        xaxis.append(0)
        aux = float(poupanca - divida)
        yaxis.append(aux)

        totalGastos = aluguel + transporte + alimentacao + contas + compras + outros

        while i < 36:

                if (poupanca - divida > objetivo):
                        break;

                xaxis.append(i)

                variacao = salario - totalGastos + poupanca * taxa - divida * juros
                if (variacao < divida):
                        divida = divida - variacao
                elif (variacao == divida):
                        divida = 0
                elif (variacao > divida):
                        variacao = variacao - divida
                        divida = 0
                        poupanca = poupanca + variacao
                aux = (poupanca - divida)
                yaxis.append(aux)
                i = i + 1

        plt.plot(xaxis, yaxis)
        plt.xlabel('Meses')
        plt.ylabel('R$')
        plt.title('Seu Dinheiro: ')
        # plt.show()

        img = BytesIO()
        plt.savefig(img)
        img.seek(0)
        plt.savefig('1.png')

        # output_file('donut.html')
        # prepare the data
        pie_input = [alimentacao, aluguel, compras, contas, outros, transporte]
        sectors = ['Alimentacao', 'Aluguel', 'Compras', 'Contas', 'Extras', 'Transporte']
        plt.pie(pie_input, labels = sectors)
        plt.savefig('2.png')

        return render_template('userpage.html', methods=['GET', 'POST'])
