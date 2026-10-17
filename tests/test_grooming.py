from datetime import date

import pytest

from cowokkit import grooming


def test_due_and_overdue():
    d = {"expenses": [], "workouts": [], "grooming": {}}
    grooming.mark_done(d, "potong_kuku", date(2026, 10, 1))
    assert grooming.next_due(d, "potong_kuku") == date(2026, 10, 8)
    assert "potong_kuku" in grooming.overdue_tasks(d, date(2026, 10, 10))
    assert "potong_kuku" not in grooming.overdue_tasks(d, date(2026, 10, 5))
    assert grooming.next_due(d, "cukur_rambut") is None


def test_unknown_task():
    with pytest.raises(ValueError):
        grooming.mark_done({"grooming": {}}, "tato")
