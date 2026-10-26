---
name: network-synchronization
description: Diagnosis dan perancangan multiplayer server-authoritative lintas Godot, Android dan browser termasuk entity ID, snapshot, rotation, interpolation, dan reconnect.
---

# Network Synchronization

## Kapan digunakan
- Kapal pemain lain mengikuti posisi player lokal atau tidak berputar.
- Koneksi berhasil tetapi posisi, yaw atau world state tidak tersinkron.
- Multiplayer Android/Godot/browser memakai server custom.
- Perlu server-authoritative authority dan recovery dari desync.

## Bacaan
Path berikut relatif terhadap root repo:
1. guides/engineering/networking-architecture-decisions.md
2. guides/engineering/network-snapshot-sync.md
3. guides/engineering/network-sync-debugging.md
4. guides/engineering/network-acceptance-tests.md
5. guides/engines/godot-multiplayer-practical.md bila memakai Godot.

## Langkah
1. Identifikasi transport server/client serta protocol/capability yang telah dinegosiasikan.
2. Pastikan server menerima input dan mengeluarkan snapshot per entity ID.
3. Uji dua client dengan prediksi/interpolasi dimatikan dahulu.
4. Audit pengikatan objek remote, world-space transform, position dan full rotation.
5. Baru tambahkan interpolation/prediction/reconciliation, kemudian combat/warp/save.
6. Laporkan hasil sebenarnya per gate; jangan menyamakan connected dengan synchronized.

## Larangan
Jangan memperlakukan client-reported damage/position sebagai state resmi. Jangan menganggap RPC Godot otomatis interoperabel dengan JSON WSS. Jangan menyimpan code/asset proyek tertentu dalam repositori panduan.
