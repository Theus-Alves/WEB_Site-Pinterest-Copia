# este codigo cria seu banco de dados 'comunidade.db' na pasta instance
# apenas para caso queira apagar o banco de dados atual e recriar

from fakepinterest import app

if __name__=="__main__":
    app.run(debug=True)