# Debugging Berbasis Bukti

1. **Reproduce:** versi build, device, kondisi awal, langkah pasti, dan frekuensi bug.
2. **Observe:** log, callstack, perubahan state, rekaman, serta waktu kejadian.
3. **Isolate:** matikan/aktifkan satu komponen untuk membatasi sumber.
4. **Hypothesize:** dugaan yang bisa dibantah dengan satu tes.
5. **Fix:** perbaikan terkecil yang menangani penyebab.
6. **Verify:** jalankan lagi skenario gagal dan regression test.

Prioritaskan crash, korupsi data, pelanggaran authority, soft-lock, lalu gangguan gameplay/visual/performa.

Anti-pola: mengubah banyak komponen sekaligus, menyebut build berhasil sebagai gameplay berhasil, menutupi error dengan workaround, atau mematikan validasi keamanan.

Catat temuan menggunakan templates/bug-report.md.
