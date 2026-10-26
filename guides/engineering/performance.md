# Optimasi Performa

## Ukur sebelum mengubah
Catat FPS median dan low-percentile, CPU/GPU frame time, draw calls, penggunaan RAM, resolusi, versi build, dan perangkat.

## Temukan bottleneck
- CPU: AI, physics, script/tick, serialisasi, UI berlebihan.
- GPU: transparansi, pixel overdraw, shadow, shader, post-processing, fill rate.
- Memori: texture/audio terlalu besar, duplikasi, resource leak, loading spike.
- Jaringan: terlalu banyak state atau payload, update tidak relevan.

## Siklus perbaikan
Profiling → hipotesis → satu perubahan → build target → ukur ulang → regression test.

Android perlu pengujian lebih lama untuk thermal throttling, driver GPU, RAM, Vulkan/OpenGL ES, dan frame pacing. Jangan menurunkan kualitas secara membabi buta.
