from fakepinterest import app, database
from fakepinterest.models import Usuario, Foto

try:
    with app.app_context():
        database.create_all()  
except:
    print("Se está vendo essa mensagem, seu banco ja foi criado ou houve um problema, verifique!")