# Statik site

Site, doğrudan HTML, CSS ve JavaScript dosyalarından oluşur. Ruby, Bundler,
Jekyll veya derleme adımı gerekmez.

GitHub Pages yayın kaynağı `master` dalının kök klasörü olarak kalır.
Kökteki `.nojekyll` dosyası Jekyll işlemesini kapatır. `CNAME`, özel alan adını
`mkorkmaz.com` olarak korur.

## Dosyalar ve adresler

- `index.html`: profil ve biyografi metnini içeren ana sayfa.
- `journal.html`: genel konulu yazıların yeniden eskiye listelendiği Journal sayfası;
  ilk yazı eklenene kadar boş durum mesajı gösterir.
- `blog.html`: mevcut yazıların ve yeni teknik içeriklerin tarih sırasına göre
  listelendiği Blog sayfası.
- `contact.html`: iletişim sayfası.
- `about.html`: `/about` ve `/about.html` adreslerinden ana sayfaya anında
  yönlendiren dosya; biyografi yalnızca ana sayfada bulunur.
- `joy-of-coding.html`, `agile-johnny.html`: eski kategori adreslerini koruyan arşiv sayfaları.
- `YYYY/MM/yazi-adi.html`: yazılar.
- `assets/`: mevcut stil, JavaScript, görsel ve yazı tipi dosyaları.
- `feed.xml`, `sitemap.xml`, `robots.txt`: statik RSS ve arama motoru dosyaları.
- `404.html`: bulunamayan adreslerde gösterilen sayfa.

Yazıların dosya yapısı, önceki Jekyll çıktısıyla aynıdır. Böylece
`/2021/06/api-problem-specification-compatible-domain-exceptions` gibi mevcut
yazı adresleri ve canonical bağlantıları korunur. Menü, ana sayfada Journal,
Blog ve Contact bağlantılarını içerir; diğer sayfalarda Home bağlantısı da bulunur.
Yerel önizleme sunucusu da
uzantısız adresleri ilgili `.html` dosyasına eşler.

`about.html`, sıfır saniyelik `meta refresh` ve ana sayfayı gösteren canonical
bağlantısı içerir. GitHub Pages üzerinde dosya tabanlı özel HTTP 301 kuralları
tanımlanamadığı için bu yönlendirme HTML üzerinden yapılır; HTTP yanıtı 200'dür.
Gerçek HTTP 301 için sunucu veya CDN katmanında `/about` ve `/about.html`
adreslerini `https://mkorkmaz.com/` adresine yönlendiren bir kural gerekir.

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
bağlantılarını güncelleyin. Teknik yazıyı Blog listesine, ilgili kategori sayfasına,
RSS'e ve site haritasına ekleyin. Sayfalarda yinelenen menü ve profil alanları
da artık HTML dosyalarında tutulur.

### Journal yazısı ekleme

Mevcut yazılar Blog'da kalır. Yeni bir Journal yazısı için mevcut bir yazının HTML
dosyasını `YYYY/MM/yazi-adi.html` biçiminde kopyalayın. Başlığı, açıklamaları,
`lang` değerini, yayın tarihini, canonical ve paylaşım adreslerini güncelleyin;
`#post-body` alanına yazının tamamını yerleştirin. Kategori bilgisini Journal
olarak değiştirin. Her yazının kendine ait adresi ve detay sayfası olur.

`journal.html` içindeki `#post-list` listesine şu yapıda bir kayıt ekleyin:

```html
<li>
    <div>
        <aside class="dates" style="color:#666;">
            <time datetime="YYYY-MM-DD">YYYY/MM/DD</time>
        </aside>
        <a href="/YYYY/MM/yazi-adi">Yazı başlığı</a>
    </div>
    <h2>Yazının kısa açıklaması</h2>
</li>
```

`datetime` alanını gerçek yayın tarihiyle ISO `YYYY-MM-DD` biçiminde doldurun.
Kayıtları HTML'de yeniden eskiye yerleştirin. Sayfa açılırken JavaScript de bu
tarihlere göre sıralar; ilk kayıt eklendiğinde boş durum mesajını gizler.
Yazının adresini `sitemap.xml` dosyasına da ekleyin. Journal yazılarını Blog
listesine veya Blog RSS akışına eklemeyin.

`drafts/`, `_drafts/` ve `_site/` Git tarafından takip edilmez ve yayına
dahil edilmez.
