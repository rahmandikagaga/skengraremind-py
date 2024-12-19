import streamlit as st
import base64
from modules.admin import admin_menu, login
from modules.ai_agent import ai_agent_search
from modules.database import get_all_tugas, delete_tugas

# Konfigurasi halaman
st.set_page_config(
    page_title="SKENGRACARE",
    page_icon="logo/logo_smk.png",
    layout="wide",
    initial_sidebar_state="expanded",
)
with open("style.css") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)


# Fungsi untuk membaca file gambar dan mengonversi ke Base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as file:
        binary_data = file.read()
        base64_data = base64.b64encode(binary_data).decode('utf-8')
    return base64_data

# Fungsi untuk menampilkan logo di homepage
def display_logo():
    logo_path = "logo/gema.png"  # Path logo
    logo_base64 = get_base64_of_bin_file(logo_path)
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{logo_base64}" alt="Logo SMK" style="width: 600px;">
            <br>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Sidebar menu
menu = st.sidebar.selectbox("Pilih Menu", ["Home", "Admin", "Daftar Tugas", "AI Assistant"])

if menu == "Home":
    display_logo()  # Menampilkan logo
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>SKENSAGRA AI REMIND TASK</h1>
            <h5>Gunakan aplikasi ini untuk melihat daftar tugas sekolah Anda.</h5>
        </div>
        """,
        unsafe_allow_html=True,
    )


elif menu == "Admin":
    # Autentikasi admin
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        st.title("Login Admin")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login(username, password):
                st.session_state["logged_in"] = True
                st.success("Login berhasil!")
                st.rerun()
            else:
                st.error("Username atau password salah!")
    else:
        st.success("Anda telah login sebagai admin.")
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.rerun()

        # Tampilkan menu admin
        admin_menu()

elif menu == "Daftar Tugas":
    st.title("Daftar Tugas")
    tugas = get_all_tugas()  # Ambil semua tugas dari database
    for t in tugas:
        st.write(f"### {t['nama_tugas']}")
        st.write(f"Deskripsi: {t['deskripsi']}")
        st.write(f"Deadline: {t['tanggal_deadline']}")
        if st.button(f"Hapus {t['nama_tugas']}", key=t["id"]):
            delete_tugas(t["id"])
            st.success(f"Tugas {t['nama_tugas']} berhasil dihapus!")
            st.rerun()

elif menu == "AI Assistant":
    st.title("AI Assistant")
    st.write("Tanyakan tugas apa yang telah diberikan.")
    
    query = st.text_input("Masukkan pertanyaan Anda")
    if st.button("Cari"):
        with st.spinner("AI sedang memproses pertanyaan..."):
            response = ai_agent_search(query)
            st.write("Jawaban AI:")
            st.write(response)
