import sqlite3

def get_db_connection():
    conn = sqlite3.connect("database/tugas_sekolah.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_all_tugas():
    conn = get_db_connection()
    tugas = conn.execute("SELECT * FROM tugas ORDER BY tanggal_deadline").fetchall()
    conn.close()
    return tugas

def add_tugas(nama_tugas, deskripsi, deadline):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO tugas (nama_tugas, deskripsi, tanggal_deadline) VALUES (?, ?, ?)",
        (nama_tugas, deskripsi, deadline),
    )
    conn.commit()
    conn.close()

def delete_tugas(tugas_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tugas WHERE id = ?", (tugas_id,))
    conn.commit()
    conn.close()