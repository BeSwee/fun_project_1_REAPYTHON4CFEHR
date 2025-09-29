1. Deskripsi Aplikasi

Aplikasi ini adalah aplikasi ramalan kartu tarot interaktif berbasis Streamlit dengan fitur AI + offline fallback.
Pengguna dapat:
Memasukkan nama mereka
Memilih gaya ramalan (Mistik, Lucu, atau Serius)
Mendapatkan ramalan dari AI (Hugging Face GPT-Neo 125M) atau dari template offline jika AI tidak tersedia.

2. Fitur Utama

Interaktif & Personal
Pengguna memasukkan nama, hasil ramalan lebih personal.
AI-Powered Tarot Reading
Menggunakan model GPT-Neo 125M dari Hugging Face.
Prompt sudah dioptimalkan untuk menghindari hasil aneh atau mengulang input.
Hybrid System (AI + Offline Template)
Jika AI gagal menghasilkan ramalan bagus → fallback ke ramalan offline.
Multi-style Reading
Mystic → puitis & misterius
Funny → lucu & menghibur
Serious → bijak & tenang
UI Modern
Kartu interaktif dengan animasi hover
Tampilan rapi & clean

3. Kebutuhan Sistem

Python: Versi 3.9+
Pustaka Python:
pip install streamlit transformers torch

4. Cara Menjalankan

Simpan kode sebagai app.py
Buka terminal, jalankan:
streamlit run app.py
Buka browser → http://localhost:8501
Masukkan nama, pilih gaya ramalan, lalu klik Draw Cards.

5. Struktur Kode

app.py
 ├─ Load Model (Hugging Face GPT-Neo 125M)
 ├─ Daftar kartu & arti ramalan
 ├─ Offline fallback templates
 ├─ Fungsi prompt AI + pembersihan output
 ├─ Tampilan Streamlit (UI)
 ├─ Tombol untuk memulai ramalan
 └─ Menampilkan hasil ramalan AI / Offline

6. Alur Kerja Aplikasi

Pengguna Input
Masukkan nama
Pilih gaya ramalan
Acak 3 kartu tarot
AI Generation
Kirim prompt ke GPT-Neo 125M
Hasil diproses & dipotong jika terlalu panjang
Fallback
Jika AI gagal → gunakan template offline
Tampilkan Hasil
Ramalan + arti kartu muncul di layar

7. Mode Gaya Ramalan

Mystic: Puitis, misterius, seperti ramalan kuno
Funny: Lucu, ringan, penuh humor
Serious: Bijak, seperti saran hidup dari mentor

8. Masalah Umum & Solusi

Model tidak terunduh: Hapus cache di C:\Users\<user>\.cache\huggingface\transformers lalu jalankan ulang
Hasil AI kosong / aneh: Aplikasi otomatis fallback ke offline template
Tidak ada internet: Aplikasi tetap jalan dengan offline template
ImportError: pipeline tidak ada: Pastikan transformers sudah diupdate: pip install --upgrade transformers

9. Screenshot (Contoh)
Tampilan awal → Input nama & pilih gaya
Kartu Tarot muncul → 3 kartu acak ditampilkan
Ramalan AI / Offline → Teks ramalan singkat & personal