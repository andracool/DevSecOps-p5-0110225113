"""Pengingat perawatan diri: cukur rambut, potong kuku, dll."""
from datetime import date, timedelta

INTERVAL_DAYS = {"cukur_rambut": 21, "potong_kuku": 7, "cukur_jenggot": 3,
                 "ganti_sikat_gigi": 90}


def mark_done(data, task, when=None):
    """Tandai tugas perawatan selesai dilakukan."""
    if task not in INTERVAL_DAYS:
        raise ValueError(f"Tugas tidak dikenal: {task}")
    data["grooming"][task] = (when or date.today()).isoformat()


def next_due(data, task):
    """Tanggal berikutnya tugas harus dilakukan (None bila belum pernah)."""
    last = data["grooming"].get(task)
    if last is None:
        return None
    return date.fromisoformat(last) + timedelta(days=INTERVAL_DAYS[task])


def overdue_tasks(data, today=None):
    """Daftar tugas yang lewat jatuh tempo atau belum pernah dilakukan."""
    today = today or date.today()
    result = []
    for task in INTERVAL_DAYS:
        due = next_due(data, task)
        if due is None or due < today:
            result.append(task)
    return result
