
"""Modul untuk menguji fungsi dan pengolahan data film."""

import os
import tempfile
import unittest

from film_app.fileio import KoleksiFilm
from film_app.processing import AnalisisFilm
from film_app.validasi import ValidasiFilmError, buat_record_film


class TestAplikasiFilm(unittest.TestCase):
    # Menyiapkan data film contoh yang digunakan oleh setiap pengujian.
    def setUp(self):
        self.film = [
            {
                "judul": "Film A",
                "genre": "Drama",
                "tahun": 2020,
                "rating": 8.5,
            },
            {
                "judul": "Film B",
                "genre": "Komedi",
                "tahun": 2022,
                "rating": 7.0,
            },
        ]

    # Memastikan data film yang valid berhasil dibuat.
    def test_validasi_film_valid(self):
        film = buat_record_film(
            judul="Film C",
            genre="Aksi",
            tahun=2023,
            rating=9,
        )
        self.assertEqual(film["judul"], "Film C")

    # Memastikan validasi menolak film yang tidak memiliki judul.
    def test_judul_kosong(self):
        with self.assertRaises(ValidasiFilmError):
            buat_record_film(
                judul="",
                genre="Drama",
                tahun=2020,
                rating=8,
            )

    # Memastikan rating di atas batas maksimal ditolak.
    def test_rating_di_luar_batas(self):
        with self.assertRaises(ValidasiFilmError):
            buat_record_film(
                judul="Film D",
                genre="Drama",
                tahun=2020,
                rating=11,
            )

    # Memastikan film diurutkan berdasarkan rating dari tertinggi.
    def test_urutkan_rating(self):
        hasil = AnalisisFilm(self.film).urutkan_rating()
        self.assertEqual(hasil[0]["judul"], "Film A")

    # Memastikan pencarian genre tidak membedakan huruf besar dan kecil.
    def test_cari_genre(self):
        hasil = AnalisisFilm(self.film).cari_genre("komedi")
        self.assertEqual(len(hasil), 1)
        self.assertEqual(hasil[0]["judul"], "Film B")

    # Memastikan ringkasan menampilkan jumlah film dan informasi tambahan.
    def test_ringkasan(self):
        hasil = AnalisisFilm(self.film).ringkasan("Pengujian")
        self.assertIn("Jumlah film: 2", hasil)
        self.assertIn("Pengujian", hasil)

    # Memastikan film yang ditambahkan dapat dibaca kembali dari file.
    def test_tambah_dan_baca_file(self):
        # Membuat folder sementara agar pengujian tidak mengubah film.txt asli.
        with tempfile.TemporaryDirectory() as folder:
            nama_file = os.path.join(folder, "film.txt")
            koleksi = KoleksiFilm(nama_file)

            # Menambahkan satu film menggunakan fungsi pengelolaan file.
            koleksi.tambah_film(
                judul="Film Uji",
                genre="Drama",
                tahun=2024,
                rating=8.2,
            )

            # Membaca kembali data untuk memeriksa hasil penyimpanan.
            hasil = koleksi.baca_semua_film()
            self.assertEqual(len(hasil), 1)
            self.assertEqual(hasil[0]["judul"], "Film Uji")


# Menjalankan pengujian ketika file ini dieksekusi secara langsung.
if __name__ == "__main__":
    unittest.main()