### Pinterest Copycat

Este é um clone do site Pinterest, desenvolvido com Flask no backend e HTML, CSS e JavaScript no frontend.

### Funcionalidades

- Login e registro de usuários.
- Senhas criptografadas para segurança do usuário.
- Cada usuário tem um perfil e pode fazer upload de fotos.
- As informações das fotos são armazenadas no banco de dados, incluindo o caminho da imagem e o ID do usuário que a postou.
- O feed mostra as fotos em ordem decrescente de data de postagem, exibindo as imagens de todos os usuários.
- Clicando em uma foto, você é redirecionado para o perfil do usuário que a postou.
- O design do site é semelhante ao do Pinterest

### Como executar o projeto
- Clone o repositório em sua máquina local
- Instale as dependências necessárias:

pip install -r requirements.txt

- Configure o banco de dados no arquivo config.py
- Execute o comando a seguir para criar as tabelas no banco de dados:

flask db upgrade

- O projeto possue um arquivo chamado "criar_banco.py",
caso queira recriar o seu banco de dados, execute o mesmo.

- Inicie o servidor:

execute o arquivo "main.py"

- Acesse http://localhost:5000 em seu navegador para visualizar o site

### Tecnologias usadas
- Flask
- SQLAlchemy
- Flask-Login
- Flask-Bcrypt
- email_validator
- Flask-wtf

### Como contribuir
- Faça um fork do repositório
- Crie uma branch para sua feature (git checkout -b feature/minha-feature)
- Faça as alterações necessárias
- Faça um commit das suas alterações (git commit -m 'Minha nova feature')
- Faça um push para a branch (git push origin feature/minha-feature)
- Abra um pull request

### Autores
Matheus Alves

### Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE.md para obter mais informações.












