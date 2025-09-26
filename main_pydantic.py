import json
from pydantic import ValidationError
from models_pydantic import ChildData, ChildResult 
import utils 

"""Pemrosesan data anak menggunakan Pydantic Model."""
def process_child_pydantic(data: ChildData) -> ChildResult:
    # 1. Normalisasi Data (tanggal sudah divalidasi oleh ChildData)
    usia_tahun, usia_bulan = utils.calculate_age(data.tanggal_lahir)
    bmi = utils.calculate_bmi(data.berat_kg, data.tinggi_cm)
    
    # 2. Fitur Turunan & Rule Check
    return ChildResult(
        nama=data.nama,
        usia_tahun=usia_tahun,
        usia_bulan=usia_bulan,
        berat_kg=data.berat_kg,
        tinggi_cm=data.tinggi_cm,
        BMI=bmi,
        kategori_usia=utils.categorize_age(usia_bulan),
        status_gizi=utils.nutrition_status(bmi),
        alergi=data.alergi,
        pola_makan_bersih=utils.clean_diet(data.pola_makan, data.alergi)
    )


if __name__ == "__main__":
    try:
        # Input
        with open("input.json", "r", encoding="utf-8") as f:
            raw = json.load(f)

        child_data = ChildData(**raw) # Validasi & Konversi data otomatis
        result = process_child_pydantic(child_data)
        
        # Output
        with open("output_pydantic.json", "w", encoding="utf-8") as f:
            json.dump(result.model_dump(), f, ensure_ascii=False, indent=2)

        print("=== Input Validated ===")
        print(child_data.model_dump_json(indent=2))
        print("\n=== Output ===")
        print(result.model_dump_json(indent=2))

    except ValidationError as e:
        print("ERROR: Data input tidak valid (Pydantic Validation Error)")
    except Exception as e:
        print(f"ERROR: {e}")