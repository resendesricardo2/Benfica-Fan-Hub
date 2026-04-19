from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
from cartaosocio import criar_socio_automatico
from cartaosocio import consultar_socio_pelo_numero
import enviarform

load_dotenv()

app = Flask(__name__)
CORS(app) 

TOKEN = os.getenv("TOKEN_API")
API_URL = os.getenv("URL_API")
API_JOGOS = os.getenv("URL_JOGOS")
API_EQUIPAS = os.getenv("URL_EQUIPAS")

BENFICA_ID = 1903
HEADERS = {'X-Auth-Token': TOKEN}

@app.route('/api/classificacao', methods=['GET'])
def get_classificacao():
    headers = {'X-Auth-Token': TOKEN}
    try:
        response = requests.get(API_URL, headers=headers)
        data = response.json()
        tabela_original = data['standings'][0]['table']
        lista_limpa = []

        for item in tabela_original:
            lista_limpa.append({
                "pos": item['position'],
                "nome": item['team']['shortName'],
                "logo": item['team']['crest'],
                "jogos": item['playedGames'],
                "vitorias": item['won'],         
                "empates": item['draw'],         
                "derrotas": item['lost'],        
                "gm": item['goalsFor'],          
                "gs": item['goalsAgainst'],      
                "diff": item['goalDifference'],
                "pontos": item['points']
            })
        return jsonify(lista_limpa)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/api/socio/aderir', methods=['POST'])
def aderir_socio():
    dados_do_utilizador = request.json 
    resultado = criar_socio_automatico(dados_do_utilizador)

    if resultado.get("status") == "sucesso":
        return jsonify({
            "sucesso": True, 
            "dados_cartao": resultado
        }), 201
    else:
        return jsonify({
            "sucesso": False, 
            "mensagem": "Erro ao processar adesão"
        }), 400

@app.route('/api/socio/login', methods=['POST'])
def login_socio():
    dados = request.json
    numero_digitado = dados.get('numero_socio')

    if not numero_digitado:
        return jsonify({"status": "erro", "mensagem": "Número de sócio é obrigatório"}), 400
    
    resultado = consultar_socio_pelo_numero(numero_digitado)
    if resultado['status'] == "sucesso":
        return jsonify(resultado), 200
    
    else:
        return jsonify(resultado), 404

@app.route('/api/jogos', methods=['GET'])
def get_jogos():
    headers = {'X-Auth-Token': TOKEN}
    try:
        response = requests.get(API_JOGOS, headers=headers)
        data = response.json()
        
        jogos_originais = data.get('matches', [])
        lista_jogos = []

        for jogo in jogos_originais:
            lista_jogos.append({
                "id": jogo['id'],
                "utcDate": jogo['utcDate'],
                "status": jogo['status'],
                "matchday": jogo['matchday'],
                "homeTeam": {
                    "id": jogo['homeTeam']['id'],
                    "nome": jogo['homeTeam']['shortName'],
                    "logo": jogo['homeTeam']['crest'],
                    "tla": jogo['homeTeam']['tla']
                },
                "awayTeam": {
                    "id": jogo['awayTeam']['id'],
                    "nome": jogo['awayTeam']['shortName'],
                    "logo": jogo['awayTeam']['crest'],
                    "tla": jogo['awayTeam']['tla']
                },
                "score": {
                    "home": jogo['score']['fullTime']['home'],
                    "away": jogo['score']['fullTime']['away']
                },
                "competition": jogo['competition']['name']
            })
            
        return jsonify(lista_jogos)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/api/plantel-match', methods=['GET'])
def get_plantel_match():
    headers = {'X-Auth-Token': TOKEN}
    try:
        res_jogos = requests.get(API_JOGOS, headers=headers)
        jogos = res_jogos.json().get('matches', [])
        
        proximo = next((j for j in jogos if j['status'] in ['SCHEDULED', 'TIMED', 'LIVE', 'IN_PLAY'] 
                       and (j['homeTeam']['id'] == 1903 or j['awayTeam']['id'] == 1903)), None)

        if not proximo:
            return jsonify({"erro": "Sem jogos agendados"}), 404

        ids = [proximo['homeTeam']['id'], proximo['awayTeam']['id']]
        squads_final = {}

        for t_id in ids:
            res_t = requests.get(f"{API_EQUIPAS}{t_id}", headers=headers)
            t_data = res_t.json()
            
            nome = t_data.get('shortName')
            squad_raw = t_data.get('squad', [])
            coach_data = t_data.get('coach', {})

            lista_pessoas = []
            for p in squad_raw:
                lista_pessoas.append({
                    "nome": p['name'],
                    "posicao": p.get('position'),
                    "nacionalidade": p.get('nationality'),
                    "role": 'PLAYER'
                })
            
            if coach_data.get('name'):
                lista_pessoas.append({
                    "nome": coach_data['name'],
                    "posicao": "Coach",
                    "role": "COACH"
                })

            squads_final[nome] = lista_pessoas

        return jsonify({
            "match": f"{proximo['homeTeam']['shortName']} vs {proximo['awayTeam']['shortName']}",
            "squads": squads_final
        })
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route("/enviar-formulario", methods=["POST"])
def enviar_formulario():
    nome = request.json.get("nome")
    email = request.json.get("email")
    mensagem = request.json.get("mensagem")
    if request.method == "POST":
        enviarform.enviar_email(nome, email, mensagem)
        return jsonify({"status": "ok"})
    return jsonify({"status": "erro", "erro": str()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)