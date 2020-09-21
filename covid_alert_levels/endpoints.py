from flask import Blueprint, g, jsonify

from .covid import CovidAlertLevel


endpoints = Blueprint("endpoints", __name__)


@endpoints.route("/level")
def get_current_alert_level():
    covid_levels: CovidAlertLevel = getattr(g, str(CovidAlertLevel))
    current_level = covid_levels.get_current_level()

    return jsonify(current_level)
