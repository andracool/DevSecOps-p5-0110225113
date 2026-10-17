from datetime import date

import pytest

from cowokkit import budget


def fresh():
    return {"expenses": [], "workouts": [], "grooming": {}}


def test_add_and_total():
    d = fresh()
    budget.add_expense(d, 50000, "makan", when=date(2026, 10, 1))
    budget.add_expense(d, 25000, "makan", when=date(2026, 10, 2))
    budget.add_expense(d, 100000, "bensin", when=date(2026, 9, 30))
    assert budget.total_by_category(d, "2026-10") == {"makan": 75000.0}


def test_invalid_amount_and_category():
    d = fresh()
    with pytest.raises(ValueError):
        budget.add_expense(d, 0, "makan")
    with pytest.raises(ValueError):
        budget.add_expense(d, 1000, "judi")


def test_over_budget():
    d = fresh()
    budget.add_expense(d, 300000, "hobi", when=date(2026, 10, 5))
    assert budget.over_budget(d, 200000, "2026-10")
    assert not budget.over_budget(d, 500000, "2026-10")
