from __future__ import annotations

import datetime
from pathlib import Path
from typing import Mapping, Sequence, Tuple, TypedDict, Union

import yaml


class AlertLevel(TypedDict):
    label: str
    rgb: Tuple[int, int, int]
    description: str
    action: str


class AlertMovement(TypedDict):
    date: datetime.date
    source: str
    from_level: str
    to_level: str
    direction: str


class AlertStatus(TypedDict):
    movement: AlertMovement
    level: AlertLevel


class CovidAlertLevel:
    levels: Mapping[str, AlertLevel]
    movements: Sequence[AlertMovement]

    @classmethod
    def load(cls, path: Union[str, Path]) -> CovidAlertLevel:
        with open(path) as f:
            data = yaml.load(f)

        movements = data['movements']

        def modify_movement(movement) -> AlertMovement:
            movement['direction'] = 'up' if movement['from_level'] < movement['to_level'] else 'down'
            return movement

        movements = list(map(modify_movement, movements))

        return cls(data["levels"], data["movements"])

    def __init__(
        self, levels: Sequence[AlertLevel], movements: Sequence[AlertMovement]
    ):
        self.levels = {level["label"]: level for level in levels}
        self.movements = movements

    def get_current_level(self) -> AlertStatus:
        movements = sorted(self.movements, key=lambda m: m["date"], reverse=True)
        latest = movements[0]

        return {"level": self.levels[latest["to_level"]], "movement": latest}
