#fun project 1 - REAPYTHON4CFEHR

import streamlit as st

# Judul dengan efek pelangi
st.markdown(
    "<h1 style='text-align: center; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"
    " -webkit-background-clip: text; color: transparent;'>✨Tes Kepribadian Sederhana✨</h1>",
    unsafe_allow_html=True
)

# Daftar pertanyaan
questions = [
    {
        "question": "Di akhir pekan, kegiatan apa yang paling ingin Anda lakukan?",
        "options": ["A. Berkumpul dengan teman atau keluarga",
                    "B. Membaca buku atau menonton film sendirian",
                    "C. Mencoba aktivitas baru seperti hiking atau kursus singkat"]
    },
    {
        "question": "Bagaimana cara Anda biasanya mengambil keputusan?",
        "options": ["A. Dengan cepat, mengandalkan insting",
                    "B. Dengan mempertimbangkan semua fakta dan risiko terlebih dahulu",
                    "C. Dengan meminta saran dari orang lain dan melihat banyak perspektif"]
    },
    {
        "question": "Saat ada tantangan baru di pekerjaan atau sekolah, Anda akan:",
        "options": ["A. Menerima tantangan dengan semangat, meski belum tahu semua detailnya",
                    "B. Menyusun rencana matang sebelum memulai",
                    "C. Mengajak tim atau teman untuk bersama-sama mencari solusi"]
    }
]

# Variabel untuk menyimpan jawaban user
answers_count = {"A": 0, "B": 0, "C": 0}

# Menampilkan pertanyaan satu per satu
for nomor_pertanyaan, data_pertanyaan in enumerate(questions):
    st.subheader(f"Pertanyaan {nomor_pertanyaan+1}")
    jawaban = st.radio(data_pertanyaan["question"], data_pertanyaan["options"], key=f"q{nomor_pertanyaan}")
    
    # Hitung jawaban berdasarkan huruf pertama
    if jawaban:
        answers_count[jawaban[0]] += 1

# Tombol untuk melihat hasil
if st.button("Lihat Hasil"):
    max_answer = max(answers_count, key=answers_count.get)
    st.subheader("=== HASIL TES KEPRIBADIAN ===")
    if len(set(answers_count.values())) == 1:
        st.write("**💫Kepribadian Campuran 🌈**: Anda memiliki sisi ekstrovert, analitis, dan kolaboratif secara seimbang.")
        st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZW5laGFobGpha2w2dTE5bDgxNXlienN4bjl5NHA3YWt5dWQ5c2psYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hTEslT7lluSFyHlyEf/giphy.gif")
    elif max_answer == "A":
        st.write("**Kepribadian 🏇Ekstrovert dan Spontan🏔️**: Anda suka hal-hal baru, cepat beradaptasi, dan cenderung energik di lingkungan sosial.")
        st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnJkY3RtdmszdHc2cDFjdWltbHljZXZmcHpqajA3MjFuc2ttb283ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oEjHElKihbq5vsRnG/giphy.gif")
    elif max_answer == "B":
        st.write("**Kepribadian 📖Analitis dan Tenang💁‍♀️**: Anda lebih suka berpikir mendalam, merencanakan dengan baik, dan menikmati waktu sendirian untuk refleksi.")
        st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExczgzZHMyM2M5eng0cjMxYm9yOHIzenpuODhmeWp0bWYzNnI0ZjJ0eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2ilegKh8fMdJAVqbG2/giphy.gif")
    else:
        st.write("**Kepribadian 👨‍👩‍👦Kolaboratif dan Fleksibel🏋️‍♂️**: Anda menghargai kerja sama, terbuka dengan ide orang lain, dan mampu menyesuaikan diri dengan situasi.")
        st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmhweWRpY3dkbDJqcnN0cmxseTE4ZHRyczN2ODc1d3gxOTBvazVlcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/z4cJCBqyDb5yOmf3GP/giphy.gif")
