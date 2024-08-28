# controllers/football_controller.py
from models.football_model import FootballModel

class FootballController:
    def __init__(self):
        self.model = FootballModel()

    def get_fixtures(self):
        return self.model.get_fixtures()

    def save_fixture(self, fixture):
        self.model.save_fixture(fixture)

    def get_fixtures_by_date(self, date):
        return self.model.get_fixtures_by_date(date)
