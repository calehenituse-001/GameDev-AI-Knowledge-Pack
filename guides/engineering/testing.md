# Testing dan Validasi

## Tingkat test
- Static: format/skema, referensi aset, lint, kecocokan versi API.
- Unit: aturan ekonomi, damage, state, parser, algoritme deterministik.
- Integration: scene loading, gameplay flow, save/load, input.
- Device: crash, framerate, thermal, touch pada target nyata.
- Network: multi-user, latency, reconnect, authority.
- Regression: perilaku yang tidak boleh rusak setelah perubahan.

Test matrix harus sesuai target. Jangan menulis tanda lulus tanpa benar-benar melakukan tes.

## Laporan
Gunakan label Not tested, Reproduced, Failed, Passed, atau Fixed-not-tested secara jujur; sertakan langkah reproduksi dan bukti.
