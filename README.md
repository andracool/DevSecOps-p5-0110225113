# CowokKit â€” DevSecOps P5 (0110225113)

## 1. Nama Aplikasi & Fungsi
**CowokKit** adalah toolkit command-line untuk kebutuhan harian cowok, terdiri dari tiga modul:
- **Budget** â€” mencatat pengeluaran (makan, bensin, nongkrong, kuota, hobi) dan ringkasan per kategori.
- **Fitness** â€” hitung BMI, kebutuhan kalori harian (Mifflin-St Jeor), dan log latihan.
- **Grooming** â€” pengingat perawatan diri (cukur rambut, potong kuku, cukur jenggot, ganti sikat gigi).

## 2. Bahasa / Framework
Python 3.12 (standard library saja untuk aplikasi), pytest + pytest-cov untuk pengujian, Bandit untuk SAST.

## 3. Cara Menjalankan
```bash
git clone https://github.com/andracool/DevSecOps-p5-0110225113.git
cd DevSecOps-p5-0110225113
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python main.py expense 25000 makan --note "nasi padang"
python main.py bmi 70 175 25 --activity sedang
python main.py workout gym 60
python main.py groom --done potong_kuku
python main.py groom
python main.py summary

pytest --cov=cowokkit      # jalankan unit test
```

## 4. Overview Pipeline CI/CD
Workflow: `.github/workflows/devsecops.yml` â€” terpicu pada **push** dan **pull_request** ke branch `main`, runner `ubuntu-latest`.

| Job | Fungsi |
|-----|--------|
| `build` | Install dependencies, jalankan unit test, coverage gate â‰¥ 80% |
| `sast-scan` (`needs: build`) | Scan kode dengan **Bandit**, unggah laporan JSON, lalu **Quality Gate** |

**Quality Gate** (`scripts/quality_gate.py`): pipeline gagal bila Bandit menemukan â‰¥ 1 temuan severity HIGH atau MEDIUM. Temuan LOW diizinkan.
