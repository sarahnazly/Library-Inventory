# Penjelasan Tugas PBP

## Tugas 2

Link App Adaptable :  https://sarah-library.adaptable.app

### Langkah Pembuatan Project Library Inventories

- Melakukan aktivasi Virtual Environment
: Hal ini dilakukan untuk mengisolasi **package** serta *dependencies* dari aplikasi sehingga tidak terjadi tabrakan dengan versi lain yang terdapat dalam komputer.

- Membuat Proyek Django Baru
: Untuk mengawali pembuatan project, saya melakukan instalasi *dependecies* dengan melakukan perintah `pip install -r requirements.txt` dan kemudian membuat proyek Django dengan nama library_inventory dengan perintah `django-admin startproject library_inventory`

- Konfigurasi Proyek dan Menjalankan Server
: Pada bagian ini saya mengizinkan akses aplikasi web dengan menambahkan "*" pada `ALLOWED_HOST` di `settings.py` dalam direktori proyek library_inventory. Kemudian untuk memastikan direktori aktif saya melakukan pemeriksaan dengan menjalankan perintah `python manage.py runserver`

- Membuat Aplikasi Main
: Setelah memiliki proyek Django, saya membuat aplikasi `main` dalam direktori proyek library_inventory. Aplikasi ini merupakan unit dari proyek Django yang mengatur fungsi-fungsi khusus dalam proyek yang sedang dibuat. Pembuatan aplikasi main dilakukan dengan perintah `python manage.py startapp main`  

- Melakukan Routing
: Langkah ini dilakukan untuk mengarahkan URL ke aplikasi main yang telah dbuat. Hal ini dilakukan dengan menambahkan routing ke file `urls.py` yang ada pada direktori proyek library_inventory dengan menambahkan `path('', include('main.urls'))`. Dengan begitu semua permintaan ke URL utama akan diteruskan ke main untuk diproses.

- Membuat Model Item
: Untuk mendefinisikan struktur data pada proyek ini, saya membuat model Item dalam file `models.py` yang terdapat dalam aplikasi main untuk mendefinisikan atribut, seperti name, amount, description, category, dan tanggal peminjaman.

- Membuat Fungsi Views.py
: Untuk mengatur logika dari proyek aplikasi ini, maka saya membuat fungsi items dalam file `views.py` yang terdapat dalam aplikasi main. Fungsi ini akan mengambil data dari model Item dan melakukan render ke dalam template HTML.

- Membuat Routing pada Fungsi
: Saya melakukan pendefinisian routing untuk fungsi yang telah dibuat di file `views.py` dalam file `urls.py`. Routing ini akan menentukan bagaimana HTTP akan mencapai fungsi yang tepat di aplikasi main ketika URL tertentu diakses.

- Implementasi Template HTML
: Saya membuat template HTML pada direktori baru di dalam aplikasi main. Template ini akan digunakan untuk mengatur tampilan halaman web yang akan diberikan kepada pengguna. Data yang diperoleh program dari `views.py` akan dimasukkan ke dalam template ini.

- Testing Django
: Saya melakukan test dari proyek ini dengan membuat unit test dan membuat TestCase dengan menggunakan models dari proyek library_inventory. Hal ini dilakukan untuk melakukan pengujian terhadap atribut yang terdapat dalam proyek.

- Add, Push, dan Commit ke dalam Repositori GitHub
: Setelah proses testing berhasil maka saya melakukan proses pengunggahan proyek ke repository Library-Inventory pada GitHub. Sebelum melakukan pengunggahan, saya membuat sebuah file `.gitignore` yang digunakan untuk menentukan berkas dan direktori yang harus diabaikan ole Git. Setelah itu barulah dilakukan add, commit, dan push ke repositori GitHub.

- Deployment ke Adaptable
: Setelah mengembangkan aplikasi secara lokal, maka saya melakukan deployment ke server atau platform hosting yang dapat diakses secara online dan memungkinkan untuk diakses oleh orang lain melalui internet.

- Membuat README.md
: Setelah semuanya selesai, saya membuat file `README.md` ini yang berisikan link dari aplikasi pada Adaptable dan menjawab pertanyaan seputar proyek aplikasi ini. Kemudian setelah selesai maka kembali melakukan add, commit, dan push ke repositori GitHub.

- Melakukan *deactivate* pada Virtual Environment
: Setelah selesai saya melakukan *deactivate* pada virtual environment karena telah selesai digunakan.

### Bagan *request client* ke web aplikasi Django dan kaitannya antara urls.py, views.py, models.py, dan berkas HTML

: Bagan 

        **Client's Web Browser**
                    ^
                    |
                    v
        **Django Web Application**
                    ^
                    |
                    v
                    |
    **urls.py** <---+--------->  **views.py**
                    |                 |
                    v                 v
                **models.py**   **items.html**
                    |
                    v
                **database**

