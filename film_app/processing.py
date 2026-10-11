
"""Modul untuk mengolah dan menganalisis data koleksi film."""


class AnalisisFilm:
    # Menyimpan daftar film yang akan digunakan dalam proses analisis.
    def __init__(self, daftar_film):
        self.daftar_film = daftar_film

    # Mengurutkan film berdasarkan rating, dari tertinggi atau terendah.
    def urutkan_rating(self, menurun=True):
        return sorted(
            self.daftar_film,
            # Menggunakan lambda sebagai kunci pengurutan berdasarkan rating.
            key=lambda film: film["rating"],
            reverse=menurun,
        )

    # Mencari film berdasarkan genre tanpa membedakan huruf besar dan kecil.
    def cari_genre(self, genre):
        return [
            film
            for film in self.daftar_film
            if film["genre"].lower() == genre.lower()
        ]

    # Mengambil satu film dengan rating tertinggi.
    def film_terbaik(self):
        # Mengembalikan None jika daftar film masih kosong.
        if not self.daftar_film:
            return None

        # Memilih film dengan rating terbesar menggunakan lambda.
        return max(
            self.daftar_film,
            key=lambda film: film["rating"],
        )

    # Membuat ringkasan koleksi dan menerima catatan tambahan melalui *args.
    def ringkasan(self, *catatan):
        # Menghitung jumlah seluruh film dalam koleksi.
        jumlah = len(self.daftar_film)

        # Memberikan pesan khusus jika belum ada data film.
        if jumlah == 0:
            hasil = "Belum ada data film."
        else:
            # Menghitung rata-rata rating seluruh film.
            rata_rata = sum(
                film["rating"] for film in self.daftar_film
            ) / jumlah

            # Menyusun jumlah film dan rata-rata rating ke dalam laporan.
            hasil = (
                f"Jumlah film: {jumlah}\n"
                f"Rata-rata rating: {rata_rata:.2f}\n"
            )

            # Menambahkan informasi film dengan rating tertinggi.
            terbaik = self.film_terbaik()
            hasil += (
                f"Film terbaik: {terbaik['judul']} "
                f"({terbaik['rating']}/10)\n"
            )

        # Menambahkan setiap catatan jika pengguna memberikannya.
        if catatan:
            hasil += "Catatan:\n"
            for catatan_item in catatan:
                hasil += f"- {catatan_item}\n"

        # Mengembalikan ringkasan dalam bentuk teks.
        return hasil

    # Menghitung jumlah film untuk setiap genre.
    def hitung_per_genre(self):
        jumlah_genre = {}

        # Menghitung kemunculan setiap genre dalam daftar film.
        for film in self.daftar_film:
            genre = film["genre"]
            jumlah_genre[genre] = jumlah_genre.get(genre, 0) + 1

        # Mengembalikan jumlah film dalam setiap genre.
        return jumlah_genre