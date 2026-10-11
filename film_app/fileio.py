
"""Modul untuk membaca, menambah, dan menulis data koleksi film."""

from pathlib import Path
from .validasi import buat_record_film, ValidasiFilmError


class KoleksiFilm:
    # Mengelola penyimpanan dan pembacaan data film dari file.
    def __init__(self, nama_file="film.txt"):
        # Menentukan lokasi file yang akan digunakan.
        self.nama_file = Path(nama_file)

        # Memastikan file data sudah tersedia sebelum digunakan.
        self.pastikan_file()

    def pastikan_file(self):
        # Membuat file baru beserta header jika file belum tersedia.
        try:
            with open(self.nama_file, "x", encoding="utf-8") as file:
                file.write("judul|genre|tahun|rating\n")
        except FileExistsError:
            # Membiarkan file yang sudah ada agar data lama tidak terhapus.
            pass

    def baca_semua_film(self):
        # Menyiapkan daftar untuk menampung data film yang berhasil dibaca.
        daftar_film = []

        try:
            # Membuka file dalam mode r untuk membaca data.
            with open(self.nama_file, "r", encoding="utf-8") as file:
                # Melewati baris pertama karena berisi nama kolom.
                next(file, None)

                # Membaca data secara berurutan dan mencatat nomor baris.
                for nomor_baris, baris in enumerate(file, start=2):
                    # Memisahkan data berdasarkan tanda pemisah "|".
                    bagian = baris.strip().split("|")

                    # Melewati baris jika jumlah kolom tidak sesuai.
                    if len(bagian) != 4:
                        print(
                            f"Baris {nomor_baris} dilewati "
                            "karena format salah."
                        )
                        continue

                    try:
                        # Mengubah tahun dan rating menjadi tipe angka.
                        # Data yang berhasil dikonversi dimasukkan ke daftar.
                        daftar_film.append({
                            "judul": bagian[0],
                            "genre": bagian[1],
                            "tahun": int(bagian[2]),
                            "rating": float(bagian[3]),
                        })
                    except (ValueError, TypeError) as error:
                        # Melewati baris yang datanya tidak dapat dikonversi.
                        print(f"Baris {nomor_baris} dilewati: {error}")

        except FileNotFoundError:
            # Menampilkan pesan jika file data tidak ditemukan.
            print("File koleksi film tidak ditemukan.")

        # Mengembalikan daftar film yang berhasil dibaca.
        return daftar_film

    def tambah_film(self, judul, genre, tahun, rating):
        # Memvalidasi data sebelum menyimpannya ke file.
        film = buat_record_film(
            judul=judul,
            genre=genre,
            tahun=tahun,
            rating=rating,
        )

        # Membuka file dalam mode a agar data baru ditambahkan
        # tanpa menghapus data film yang sudah tersimpan.
        with open(self.nama_file, "a", encoding="utf-8") as file:
            file.write(
                f"{film['judul']}|{film['genre']}|"
                f"{film['tahun']}|{film['rating']}\n"
            )

        # Mengembalikan data film yang berhasil ditambahkan.
        return film

    def tulis_laporan(self, isi, nama_file="laporan_film.txt"):
        # Membuka file dalam mode w untuk membuat atau mengganti laporan.
        with open(nama_file, "w", encoding="utf-8") as file:
            # Menuliskan isi ringkasan ke file laporan.
            file.write(isi)