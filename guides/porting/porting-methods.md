# Porting Game: Metode dan Verifikasi

Jangan menyamakan screenshot, launcher APK, atau executable yang terbuka dengan native port yang selesai.

## Metode
- **Source port:** membangun ulang source tersedia secara sah untuk platform target.
- **Static/dynamic recompilation:** mengubah representasi executable, dengan tantangan ABI, OS, dependency, dan GPU API.
- **Compatibility layer:** menerjemahkan API seperti Wine serta instruction translation bila diperlukan.
- **Emulasi:** menjalankan lingkungan mesin/platform asal.
- **Reimplementation:** menulis kembali gameplay/sistem dengan engine lain.

## Audit yang perlu dicatat
Binary architecture, native libraries, dependency runtime, renderer, data format, input, audio, persistence, dan area gameplay yang benar-benar teruji.

## Tahapan
Legal/access review → audit dependency → proof-of-concept → input/audio/render → save → performa → packaging → device test.

Pastikan izin atas source code, aset, executable, SDK, merek, dan distribusi ulang.
