# Sprite 2D dan Aset Raster yang Siap Dipakai Game

Panduan universal untuk kapal 2D, karakter, tiles, sprite sheet, HUD dan visual effects. Tujuan bukan sekadar gambar menarik, melainkan aset dengan dimensi, anchor dan animasi yang stabil dalam engine.

## Pipeline
1. Audit sprite asli, perspektif (atas/samping/isometrik), arah hadap, ukuran canvas, ukuran gambar nyata nontransparan, dan batasan resolusi.
2. Tetapkan style bible: silhouette, palet, outline, pencahayaan, material, detail density dan area kosong.
3. Buat satu sprite acuan, uji pada ukuran tampilan gameplay. Baru perluas ke satu keluarga aset.
4. Gunakan PNG dengan alpha nyata bila diperlukan; periksa fake checkerboard/background yang tidak transparan.
5. Normalisasi canvas dan **pivot/anchor** antar sprite/animation frame. Pastikan cropping tidak menggeser posisi dunia.
6. Untuk animasi: gunakan spritesheet dengan urutan frame, ukuran dan orientasi yang konsisten; preview bergerak untuk mendeteksi flicker.
7. Tetapkan texture filtering/mipmap/compression sesuai art style (pixel art biasanya nearest; sprite halus bisa linear sesuai target).
8. Buat collider berdasarkan gameplay dan bentuk; jangan otomatis menganggap kanvas 256x256 atau 512x512 sebagai ukuran collision.

## Gerak dan tampilan
- Sinkronkan arah visual sprite dengan convention dunia (misalnya depan sprite menghadap ke atas gambar); rotasi sprite dapat berbeda dari heading engine karena orientation offset.
- Jangan parenting sprite pemain lain ke kamera atau pemain lokal tanpa alasan yang tepat.
- Pisahkan sprite entity dengan shield/damage/thruster overlay; samakan anchor dan lifetime supaya tidak 'menempel' entitas lain.
- Periksa overdraw dan ukuran atlas pada target mobile.

## QA
- Preview berdampingan dengan referensi, cek alpha, bounding box, anchor, dan ketebalan detail pada ukuran layar asli.
- Uji frame animasi ketika bergerak dan berputar, zoom masuk/keluar, kondisi gelap/terang, occlusion dan depth/z-index.
- Render geometry dan collision dipisah: sprite dapat tersembunyi di belakang objek karena aturan layer/depth, bukan kesalahan network.
- Uji di Android dan pada target resolusi; keberhasilan gambar dibuka belum membuktikan seluruh sprite bekerja dalam gameplay.

## Sprite 2D untuk multiplayer
Tidak perlu mengirim file PNG pada setiap update posisi. Client memuat `asset_id` dari bundle/cache dengan versi dan checksum yang cocok. Snapshot memuat `entity_id`, posisi dunia, rotasi/heading, velocity, state animasi dan timestamp/tick. Overlay lokal/hit effect dikendalikan berdasarkan peristiwa dan otoritas server yang jelas.

## Referensi
- https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/main/skills/disciplines/create-game-assets/references/raster-pipeline.md
- https://docs.godotengine.org/en/4.7/classes/class_sprite2d.html
- https://docs.godotengine.org/en/4.7/classes/class_animatedsprite2d.html

**Status:** panduan, bukan paket PNG/sprite yang sudah dihasilkan atau teruji.
