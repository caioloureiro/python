from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def buscar_dados():
    # Configure com seus dados do MySQL
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="caio1234",
        database="digi8353_catalogo"
    )
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM fastdial")
    dados = cursor.fetchall()
    conexao.close()
    return dados

@app.route('/')
def home():
    lista_dados = buscar_dados()
    return render_template('index.html', itens=lista_dados)

if __name__ == '__main__':
    app.run(debug=True)