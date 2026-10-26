# Unity — Panduan Universal

Periksa versi editor, render pipeline (Built-in/URP/HDRP), paket, dan target platform.

- Pisahkan MonoBehaviour yang menangani scene dari domain logic bila perlu.
- Gunakan ScriptableObject untuk konfigurasi data sesuai kasus.
- Periksa urutan Awake/OnEnable/Start/Update/FixedUpdate; hindari state ganda.
- Uji migrasi prefab/scene bila mengubah serialisasi.
- Untuk mobile periksa Canvas rebuild, touch input, safe area, kompresi aset, dan lifecycle.

Validasi dengan player build target, Console, Profiler, serta import settings dan native plugins.

Referensi: https://docs.unity3d.com/
