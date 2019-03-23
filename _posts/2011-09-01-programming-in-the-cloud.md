---
layout: post
title: 'Bulutta Uygulama Geliştirme'
description: 'Programming in the Cloud'
date: 2011-09-01
tags: [Joy Of Coding, Turkish]
categories: [Joy of Coding]
reading_time: "5-6 min."
---

Hepimiz kendi çapında belli birtakım araçlar ile uygulama geliştirmekteyiz. Daha çok web tabanlı uygulama geliştiren bir kişi olarak klasik uygulama geliştirme "soft setup"ım şu şekilde:

- Apache Web Server
- [Zend Server CE](http://www.zend.com/en/products/server-ce/ "Zend Server Community Edition ")
- MySQL
- [Memcached](http://memcached.org "Memcached")
- [Zend Studio](www.zend.com/products/studio/ "PHP Editor - Zend Studio The Leading PHP IDE")
- [Git](http://git-scm.com/ "Git - Version Control System") ve [Github](http://github.com/ "Secure source code hosting and collaborative development")
- Firefox ve Firebug

Her ne kadar Memcached'i ihtiyacım oldukça komut satırından çalıştırsam da Apache, Zend ile servislere eklenen lighttpd ve mysql arkaplanda kendilerine ihtiyaç olmasa bile çalışmaya devam etmekteler. Zend Studio da Java ile çalışan ve sistem hafızasında hatrı sayılır yer kaplayan bir uygulama. Bu setup ile yeni açılmış bir makine ile bile gerek işlemci gerek sistem hafızası olarak sistem kaynaklarını bonkörce kullanmaktayım. 

Sistem kaynakları dışında geliştirilen uygulamaların gerek belirli aralıklarla yedeklenmesi, gerek ekip çalışmasının mümkün olması ve versiyon kontrolü amacıyla git'i daha doğrusu Github'ı kullanmaktayım. Her ne kadar [Time Machine](http://en.wikipedia.org/wiki/Time_Machine_(Mac_OS) "Mac OS Time Machine") ile genelde işimi görmüş olsam da (MySQL data klasörü de dahil olmak üzere) hard diskte ya da yedekleri aldığım harici diskte bir sıkıntı olur, makine çalınır/kırılır/bir şey olur gibi sıkıntıları aşmak adına Github bize bir çok ekstra güzelliği ile kullanıcı dostu bir ortam sağlıyor. Zaten geliştirilen uygulamanın lokal kopyasının yanı sıra harici disk ve internet üzerinden bir yerlerde birer kopyasının da düzenli olarak tutulması artık bir zorunluluk haline geldi hepimiz için. 

Web tabanlı uygulamalar geliştiren birisi olarak size acil olarak ulaşılamazsa olmaz. Bu yüzden de tatile çıksanız bile "nedense" yanınızda bir laptop muhakkak olur. Bir workstation olmasa da normal bir laptop'tan daha fazlasının beklendiği bu makineler ağırlık olarak da can sıkıcı olabiliyor. 

Bu laf kalabalığını şunun için yapıyorum: Artık programlama da dahil olmak üzere bir çok iş akışı internet üzerinden internet tarayıcılar içinden yapılmaya başlanıyor. Artık hayatımızın bir parçası olan "Bulut Bilişim"e daha fazla aşina olmaya başlıyoruz. Yukarıda bahsettiğim konuları ve benzeri bir çok sıkıntıyı artık bu yöntemle giderebiliyoruz. 

Bu bağlamda uygulama geliştirmek için kullandığım ve beni büyük bir ölçüde rahatlatan yeni setup'ım ve iş akışımdan bahsetmek istiyorum: 

Öncelikle kişisel olarak tercih ettiğim Rackspace'den bir adet [Cloud sunucu](http://www.rackspace.com/cloud/cloud_hosting_products/servers/ "Rackspace Cloud Servers") kiraladım (Herhangi bir sanal ya da normal dedicated sunucu da doğal olarak işinizi görebilecektir). Uzun süredir CentOS kullanan biri olarak ve daha sonra kurmak durumunda kalabileceğim bir takım uygulama ve servisleri düşündüğümde bu sunucu için en uygun işletim sistemini Ubuntu olarak belirledim. Bu işletim sistemini sunucunuzu oluştururken seçebiliyorsunuz, Rackspace size üzerinde sadece SSH erişimi olan tertemiz bir sunucunu veriyor. Sisteme login olunca sırasıyla şu servisleri kurdum:

- MySQL 5
- Zend Server CE
- Memcached
- Git

Bunlar kendi makinemde de olan standart servisler. Bulut içinde uygulama geliştirmek için internet tarayıcı içinde çalışan bir editöre ihtiyacım oldu. Zend Studio ile Remote Server bağlantısı ile de yapabilmeme rağmen bunun için son zamanlarda popülerliği giderek artan [Cloud9 IDE](http://c9.io/ "Cloud9 IDe")'nin ideal bir seçim olduğuna karar verdim. Otomatik kod tamamlama ve PHP debugging özelliklerinin olmaması bir sıkıntı. Debugging ve kod profilleme çalışmalarını belirli aralıklarla Zend Studio ile yapmaya karar verdim. 

[Node.js](http://nodejs.org "Node.js") ile çalışan Cloud9 IDE için sırasıyla Node.js'yi kurup Github'dan [Cloud9 IDE](https://github.com/ajaxorg/cloud9/ "Cloud9 Github Repository") dosyalarını klonlayarak komut satırından Could9 IDE'yi başlattım. Rackspace'in bana verdiği IP adresini ve Cloud9 IDE'nin portunu yazarak IDE'yi test ettim. Başarıyla çalıştığından emin olduktan sonra Cloud9 IDE'nin çalışacağı IP adresi, portu ve workspace'i belirleyip son testimi yaptım. 

Burada karşıma çıkan ilk sıkıntı Rackspace'in bana verdiği IP adresini ve Cloud9 IDE'nin portunu bilen bir kişinin de Cloud9 IDE'yi açabilecek olması. Bunun önüne geçebilmek için ilk uyguladığım yöntem bir VPN kurmak oldu. Ubuntu üzerinde PPTP (_Point-to-Point Tunneling Protocol_) sunucusu kurup bir kullanıcı adı ve şifre belirleyerek konfigürasyonu test ettim. VPN servisinin düzgün çalıştığından emin olduktan sonra sırasıyla şu firewall ayarlarını yaptım:

- Web sunucuya erişmek için 80 nolu portu erişime açtım
- VPN servisinden yararlanabilmek için 1723 nolu portu erişeme açtım
- Cloud9 IDE'yi kullanabilmek için belirlediğim portu erişime açtım

Cloud9 IDE'yi makine yeniden başlatıldığında çalışacak şekilde ayarlamasını henüz gerçekleştiremedim, biraz daha uğraşmak yerine ilk reboot sonrası sisteme login olup 

```sh
/root/cloud9/cloud9/bin/cloud9.sh -l 172.168.0.1 -w /var/www > /dev/null 2>&1 &
```
 komutu çalıştırıp sistemden çıkıyorum. Firewall'u aktive edip sistemi yeniden başlatıp Cloud9 IDE'yi başlattıktan sonra tüm kontrolleri yeniden yapıp sistemi artık istediğim an kullanmaya hazır hale getirdim. 
 
Artık Github'dan projelerimi workspace içine ilgili yerlerine klonlayıp yeri geldiğinde commit ve push komutları ile işletim sisteminden ve lokasyondan bağımsız bir şekilde uygulama geliştirebiliyorum. 

Bir sonraki aşama Cloud9 IDE'yi otomatik başlatıp, tek bir kişi için geçerli olan bu yapıyı çok kullanıcılı bir sistem haline getirmek ve Github'a değişiklikleri commit ve push edebilmek olacaktır. Tüm bunlarla uğraşmayıp doğrudan http://c9.io adresinde bir hesap da açılabilir tabi ihtiyaçlarınızı karşılayabildiğiniz sürece.