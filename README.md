# instagram-post-crawler
Merupakan program yang berguna untuk mendapatkan dan mengolah konten post di Instagram.

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

### Tentang
Instagram Post Crawler ini akan mengambil konten post dari user berupa username, caption, hashtag, likes, dan comments.
Cara kerjanya:
1. Program ini akan mengambil post dan username setiap followers dari username pertama (target)
2. Kemudian akan dilanjutkan mengambil konten post dari setiap followers
3. Setelah selesai, target selanjutnya akan dipilih secara acak dari followers username pertama
4. Kembali ke langkah 1, tetapi dengan target yang sudah dipilih sebelumnya
5. Program akan berhenti ketika semua akun menyentuh limit

### Yang di Butuhkan
- Python 3.5+
- Koneksi Bagus
- Beberapa Akun Instagram (karena Instagram memiliki limit akses)
- Library Python berupa: **pandas, selenium, emoji**
- Chrome WebDriver

### Cara Penggunaan
1. Unduh/clone repository ini.
2. Install python dan library yang diperlukan. Untuk library dapat diinstall melalui cmd: ```pip install <nama library>```
3. Download Chrome WebDriver dan taruh file exe nya di folder yang sama dengan file ini.
3. Siapkan beberapa akun dan buat file txt dengan format **username:password**
3. Jalankan script python dengan mengklik 2x atau dengan command ```python crawl.py```
4. Isi input nama file akun dan username pertama yang ingin di scrape


## Lisensi

Distributed under the MIT License. See `LICENSE` for more information.

## Kontak

Lazuardy Khatulistiwa - [@lazuardyk](https://twitter.com/lazuardyk) - lazdevs@gmail.com

Project Link: [https://github.com/lazuardyk/instagram-post-crawler/](https://github.com/lazuardyk/instagram-post-crawler/)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/lazuardyk/sipema.svg?style=flat-square
[contributors-url]: https://github.com/lazuardyk/sipema/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/lazuardyk/sipema.svg?style=flat-square
[forks-url]: https://github.com/lazuardyk/sipema/network/members
[stars-shield]: https://img.shields.io/github/stars/lazuardyk/sipema.svg?style=flat-square
[stars-url]: https://github.com/lazuardyk/sipema/stargazers
[issues-shield]: https://img.shields.io/github/issues/lazuardyk/sipema.svg?style=flat-square
[issues-url]: https://github.com/lazuardyk/sipema/issues
[license-shield]: https://img.shields.io/github/license/lazuardyk/sipema.svg?style=flat-square
[license-url]: https://github.com/lazuardyk/sipema/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/lazuardyk
[product-screenshot]: screenshot.png
