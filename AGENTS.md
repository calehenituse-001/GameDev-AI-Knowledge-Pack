# Universal Game Development Agent Rules

Berlaku bagi coding agent yang diminta memakai panduan repositori ini.

## Sebelum mengubah sesuatu
1. Identifikasi engine + versi, platform, tugas, batasan, dan target pengujian.
2. Periksa file proyek, log, dan dokumentasi resmi; jangan menebak API atau path.
3. Pilih panduan relevan dari skills/router/SKILL.md.
4. Tuliskan kriteria lulus/gagal serta apa yang tidak boleh berubah.

## Ketika implementasi
- Pisahkan UI, state game, simulasi, persistence, rendering, dan networking.
- Isolasi perubahan kecil; jangan mengubah semua entitas jika hanya satu kelompok yang dituju.
- Untuk multiplayer, verifikasi aksi yang berpengaruh pada gameplay di server.
- Pertahankan kompatibilitas perangkat, engine, dan data save.
- Gunakan kode/aset pihak ketiga hanya dengan izin yang sesuai.

## Setelah implementasi
Laporkan: (a) perubahan sebenarnya, (b) alasan dan risiko, (c) tes yang dilakukan serta buktinya, (d) tes yang belum dilakukan, (e) rollback.

**Jangan pernah mengklaim telah mengakses, mengompilasi, menjalankan, atau menguji sesuatu yang belum dilakukan.**

Repositori ini berisi pengetahuan umum; file game, hasil build, dan laporan proyek tetap berada di repositori proyek masing-masing.
