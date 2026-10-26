# Alur Kerja Pengembangan Game

## 1. Definisikan tugas
Tuliskan pengalaman pemain yang diinginkan, platform target, engine/versi, dan batas fitur yang tidak boleh rusak.

## 2. Pilih lingkup teknis
Pisahkan input, data/state, simulasi, physics, rendering, audio, UI, save, networking. Tetapkan client/server ownership bila online.

## 3. Buat acceptance criteria
Contoh: tidak crash, berhasil di target device, save tetap kompatibel, perubahan tidak memengaruhi NPC, mudah rollback.

## 4. Bangun bertahap
Buat reproduksi atau prototipe kecil, ubah satu hal, ukur hasilnya, baru lanjut. Hindari menggabungkan fitur tidak terkait dalam satu perbaikan.

## 5. Verifikasi
Tes editor tidak sama dengan tes APK atau browser. Periksa log, profiler, input nyata, stabilitas, dan regression test.

## 6. Dokumentasikan
Gunakan templates/implementation-report.md di repositori proyek. Catat secara terpisah hal yang telah diuji dan hal yang belum terbukti.
