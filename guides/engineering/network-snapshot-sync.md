# Server Snapshot & Synchronization

## Entity state

Kirim state per entitas, bukan transform pemain lokal untuk semua objek. Field minimal: protocol_version, room_id, world_epoch, server_tick, entity_id, owner_id, position, orientation, velocity dan last_input_seq. Contoh state posisi 3D (x,y,z) memakai orientasi quaternion ternormalisasi; game 2D dapat memakai (x,y,yaw). Tetapkan satuan, sistem koordinat, dan konvensi rotasi secara eksplisit.

## Processing pipeline

1. Client membaca kontrol dan memberi input sequence.
2. Server memvalidasi input, kepemilikan entitas dan rate limit.
3. Server menjalankan fixed simulation tick dan menghasilkan snapshot resmi.
4. Client membangun entity map berdasarkan entity_id, bukan array index.
5. Objek remote mengambil snapshot miliknya dalam world-space, tidak diparent ke kamera atau player lokal.
6. Interpolasi posisi memakai dua server snapshots; 3D quaternion menggunakan slerp, 2D menggunakan shortest-angle interpolation.
7. Pada warp/reconnect ubah world_epoch dan kosongkan buffer usang.

## Prediction dan reconciliation

Awali pengujian tanpa client-side prediction agar validitas data dua player bisa diperiksa. Selanjutnya local player menyimpan input pending; ketika authoritative snapshot mengakui last_input_seq, rollback ke state server lalu replay input belum diakui. Koreksi kecil boleh diperlunak untuk tampilan, teleport/hard warp harus snap.

Angka awal **hipotesis yang harus diprofil**: server 30 tick/s, snapshot 10–20/s, interpolation buffer 100–150ms; bukan jaminan cocok untuk semua jaringan.

## Pemisahan visual

State authoritative, predicted local state dan remote render transforms harus berbeda. Bila sprite terlihat di belakang planet, bedakan occlusion normal dari kesalahan depth, Z-index, collision/visibility layer, parent transform, atau koordinat snapshot. Kamera boleh mengikuti local player, tetapi bukan sumber state gerakan remote.

## Tes

Dua client A/B bergerak/berputar secara independen. Bandingkan raw server position/orientation dan posisi/rotasi visual pada keduanya. Uji late join, drop connection, reconnect, warp, entity despawn dan snapshot lama.
