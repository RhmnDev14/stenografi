# Steganografi LSB (Least Significant Bit)

Program berbasis web (UI) untuk menyisipkan pesan rahasia ke dalam gambar (Encode) dan membaca kembali pesan yang disisipkan tersebut (Decode) menggunakan teknik steganografi *Least Significant Bit* (LSB).

## Fitur
1. **Encode**: Menyembunyikan pesan teks ke dalam sebuah gambar.
2. **Decode**: Membaca pesan teks rahasia yang tersembunyi dari sebuah gambar.

## Prasyarat
1. **Python**: Pastikan kamu sudah menginstal Python (versi 3.8 ke atas) di komputermu.
   - Jika belum punya, silakan download secara gratis di [Situs Resmi Python (python.org)](https://www.python.org/downloads/). 
   - *(Penting bagi pengguna Windows: pastikan untuk mencentang kotak **"Add Python to PATH"** di halaman awal saat melakukan instalasi!)*
2. **Library**: Program ini membutuhkan library `Pillow` untuk memproses gambar dan `streamlit` untuk antarmuka web.

Setelah Python terinstal, kamu bisa menginstal kedua library tersebut dengan menjalankan perintah berikut di terminal / command prompt:
```bash
pip install Pillow streamlit
```

## Cara Instalasi & Menjalankan Program
1. Buka terminal atau command prompt.
2. Clone repositori ini ke komputer kamu:
   ```bash
   git clone https://github.com/RhmnDev14/stenografi.git
   ```
3. Masuk ke dalam folder program:
   ```bash
   cd stenografi
   ```
4. Jalankan script utama:
   ```bash
   python3 main.py
   ```
5. Browser akan otomatis terbuka dan menampilkan antarmuka web steganografi.

## Panduan Penggunaan Web UI

### 1. Encode (Menyembunyikan Pesan)
1. Buka tab **"🔒 Encode (Sembunyikan Pesan)"**.
2. Klik tombol **Browse files** lalu pilih gambar sumber (format JPG atau PNG).
3. Ketikkan pesan rahasia kamu di dalam kotak teks yang disediakan.
4. Klik tombol **Encode & Sembunyikan Pesan**.
5. Tunggu prosesnya selesai, lalu klik tombol **⬇️ Download Gambar Hasil (.png)** untuk menyimpan gambar yang sudah disisipi pesan rahasia.

   > **⚠️ PENTING:** Format gambar hasil *harus* `.png`. Jika gambar hasil ini dikonversi lagi menjadi `.jpg` atau dikirim melalui platform chat yang melakukan kompresi gambar (seperti WhatsApp biasa), pesan rahasia yang ada di dalamnya akan rusak/hilang.

### 2. Decode (Membaca Pesan)
1. Buka tab **"🔓 Decode (Baca Pesan)"**.
2. Klik tombol **Browse files** dan pilih gambar PNG yang sudah disisipi pesan rahasia.
3. Klik tombol **Decode & Baca Pesan**.
4. Program akan mengekstrak LSB dari gambar dan menampilkan pesan rahasianya di layar!

## Cara Kerja (Teknis Singkat)
Program ini bekerja dengan memanipulasi bit paling tidak signifikan (Least Significant Bit / LSB) dari setiap channel warna (Red, Green, Blue) pada piksel gambar. Pesan teks dari pengguna diubah ke dalam bentuk biner (0 dan 1), lalu setiap bit disisipkan menggantikan bit paling belakang pada nilai piksel gambar aslinya.

Untuk mengetahui di mana pesan tersebut berakhir saat di-decode, program otomatis menambahkan tanda batas atau *delimiter* (yaitu `#####`) di akhir pesan.
