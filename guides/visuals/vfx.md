# Visual Effects yang Terbaca dan Efisien

Pola: gameplay trigger → muzzle/arah yang benar → wind-up → efek utama → impact → afterglow/debris → cleanup.

## Pemeriksaan
- Efek beam/projectile berasal dari titik tembak yang benar, bukan offset layar.
- Hit impact sesuai collision point asli dan tetap sinkron dengan rotasi/gerak.
- Jangan mencampur damage hitbox dengan partikel render; damage tidak bergantung FPS.
- Hilangkan artefak kotak/quad dari blend mode, texture alpha, billboard, atau UV keliru.
- Siapkan tingkat kualitas partikel/lighting untuk perangkat lemah.

Uji pada zoom/jarak berbeda, occlusion, objek kecil, scene reload, dan beberapa efek bersamaan.
