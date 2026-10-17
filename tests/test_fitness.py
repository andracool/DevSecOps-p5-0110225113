from datetime import date

import pytest

from cowokkit import fitness


def test_bmi_and_category():
    v = fitness.bmi(70, 175)
    assert v == 22.9
    assert fitness.bmi_category(v) == "normal"
    assert fitness.bmi_category(17) == "kurus"
    assert fitness.bmi_category(27) == "gemuk"
    assert fitness.bmi_category(32) == "obesitas"
    with pytest.raises(ValueError):
        fitness.bmi(0, 175)


def test_calories():
    assert fitness.daily_calories(70, 175, 25, "rendah") == round((700 + 1093.75 - 125 + 5) * 1.2)
    with pytest.raises(ValueError):
        fitness.daily_calories(70, 175, 25, "ekstrem")


def test_workout_log():
    d = {"expenses": [], "workouts": [], "grooming": {}}
    fitness.log_workout(d, "gym", 60, when=date(2026, 10, 1))
    fitness.log_workout(d, "lari", 30, when=date(2026, 10, 2))
    assert fitness.weekly_minutes(d, {"2026-10-01", "2026-10-02"}) == 90
    with pytest.raises(ValueError):
        fitness.log_workout(d, "gym", 0)
