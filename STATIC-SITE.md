# Statik site

Site, doğrudan HTML, CSS ve JavaScript dosyalarından oluşur. Ruby, Bundler,
Jekyll veya derleme adımı gerekmez.

GitHub Pages yayın kaynağı `master` dalının kök klasörü olarak kalır.
Kökteki `.nojekyll` dosyası Jekyll işlemesini kapatır. `CNAME`, özel alan adını
`mkorkmaz.com` olarak korur.

## Dosyalar ve adresler

- `index.html`: ana sayfa ve yazı listesi.
- `about.html`, `contact.html`, `joy-of-coding.html`, `agile-johnny.html`: diğer sayfalar.
- `YYYY/MM/yazi-adi.html`: yazılar.
- `assets/`: mevcut stil, JavaScript, görsel ve yazı tipi dosyaları.
- `feed.xml`, `sitemap.xml`, `robots.txt`: statik RSS ve arama motoru dosyaları.
- `404.html`: bulunamayan adreslerde gösterilen sayfa.

Dosya yapısı, önceki Jekyll çıktısıyla aynıdır. Böylece `/about` ve
`/2021/06/api-problem-specification-compatible-domain-exceptions` gibi mevcut
adresler ve canonical bağlantıları korunur. Yerel önizleme sunucusu da
uzantısız adresleri ilgili `.html` dosyasına eşler.

## Yerel önizleme ve kontroller

Önizleme için Python 3'ün standart kütüphanesi yeterlidir:

```sh
python3 tools/serve.py
```

Siteyi `http://127.0.0.1:4000/` adresinden açın. Sunucu yalnızca yerel
bilgisayardan erişilebilir; taslakları ve geliştirme dosyalarını sunmaz.
Python dosyaları sitenin çalışması veya GitHub Pages yayını için gerekli değildir.

Kontrolleri çalıştırmak için:

```sh
python3 -m unittest discover -s tools -p 'test_*.py'
```

## İçerik güncelleme

Sayfaları doğrudan HTML dosyalarında düzenleyin. Yeni bir yazı için mevcut
bir yazının dosyasını kopyalayıp içerik, başlık, tarih, dil, canonical ve paylaşım
bağlantılarını güncelleyin. Yazıyı ana sayfaya, ilgili kategori sayfasına,
RSS'e ve site haritasına ekleyin. Sayfalarda yinelenen menü ve profil alanları
da artık HTML dosyalarında tutulur.

`drafts/`, `_drafts/` ve `_site/` yerel dosyalar olarak korunur ve Git tarafından
takip edilmez. Önceki kurulumdan kalan yerel `README.md` ve `test/site_test.rb`
dosyaları da korunur; yeni yapı bu dosyaları kullanmaz.
