# Web / Browser — Panduan Universal Game

Periksa dukungan engine untuk WebGL/WebGPU dan browser target.

- Browser tidak bisa menggunakan raw TCP/UDP sockets secara umum; gunakan transport web seperti WebSocket/WebRTC.
- Perhatikan autoplay audio, CORS, HTTPS, caching, IndexedDB/local storage, tab background, serta input touch.
- Kurangi ukuran unduhan awal; siapkan loading progresif bila tersedia.
- Uji web mobile, resize, reconnect, asset gagal dimuat, dan memori browser.

Jangan menganggap fitur jaringan desktop/native langsung tersedia pada HTML5 export.
