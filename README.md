# PBP

## GameSthar
### Nama : Shaquille Athar Adista
### NPM  : 2206081875
### Link Adaptable : https://gamesthar.adaptable.app/main (Got Disabled :< )
---
## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 

<p>as<p>

---
## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. 

<p>as<p>

---
## 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

<p>Kita menggunakan virtual environment agar kita dapat memisahkan ruang kerja kita, jadinya kita dapat menggunakan versi python atau depedensi yang berbeda-beda antar virtual environment, dengan menggunakan virtual environment kita juga dapat menjaga kebersihan sistem kita, kita dapat menghindari potensi adanya masalah konflik depedensi dan kita juga dapat menciptakan proyek-proyek yang bersih dan terorganisir. Namun, kita juga tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual env, tetapi hal ini dapat mengakibatkan lingkungan kerja kita menjadi tidak terstruktur dan mungkin saja akan terdapat kesalahan dikarenakan perbedaan versi python atau dependensi di project-project kita.<p>

---
## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.   

### MVC (Model View Controller) 

MVC adalah sebuah cara dalam membuat aplikasi atau website dengan memisahkan masing-masing bagiannya, yaitu database dalam model, tampilan dalam view, dan perintah-perintah yang memiliki fungsi dalam menghubungkan view dan model di controller. 
  - Model, merupakan komponen pertama dari MVC adalah model yang berfungsi untuk menyiapkan, mengorganisasikan, bahkan memanipulasikan data pada database.
  - View, merupakan bagian yang menampilkan desain tampilan dan juga informasi(data) kepada user atau pengguna (end user)
  - Controller, merupakan bagian yang menghubungkan model dan view pada setiap proses dan request dari user.  

  Dengan konsep model view controller, website sendiri terdiri dari masing-masing bagian yang terpisah sehingga, memudahkan dalam mengembangkan dan pengerjaan. Proses pengerjaan aplikasi atau 
  website pun dapat dilakukan dengan cepat karena tim developer dapat lebih fokus ke salah satu bagiannya saja dari model, view, dan controller. Konsep MVC ini sudah diterapkan di berbagai framework PHP, Laravel, CodeIgniter, YII, Symfony, Yii, dan Zend.  

### MVT (Model View Template) 

MVT adalah sebuah pola desain arsitektur website yang terbagi menjadi tiga lapisan, yakni model, view, dan template. Konsep ini diyakini bisa mempercepat proses   pembuatan website. Dengan konsep MVT ini, developer dapat mengorganisasi memisahkan dan komponen-komponen utama dalam aplikasi web. Beikut adalah penjelasan masing-masing bagian.
   - Model, merupakan bagian yang merepresentasi data dari aplikasi yang dibuat. Model adalah bagian yang berinteraksi dengan database dan mengelola data aplikasi. Model mendefinisikan       
      struktur dan hubungan data. 
   - View, bertanggung jawab untuk menangani logika bisnis dan tampilan dalam aplikasi. View berguna untuk mengtroller bagaimana data yang dikelola oleh model akan ditampilkan kepada 
      pengguna. Dalam MVT, view berperan sebagai pengatur tampilan dan mengambil data dari model untuk disajikan kepada pengguna. Dalam Django view dapat berupa fungsi atau kelas.
   - Template, komponen yang digunakan untuk merancang tampilan atau antarmuka pengguna. Template memisahkan tampilan (kode HTML) dengan logika aplikasi. Dalam MVT, template digunakan untuk  
      merancang tampilan yang akhirnya akan diisi dengan data dari model melalui view. 
    
### MVVM (Model View ViewModul) 

MVVM adalah pola desain software yang membagi kode aplikasi ke dalam tiga lapisan, yaitu modul, view, dan viewmodul. Tujuan penggunaan MVVM sendiri adalah menjaga  kode UI agar tetap sederhana dan tanpa mengandung app logic agar mudah untuk dikelola.
   - Model merupakan tempat untuk logika bisnis dan data aplikasi, yang didapatkan dari viewmodel setelah menerima input pengguna melalui view. 
   - View bertanggung jawab menentukan struktur, tata letak, teks, gambar, dan elemen antarmuka lainnya yang nantinya dilihat oleh pengguna. Seluruh elemen tersebut ditulis dalam bahasa XML  
     dengan kode yang terbatas. Tujuan dari view adalah menginformasikan viewmodel apa yang dilakukan oleh pengguna. Layer ini tidak mengandung logika aplikasi apapun. Namun dalam beberapa kasus, view bisa berisi logika UI yang mengimplementasikan perilaku visual yang sulit diekspresikan dalam XML, seperti animasi.
   - ViewModel adalah layer yang berinteraksi langsung dengan Model, serta menyajikan data untuk View layer. Layer viewmodel berada di antara layer view dan model, dan berfungsi sebagai   
     penghubung keduanya. Viewmodel mendapatkan input dari view mengenai aktivitas pengguna, dan melakukan data binding 2 arah (2-way data binding). Data binding adalah proses mengikat dua  data sumber bersama dan menyinkronkan keduanya. Perubahan pada elemen dalam kumpulan data secara otomatis diperbarui dalam kumpulan data terikat, dan menentukan fungsi UI. Setelah mendapatkan data, viewmodel meneruskannya ke layer model untuk dimanipulasi dan disimpan. Perubahan status yang terjadi selama proses tersebut akan diumumkan melalui notifikasi perubahan.

**Perbedaan MVC, MVT, dan MVVM**
- MVC menggunakan Controller sebagai penghubung antara Model dan View. MVT menggunakan view untuk menerima http request dan mengembalikan HTTP request yang telah diterima (menghubungkan  
      model dan template). MVVM menggunakan ViewModel sebagai penghubung anatara Model dan View melalui binding
- MVC menggunakan View untuk menampilkan desain dan data kepada user. MVT menggunakan Template untuk menampilkan desain dan data kepada user. MVVM menggunakan view untuk menampilkan  
      tampilan yang dilihat user 
- MVC cocok digunakan pada aplikasi dengan kompleksitas yang tinggi dan interaksi pengguna yang rumit. MVT cocok digunakan untuk aplikasi kecil dan besar. MVVM cocok digunakan untuk  
      aplikasi dengan tampilan yang kompleks dan dipengaruhi oleh banyak perubahan data.
- MVC modifikasi dapat sulit tergantung pada bagaimana aplikasi dirancang. MVT modifikasi umumnya dianggap mudah karena pemisahan yang kuat antara Model, View, dan Template. MVVM modifikasi 
      dapat lebih mudah jika pengikatan data (data binding) diatur dengan baik.
- MVC hubungan erat (sangat berpasangan) antara Model, View, dan Controller. MVT hubungan yang lebih longar antara Model, View, dan Template. MVVM hubungan yang kuat antara View dan 
      ViewModel.
- MVC digunakan oleh Java, Spring. MVT digunakan oleh Django. MVVM digunakan oleh Microsoft APF, Angular JS
    
