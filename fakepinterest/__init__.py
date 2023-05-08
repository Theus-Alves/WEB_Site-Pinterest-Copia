from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

# Cria uma instância do objeto Flask
app = Flask(__name__)

# Configuração do banco de dados usando SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
database = SQLAlchemy(app)

# Configuração da chave secreta para proteção de sessões
app.config["SECRET_KEY"] = "a3190c71717b80582c2b580d8bc02528"

# Configuração do diretório para upload de arquivos
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"



# Instância do Bcrypt para criptografar senhas
bcrypt = Bcrypt(app)

# Instância do LoginManager para gerenciar sessões de usuários
login_manager = LoginManager(app)

# Define a página de login
login_manager.login_view = "homepage"

# Importa as rotas da aplicação
from fakepinterest import routes


