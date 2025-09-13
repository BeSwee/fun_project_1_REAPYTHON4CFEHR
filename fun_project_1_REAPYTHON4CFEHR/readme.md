1. Deskripsi Singkat

Aplikasi ini adalah Tes Kepribadian Sederhana berbasis Streamlit. Pengguna akan menjawab 3 pertanyaan, masing-masing dengan 3 pilihan jawaban (A, B, C). Hasil tes ditentukan berdasarkan jawaban yang paling banyak dipilih, dan aplikasi menampilkan deskripsi kepribadian serta animasi GIF yang sesuai.

2. Teknologi yang Digunakan

Python 3.x → Bahasa pemrograman utama
Streamlit → Framework untuk membuat aplikasi web interaktif
HTML + CSS → Untuk mempercantik tampilan teks seperti efek pelangi

3. Cara Menjalankan Aplikasi

-. Pastikan Python sudah terinstal.
-. Instal Streamlit dengan perintah:
pip install streamlit
-. Simpan kode dalam file tes_kepribadian.py
-. Jalankan aplikasi dengan perintah:
streamlit run tes_kepribadian.py
-. Browser akan terbuka otomatis di http://localhost:8501.

4. Alur Kerja Program

Judul Aplikasi → Menampilkan teks pelangi dengan efek menarik.
Menampilkan Pertanyaan → Setiap pertanyaan memiliki 3 opsi (A, B, C).
Menyimpan Jawaban → Sistem menghitung jawaban berdasarkan huruf pertama.
Tombol Lihat Hasil → Menentukan kepribadian berdasarkan mayoritas jawaban.
Menampilkan Hasil → Deskripsi kepribadian + animasi GIF yang sesuai.

5. Struktur Kode

a. Import Library
"import streamlit as st"
Streamlit digunakan untuk membuat antarmuka web.

b. Judul Aplikasi
"
st.markdown(
    "<h1 style='text-align: center; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"
    " -webkit-background-clip: text; color: transparent;'>✨Tes Kepribadian Sederhana✨</h1>",
    unsafe_allow_html=True
)
"
Menampilkan judul dengan efek pelangi menggunakan HTML + CSS.

c. Daftar Pertanyaan
"
questions = [
    {
        "question": "Di akhir pekan, kegiatan apa yang paling ingin Anda lakukan?",
        "options": ["A. Berkumpul dengan teman atau keluarga",
                    "B. Membaca buku atau menonton film sendirian",
                    "C. Mencoba aktivitas baru seperti hiking atau kursus singkat"]
    },
    ...
]
"
question → Teks pertanyaan.
options → Pilihan jawaban A, B, C.

d. Menampilkan Pertanyaan & Menyimpan Jawaban
"
answers_count = {"A": 0, "B": 0, "C": 0}

for nomor_pertanyaan, data_pertanyaan in enumerate(questions):
    st.subheader(f"Pertanyaan {nomor_pertanyaan+1}")
    jawaban = st.radio(data_pertanyaan["question"], data_pertanyaan["options"], key=f"q{nomor_pertanyaan}")
    
    if jawaban:
        answers_count[jawaban[0]] += 1
"
st.radio() → Menampilkan pilihan jawaban dalam bentuk radio button.
Jawaban disimpan dalam dictionary answers_count.

e. Menampilkan Hasil Tes
"
if st.button("Lihat Hasil"):
    max_answer = max(answers_count, key=answers_count.get)
    st.subheader("=== HASIL TES KEPRIBADIAN ===")
"
-. st.button() memicu perhitungan setelah semua pertanyaan dijawab.
-. Logika hasil:
Jika semua skor sama → Kepribadian Campuran
Jika salah satu jawaban dominan → tampilkan hasil sesuai tipe kepribadian

"
if len(set(answers_count.values())) == 1:
    st.write("**💫Kepribadian Campuran 🌈**: Anda memiliki sisi ekstrovert, analitis, dan kolaboratif secara seimbang.")
    st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZW5laGFobGpha2w2dTE5bDgxNXlienN4bjl5NHA3YWt5dWQ5c2psYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hTEslT7lluSFyHlyEf/giphy.gif")
"
-. Menampilkan hasil kepribadian beserta GIF animasi yang relevan.

6. Output Aplikasi

Halaman utama → Menampilkan judul dengan efek pelangi.
Pertanyaan interaktif → 3 pertanyaan dengan pilihan A, B, C.
Hasil Tes → Deskripsi kepribadian + animasi GIF.
