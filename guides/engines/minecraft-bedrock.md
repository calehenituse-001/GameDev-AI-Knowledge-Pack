# Minecraft Bedrock Add-On — Panduan Universal

Bedrock bukan Java Edition. Periksa versi Minecraft, Script API dan manifest sebelum implementasi.

- Bedakan Behavior Pack dan Resource Pack beserta namespace/identifier, entity geometry, texture, animation controller, dan particle.
- Jangan mengasumsikan Forge/Fabric kompatibel.
- Target otomatis wajib mengecualikan owner/sekelompok teman sesuai aturan.
- Pastikan projectile origin, rotasi, hitbox, collision, dan efek visual memakai ruang koordinat yang benar.
- Visual projectile tidak sama dengan logic damage; validasi keduanya.

Validasi import, content log, schema JSON, spawn, animasi, hitbox, collision, particle/material, dan Android device.

Referensi: https://learn.microsoft.com/en-us/minecraft/creator/
