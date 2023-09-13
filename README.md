# PBP

## GameSthar
### Nama : Shaquille Athar Adista
### NPM  : 2206081875
### Link Adaptable : https://gamesthar.adaptable.app/main (Got Disabled :< )
---
## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 

**Membuat sebuah proyek Django baru**

+ Buat direktori baru dengan nama `game_sthar`.
+ Terus, saya membuat _virtual environment_ dengan menjalankan perintah .

  ```
  python -m venv env
  ```
+ _virtual environment_ yang telah saya buat tadi berfungsi agar lingkungan kerja kita terisolasi sehingga __package__ serta __dependencies__ tidak akan bertabrakana dengan versi lain yang ada di komputer saya. Cara mengaktifkan __virtual environment__ adalah dengan menjalankan perintah.

  ```
  env\Scripts\activate.bat
  ```

Saya menggunakan perintah tersebut, karena saya menjalankannya di windows.

+ Selanjutnya saya membuat file `requirements.txt` di directory tadi, dan saya menambahkan beberapa __dependecies__ di dalamnya. Tujuannya adalah agar saya dapat menginstall __dependecies__ yang saya butuhkan di project ini.

  ```
  django
  gunicorn 
  whitenoise
  psycopg2-binary
  requests
  urllib3
  ```

+ Setelah itu, saya menjalankan perintah berikut untuk menginstall semua __dependecies__ yang ada di `requirements.txt`. Saya menginstall __dependecies__ ini di __virtual env__ yang telah saya buat tadi.

  ```
  pip install -r requirements.txt

  ```

+ Kemudian saya membuat project django yang bernama `game_sthar` dengan perintah berikut.

  ```
  django-admin startproject game_sthar .

  ```

+ Setelah terbentuk folder `game_sthar`, kemudian saya mencari file `settings.py` dan menambahkan `*` pada `ALLOWED_HOSTS`. Ini bertujuan agar kita mengizinkan akses dari semua host, yang akan membuat aplikasi dapat diakses secara luas.

+ Kemudian, saya menginisiasi direktori `game_sthar` sebagai repo github dengan cara `git init`.

+ Lalu, saya menambahkan `.gitignore` di dalam direktori tadi.


**Membuat aplikasi dengan nama `main` pada proyek tersebut**

+ Di proyek game sthar saya membuat aplikasi baru bernama `main` dengan cara menjalankan perintah berikut.
  ```
  python manage.py startapp main
  ```

+ Kemudian saya akan menambahkan aplikasi `main` ke dalam proyek game sthar dengan cara membuat berkas `setting.py` yang ada di dalam direktori `game_sthar`, kemudian pada `INSTALLED_APPS` saya akan menambahkan `main`.

