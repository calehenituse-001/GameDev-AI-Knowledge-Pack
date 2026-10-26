# Input, Movement, Physics, dan Camera

Pisahkan: input intent → perhitungan kecepatan/rotasi → physics → posisi state → animasi dan kamera.

## Movement
- Gunakan delta time pada callback engine yang tepat.
- Atur acceleration, inertia, drag, deceleration, reverse, speed cap, dan angular speed secara eksplisit.
- Periksa collision layer/mask serta swept collision untuk projectile cepat.
- Uji joystick/touch, diagonal input, drift, pause/resume, dan variasi FPS.

## Kamera
Tegaskan world-space vs screen-space. Tetapkan smoothing, look-ahead, clamp, dan zoom. Render interpolation tidak boleh mengubah state simulasi server.

## Multiplayer
Remote entity memakai state replikasi miliknya sendiri; jangan tanpa sengaja melakukan parenting ke transform pemain lokal.
