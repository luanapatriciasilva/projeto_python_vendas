from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Substitua por uma chave segura
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelos do banco de dados
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)

# Criar banco de dados
with app.app_context():
    db.create_all()

# Rotas
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = username
            return redirect(url_for('index'))
        return 'Login inválido'
    return render_template('login.html')

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')

@app.route('/dicionario', methods=['GET', 'POST'])
def dicionario():
    terms = read_terms()
    if request.method == 'POST':
        action = request.form.get('action')
        term = request.form.get('term')
        definition = request.form.get('definition')
        if action == 'add':
            write_term(term, definition)
        elif action == 'update':
            old_term = request.form.get('old_term')
            update_term(old_term, term, definition)
        elif action == 'delete':
            delete_term(term)
        return redirect(url_for('dicionario'))
    return render_template('dicionario.html', terms=terms)

@app.route('/filtrar', methods=['GET'])
def filtrar():
    category = request.args.get('category')
    if category:
        products = Product.query.filter_by(category=category).all()
    else:
        products = Product.query.all()
    return render_template('index.html', products=products)

# Funções para o dicionário de termos
def read_terms():
    if not os.path.exists('termos.txt'):
        with open('termos.txt', 'w') as f:
            f.write('')
    with open('termos.txt', 'r', encoding='utf-8') as f:
        terms = [line.strip().split(':') for line in f if line.strip()]
        return {term[0]: term[1] for term in terms}

def write_term(term, definition):
    with open('termos.txt', 'a', encoding='utf-8') as f:
        f.write(f'{term}:{definition}\n')

def update_term(old_term, new_term, new_definition):
    terms = read_terms()
    if old_term in terms:
        del terms[old_term]
        terms[new_term] = new_definition
        with open('termos.txt', 'w', encoding='utf-8') as f:
            for term, definition in terms.items():
                f.write(f'{term}:{definition}\n')

def delete_term(term):
    terms = read_terms()
    if term in terms:
        del terms[term]
        with open('termos.txt', 'w', encoding='utf-8') as f:
            for term, definition in terms.items():
                f.write(f'{term}:{definition}\n')

if __name__ == '__main__':
    app.run(debug=True)