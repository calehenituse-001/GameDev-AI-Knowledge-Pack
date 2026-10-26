# Godot 4.7 Multiplayer: Pilih Transport yang Tepat

## Jalur 1 — Godot high-level + Godot server

Gunakan MultiplayerSpawner untuk lifecycle instansi network dan MultiplayerSynchronizer untuk replikasi properti milik node authority. Buat server authoritative untuk physics, damage, ekonomi dan kontrol NPC. Dokumentasi dan contoh sederhana dapat memakai authority milik client untuk movement; jangan langsung mengadopsi pola tersebut jika ingin anti-cheat.

RPC membutuhkan NodePath yang sama di tiap peer, deklarasi @rpc yang kompatibel, dan authority yang benar. MultiplayerSynchronizer tidak mereplikasi nilai Object/Resource umum secara langsung.

## Jalur 2 — Godot + custom WebSocket JSON server

Gunakan WebSocketPeer, connect_to_url(wss_url), poll() di setiap frame, get_ready_state(), get_available_packet_count(), get_packet(), parsing JSON dan send_text(). Susun adapter NetworkClient, WorldReplicator, dan RemoteInterpolator. **MultiplayerSpawner/MultiplayerSynchronizer tidak otomatis membaca payload JSON custom dari server Node.js.**

Jangan mengirim input sebelum socket OPEN dan handshake/room ready. Tangani close reason, reconnect backoff, session/auth, pending buffer dan version mismatch. Pada Android, aktifkan INTERNET permission di export preset.

## Checklist 3D

- Posisi entity memakai Vector3/world-space, bukan screen-space.
- Rotasi full 3D memakai Basis/Quaternion konvensi yang konsisten.
- Remote mesh/node bukan child LocalShip atau CameraRig.
- Gunakan ID entitas stabil dan actor ownership yang tervalidasi.
- Bedakan simulasi server dan smoothing render.
- Test dua perangkat berbeda; jangan percaya hasil editor saja.

## CI (untuk repo proyek)

Import Godot pada fresh checkout sebelum test headless. Test runner SceneTree harus mengakhiri proses dengan exit status gagal jika ada tes gagal. Gunakan GitHub Actions untuk lint/schema/protocol tests; tes APK/VPhone/perangkat tetap terpisah.

Referensi: https://docs.godotengine.org/en/4.7/tutorials/networking/high_level_multiplayer.html dan https://docs.godotengine.org/en/4.7/classes/class_websocketpeer.html
