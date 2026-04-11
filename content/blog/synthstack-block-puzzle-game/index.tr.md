+++
title = "SynthStack: Bir Tetris Klonu"
date = 2026-04-11
description = "iOS için neon synthwave estetiğinde bir blok bulmaca oyunu geliştirdim. İşte SynthStack'in hikayesi, yol boyunca aldığım kararlar ve App Store'a oyun çıkarırken öğrendiklerim."

[taxonomies]
tags = ["ios", "swift", "spritekit", "oyun-geliştirme", "synthstack", "yan-proje"]

[extra]
social_media_card = "photos/posts/synthstack.png"
+++


{{ img(src="photos/posts/ss-0.jpeg", class="xx-smaller-img", caption="Engeller yolun önünde durmaz. Engeller yolun kendisidir.") }}

Tetris'i her zaman sevmişimdir. Meditasyon gibi bir yanı var — parçaları düşürmenin ritmi, satır temizlemenin verdiği tatmin, her şey oturduğunda girdiğin akış hali. Bir noktada düşündüm: ya kendi versiyonumu yapsam, gerçekten oynamak istediğim estetikte?

**SynthStack** böyle başladı. Neon ve synthwave görsellerle sarılmış, iOS için SpriteKit ile geliştirilmiş bir blok bulmaca oyunu.

### Neden Bir Tetris Oyunu Yaptım?

{{ img(src="photos/posts/ss-3.jpeg", class="xx-smaller-img", caption="Oyun içi ekran görüntüsü - zen modu") }}

Açıkçası bir öğrenme egzersizi olarak başladı. SpriteKit ve GameplayKit'e — Apple'ın hak ettiği ilgiyi görmeyen yerel oyun framework'lerine — daha derinlemesine dalmak istiyordum. Bir Tetris klonu yapmak mükemmel bir kapsam gibi görünüyordu: ilginç olacak kadar karmaşık, gerçekten bitirebilecek kadar basit.

Ama başlayınca, bir klonun ötesine geçti. *Benim* oyunummuş gibi hissettirmesini istiyordum.

### Neon Estetiği

Synthwave ve cyberpunk görsellerine bayılırım. Derin uzay siyahları, neon cyan vurgular, parlayan kenarlıklar, köşe noktaları olan holografik blok hücreleri. Tüm arayüz programatik olarak oluşturuluyor — butonlar veya paneller için görsel dosyası yok. Her şey `UIGraphicsImageRenderer` ve `SKTexture` ile render ediliyor, bu da görsellerin her cihazda mükemmel ölçeklenmesi anlamına geliyor.

Tasarım sistemi (`DS`) tüm renk paletini tanımlıyor ve dokuları çalışma zamanında üretiyor: parıltı haleli yuvarlak dikdörtgenler, tarama çizgisi vurgulu blok hücreleri, nokta ızgara arka planları, köşe parantez süslemeleri. Küçük bir şey ama tutarlı bir tasarım diline sahip olmak oyunun bütünlüklü hissettirmesini sağladı.

### Oyun Modları

{{ img(src="photos/posts/ss-1.jpeg", class="xx-smaller-img", caption="Oyun içi ekran görüntüsü - mod seçimi") }}

Oyun üç modla çıktı:

- **Zen**: sonsuz oyun, baskı yok, sadece keyif
- **Sprint**: 40 satırı olabilecek en hızlı şekilde temizle
- **Zamana Karşı**: 2 dakikada en yüksek skoru yap

Her modun Game Center üzerinden kendi skor tablosu var ve Sprint, zorluk seviyesi başına en iyi sürenizi takip ediyor.

### Kedi Modu

{{ img(src="photos/posts/ma-cats.jpeg", class="xx-smaller-img", caption="Syntax & Lumos") }}

Syntax ve Lumos adında iki kedim var. Ekranda farenin gelip gittiği ve kedilerin yakalamaya çalıştığı videoları görmüşsünüzdür. Ben de bunu taklit etmek istedim ve parçaların etrafta süzüldüğü, basıldığında patladığı kedi modunu oluşturdum. Kedilerimin ilgisini umduğum kadar çekmedi ama yine de tutmaya karar verdim. Beğenecek kediler olabilir.

### Puanlama: Kılavuza Uygun

Modern Tetris puanlama kılavuzunu uyguladım: satır temizleme başına temel puanlar (100/300/500/800), seviye çarpanı, T-Spin bonusları, ardışık zor temizlemeler için back-to-back zincirleri (1.5x çarpan), kombo bonusları ve All Clear (Mükemmel Temizlik) ödülleri. Tahtadaki tüm blokları temizlerseniz seviye × 3500 puan kazanırsınız.

### Masaüstü Modu ve Klavye Desteği

Son zamanlarda eklediğim bir özellik, oyun Mac'te çalışırken ("Designed for iPad" modu) tam klavye desteği. GameController framework'ündeki `GCKeyboard` kullanılarak:

- Hareket için ok tuşları (DAS/ARR ile — Delayed Auto Shift ve Auto Repeat Rate, tıpkı yarışmacı Tetris'teki gibi)
- Hard drop için Space
- Saat yönünde döndürme için yukarı ok veya X, saat yönünün tersine için Z
- Parça tutma için C veya Shift
- Duraklatma için Escape veya P

"Nasıl Oynanır" talimatları ekranı Mac'te olduğunuzu otomatik algılayıp dokunma hareketleri yerine klavye kontrollerini gösteriyor.

### Öğrendiklerim

**SpriteKit hafife alınıyor.** Apple platformlarında 2D oyunlar için gerçekten iyi. GameplayKit entegrasyonu (durum makineleri, kural sistemleri, varlık-bileşen) devasa bir motor çekmeden sağlam bir mimari veriyor.

**Birinci günden yerelleştirme.** SynthStack 13 dilde yerelleştirildi. Basit bir `L10n()` yardımcısı ve `.lproj` paketlerine baştan sahip olmak bunu zahmetsiz hale getirdi. Tüm dillere yeni bir metin eklemek 5 dakikalık bir iş.

**Dokunsal geri bildirim önemli.** Yumuşak düşüşte hafif titreşim, sert düşüşte ağır titreşim, parça kilitlenmede orta, bonuslarda ve seviye atlamada bildirim. Dokunsal geri bildirim açıkken ve kapalıyken oyun tamamen farklı hissettiriyor.

**En basit şeyi çıkar, sonra cilala.** İlk versiyon sadece Zen modu ve temel puanlamaydı. Sprint, Zamana Karşı, parça tutma, önizleme kuyruğu, tekrar izleme sistemi, T-Spin algılama — hepsi sonra geldi.

### Deneyin

SynthStack App Store'da ücretsiz. Tetris ve synthwave estetiğini seviyorsanız bir şans verin.

[SynthStack'i App Store'dan İndirin](https://apps.apple.com/us/app/synthstack-block-puzzle-game/id6504832555)

Geri bildiriminiz veya bulduğunuz hatalar varsa duymaktan memnuniyet duyarım.
