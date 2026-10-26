# Arsitektur Sinkronisasi Multiplayer (Lintas Engine)

## Dua pendekatan yang berbeda

**Godot high-level:** ENetMultiplayerPeer, RPC, MultiplayerSpawner dan MultiplayerSynchronizer digunakan jika server dan client menjalankan protokol Godot yang kompatibel. Server Node.js biasa dengan JSON WebSocket tidak memahami RPC Godot secara otomatis.

**Custom WSS protocol:** server WebSocket dapat melayani client Android, browser, dan Godot melalui adapter masing-masing. Gunakan WebSocketPeer di Godot untuk membaca dan menulis pesan, lalu implementasikan mapping entitas, snapshot dan interpolasi sendiri.

Render web service dapat menerima WSS; port publik HTTP dan WebSocket sama. ENet berbasis UDP bukan pengganti WSS pada alamat layanan tersebut.

## Alur otoritas

Client mengirim input intent dan sequence; server memvalidasi identitas dan gerakan lalu mengubah state. Server mengirim snapshot per entitas yang memiliki entity_id, owner_id, world/room ID, tick, position, rotation dan velocity. Damage, health, ekonomi serta aksi warp tidak boleh dipercayakan kepada client.

Gunakan capability negotiation dan versi protokol. Koneksi socket yang sukses tidak membuktikan fitur sinkronisasi telah aktif. Server produksi tetap stabil sampai staging lulus tes dua client.

## Catatan

Sharing transport protocol tidak sama dengan sharing game simulation. Game 2D dan 3D dapat berbagi format dasar tetapi membutuhkan adapter posisi/orientasi dan aturan room/simulasi terpisah.

## Referensi

- https://docs.godotengine.org/en/4.7/tutorials/networking/high_level_multiplayer.html
- https://docs.godotengine.org/en/4.7/classes/class_multiplayersynchronizer.html
- https://docs.godotengine.org/en/4.7/classes/class_multiplayerspawner.html
- https://docs.godotengine.org/en/4.7/classes/class_websocketpeer.html
- https://render.com/docs/websocket
- https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/main/skills/godot/godot-multiplayer/SKILL.md
