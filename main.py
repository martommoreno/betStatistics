# main.py
from controllers.football_controller import FootballController
from views.football_view import FootballView

def main():
    controller = FootballController()
    view = FootballView()

    # Exemplo de salvar um fixture
    fixture = ('Team A', 'Team B', '2024-08-27')
    controller.save_fixture(fixture)

    # Exemplo de exibir fixtures
    fixtures = controller.get_fixtures()
    view.display_fixtures(fixtures)

if __name__ == "__main__":
    main()