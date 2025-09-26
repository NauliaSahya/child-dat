import json
import utils

"""
Pemrosesan data anak (input-> output) dengan file JSON.
"""
def process_child(data: dict) -> dict: 
    try:
        # 1. Normalisasi Data
        dob = utils.parse_date(data["tanggal_lahir"]) # Panggil fungsi parsing
        usia_tahun, usia_bulan = utils.calculate_age(dob)
        bmi = utils.calculate_bmi(data["berat_kg"], data["tinggi_cm"])
        
        # 2. Fitur Turunan & Rule Check
        return {
            "nama": data["nama"],
            "usia_tahun": usia_tahun,
            "usia_bulan": usia_bulan,
            "berat_kg": data["berat_kg"],
            "tinggi_cm": data["tinggi_cm"],
            "BMI": bmi,
            "kategori_usia": utils.categorize_age(usia_bulan),
            "status_gizi": utils.nutrition_status(bmi),
            "alergi": data["alergi"],
            "pola_makan_bersih": utils.clean_diet(data["pola_makan"], data["alergi"])
        }
    except KeyError as e:
        raise ValueError(f"Input JSON hilang key: {e}") # Jika ada kolom data yang hilang atau salah di JSON 
    except TypeError as e:
        raise ValueError(f"Tipe data tidak sesuai: {e}") # JIka tipe data di JSON salah


if __name__ == "__main__":
    try:
        # Read input
        with open("input.json", "r", encoding="utf-8") as f:
            raw = json.load(f)

        result = process_child(raw) # Pemrosesan
        
        # Output
        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print("=== Input ===")
        print(json.dumps(raw, ensure_ascii=False, indent=2))
        print("\n=== Output ===")
        print(json.dumps(result, ensure_ascii=False, indent=2))

    except Exception as e:
        print(f"ERROR: {e}")