"""Pencatat pengeluaran bulanan (nongkrong, bensin, kuota, dll)."""
from collections import defaultdict
from datetime import date

CATEGORIES = ("makan", "bensin", "nongkrong", "kuota", "hobi", "lainnya")


def add_expense(data, amount, category, note="", when=None):
    """Tambah pengeluaran. Jumlah harus > 0 dan kategori valid."""
    if amount <= 0:
        raise ValueError("Jumlah pengeluaran harus lebih dari 0")
    if category not in CATEGORIES:
        raise ValueError(f"Kategori tidak valid: {category}")
    entry = {
        "amount": float(amount),
        "category": category,
        "note": note,
        "date": (when or date.today()).isoformat(),
    }
    data["expenses"].append(entry)
    return entry


def total_by_category(data, month=None):
    """Total pengeluaran per kategori; opsional difilter 'YYYY-MM'."""
    totals = defaultdict(float)
    for item in data["expenses"]:
        if month and not item["date"].startswith(month):
            continue
        totals[item["category"]] += item["amount"]
    return dict(totals)


def over_budget(data, limit, month):
    """True bila total pengeluaran bulan tersebut melebihi limit."""
    return sum(total_by_category(data, month).values()) > limit
