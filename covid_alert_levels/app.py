import datetime
import os
from pathlib import Path
from typing import Union

from flask import Flask, g, render_template

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

    @app.template_filter('daysago')
    def daysago(date: datetime.date) -> str:
        delta = datetime.date.today() - date
        seconds = delta.total_seconds()
        days = seconds % 3600

        if days == 0:
            return "today"

        return "%d days ago" % days

    app.register_blueprint(endpoints)

    @app.route('/')
    def homepage():
        # Get current level
        covid_levels: CovidAlertLevel = getattr(g, str(CovidAlertLevel))
        current_level = covid_levels.get_current_level()

        return render_template('home.html', level=current_level['level'], movement=current_level['movement'])

    return app
