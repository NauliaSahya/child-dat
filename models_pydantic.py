from datetime import date
from pydantic import BaseModel, field_validator
import utils 

"""Model input anak. Validasi otomatis dengan Pydantic."""
class ChildData(BaseModel):
    nama: str
    tanggal_lahir: date 
    alergi: list[str]
    berat_kg: float
    tinggi_cm: int
    pola_makan: list[str]

    @field_validator("tanggal_lahir", mode="before") # Pydantic: Aturan ini dijalankan sebelum Pydantic cek tipe tanggal.
    @classmethod
    def validate_and_parse_date(cls, v):
        if isinstance(v, date):
            # Kalau datanya sudah berupa date, langsung di return
            return v
        if isinstance(v, str):
            # Menggunakan fungsi parsing yang ada di utils
            return utils.parse_date(v)
        raise ValueError("Format tanggal tidak dikenali.")

    @field_validator("tinggi_cm", mode="before")
    @classmethod
    def parse_height(cls, v):
        # Memastikan tinggi berupa int.
        if isinstance(v, str) and v.isdigit():
            return int(v)
        return v


"""Model output hasil pemrosesan."""
class ChildResult(BaseModel):
    nama: str
    usia_tahun: float
    usia_bulan: int
    berat_kg: float
    tinggi_cm: int
    BMI: float
    kategori_usia: str
    status_gizi: str
    alergi: list[str]
    pola_makan_bersih: list[str]