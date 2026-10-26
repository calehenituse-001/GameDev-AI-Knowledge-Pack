---
name: gamedev-guide-router
description: Memilih panduan game development lintas engine/platform berdasarkan jenis tugas dan risiko; tidak mengimplementasi proyek secara otomatis.
---

# GameDev Guide Router

## Input
Tugas, engine + versi (jika tersedia), target platform, batasan perangkat dan cara verifikasi.

## Routing
| Tugas | Dokumen yang dibaca |
|---|---|
| Godot | guides/engines/godot.md |
| Unity | guides/engines/unity.md |
| Unreal | guides/engines/unreal.md |
| Minecraft Bedrock Add-On | guides/engines/minecraft-bedrock.md |
| Android | guides/platforms/android.md |
| Web / browser | guides/platforms/web.md |
| Multiplayer / PvP | guides/engineering/multiplayer.md |
| Movement / kamera / physics | guides/engineering/physics-camera.md |
| FPS / lag / memory | guides/engineering/performance.md |
| Save / migrasi data | guides/engineering/save-data.md |
| Crash / bug | guides/engineering/debugging.md dan guides/engineering/testing.md |
| Asset 2D/3D | guides/visuals/asset-pipeline.md |
| Particle / beam / ledakan | guides/visuals/vfx.md |
| Porting / recompilation | guides/porting/porting-methods.md |
| Desain arsitektur | guides/engineering/architecture.md |

## Alur
1. Baca AGENTS.md dan guides/00-start-here.md.
2. Baca paling banyak satu dokumen engine dan satu dokumen platform per konteks bila relevan.
3. Tambahkan panduan pekerjaan; baca debugging/testing bila melakukan validasi.
4. Verifikasi dokumentasi API aktual serta fakta proyek sebelum mengusulkan perubahan.
5. Hasilkan acceptance criteria, implementasi yang bisa diuji, dan laporan tes jujur.

Router ini tidak otomatis dijalankan oleh ChatGPT atau semua AI agent. Perlu dukungan membaca file skill, atau pemanggilan manual.
