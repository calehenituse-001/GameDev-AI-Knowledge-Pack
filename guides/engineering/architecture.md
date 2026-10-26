# Arsitektur Game yang Bisa Dirawat

## Prinsip inti
- Pisahkan input, simulasi, presentasi, persistence, dan jaringan.
- Gunakan komposisi yang cocok dengan engine; hindari inheritance mendalam tanpa manfaat.
- Gunakan event/signal untuk mengurangi coupling.
- Jadikan angka balance sebagai konfigurasi yang tervalidasi.

## Kontrak tiap sistem
Catat data masuk/keluar, state yang dimiliki, lifecycle, error handling, dan dependensi.

## Review
- Apakah UI tanpa sengaja mengubah gameplay state?
- Apakah scene reload, pause/resume, dan reconnect aman?
- Apakah ada kepemilikan state ganda atau dependensi melingkar?
- Bagaimana migrasi data ketika format berubah?

Mulai dari solusi sederhana. Tambahkan abstraksi hanya ketika manfaatnya terbukti. Rekam trade-off dalam Architecture Decision Record (ADR).
