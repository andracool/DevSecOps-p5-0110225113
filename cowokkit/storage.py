"""Penyimpanan data sederhana berbasis file JSON."""
import json
from pathlib import Path

DEFAULT_PATH = Path.home() / ".cowokkit.json"


def load(path=DEFAULT_PATH):
    """Baca data dari file JSON. Jika belum ada, kembalikan struktur kosong."""
    path = Path(path)
    if not path.exists():
        return {"expenses": [], "workouts": [], "grooming": {}}
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def save(data, path=DEFAULT_PATH):
    """Simpan data ke file JSON."""
    path = Path(path)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
