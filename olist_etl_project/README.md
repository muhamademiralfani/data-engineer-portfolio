# Proyek Pipeline ETL Data E-commerce Olist

Proyek ini adalah contoh pipeline ETL (Extract, Transform, Load) sederhana yang memproses data dari Olist E-commerce Dataset.

## Deskripsi Proyek

Pipeline ini melakukan tiga langkah utama:
1.  **Extract:** Membaca data mentah dari beberapa file `.csv` (customers, orders, dan payments).
2.  **Transform:** Membersihkan dan menggabungkan data tersebut. Transformasi yang dilakukan meliputi penggabungan tabel, konversi tipe data tanggal, dan penanganan nilai yang hilang (null).
3.  **Load:** Memuat data yang sudah bersih dan terstruktur ke dalam sebuah database SQLite sebagai tabel fakta `fact_orders`.

## Arsitektur Pipeline

Berikut adalah diagram sederhana alur data dalam pipeline ini:

![Arsitektur Sederhana](https://i.imgur.com/your-diagram-image.png) 
*(Catatan: Anda bisa membuat diagram sederhana menggunakan draw.io atau excalidraw lalu upload gambarnya dan ganti link di atas)*

```
[File CSV] ---> [Script Python (Pandas)] ---> [Database SQLite]
```

## Tech Stack

* **Bahasa:** Python 3
* **Library:**
    * Pandas: Untuk manipulasi dan analisis data.
    * SQLAlchemy: Untuk berinteraksi dengan database SQL.
* **Database:** SQLite

## Cara Menjalankan Proyek

1.  **Clone repository ini:**
    ```bash
    git clone [https://github.com/](https://github.com/)<nama-user-github-anda>/data-engineer-portfolio.git
    cd data-engineer-portfolio/olist_etl_project
    ```

2.  **Buat dan aktifkan virtual environment:**
    ```bash
    python -m venv venv
    source venv/Scripts/activate # Untuk Windows (Git Bash)
    # source venv/bin/activate  # Untuk Mac/Linux
    ```

3.  **Install dependensi:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Kita akan membuat file ini di langkah berikutnya)*

4.  **Unduh dataset** dari [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) dan letakkan file-file `.csv` di dalam folder `data`.

5.  **Jalankan pipeline:**
    ```bash
    python pipeline.py
    ```
    Hasilnya akan berupa file `olist_dwh.db`.