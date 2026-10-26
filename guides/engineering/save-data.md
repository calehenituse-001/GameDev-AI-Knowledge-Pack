# Save, Data, dan Migrasi

- Simpan gameplay state yang diperlukan, bukan seluruh objek runtime.
- Gunakan schema_version dan fungsi migrasi untuk format lama.
- Gunakan atomic write atau temporary file bila filesystem mendukung.
- Sediakan mekanisme backup/recovery yang diuji.
- State ekonomi multiplayer yang authoritative disimpan dan divalidasi server, bukan dipercayakan pada client.

## Test matrix
New game → save → load; save lama → migrate → load; force-close saat write; file parsial/rusak; backup/restore; konflik cloud; save dari kombinasi versi yang berbeda.

Bedakan error yang bisa diperbaiki dan data yang memang tidak lagi kompatibel.
