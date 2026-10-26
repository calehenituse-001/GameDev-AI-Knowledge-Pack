# Mengusut Multiplayer Desync

**Empat gate status:** (1) transport connected, (2) protocol negotiated, (3) replication valid, (4) gameplay server-authoritative. Jangan mengklaim level 3 hanya karena level 1 berhasil.

| Gejala | Audit prioritas |
|---|---|
| Remote menempel kapal lokal | entity_id, owner_id, reference alias, remote scene parent, local vs global transform. |
| Remote tidak berputar | payload orientasi, yaw radian/derajat, quaternion, mesh axis, apply rotation. |
| Remote hilang di planet | posisi world, depth/z-index, visibility layer, camera angle, lalu snapshot. |
| Terlihat satu arah saja | initial snapshot, server broadcast, room filter, spawn map, permissions. |
| Posisi meloncat | stale tick, world_epoch, buffering, packet age, interpolation reset. |
| Tersambung tapi tidak bergerak | protocol/capability disabled, handshake tidak selesai, input tidak dikirim, server tidak simulasi. |
| Duplikat setelah reconnect | session cleanup, despawn, stable entity mapping, epoch baru. |

## Urutan diagnosis

1. Pastikan server benar-benar mengumumkan capability/versi yang ingin dipakai; jangan uji gerak jika fitur itu mati.
2. Dua client memakai input berbeda: A thrust kiri, B diam lalu berputar kanan.
3. Di server log: session, room, tick, entity ID, sender, input sequence, validated controls.
4. Di tiap client log: snapshot tick, remote entity ID, raw position + orientation.
5. Di renderer log: transform yang benar-benar diterapkan. Bandingkan dengan raw snapshot sebelum smoothing.
6. Baru kemudian nyalakan interpolation dan prediction secara bertahap.
7. Uji room change/warp, respawn, disconnect, latency dan packet reorder bila transport mengizinkan.

Status laporan: NOT TESTED, TRANSPORT PASS, PROTOCOL PASS, REPLICATION PASS, GAMEPLAY PASS. Keberhasilan kompilasi/aplikasi start tidak otomatis menaikkan status.
