# pipeline.py

import pandas as pd
from sqlalchemy import create_engine
import os

# --- EXTRACT ---
# Path ke folder data Anda
data_path = './data/'

# Mendefinisikan file-file yang akan kita gunakan
files_to_load = {
    'customers': 'olist_customers_dataset.csv',
    'orders': 'olist_orders_dataset.csv',
    'payments': 'olist_order_payments_dataset.csv'
}

# Dictionary untuk menampung DataFrames
dataframes = {}

print("1. Memulai proses Ekstraksi Data (Extract)...")
for name, filename in files_to_load.items():
    file_path = os.path.join(data_path, filename)
    dataframes[name] = pd.read_csv(file_path)
    print(f"  - File {filename} berhasil dimuat.")
print("Proses Ekstraksi Selesai.\n")


# --- TRANSFORM ---
print("2. Memulai proses Transformasi Data (Transform)...")

# Menggabungkan (merge) tabel orders dengan customers
df_merged = pd.merge(
    dataframes['orders'], 
    dataframes['customers'], 
    on='customer_id', 
    how='left'
)

# Menggabungkan hasil dengan tabel payments
df_final = pd.merge(
    df_merged,
    dataframes['payments'],
    on='order_id',
    how='left'
)

# Contoh transformasi sederhana:
# 1. Mengubah kolom tanggal menjadi tipe datetime
date_columns = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']
for col in date_columns:
    df_final[col] = pd.to_datetime(df_final[col], errors='coerce') # errors='coerce' akan mengubah error parsing menjadi NaT (Not a Time)

# 2. Membersihkan data null (contoh: mengisi nilai payment_value yang kosong dengan 0)
df_final['payment_value'].fillna(0, inplace=True)

# 3. Memilih kolom-kolom yang relevan saja untuk dimuat
columns_to_keep = [
    'order_id',
    'customer_id',
    'order_status',
    'order_purchase_timestamp',
    'payment_type',
    'payment_installments',
    'payment_value',
    'customer_unique_id',
    'customer_city',
    'customer_state'
]
df_final = df_final[columns_to_keep]

print("  - Data telah digabungkan dan dibersihkan.")
print("Proses Transformasi Selesai.\n")


# --- LOAD ---
print("3. Memulai proses Pemuatan Data (Load)...")

# Membuat koneksi ke database SQLite
# Database akan dibuat secara otomatis dalam file bernama 'olist_dwh.db'
db_path = 'olist_dwh.db'
engine = create_engine(f'sqlite:///{db_path}')

# Memuat DataFrame akhir ke dalam tabel 'fact_orders' di database SQLite
table_name = 'fact_orders'
df_final.to_sql(table_name, engine, if_exists='replace', index=False)

print(f"  - Data berhasil dimuat ke tabel '{table_name}' di database '{db_path}'.")
print("Proses Pemuatan Selesai.\n")

print("Pipeline ETL selesai dijalankan!")