: **Client Web Browser** sebuah *request* dimulai dari web browser pengguna atau *client* ketika mereka memasukkan URL atau mengklik link. Kemudian permintaan tersebut akan diterima oleh aplikasi **web yang berbasis Django** dan diproses serta mengirimkan respon kembali ke *client*. File `urls.py` bertanggung jawab untuk menentukan bagaimana permintaan URL ini akan diarahkan dan menghubungkan URL yang diterima dari *client* dengan fungsi tindakan yag disesuaikan pada `views.py`. Ketika permintaan URL diteruskan oleh `urls.py`, `views.py` mengambil alih untuk memproses permintaan tersebut. `views.py` dapat mengakses model untuk memproses data dan merender `items.html` atau mengembalikan respins JSON, tergantung pada kasus penggunaan. `models.py` akan menggambarkan struktur data dalam aplikasi dan memberikan definisi model yang digunakan untuk berinteraksi dengan database atau data lainnya. `models.py` dapat digunakan oleh `views.py` untuk mengambil atau penyimpan data. `items.html` digunakan untuk mengatur tampila yang akan diberikan kepada pengguna atau *client*. `views.py` dapat merender `items.html` dengan data yang diambil dari model dan kemudian mengirimkannya kembali ke *client* sebagai respons HTML yang siap ditampilkan.

### Alasan Menggunakan Virtual Environment dan Apa yang Terjadi Apabila Tidak Menggunakan Virtual Environment
: Virtual environment digunakan untuk mengisolasi lingkungan dari pengembangan python dan hal ini akan memungkinkan penggunaan *package* dan dependensi proyek yang spesifik. Dengan digunakannya virtual environment, maka hal tersebut dapat membantu dalam mencegah konflik antar proyek dan menjaga kestabilan dari proyek. Selain itu kita dapat melakukan pengelolaan versi python dan *package* yang berbeda untuk setiap proyek dan terhindar dari masalah kompabilitas.
Kita tetap dapat membuat aplikasi Django tanpa virtual environment, namun hal tersebut tidak disarankan karena memungkinkan terjadinya konflik antar *package*, kesulitan pengelolaan berbagai versi python, dan juga adanya kesulitan dalam mengisolasi dependensi proyek yang berbeda.

### MVC, MVT, MVVM, dan Perbedaannya

- MVC 
: *Model View Controller* adalah suatu model yang komponennya terbagi menjadi 3, yaitu Model, View, dan Controller. Komponen `model` berisikan logika dan status data yang terdapat dalam aplikasi. Komponen ini bertugas untuk mendapatkan dan memanipulasi data, berinteraksi dengan controller, berinteraksi dengan database, dan memperbarui tampilan dari aplikasi yang dikembangkan. Komponen `view` berhubungan dengan *interface* pengguna yang terdiri dari HTML/CSS.XML. View bekerjasama dengan controller untuk menciptakan tampilan yang dinamis. Komponen `controller` merupakan suatu komunikator antara view dan model.

- MVT
: *Model View Template* adalah suatu model yang komponennya terbagi menjadi 3, yaitu Model, View, dan Template. Komponen `model` berfungsi untuk mengelola data dan logika dari aplikasi. Komponen `template` merupakan komponen yang berhubungan dengan *interface* pengguna. Komponen ini bekerjasama dengan `view` yang merupakan komponen komunikator dari model dan template untuk menciptakan tampilan yang dinamis.

- MVVM
: *Model View ViewModel* merupakan suatu model yang komponennya terbagi menjadi 3, yaitu Model, View, dan ViewModel. Komponen `model` berfungsi untuk mengelola data yang digunakan untuk menjalankan suatu aplikasi. Komponen `view` berfungsi sebagai *interface* grafis antara pengguna dengan pola desain. Komponen ini juga berfungsi untuk menampilkan output dari data yang telah diproses. Komponen `ViewModel` di salah satu sisi merupakan abstraksi dari komponen `view`, namun di sisi yang lain komponen ini berfungsi sebagai penyedia pembungkus data model untuk ditautkan.

- Perbedaan
- MVP dengan MVT
: MVT merupakan varian dari MVC yang digunakan dalam kerangka kerja Django. Pada MVT komponen `view` berperan seperti `controller` dalam MVC, sementara komponen `template` berperan seperti `view` dalam MVC.
- MVVM dengan MVC/MVT
: MVVM lebih umum untuk digunakan dalam pengembangan aplikasi berbasis kerangka kerja JavaScript, sementara MVC/MVT biasanya terkait dengan pengembangan server-side seperti Django. Kemudian MVVM juga dirancang untuk lebih memisahkan logika tampilan dari komponen `model` jika dibandingkan dengan MVC/MVT.

### Referensi :
- https://pythonistaplanet.com/difference-between-mvc-and-mvt/#google_vignette
- https://agus-hermanto.com/blog/detail/mvc-vs-mvp-vs-mvvm-apa-perbedaannya-mana-yang-terbaik-diantara-ketiganya-a
- https://pbp-fasilkom-ui.github.io/ganjil-2024/
- https://www.petanikode.com/python-virtualenv/

## Tugas 3

### Perbedaan POST dan GET dalam Django
