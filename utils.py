from datetime import date
import re


"""Mengubah string tanggal menjadi objek date"""
def parse_date(s: str) -> date:
    months = {
        "januari": 1, "februari": 2, "maret": 3, "april": 4,
        "mei": 5, "juni": 6, "juli": 7, "agustus": 8,
        "september": 9, "oktober": 10, "november": 11, "desember": 12
    }
    # Format DD Bulan YYYY
    try:
        d, m, y = s.split()
        return date(int(y), months[m.lower()], int(d))
    except (ValueError, KeyError, AttributeError):
        # Jika parsing gagal, beri tahu masalah tanggal (penting di versi dict)
        raise ValueError("Format tanggal harus 'DD Bulan YYYY'.")


"""Menghitung usia dalam tahun (float) dan bulan (int)."""
def calculate_age(dob: date) -> tuple[float, int]:
    ref = date.today() # Dihitung berdasarkan tanggal hari ini
    days = (ref - dob).days # Hitung selisih dalam hari
    years = round(days / 365.25, 2) # Konversi hari ke tahun, menggunakan 365.25 (akomodasi tahun kabisat), dibulatkan
    months = (ref.year - dob.year) * 12 + (ref.month - dob.month) # Bulan = tahun x 12 + selisih bulan
    if ref.day < dob.day: 
        months -= 1 # Kalau belum genap satu bulan
    return years, max(0, months)


"""Hitung BMI = berat (kg) / (tinggi (m))^2."""
def calculate_bmi(weight: float, height_cm: float) -> float:
    return round(weight / ((height_cm / 100) ** 2), 1)


"""Kategori usia berdasarkan bulan."""
def categorize_age(months: int) -> str:
    if months < 12:
        return "infant"         # < 12 bulan
    elif months <= 36:
        return "toddler"        # 12-36 bulan
    return "preschooler"        # > 36 bulan


"""Status gizi sederhana berdasarkan BMI."""
def nutrition_status(bmi: float) -> str:
    if bmi < 14:
        return "underweight"    # BMI < 14
    elif bmi < 18:
        return "normal"         # 14 <= BMI < 18
    return "overweight"         # BMI >= 18


"""Hapus item makanan dari diet yang ada di daftar alergi."""
def clean_diet(diet: list[str], allergies: list[str]) -> list[str]:
    al = {a.lower() for a in allergies} # Himpunan daftar alergi
    return [m for m in diet if m.lower() not in al] # Mengembalikan list diet yang tidak ada di dalam himpunan alergi