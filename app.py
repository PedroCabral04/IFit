from flask import Flask, jsonify, render_template, request, redirect, url_for, flash, session
from flask_mail import Mail, Message
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from flask import flash

app = Flask(__name__)
app.secret_key = 'f3cfe9ed8fae309f02079dbf'

# Configuração do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'pedroscabral04@gmail.com'
app.config['MAIL_PASSWORD'] = 'dbll dqhy fqys unoe'
mail = Mail(app)

# Configuração do banco de dados
DATABASE_URL = "dbname='IFit' user='postgres' password='123' host='localhost' port='5432'"

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Tentativa de login para o usuário: {username}")  # Log

        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
                    user = cur.fetchone()
                    print(f"Usuário encontrado: {user is not None}")  # Log

            if user and check_password_hash(user[3], password):
                print("Senha válida, login bem-sucedido")  # Log
                session['username'] = username
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('index'))
            else:
                print("Usuário não encontrado ou senha inválida")  # Log
                flash('Usuário ou senha incorretos!', 'danger')
        except Exception as e:
            print(f"Erro durante o login: {str(e)}")  # Log
            flash('Ocorreu um erro durante o login. Por favor, tente novamente.', 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                # Verifica se o email já existe
                cur.execute("SELECT * FROM users WHERE email = %s", (email,))
                if cur.fetchone() is not None:
                    flash('Este email já está cadastrado. Por favor, use outro email.', 'danger')
                    return redirect(url_for('register'))
                else:
                    # Se o email não existe, procede com o cadastro
                    hashed_password = generate_password_hash(password)
                    try:
                        cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                                    (username, email, hashed_password))
                        conn.commit()
                        flash('Cadastro realizado com sucesso! Agora você pode fazer login.', 'success')
                        return redirect(url_for('login'))
                    except Exception as e:
                        conn.rollback()
                        flash(f'Ocorreu um erro: {str(e)}', 'danger')
                        return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/planos')
def planos():
    return render_template('planos.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(
            subject=f"Novo contato de {name}",
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']],
            body=f"Nome: {name}\nEmail: {email}\nMensagem: {message}"
        )
        
        try:
            mail.send(msg)
            flash('Mensagem enviada com sucesso!', 'success')
        except Exception as e:
            flash(f'Ocorreu um erro ao enviar a mensagem: {str(e)}', 'danger')

        return redirect(url_for('contato'))

    return render_template('contato.html')


@app.route('/check_email', methods=['POST'])
def check_email():
    email = request.form['email']
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cur.fetchone()
    return jsonify({'exists': user is not None})

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Você foi desconectado com sucesso.', 'success')
    return redirect(url_for('index'))

@app.route('/pagamento/<plano>')
def pagamento(plano):
    if 'username' not in session:
        flash('Faça login para contratar um plano.', 'warning')
        return redirect(url_for('login'))
    return render_template('pagamento.html', plano=plano)

@app.route('/processar_pagamento', methods=['POST'])
def processar_pagamento():
    if 'username' not in session:
        flash('Faça login para contratar um plano.', 'warning')
        return redirect(url_for('login'))

    flash('Pagamento processado com sucesso!', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)