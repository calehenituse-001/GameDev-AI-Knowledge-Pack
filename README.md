# GameDev AI Knowledge Pack

**Perpustakaan panduan pengembangan game lintas proyek, engine, dan platform.**

Repositori ini hanya menyimpan panduan, checklist, template laporan, dan Agent Skills yang dapat dipakai ulang. Ini **bukan** repositori source code game, APK, ISO, aset, save, atau hasil build suatu proyek.

## Mulai dari sini
1. Baca [AGENTS.md](AGENTS.md) untuk aturan umum coding agent.
2. Baca [skills/router/SKILL.md](skills/router/SKILL.md) untuk memilih panduan yang tepat.
3. Ikuti [alur kerja](guides/00-start-here.md).
4. Pilih panduan menurut engine, platform, dan masalah teknis.
5. Simpan laporan pekerjaan aktual di repositori proyek masing-masing.

## Peta dokumentasi
| Topik | Lokasi |
|---|---|
| Arsitektur, debug, test, jaringan, performa, save, kamera | [Engineering](guides/engineering/) |
| Pipeline aset 2D/3D dan VFX | [Visuals](guides/visuals/) |
| Godot, Unity, Unreal, Minecraft Bedrock | [Engines](guides/engines/) |
| Android dan web | [Platforms](guides/platforms/) |
| Pendekatan porting dan kompatibilitas | [Porting](guides/porting/) |
| Laporan bug, implementasi, format skill baru | [Templates](templates/) |
| Referensi eksternal | [References](references/) |

## Prinsip
- **Universal:** tidak mencantumkan konfigurasi, asset, atau kode dari game tertentu.
- **Evidence first:** bedakan hipotesis, implementasi, build sukses, dan tes perangkat nyata.
- **Engine aware:** periksa versi engine dan API sebelum menulis instruksi.
- **Small changes:** perubahan seminimal mungkin, dengan pengujian dan rollback.
- **Security and legality:** hindari secrets; hormati lisensi dan hak cipta.

## Status & sumber
**Starter v0.1** — panduan awal, bukan mirror seluruh skill pihak ketiga. Salah satu sumber inspirasi adalah [Awesome GameDev Agent Skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills); lihat [catatan sumber](references/upstream-skills.md). Skill tidak otomatis terpasang di semua AI coding agent.

Belum ada lisensi eksplisit untuk materi asli repositori ini. Pemilik dapat memilih lisensi melalui commit terpisah setelah meninjau ketentuannya.
