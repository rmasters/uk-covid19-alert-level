import os
from pathlib import Path

from flask import Flask, g

from .covid import CovidAlertLevel
from .endpoints import endpoints


def create_app() -> Flask:
    app = Flask(__name__)

    root_path = Path(__file__).parent / ".."

    # Load data
    covid_levels_data = os.environ.get("COVID_LEVELS_PATH", root_path / "levels.yml")
    covid_levels = CovidAlertLevel.load(covid_levels_data)

    @app.before_request
    def provide_levels():
        setattr(g, str(CovidAlertLevel), covid_levels)

    app.register_blueprint(endpoints)

    return app
