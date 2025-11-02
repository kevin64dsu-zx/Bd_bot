from flask import Flask, render_template
import db  # nosso arquivo de funções de banco

app = Flask(__name__)

# Rota principal
@app.route("/")
def index():
    mensagens = db.buscar_historico()  # pega todas as mensagens
    return render_template("index.html", mensagens=mensagens)

if __name__ == "__main__":
    db.criar_tabela()  # garante que a tabela exista ao iniciar
    app.run(debug=True)