+ Dalam direktori `main` saya membuat direktori baru yang bernama `templates` dan membuat file `main.html` di dalam direktori `templates`, Isi dari main dalah dilihat di [sini](https://github.com/AtharAdista/game-sthar/blob/main/main/templates/main.html)

**Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**

+ Buka berkas `urls.py` yang ada di dalam direktori `game_sthar` lalu import fungsi `include` dari `django.urls` dan tambahakn rute URL untuk mengarahkan ke `main` di `urlpatterns`

  ```
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('main/', include('main.urls')),
  ]
  ```

**Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib.**

 + Saya membuat file `models.py` yang ada di direktori `main` untuk membuat model baru.
   - Saya mengisi file `models.py` sebagai berikut.
     ```
     from django.db import models
     class Product(models.Model):
        name = models.CharField(max_length=255)
        data_added = models.DateField(auto_now_add=True)
        amount = models.IntegerField()
        description = models.TextField()
        price = models.IntegerField()
        category = models.TextField()
        platform = models.TextField()

     ```
+ Kemudian saya melakukan perintah `makemigrations` untuk membuat migrasi model dan `migrate` untuk menerapkan migrasi ke dalam basis data.
  ```
  python manage.py makemigrations
  python manage.py migrate

  ```

**Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**

+ Buka file `views.py` yang ada di dalam folder `main`. kemudian tambahkan baris impor `from django.shortcuts import render`. 
+ Lalu tambahkan fungsi `show_main` seperti di bawah ini.

  ```
  from django.shortcuts import render

  def show_main(request):
      context = {
          'name' : 'Shaquille Athar Adista',
          'class' : 'PBP A',

      }

      return render(request, "main.html", context)
  ```

**Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**

+ Lakukan git add, commit, dan push sebelum mendeploy web kita.
+ Buka web **Adaptable** dan sign-in.
+ pilih `New App`. Pilih `Connect an Existiting Repository`. Lalu hubungkan semua repositori kita dengan Adaptable.io pada proses instalasi.
+ pilih repositori `game_sthar` dan pilih branch yang mau kita deploy.
+ pilih `python App Template`, kemudian pilih `PostgreSQL`.
+ pada bagian `version`, sesuaikan dengan versi python kita dan pada bagian `Start Command` masukkan perintah `python manage.py migrate && gunicorn game_sthar.wsgi`.
+ pilih nama domain yang kita mau dan centang bagian `HTTP Listener on PORT` dan deploy app.

 **BONUS**

 - Saya juga menambahkan unit test
  ```
  from django.test import TestCase, Client
  from .models import Product

  class mainTest(TestCase):
      def setUp(self):
          self.data= Product.objects.create(
              name = "Fifa 23",
              price = 40000,
              amount = 20,
              category = "Sport",
              platform = "PC, Nitendo Switch, Xbox X|S, Xbox One, Playstation 4",
              description = "The game offers revamped Career Mode, FIFA Ultimate Team (FUT), and the return of Volta Football for a diverse gaming experience.",

          ) 
    
      def test_product(self):
          self.assertEqual(self.data.name, "Fifa 23")
          self.assertEqual(self.data.price, 40000)
          self.assertEqual(self.data.amount, 20)
          self.assertEqual(self.data.category, "Sport")
          self.assertEqual(self.data.platform, "PC, Nitendo Switch, Xbox X|S, Xbox One, Playstation 4")
          self.assertEqual(self.data.description, "The game offers revamped Career Mode, FIFA Ultimate Team (FUT), and the return of Volta Football for a diverse gaming experience.") 

      def test_product_amount_not_negative(self):
          product = Product(name="Test Game", amount=10, price=100, category="Game", platform="PC", description="Test")
        
          self.assertTrue(product.amount >= 0)
    
      def setUp_web(self):
          self.client = Client()

      def test_template_elements(self):
          response = self.client.get('/main/') 

          self.assertEqual(response.status_code, 200) 

          self.assertContains(response, "<h1>Game Sthar</h1>")
          self.assertContains(response, "<h5>Name: </h5>")
          self.assertContains(response, "<h4>Game: </h4>")
          self.assertContains(response, "<h4>Amount: </h4>")
          self.assertContains(response, "<h4>Price: </h4>")
          self.assertContains(response, "<h4>Category: </h4>")
          self.assertContains(response, "<h4>Platform: </h4>")
          self.assertContains(response, "<h4>Description: </h4>")
   
          context = response.context  
          self.assertIn("name", context)
          self.assertIn("game", context)
          self.assertIn("amount", context)
          self.assertIn("price", context)
          self.assertIn("category", context)
          self.assertIn("platform", context)
          self.assertIn("description", context)

  ```

---
## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. 

![MVT architecture](https://github.com/AtharAdista/game-sthar/blob/main/Model.png)

 + User akan menuliskan sesuatu di browser
 + Klien(browser) mengirim permintaan HTTP ke Django
 + Django menerima permintaan dan menyampaikannya ke 
   `urls.py`
 + `urls.py` akan mengarahkan request ke View sesuai url yang diterima
 + View dapat berinteraksi dengan model yang merupakan komponen yang bertanggung jawab terhadap database
 + Setalah mendapatkan data dari model, maka View akan menampilkannya ke Template HTML, kemudian akan dikembalikan lagi ke View dan View akan 
   menghasilkan respon HTTP yang akan dikirim kembali ke klien.
 + Klien menerima respon dan menampilkan halaman web atau data yang diberikan.
 + Klien (browser) menampilkan halaman atau data kepada pengguna.

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
- MVC menggunakan Controller sebagai penghubung antara Model dan View. MVT menggunakan View untuk menerima http request dan mengembalikan HTTP  
  request yang telah diterima (menghubungkan Model dan Template). MVVM menggunakan ViewModel sebagai penghubung anatara Model dan View melalui binding
- MVC menggunakan View untuk menampilkan desain dan data kepada user. MVT menggunakan Template untuk menampilkan desain dan data kepada user. MVVM 
  menggunakan View untuk menampilkan tampilan yang dilihat user 
- MVC cocok digunakan pada aplikasi dengan kompleksitas yang tinggi dan interaksi pengguna yang rumit. MVT cocok digunakan untuk aplikasi kecil 
  dan besar. MVVM cocok digunakan untuk aplikasi dengan tampilan yang kompleks dan dipengaruhi oleh banyak perubahan data.
- MVC modifikasi dapat sulit tergantung pada bagaimana aplikasi dirancang. MVT modifikasi umumnya dianggap mudah karena pemisahan yang kuat antara 
  Model, View, dan Template. MVVM modifikasi dapat lebih mudah jika pengikatan data (data binding) diatur dengan baik.
- MVC hubungan erat (sangat berpasangan) antara Model, View, dan Controller. MVT hubungan yang lebih longar antara Model, View, dan Template. MVVM 
  hubungan yang kuat antara View dan ViewModel.
- MVC digunakan oleh Java, Spring. MVT digunakan oleh Django. MVVM digunakan oleh Microsoft APF, Angular JS
    
Sumber : 
+ https://www.niagahoster.co.id/blog/mvc-adalah/
+ https://www.geeksforgeeks.org/difference-between-mvc-and-mvt-design-patterns/
+ https://revou.co/kosakata/mvvm
