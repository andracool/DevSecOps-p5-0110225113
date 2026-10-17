"""Kalkulator kebugaran: BMI, kebutuhan kalori, dan log latihan."""
from datetime import date

ACTIVITY = {"rendah": 1.2, "sedang": 1.55, "tinggi": 1.725}


def bmi(weight_kg, height_cm):
    """Hitung Body Mass Index."""
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Berat dan tinggi harus positif")
    h = height_cm / 100
    return round(weight_kg / (h * h), 1)


def bmi_category(value):
    """Kategori BMI standar WHO."""
    if value < 18.5:
        return "kurus"
    if value < 25:
        return "normal"
    if value < 30:
        return "gemuk"
    return "obesitas"


def daily_calories(weight_kg, height_cm, age, activity="sedang"):
    """Kebutuhan kalori harian pria (Mifflin-St Jeor x faktor aktivitas)."""
    if activity not in ACTIVITY:
        raise ValueError("Level aktivitas: rendah/sedang/tinggi")
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    return round(bmr * ACTIVITY[activity])


def log_workout(data, name, minutes, when=None):
    """Catat sesi latihan."""
    if minutes <= 0:
        raise ValueError("Durasi harus positif")
    entry = {"name": name, "minutes": minutes,
             "date": (when or date.today()).isoformat()}
    data["workouts"].append(entry)
    return entry


def weekly_minutes(data, dates):
    """Total menit latihan pada daftar tanggal (ISO) tertentu."""
    return sum(w["minutes"] for w in data["workouts"] if w["date"] in dates)
