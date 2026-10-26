# Model 3D yang Benar-Benar Siap Dipakai Game

Panduan universal lintas proyek untuk model ruang angkasa, karakter, properti, bangunan dan senjata. **Render/foto yang tampak 3D bukan file model 3D**. Hasil utama berupa mesh 3D dengan struktur yang bisa dibaca game engine.

## Tahap produksi
1. Audit referensi: identitas desain, bentuk dan ukuran relatif, fungsi gameplay, target hardware.
2. Tetapkan pandangan orthographic: atas, depan, belakang, kiri, kanan; gunakan skala yang konsisten. Perspective view hanya tambahan untuk evaluasi.
3. Buat *blockout* dengan silhouette yang benar; jangan menambah detail sebelum bentuk disetujui.
4. Buat mesh yang wajar: simetri bagian yang memang harus simetris, normals, topology, UV dan material PBR.
5. Pisahkan komponen yang bergerak: pintu hanggar, turret yaw/pitch, nozzle, roda, panel, dan sebagainya.
6. Siapkan transform origin dan hierarki marker: forward axis, up axis, pivot animasi, muzzle, thrusters, docking dan collision.
7. Ekspor model ke format runtime, umumnya **glTF/GLB 2.0** jika engine mendukung. Simpan file editable (misalnya .blend) terpisah.
8. Impor ke engine target, uji animasi, scale, collider, shading dan performa pada perangkat sebenarnya.

## Kontrak 3D minimal
- Satu sistem koordinat dan unit dunia yang disepakati; nyatakan orientasi depan/belakang secara eksplisit.
- Nama node stabil untuk attachment, senjata, hanggar, collision, dan animasi.
- Proporsi antar kelas objek tidak dipaksakan sama; kamera dinilai terpisah dari world scale.
- Render mesh **bukan** collider wajib: buat collision proxy sederhana dengan toleransi yang wajar.
- Detail mesh, draw calls, jumlah material, ukuran tekstur, LOD dan instancing disesuaikan dengan target perangkat.
- Jangan memasang dekorasi senjata secara permanen pada model dasar bila senjata harus bisa diganti di gameplay.
- Untuk fitur yang harus bergerak, pastikan komponen merupakan geometri terpisah dengan pivot yang sesuai.

## QA wajib sebelum disebut selesai
- Bandingkan hasil **top/front/rear/side** terhadap referensi; depan dan belakang tidak boleh identik secara keliru.
- Periksa silhouette, lubang, clipping, overlapping faces, UV, normals dan ukuran bounding box.
- Periksa posisi muzzle, engine exhaust, hanggar dan collision proxy pada pose netral.
- Putar kamera 360° dan jalankan animasi di engine, bukan hanya melihat preview satu sudut.
- Bandingkan FPS, memori, dan penampilan pada target Android/mobile jika itu tujuan distribusi.

## Model 3D untuk multiplayer
Asset model disimpan/dimuat pada client sesuai manifest dan versi konten. Saat simulasi, **jangan kirim GLB setiap frame**; kirim identitas entitas/model + transform, velocity dan state animasi yang relevan. Network node milik setiap entitas harus berdiri sendiri, tidak menggunakan transform kamera/player lokal.

## Referensi teknis
- https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/main/skills/disciplines/create-game-assets/SKILL.md
- https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/main/skills/disciplines/create-game-assets/references/three-d-pipeline.md
- https://registry.khronos.org/glTF/
- https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/index.html

**Status:** panduan dan checklist; tidak menciptakan atau menguji model 3D secara otomatis.
