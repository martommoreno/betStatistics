# views/football_view.py
class FootballView:
    @staticmethod
    def display_fixtures(fixtures):
        for fixture in fixtures:
            print(f"Home: {fixture[0]}, Away: {fixture[1]}, Date: {fixture[2]}")