---
layout: post
title:  "Belirsizliği yönetmek kimin görevidir?"
description: "\"Who is responsible for managing the uncertainty?\""
date: 2019-03-26
tags: [Agile, Turkish]
categories: [Agile Johnny]
reading_time: "6-8 min."
---


> "**The point isn’t to make good estimates — the point is to do good work at a consistent pace**." <br/><br/>
[Nature of Software Development: Keep It Simple, Make It Valuable, Build It Piece by Piece](https://pragprog.com/book/rjnsd/the-nature-of-software-development){:target="_blank"} by [Ron Jeffries](https://twitter.com/ronjeffries){:target="_blank"}


Yeni bir projeye başlıyorsunuz, heyecanlısınız. Her şey çok güzel ve çok farklı olacak. Birtakım listeler dökülüyor; şunlar yapılmalı, bunlar muhakkak olmalı, onu dahil etmeli vs vs. Ve sıfırıncı günde o soru karşınıza çıkıyor: "**Ne zamana biter?**"

Hemen hemen herkesin üç aşağı beş yukarı bir zamanlama tahmini algısı vardır. Buna göre bir tahminde bulunur.

Zamanlama vermek, tahminde bulunmak, efor belirtmek şeklinde karşımıza çıkan isteklere binaen verilen cevaplar çoğu zaman sorunludur. Her şeyden önce gerçekçi bir tahminde bulunmak gerçekten zordur. Çünkü elimizde en ince detayına kadar belirlenmiş ya da görünmeyen teknik zorluk içermeyen bir talep çoğu zaman yoktur. 

Taleplerin arasında ve içinde bir çok gizli talep, hafife alınmış zorlayıcı faktör gizlidir ve değerlendirken bunlar gözden kaçar. Bu sebeple bu soruyla karşılaşan geliştiriciler iyimser davranıp olabilirin altında zamanlama verebilirler.


Başka bir sorun ise kendine güveni olmayan ya da kendisini sağlama almak isteyen geliştiriciler: olabilirin çok üzerinde zaman verebilirler. "Bu ne zamana biter" sorusu bir kontrat vurgusuyla geldiğinde kişiler kendilerini korumak isteyeceklerdir.

"Ne zamana biter" sorusu, projenin genelinin dışında, yapılacak en küçük işe kadar sızma eğilimindedir: "E-posta doğrulaması yapılmalıdır maddesi ne kadar sürer? gibi. Bir ton madde listelenip teker teker efor talep edilir. 

Bu zamanlama isteği talebine bir gün içinde cevap veriyorsanız geçmiş olsun, her şeyi ya altında ya da üstünde tahmin ediyorsunuz demektir. İnsan zihni çok kuvvetli olabilir ama burada çok boyutlu bir matris çarpımına benzer bir yapı vardır, buna hakim olmak o kadar kolay olmayabilir. Efor talebine uzun uzun düşünüp cevap verecek zamanınız da hiçbir zaman olmayacaktır. Zaten enerjinizi ve zamanınızı oraya akıtmanın da bir anlamı yoktur.

Maddeler listelendi, her bir madde için zamanlama verildi diyelim. **Gantt Chart Mafyası** elinde bir zaman çizelgesi ile sürekli başınızda olacaktır. Bu zaman çizelgesinde her en ufak sapma, tüm ekibe **_mutsuzluk ve endişe vermekten başka bir işe yaramayacaktır_**. 

Yazılım geliştirme, bir imalat atölyesi çalışması gibi, dört işlem hesaplamalarıyla, ölçümlemelerle zamanlama takibi yapılabilir bir süreç değildir. Zaman baskısı ile ancak ve ancak bir geliştiriciyi kaliteden ödün vermeye itersiniz. **Zamanlama tahminlerine teslim etme tarihi muamelesi yapamazsınız**.


Evet, ortada hep bir belirsizlik vardır ve yöneticiler bunun yönetimini kendileri yapmak yerine genelde geliştiricilerden beklerler. Siz, bu konuda endişenizi dile getirip, zamanlama ile ilgili çekincelerinizi belirttiğinizde mutsuz olurlar. Proje hep daha önce teslim edilmelidir.

Peki, **_belirsizliği yönetmek kimin görevidir?_**


Cevap vermek yerine başka bir soru sorayım: **_neden belirsizliği yönetiyoruz ki?_**


Projeyi bir teslim tarihi girdabında boğmak yerine, onu 1-2 haftada yapılabilir küçük parçalara bölüp, sırasıyla onları analiz edip bitirerek ilerlemek projenin daha doğru ilerlemesi açısından daha doğru görünüyor. 

Hiçbir proje başladığı andaki haliyle kalmaz, sürekli değişir. Bu yüzden değişimi göz önünde bulundurarak sistemi tasarlamak ve geliştirmek durumundayız. Bu yüzden küçük adımlarla geliştirmeler yapıp, belli aralıklarla bunları gözden geçirmeli, değerlendirmeli, gerekli değişiklikleri yapıp bir sonraki adıma geçmeliyiz. Bu _doğru şeyi doğru şekilde yapmak_ adına elzemdir.

Yapılacakları listeleyin, elde edilmesi hedeflenen uygulamaya en çok değer katan maddeleri önceliklendirip, bunları geliştirmeye başlayın. Uygulamanın aslında daha hızlı çıktığını görecekseniz. Örneğin; bir muhasebe uygulaması geliştiriyorsanız, müşterinin kişisel bilgilerini yöneten kısmı yazmaktan çok, onun gelir ve giderlerini işleyen kısmı yazmanız uygulamaya dair olumlu algıyı daha önce oluşturacaktır.


Bir önceki yazıda “Bu projenin bir teslim tarihi var” diyen arkadaş burada çıkışını yine yapacaktır.

Öncelikle şunu belirteyim: Kendinizi sağlama alıp, geniş geniş bir zaman belirlemediyseniz, ekibinizi "yakmadan" o tarihte projeyi teslim etmeniz pek olası değildir. Geriye dönüp şöyle bir düşünün, ne demek istediğimi anlayacaksınız. Aslında projenin bitebileceği zaman kabaca sabittir. Onun öncesinde bir teslim tarihi belirlemeniz bunu değiştirmeyecektir.

Burada önemli olan, belirlenen teslim tarihinde elde edilmesi hedeflenen uygulamaya değer katan maddelerden ne kadar çoğunu o tarihte bitirebildiğinizdir. Bu önceliklendirmeyi yapmadan ilerlerseniz, hem o ana kadar yaptığınız kısım kimseyi tatmin etmeyecektir, hem de kalan kısımda ekibi yakmadan ilerlemeniz pek olası olmayacaktır.

Prensip olarak bir teslim tarihi belirleyin ama, kişisel tecrübem, bunu Allah Kelamı haline getirmeyin. Evet, maliyetler üç aşağı beş yukarı zamana ve ayrılan iş gücüne göre değişiyor, müşteri (ya da patron) işin başında bu işin maliyeti ne olacak bilmek isteyecektir. Tecrübeniz ve sezgileriniz kabaca bir fikir verecektir. Risklerinizi değerlendirip ona göre bir "söz" vermenizde fayda var. Projeyi nasıl ele alacaksınız, süreçlerinizi ve olası sarkmaları nasıl yöneteceksiniz belirtin. Kimse günün sonunda elinde işe yaramaz bir uygulama olsun istemeyecektir.

Olmazsa olmaz bir teslim tarihi varsa, projeye en çok değer katan ve o tarihe bitebilecek olan maddeleri belirleyin, bunu müşteri ile paylaşın, kalan kısımları da ne şekilde teslim edebileceğinizi belirtin ve onların onayını alın. Aksi taktirde yerine getiremeceğiniz bir taahhütün altına giriyorsunuz demektir. 

"_Geliştir - Geribildirim al -  Değiştir ve bir sonraki adıma geç_ döngüsü" ile ilerleyemeyecekseniz, yapılacakları yazılı halde iki taraf olarak onaylayın. Teslim tarihine kadar bunlara yeni maddeler eklenemeyeceğini kabul ettirin ve akabinde bunları yetiştirmeye çalışın. Buradaki en büyük sorun geribildirim almadan ilerlendiği için sürecin sonuda elde edilen "ürün" başta istenen de olsa arzulanan ürün olmama olasılığının yüksek olması.

Bir geliştiricinin görevi teknik meselelerle uğraşmak olmalıdır, işi yürütme süreçlerini takip etmek değil.

Evet, belirsizliği yönetmek kimin görevidir? Bence geliştiricilerin görevi olmadığı ortada.




