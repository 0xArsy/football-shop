=== TUGAS 4 ===

Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
= AuthenticationForm adalah form bawaan Django untuk proses login (username + password)
Kelebihannya: langsung aman (validasi, integrasi dengan sistem authenticate()), cepat dipakai tanpa bikin form manual, dan kompatibel dengan middleware Django
Kekurangannya: interface-nya dasar (harus costum kalau mau pakai email sebagai login), dan kalau butuh logika login kustom harus ditambah sendiri

Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
= Autentikasi itu soal memastikan siapa orangnya (misalnya login dengan akun). Otorisasi itu soal menentukan apa yang boleh dia lakukan setelah masuk (misalnya bisa edit data atau cuma lihat saja). Django sudah menyiapkan dua-duanya, jadi pengguna bisa login, lalu sistem juga tahu apa saja izin yang dia punya

Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
= Session lebih aman karena data utamanya disimpan di server, tapi butuh penyimpanan tambahan. Cookies lebih simpel dan bisa bertahan lebih lama, tapi ada risiko kalau tidak dijaga, misalnya bisa dibaca atau diubah orang lain

Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
= Tidak sepenuhnya aman. Ada risiko seperti dicuri atau dipakai orang lain kalau tidak hati-hati. Django sudah menambahkan perlindungan bawaan, misalnya token keamanan dan pengaturan khusus di cookies, tapi tetap harus kita atur dengan benar

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
= Pertama bikin app baru untuk autentikasi lalu tambahkan di settings
Lalu bikin halaman login, register, dan logout.
Tambahkan relasi antara produk dan pengguna supaya setiap produk jelas dibuat oleh siapa.
Bikin proteksi biar halaman utama hanya bisa diakses setelah login.
Tampilkan siapa yang membuat produk dan kapan terakhir login.
Terakhir, coba buat dua akun berbeda dan masing-masing isi dengan beberapa data produk.
<img width="576" height="546" alt="image" src="https://github.com/user-attachments/assets/f5c73b62-bf36-475d-88ed-758190d54dd2" />
<img width="613" height="535" alt="image" src="https://github.com/user-attachments/assets/aa57c9b1-b113-4be2-a153-3aa1af04dda9" />
<img width="345" height="846" alt="image" src="https://github.com/user-attachments/assets/58278930-7acd-4012-a242-edba33302f3c" />



 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
= Data delivery memungkinkan komunikasi antar backend > frontend > service). Tanpa format standar (XML/JSON), sulit bertukar data antar aplikasi/platform berbeda

 Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
 = JSON umumnya lebih ringkas, dan lebih efisien untuk web API. XML punya fitur lebih kuat, tapi lebih verbos sehingga JSON lebih populer untuk REST API modern
 
 Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
 = is_valid() memvalidasi input user sesuai aturan field dan mengisi cleaned_data. Diperlukan untuk mencegah data invalid masuk ke database
 
 Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
= csrf_token mencegah serangan CSRF (Cross-Site Request Forgery) dengan memastikan request POST berasal dari situs yang sama. Tanpa token, penyerang bisa mengelabui user yang sedang login untuk mengirim request berbahaya ke aplikasi kita
 
 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
= Membuat form main/forms.py > membuat views main/views.py > menambahkan urls main/urls.py > membuat/ubah templates > runserver > test via browser & postman > ambil screenshot > tambahkan ke README > git add/commit/push.
 
 Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
 = Tutorial sudah jelas untuk dasar, terima kasih

<img width="1336" height="900" alt="image" src="https://github.com/user-attachments/assets/24ea5971-81cf-4f3d-a59a-25c8373aba63" />
<img width="1350" height="932" alt="image" src="https://github.com/user-attachments/assets/bfab9084-ea44-4d6a-a6cb-3b58a1beff50" />
<img width="1337" height="885" alt="image" src="https://github.com/user-attachments/assets/020ebc4f-39a8-4df6-9f6c-8618dc8323af" />
<img width="1350" height="924" alt="image" src="https://github.com/user-attachments/assets/5cae3eda-0c02-4b86-9a65-5222cb6de138" />






















Z Arsy Alam Sin (2406495836)
Kelas : A

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
