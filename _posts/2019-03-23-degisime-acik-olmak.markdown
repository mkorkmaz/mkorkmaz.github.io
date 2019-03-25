---
layout: post
title:  "Değişime açık olmak"
description: "\"Embracing change\""
date: 2019-03-23
tags: [Agile, Turkish]
categories: [Agile Johnny]
reading_time: "3-4 min."
---


> “**Things do change. That's why we design and build with change in mind.**” <br>— Ron Jeffries

[Agile Manifesto](https://agilemanifesto.org/){:target="_blank"}'nun vurguladığı değerlerden biridir "**Responding to change _over_ following a plan**". Peki sabit bir planı uygulamaktansa "değişime cevap verebilmek" ya da başka bir deyişle "değişime açık olmak", bir geliştirici için ne ifade ediyor?


Günün sonunda, hepimiz üzerinde çalıştığımız projenin ortaya çıkaracağı **_değeri_** görmek için çalışıyoruz. Değer, yerine göre, projeden projeye içeriği ve anlamı değişebilen bir kavram. Bazı projeler için değer paradır, bazı projeler için daha fazla etkileşimdir, bazı projeler için müşteri memnuniyetidir. 

Projeye dahil olan herkesin, proje sahibinden QA mühendisine kadar herkesin unutmaması gereken şey hepimiz üzerinde çalıştığımız projenin sonunda ortaya çıkacağı değer için çalışıyoruz. "Para kazanmak, geçimimizi sağlamak, verilen görevi yapmış olmak, entelektüel haz almak vs gibi amaçlar için çalıştığımızı" da söyleyebilir, ona göre hareket edebilir, ve başarısız olmaya aday bir projenin tabutuna bir çivi de siz çakarsınız. 


Unutmayın, ancak ve ancak "**doğru işi doğru şekilde**" yaparsanız üzerinde çalıştığınız proje amaçlanan değere ulaşmaya yaklaşabilir. Diğer tüm kazanımlar bunun yan ürünüdür.

"Doğru işi doğru yapmak" nedir? 

_Doğru iş_, ortaya çıkan iş fikrinin ürün olarak son haline geldiğinde, istenen şekilde olduğunu görebilmektir kısaca. Onu _doğru yapmak_ ise işin teknik kısımlarıdır, yani UX ve bilgi mimarisi süreçlerinde, tasarım süreçlerinde iş fikrini iyi yansıtacak şekilde ele almak, yazılım kısmında temiz mimari ve temiz kod prensiplerine uygun şekilde ürünü çıkarmaktır.


Buraya kadar hemfikir isek devam edebiliriz.

Dolayısıyla, bir işi doğru yapabilmek için, projeyi geliştirme sürecinde belirli aralıklarla gelen geribildirimleri değerlendirmek ve alınan kararlar doğrultusunda gerekli değişiklikleri yapmak kaçınılmazdır. Bu yüzden gelebilecek değişiklik taleplerine hazır olmak gerekiyor. **Agile** ya da **_çevik_** uygulama geliştirmenin temelinde bu vardır. 

Bu noktada "bu projenin bir teslim tarihi var kardeşim" itirazları gelebilir.
 
Peki kişi değişime nasıl açık olabilir, gelen değişiklik taleplerine nasıl hazır olabilir?

Her şeyden önce özgüveni yerinde olan kişiler değişime açık olabilirler. "**Özgüven**"den kastım "beni kesseler acımaz" değil tabi. Neyi nasıl ve neden yaptığını bilen kişiler özgüven açısından güçlü olurlar. Bana göre bunu bize sağlayan önemli konular **test yazmak, temiz mimari ve temiz kod**dur.


Bir geliştirici açısından bu bahsettiğimiz özgüveni en başta "**test yazmak**" sağlar. Gelen değişiklik taleplerini uyguladığımızda, farkında olmadan, alakasız sandığımız bir yerin yanlış çalışmasına neden olabiliriz. Yazdığımız kodun testini yazmamız "daha az hata içeren" kod yazmamızı sağlamanın yanı sıra, bizi bu konuda koruyacaktır. Bu noktada [TDD](https://www.jamesshore.com/Agile-Book/test_driven_development.html){:target="_blank"} ve [BDD](https://docs.cucumber.io/bdd/overview/){:target="_blank"} bizim yardımcımız olacaktır.

**Temiz mimari**, üzerinde çalıştığımız problemin doğru bir şekilde modellenmesi ve bunun uygulama haline getirilmesi ile ilgilidir. Burada [Hexagonal Mimari](https://fideloper.com/hexagonal-architecture){:target="_blank"} gibi konseptler, [DDD](https://www.infoq.com/minibooks/domain-driven-design-quickly){:target="_blank"} gibi yaklaşımlar bize yol gösterici olacaktır.

**Temiz kod** sadece göze hoş gelen kod yazmak anlamına gelmiyor tabi. [SOLID](http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod){:target="_blank"} pattern'lerine bağlı, [STUPID](https://nikic.github.io/2011/12/27/Dont-be-STUPID-GRASP-SOLID.html){:target="_blank"} pattern'lerinden kaçınan bir yapı kurmak, [Defensive Programlama](https://ocramius.github.io/extremely-defensive-php/#/){:target="_blank"} konusunda duyarlı olmak, [Object Calisthenics](https://www.cs.helsinki.fi/u/luontola/tdd-2009/ext/ObjectCalisthenics.pdf){:target="_blank"} kurallarına riayet etmeye çalışmak bize yardımcı olacaktır.

Bu bahsettiğim konular ışığında, değişimi özgüvenli bir şekilde "kucaklamamız" mümkün olacaktır diye düşünüyorum. Test yazmayan ve temiz mimari ile temiz kodu tamamıyla gözardı eden bir anlayış ile "_Agile gitmek_" mümkün görünmüyor bana.

"Bu projenin bir teslim tarihi var" diyen arkadaş, seni unutmadım, onu da daha sonra irdeleyeceğiz.

