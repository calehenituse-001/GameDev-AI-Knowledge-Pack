# Multiplayer dan Server Authority

## Aturan
- Server menjadi sumber state tepercaya untuk damage, health, shield, ekonomi, inventory, cooldown, spawn, dan hasil simulasi yang sensitif.
- Client mengirim **intent/input**, bukan hasil mutlak.
- Validasi identitas, kepemilikan entitas, biaya, range, cooldown, dan sequence.
- Pisahkan prediksi visual client dari state resmi server.

## Replikasi
Gunakan simulation tick terukur, sequence/timestamp, relevancy filtering, interpolation, prediction dan reconciliation sesuai genre. Tentukan aturan reconnect, timeout, desync, respawn, serta snapshot awal saat join.

## Pengujian
Dua client dengan input berbeda; uji latency, packet loss, reconnect, pergantian area, aksi bersamaan, dan perubahan state yang tidak berhak.

## Transport
Native dapat memakai ENet/UDP bila cocok. Browser tidak menyediakan raw UDP; evaluasi WebSocket dan WebRTC sesuai dukungan engine serta hosting.

Jangan mengandalkan anti-cheat yang hanya berjalan pada client. Log audit tanpa membocorkan rahasia atau data pribadi.

## Pendalaman masalah sinkronisasi

Lihat [pemilihan arsitektur](networking-architecture-decisions.md), [snapshot & interpolation](network-snapshot-sync.md), [diagnosis desync](network-sync-debugging.md), dan [tes dua client](network-acceptance-tests.md). Untuk Godot, lihat [panduan Godot 4.7](../engines/godot-multiplayer-practical.md). Dua implementasi berbeda dapat memakai protokol serupa tetapi tidak harus berbagi rules world/physics yang sama.
