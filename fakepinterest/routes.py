# criar as rotas do nosso site (os links)
from flask import render_template, url_for, redirect
from fakepinterest import app, database, bcrypt
from fakepinterest.models import Usuario, Foto
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import FormLogin, FormCriarConta, FormFoto
from werkzeug.utils import secure_filename
import os

# rota para a página inicial, que contém um formulário de login
@app.route("/", methods=["GET", "POST"])
def homepage():
    # criar uma instância do formulário de login
    form_login = FormLogin()
    if form_login.validate_on_submit():
        # procurar por um usuário com o email fornecido pelo formulário
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        # verificar se a senha fornecida pelo usuário é correta
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            # fazer o login do usuário
            login_user(usuario)
            # redirecionar para a página de perfil do usuário
            return redirect(url_for("perfil", id_usuario=usuario.id))
    # renderizar a página inicial com o formulário de login
    return render_template("homepage.html", form=form_login)

# rota para a página de criação de conta
@app.route("/criarconta", methods=["GET", "POST"])
def criar_conta():
    # criar uma instância do formulário de criação de conta
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        # criar um hash da senha fornecida pelo usuário
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data)
        # criar um novo usuário com as informações fornecidas
        usuario = Usuario(username=form_criarconta.username.data,
                          senha=senha, email=form_criarconta.email.data)
        # adicionar o usuário ao banco de dados
        database.session.add(usuario)
        database.session.commit()
        # fazer o login do usuário
        login_user(usuario, remember=True)
        # redirecionar para a página de perfil do usuário
        return redirect(url_for("perfil", id_usuario=usuario.id))
    # renderizar a página de criação de conta com o formulário
    return render_template("criarconta.html", form=form_criarconta)


@app.route("/perfil/<id_usuario>", methods=["GET", "POST"])
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        # o usuário está vendo o próprio perfil
        form_foto = FormFoto()
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            # salvar o arquivo dentro da pasta certa
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   app.config["UPLOAD_FOLDER"],
                                   nome_seguro)
            arquivo.save(caminho)
            # criar a foto no banco com o item "imagem" sendo o nome do arquivo
            foto = Foto(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(foto)
            database.session.commit()
        # renderiza a página do perfil, com o formulário para adicionar fotos
        return render_template("perfil.html", usuario=current_user, form=form_foto)
    else:
        # usuário está vendo o perfil de outro usuário
        usuario = Usuario.query.get(int(id_usuario))
        # renderiza a página do perfil, sem o formulário de fotos
        return render_template("perfil.html", usuario=usuario, form=None)


@app.route("/logout")
@login_required
def logout():
    # faz logout do usuário atual
    logout_user()
    # redireciona para a página inicial
    return redirect(url_for("homepage"))


@app.route("/feed")
@login_required
def feed():
    # pega todas as fotos no banco de dados, ordenadas por data de criação
    fotos = Foto.query.order_by(Foto.data_criacao.desc()).all()
    # renderiza a página de feed com todas as fotos
    return render_template("feed.html", fotos=fotos)

