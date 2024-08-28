#app.py
from flask import Flask, render_template, request, jsonify
from controllers.football_controller import FootballController
from datetime import date
import requests



app = Flask(__name__)
controller = FootballController()


@app.route('/')
def home():
    fixtures = controller.get_fixtures_by_date(date.today())
    return render_template('home.html', fixtures=fixtures)


@app.route('/fetch_data', methods=['POST'])
def fetch_data():

    date = request.form['date']
    fixtures = controller.get_fixtures_by_date(date)

    if not fixtures:
        api_key = '0f459fdbb59bedebdeed8dcfc3d23cdb'

        SPORT = 'soccer_brazil_campeonato'

        odds_response = requests.get(
            f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds',
            params={
                'api_key': '0f459fdbb59bedebdeed8dcfc3d23cdb',
                'regions': 'us2',
               #'markets': MARKETS,
                'oddsFormat': 'decimal'
            }
        )
        if odds_response.status_code != 200:
            odds_json = odds_response.json()
            print('Number of events:', len(odds_json))
            print(odds_json)
        else:
            return []

        return render_template('home.html', matches=match_info)

@app.route('/generate_data', methods=['POST'])
def generate_data():
    data = request.get_json()
    fixture_id = data['fixture_id']
    # Processar o ID do fixture e gerar as estatísticas
    # Retornar os dados como JSON
    return jsonify({"message": "Estatísticas geradas com sucesso"})


if __name__ == "__main__":
    app.run(debug=False)
