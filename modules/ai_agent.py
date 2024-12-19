import openai
from modules.database import get_all_tugas
from modules.database import get_db_connection
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("openai_api_key")

def ai_agent_search(query):
    # Ambil semua tugas dari database atau sumber lainnya
    conn = get_all_tugas()
    conn = get_db_connection()
    tugas = conn.execute("SELECT * FROM tugas ORDER BY tanggal_deadline").fetchall()
    
    
    # Format daftar tugas menjadi string yang dapat dipahami oleh GPT-4
    tugas_list = [f"{t['nama_tugas']}: {t['deskripsi']} (Deadline: {t['tanggal_deadline']})" for t in tugas]
    tugas_text = "\n".join(tugas_list)
    
    # Kirimkan pesan ke GPT-4 dengan menggunakan format yang benar
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Kamu adalah asisten yang membantu menjawab pertanyaan berdasarkan daftar tugas."},
            {"role": "user", "content": query},
            {"role": "system", "content": f"Berikut adalah daftar tugas sekolah:\n{tugas_text}"}
        ],
        max_tokens=150,
    )
    
    return response['choices'][0]['message']['content']