
"""Modul untuk memvalidasi data film."""


class ValidasiFilmError(Exception):
    # Membuat exception khusus untuk kesalahan validasi data film.
    pass


def buat_record_film(**kwargs):
    # Mengambil data film berdasarkan nama atribut yang dikirim.
    judul = kwargs.get("judul", "").strip()
    genre = kwargs.get("genre", "").strip()
    tahun = kwargs.get("tahun")
    rating = kwargs.get("rating")

    # Menolak data jika judul film kosong.
    if not judul:
        raise ValidasiFilmError("Judul film tidak boleh kosong.")

    # Menolak data jika genre film kosong.
    if not genre:
        raise ValidasiFilmError("Genre film tidak boleh kosong.")

    # Mengubah tahun dan rating menjadi tipe angka.
    # Jika konversi gagal, tampilkan exception validasi.
    try:
        tahun = int(tahun)
        rating = float(rating)
    except (TypeError, ValueError):
        raise ValidasiFilmError(
            "Tahun dan rating harus berupa angka."
        )

    # Memastikan tahun rilis berada pada rentang yang ditentukan.
    if not 1888 <= tahun <= 2100:
        raise ValidasiFilmError("Tahun film tidak valid.")

    # Memastikan rating berada di antara 0 sampai 10.
    if not 0 <= rating <= 10:
        raise ValidasiFilmError(
            "Rating harus antara 0 sampai 10."
        )

    # Memastikan judul dan genre tidak kosong setelah validasi.
    assert judul and genre

    # Mengembalikan data film dalam bentuk dictionary.
    return {
        "judul": judul,
        "genre": genre,
        "tahun": tahun,
        "rating": rating,
    }