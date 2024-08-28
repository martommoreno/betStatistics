# models/football_model.py
import mysql.connector
from config import db_config

class FootballModel:
    def __init__(self):
        self.connection = mysql.connector.connect(**db_config)
        self.cursor = self.connection.cursor()

    def get_fixtures(self):
        query = "SELECT * FROM fixtures WHERE date = CURRENT_DATE"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def save_fixture(self, fixture):
        query = "INSERT INTO fixtures (team_home, team_away, date, ) VALUES (%s, %s, %s)"
        self.cursor.execute(query, fixture)
        self.connection.commit()

    def get_fixtures_by_date(self, date):
        query = "SELECT * FROM fixtures WHERE date = %s"
        self.cursor.execute(query, (date,))
        return self.cursor.fetchall()
