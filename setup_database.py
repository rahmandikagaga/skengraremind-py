import sqlite3

# Membuat atau membuka database
conn = sqlite3.connect("database/tugas_sekolah.db")
cursor = conn.cursor()

# Membuat tabel tugas
cursor.execute("""
CREATE TABLE IF NOT EXISTS tugas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_tugas TEXT NOT NULL,
    deskripsi TEXT,
    tanggal_deadline DATE NOT NULL
);
""")

# Contoh data awal
cursor.executemany("""
INSERT INTO tugas (nama_tugas, deskripsi, tanggal_deadline)
VALUES (?, ?, ?)
""", [
    ("Matematika", "Latihan soal integral", "2024-12-01"),
    ("Fisika", "Praktikum gerak jatuh bebas", "2024-12-05")
])

conn.commit()
conn.close()

print("Database dan tabel berhasil dibuat.")