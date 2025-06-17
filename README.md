#Tugas 2 Pemrograman Jaringan

## Alendra Rafif
## 5025221297

## Deskripsi
Repositori ini berisi implementasi program **Time Server TCP multithreaded** untuk memenuhi **Tugas 2** mata kuliah **Pemrograman Jaringan**. Server dibuat menggunakan Python dan mendukung komunikasi dengan beberapa klien secara bersamaan menggunakan multithreading. Klien dapat meminta informasi waktu dari server (TIME) dan mengakhiri koneksi dengan server (QUIT).

---

## 🛠️ Fitur Server

-  Menggunakan **port 45000** dan protokol **TCP**
-  Menangani banyak klien secara **concurrent** menggunakan 
-  Melayani perintah:
  - `"TIME\r\n"` → membalas waktu saat ini dalam format `JAM hh:mm:ss\r\n`
  - `"QUIT\r\n"` → menutup koneksi dengan klien
- Menggunakan encoding UTF-8 untuk komunikasi

---

## 📄 Format Protokol

### Request dari Klien:
- `"TIME\r\n"` → meminta waktu sekarang
- `"QUIT\r\n"` → keluar dari koneksi

### Respon dari Server:
- `"JAM hh:mm:ss\r\n"` → respon terhadap perintah `TIME`
- `"INVALID COMMAND\r\n"` → jika perintah tidak dikenali

---

## Cara Menjalankan Program

### 1. Jalankan Server pada mesin 1
```bash
python server_thread.py
```
### 2. Simulasikan Client menggunakan telnet pada mesin 2 dan 3
```
telnet 172.16.16.101 45000
```

### 3. Kirimkan perintah dari client ke server
untuk mendapatkan waktu saat ini:
```
TIME
```

Untuk mengakhiri koneksi
```
QUIT
```
