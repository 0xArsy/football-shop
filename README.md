Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
= Saya membuat project Django, menambahkan app, lalu mendefinisikan model Product di models.py. Setelah itu menjalankan makemigrations dan migrate agar model tersimpan di database. Data diambil lewat views.py, dihubungkan dengan urls.py, lalu ditampilkan pada template HTML. Terakhir diuji dengan runserver dan dideploy ke PWS.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
= Client mengirim request ke urls.py, lalu diarahkan ke views.py. Jika butuh data, view memanggil models.py, kemudian hasilnya dikirim ke template HTML untuk dirender. Response HTML dikembalikan ke client. Jadi urls.py = rute, views.py = logika, models.py = data, HTML = tampilan

Jelaskan peran settings.py dalam proyek Django!
= settings.py adalah pusat konfigurasi. Semua pengaturan seperti database, daftar app, middleware, template, static file, dan keamanan dikelola di sini agar project bisa berjalan.

Bagaimana cara kerja migrasi database di Django?
= makemigrations membuat file migrasi sesuai perubahan model, lalu migrate mengeksekusinya di database. Django juga mencatat riwayat migrasi, jadi perubahan lebih aman dan terkontrol

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
= Django dipilih karena strukturnya rapi, fiturnya lengkap (ORM, auth, admin panel), dan berbasis Python yang mudah dipahami pemula. Cocok untuk belajar konsep web development

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
= Aman
