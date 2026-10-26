# Test Matrix untuk Sinkronisasi 2 Client

Sebelum uji, simpan engine/version, server version + feature flags, client versions, target platform, time, commit/build, transport dan room.

| Tes | Langkah | Lulus jika |
|---|---|---|
| Handshake | Connect A dan B, periksa capability acknowledgement | Versi cocok dan kedua client join zone sama. |
| Identity | Spawn A dan B di titik berbeda | Entity ID unik; A dan B tidak menyalin parent atau transform. |
| Movement | A bergerak kiri/maju, B berhenti | B melihat A bergerak; A melihat B diam. |
| Rotation | B putar penuh, A tidak berputar | A melihat rotasi B, orientasi tidak dibalik. |
| Simultaneous | A dan B bergerak arah berbeda | Dua entitas tetap independen tanpa remote-follow. |
| Late join | C menyusul join setelah A/B bergerak | Initial snapshot lengkap, tanpa duplikasi. |
| Ownership | A mencoba memberi input yang mengaku milik B | Server menolak tanpa mengubah state B. |
| Warp/room | A pindah zona lalu kembali | Stale snapshot zona lama diabaikan dan spawn/despawn benar. |
| Reconnect | Putus sementara lalu join kembali | Satu entitas aktif, sesi lama cleanup. |
| Jitter | Simulasikan delay bervariasi | Gerak remote cukup mulus tanpa klaim presisi berlebih. |
| Rendering | Lewati depan/belakang objek besar | Occlusion sesuai depth, bukan entity disappear permanen. |
| Persistence | Server menyimpan state lalu restore | State sesuai aturan, tidak bercampur dengan save lokal. |

**Catatan bukti:** log server+dua client, video masing-masing, RTT/jitter, packet/tick/sequence, dan hasil PASS/FAIL yang benar-benar diuji. Simpan data aktual di repositori proyek, bukan di knowledge-pack universal.

## Gate rilis

Tahap awal: dua-client position+rotation+entity identity PASS. Setelah itu prediction/reconciliation, combat authority, warp, save dan skala multi-user. Tanpa bukti perangkat dan server staging, tetap tandai NOT TESTED.
