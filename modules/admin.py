import streamlit as st
from modules.database import get_all_tugas, add_tugas, delete_tugas

def login(username, password):
    # Contoh kredensial (ganti dengan database jika ada)
    valid_users = {"admin": "admin123"}
    return valid_users.get(username) == password


def admin_menu():
    st.title("Admin Panel")
    st.subheader("Tambah Tugas Baru")
    
    nama_tugas = st.text_input("Mata Pelajaran")
    deskripsi = st.text_area("Deskripsi")
    deadline = st.date_input("Tanggal Deadline")
    
    if st.button("Tambah Tugas"):
        add_tugas(nama_tugas, deskripsi, str(deadline))
        st.success("Tugas berhasil ditambahkan!")

        
    