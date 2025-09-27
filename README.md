# Child Data Processing

Program sederhana untuk memproses data anak.  
Terdapat **dua versi**:

1. **Non-Pydantic**  
   - Hanya menggunakan Python standard library.  
   - Fokus pada perhitungan sederhana.  
   - Branch: `main`  

2. **Pydantic**  
   - Menggunakan [Pydantic](https://docs.pydantic.dev) untuk validasi input otomatis.  
   - Memberikan error detail bila input salah format.  
   - Branch: `pydantic`  

---

## 📂 Struktur Project
   ├──main.py # Main program non-pydantic
   ├── utils.py # Fungsi utilitas (dipakai di kedua versi)
   ├── input.json # Contoh input
   ├── output.json # Contoh output non-pydantic
   ├── main_pydantic.py # Mian program pydantic
   ├── models_pydantic.py # Model input/output pydantic
   ├── output_pydantic.json # Contoh output pydantic
   ├── requirements.txt # Library tambahan (untuk versi pydantic)
   └── README.md

📥 Contoh Input (input.json)
{
  "nama": "Adit",
  "tanggal_lahir": "25 Juni 2021",
  "alergi": ["susu", "kacang"],
  "berat_kg": 15.8,
  "tinggi_cm": 100,
  "pola_makan": ["nasi", "ayam", "susu", "ikan"]
}

📥 Hasil Output
1. **Non-Pydantic**  
<img width="366" height="788" alt="image" src="https://github.com/user-attachments/assets/fca19421-dda3-45b7-9092-c084f1cd6466" />

2. **Pydantic**  
<img width="363" height="802" alt="image" src="https://github.com/user-attachments/assets/06a78c26-0a03-4c56-a8e5-a546c854e90f" />

