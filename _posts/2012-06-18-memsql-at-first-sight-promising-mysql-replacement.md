---
layout: post
title: 'İlk Bakışta MemSQL'
description: 'MemSQL at First Sight'
date: 2012-06-18
tags: [Joy Of Coding, Turkish]
categories: [Joy of Coding]
reading_time: "4-5 min."
---

#### TL;DR English

- MemSQL is promising MySQL replacement but there are some issues like this serious one: not joining more than two tables for now.
- Connection adapters are already there: Use MySQL connection adapters.
- Same SQL syntax of MySQL except not implemented ones that noted on MemSQL developer site.
- MemSQL uses memory and is kinda like Memcache+MySQL
- MemSQL creates shared object libraries for every different type of queries. First execution may be slow (creating shared object library takes times, of course, let's call it "learning step") but next ones are blazingly fast.

---
 
#### TL;DR Türkçe

- MemSQL gelecek vaadeden ve MySQL'in yerine kullanılabilecek bir veritabanı fakat an itibariyle ikiden fazla tablodan veri çekme noktasında desteğinin olmaması gibi durumlar mevcut.
- MemSQL'e bağlanmak için herhangi bir MySQL adaptörünü kullanabilirsiniz.
- Bazı özellikler henüz uygulanmamış olsa da MySQL ile aynı söz dizilimini kulanılmaktadır.
- MemSQL RAM'i kullanarak disk üzerindeki I/O tasarrufuyla hız kazanıyor. Benzetme her na kadar doğru olmasa da Memcache+MySQL gibi düşünebiliriz.
- MemSQL her bir query tipi için shared object kütüphanesi oluşturur. İlk sorgunun cevap döndürmesi biraz zaman alabilir shared object kütüphanesi oluşturulmasından dolayı ama bu "ilk öğrenme" evresinden sonraki sorgulara hızlı cevap verebiliyor.

---

# <center>İlk Bakışta MemSQL</center>

Yüksek performans beklenen veritabanı uygulamalarının en büyük maliyeti veritabanına yapılan sorgulardır. Özellikle veri girişinin de yoğun olduğu ve anlık sorgu miktarının çok olduğu durumlarda veritabanının performansı gerçekten kritik bir hal alıyor. Bu durumu bertaraf etmek için kullanılan çeşitli yöntemlerden biri de caching. Daha önce sorgulanmış bir talebi tekrar veritabanına sormadan cevaplayabilmek uygulamanın performansına yönelik yazılımsal anlamda büyük fayda sağlamaktadır. 

Çeşitli caching stratejileri var tabi: Talep oldukça ya da önceden kestirelebilecek tüm istekleri daha uygulama içinden talep edilmeden önce cache'lemek gibi. MemSQL de işte bu tip durumdaki uygulamalar göz önünde bulundurularak geliştirilmiş ve MySQL ile aynı söz dizilimini kullanan ve aynı bağlantı adaptörlerini kullanan bir veritabanı. RAM'i kullandığı için diskten okuma maliyetini otomatikmen ortadan kaldırdığından sorguların cevap süreleri inanılmaz azalıyor. 

Maalesef MySQL'in tüm özellikleri MemSQL'e aktarılmış değil. Mesela bir çok uygulama için kısıtlayıcı olacak olan ikiden fazla tabloyu birbirine bağlayarak veri çekmek henüz MemSQL'de mümkün değil. 

MemSQL'in kurulumu basit. GNU/Linux'ta gerekli geliştirme paketleri yüklü olduğu ve sistem RAM miktarı en az 8GB olduğu sürece bir sıkıntı yaşanmıyor. 

Denemelerimi 103 Tablo ve toplamda 771 MB yer kaplayan bir CMS veritabanı ile yaptım. MySQL'den MemSQL'e datayı Navicat ile aktardım. Aktarım sırasında ufak tefek sıkıntılar olduysa da sorun çıkaracak hatalar ile karşılaşmadım. Aktarım sonrasında Navicat tablo isimlerini her ne kadar listeleyemese de komut satırından mysql komutu vasıtasıyla bağlandığımda hiç bir sıkıntı yaşamadım. Uygulamayı MemSQL ile çalışmasını sağlamak için php\_mysqli kullanarak çalışan uygulamanın MySQL konfigürasyon kısmındaki bağlantı bilgilerini değiştirerek yapmam yeterli oldu. 

Yukarıda da bahsettiğim ikiden fazla tabloyu birbirine bağlayarak veri çekme noktası dışındaki kısımlar gayet düzgün çalıştı. Sunucuyu kontrol ettiğimde gördüğüm kadarıyla MemSQL her bir tabloya herbir ayrı tip query için kendi cache klasöründe tablo ismiyle oluşturduğu başka bir klasör içinde bir shared object kütüphanesi oluşturuyor. Bu kütüphanelerin header ve c kaynak kodlarını da ilgili klasörde bulup incelemek mümkün. 

Sonuç olarak MemSQL takip edilmesi gereken bir proje ve bir çok uygulamanın olmazsa olmaz temel ihtiyaçlarını karşıladığı noktadan itibaren de vazgeçilmez olacaktır diye düşünüyorum. 

Kaynak ve ilgili siteler: 
- <http://memsql.com/> 
- <http://developers.memsql.com/> 
- <https://twitter.com/memsql>