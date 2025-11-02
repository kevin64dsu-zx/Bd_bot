from flask import Flask, render_template

app = Flask(__name__)

# Simulação de dados que o banco traria
mensagens_teste = [
    (1, "João", "Oi, tudo bem?", "Usuario", "2025-11-01 09:00"),
    (2, "Bot", "Tudo ótimo! Como posso ajudar?", "Bot", "2025-11-01 09:01"),
    (3, "Maria", "Quero saber sobre o produto X", "Usuario", "2025-11-01 09:02"),
]

@app.route("/")
def index():
    return render_template("index.html", mensagens=mensagens_teste)

if __name__ == "__main__":
    app.run(debug=True)
