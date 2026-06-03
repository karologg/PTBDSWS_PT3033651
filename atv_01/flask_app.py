#semana 2

from flask import Flask, request, url_for

app = Flask(__name__)

#home
@app.route("/")
def home():
    return f"""
    <h1>Avaliação contínua: Aula 030</h1>
    <ul>
        <li><a href="{url_for('home')}">Home</a></li>
        <li><a href="{url_for('identificacao', nome='Karol Gotto', prontuario='PT3033651', instituicao='IFSP')}">Identificação</a></li>
        <li><a href="{url_for('contexto_requisicao')}">Contexto de requisição</a></li>
    </ul>
    """

#identificação
@app.route("/user/<nome>/<prontuario>/<instituicao>")
def identificacao(nome, prontuario, instituicao):
    return f"""
    <h1> Avaliação contínua: Aula 030</h1>

    <h2><b>Aluna:</b> {nome}</h2>
    <h2><b>Prontuário:</b> {prontuario}</h2>
    <h2><b>Instituição:</b> {instituicao}</h2>

    <p><a href="{url_for('home')}">Voltar</a></p>
    """

#contexto requisição
@app.route("/contextorequisicao")
def contexto_requisicao():
    user_agent = request.headers.get("User-Agent", "desconhecida")
    remote_ip = request.remote_addr or "desconhecido"
    host = request.host

    return f"""
    <h1> Avaliaçao contínua: Aula 030</h1>

    <h2><b>Seu navegador é:</b> {user_agent}</h2>
    <h2><b>O IP do computador remoto é:</b> {remote_ip}</h2>
    <h2><b>O host da aplicação é:</b> {host}</h2>

    <p><a href="{url_for('home')}">Voltar</a></p>
    """

    if __name__ == "__main__":
        app.run(debug=True)
