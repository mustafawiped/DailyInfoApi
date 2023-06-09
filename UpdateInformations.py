import json
import requests
import random
import base64

bilgiler = [
    "Her gün en az 8 saat uyumak sağlığımız için önemlidir.",
    "Düzenli egzersiz yapmak fiziksel ve zihinsel sağlığımızı destekler.",
    "Yeterli miktarda su içmek vücudun hidrasyonunu sağlar.",
    "Sevdiklerimize zaman ayırmak önemlidir, ilişkileri güçlendirir.",
    "Sağlıklı beslenmek vücudumuzun ihtiyaçlarını karşılamaya yardımcı olur.",
    "Stres yönetimi teknikleri uygulamak zihinsel sağlığı destekler.",
    "Pozitif düşünmek ruh sağlığımızı olumlu yönde etkiler.",
    "Günlük egzersiz yapmak enerji seviyemizi yükseltir.",
    "Düzenli olarak sevdiklerimize 'seni seviyorum' demek önemlidir.",
    "Gülümsemek sadece kendimize değil, çevremizdeki insanlara da iyi gelir.",
    "Kendimize zaman ayırmak kişisel gelişimimiz için önemlidir.",
    "İyi bir uyku için rahat bir uyku ortamı oluşturmak faydalıdır.",
    "Yeni şeyler öğrenmek zihinsel sağlığımızı geliştirir.",
    "İçtiğimiz suyun temiz ve güvenli olduğundan emin olmalıyız.",
    "Sevdiklerimize minnettarlık göstermek güçlü bir ilişkiyi destekler.",
    "Kitap okumak bilgi birikimimizi artırır.",
    "Hayatın küçük zevklerinin tadını çıkarmak mutluluk verir.",
    "Sağlıklı bir kahvaltı yapmak günün enerjik başlamasını sağlar.",
    "İnsanlarla empati kurmak anlayışımızı derinleştirir.",
    "Kötü bir gün geçirdiysek, olumlu bir şey bulmaya çalışmak önemlidir.",
    "Doğayla bağlantı kurmak huzur verir.",
    "Sevdiğimiz bir hobiyi yapmak bizi mutlu eder.",
    "Gülümsemek stresi azaltmaya yardımcı olur.",
    "Negatif düşünceleri olumlu düşüncelerle değiştirmek önemlidir.",
    "Minik molalar vermek verimliliği artırır.",
    "Hayal kurmak ve hedefler belirlemek motivasyon sağlar.",
    "Yürüyüşe çıkmak hem fiziksel hem de zihinsel sağlığa iyi gelir.",
    "Yaratıcı bir aktiviteye zaman ayırmak stresi azaltır.",
    "İş çıkışında rahatlama aktiviteleri yapmak önemlidir.",
    "Teşekkür etmek ve minnettarlık duygularını ifade etmek pozitif bir etki yaratır.",
    "Sağlıklı bir öğle yemeği yemek enerjimizi yükseltir.",
    "Sevdiklerimizle güzel anılar oluşturmak değerlidir.",
    "Düzenli olarak günlük plan yapmak organize olmamızı sağlar.",
    "Müzik dinlemek stresi azaltır ve ruh halini yükseltir.",
    "Kendimize küçük hedefler belirlemek motivasyon sağlar.",
    "Kendimize zaman ayırmak için haftada bir günü boş bırakmak faydalıdır.",
    "Sevdiğimiz bir şey üzerinde çalışmak bizi mutlu eder.",
    "Dışarıda vakit geçirmek doğanın güzelliğini keşfetmeye yardımcı olur.",
    "Gülümseyen insanlarla vakit geçirmek pozitif bir etki yaratır.",
    "İyi bir arkadaş olmak diğer insanlarla sağlıklı ilişkiler kurmayı destekler.",
    "İçsel sesimize kulak vermek ve kendimize iyi bakmak önemlidir.",
    "Bol bol su içmek cildimizin sağlıklı kalmasını sağlar.",
    "Hayatta şükran duyduğumuz şeyleri hatırlamak pozitif enerji verir.",
    "Yaratıcılığımızı kullanabileceğimiz bir hobi edinmek bizi mutlu eder.",
    "Güne meditasyon veya yoga ile başlamak zihinsel odaklanmayı artırır.",
    "İşyerinde kısa molalar vermek verimliliği artırır.",
    "Yeni bir şey denemek bizi geliştirir ve heyecan verir.",
    "İnsanlara yardım etmek kendimizi daha iyi hissetmemizi sağlar.",
    "İlham verici bir kitap okumak motivasyon sağlar.",
    "Kendimize zaman ayırırken sürekli bir hedef belirlemek önemlidir.",
    "Sevdiklerimizle sık sık güzel anılar biriktirmek değerlidir.",
    "Kendimize bol bol dinlenme ve gevşeme zamanı ayırmak önemlidir.",
    "Hoşumuza giden bir müzik dinlemek enerjimizi yükseltir.",
    "Bir şeyi başarmak için adım atmak bizi motive eder.",
    "İlham veren bir film izlemek motivasyon sağlar.",
    "Sevdiğimiz bir aktiviteyle zaman geçirmek stresi azaltır.",
    "Her gün için bir şükran listesi yapmak pozitif düşünmeye yardımcı olur.",
    "Kötü bir gün yaşadıysak, kendimize biraz zaman ayırmak önemlidir.",
    "İş yerinde ara sıra kısa bir yürüyüş yapmak enerji seviyemizi artırır.",
    "Hayatta küçük mutluluklar bulmak bizi motive eder.",
    "Sağlıklı bir atıştırmalık seçmek enerjimizi dengelemeye yardımcı olur.",
    "Kendimize olan güvenimizi artırmak için başarılardan öğrenmek önemlidir.",
    "Hobilerimize zaman ayırmak kişisel tatmini artırır.",
    "Kötü bir deneyimden ders çıkarmak kişisel gelişimi destekler.",
    "Sevdiklerimize sık sık sarılmak ve sevgimizi göstermek önemlidir.",
    "Olumlu bir sabah rutini oluşturmak günü iyi başlatmamıza yardımcı olur.",
    "Yeni bir beceri öğrenmek kendimize olan güvenimizi artırır.",
    "Başkalarının başarılarını kutlamak pozitif bir ortam yaratır.",
    "Bir hobiden zevk almak bizi rahatlatır ve stresten uzaklaştırır.",
    "İyi bir gece uykusu için rahat bir uyku ortamı oluşturmak önemlidir.",
    "Hayatımızda önemli olan insanlarla düzenli olarak iletişimde olmak değerlidir.",
    "Kişisel gelişim kitapları okumak bizi ileriye taşır.",
    "İçinde bulunduğumuz anın tadını çıkarmak anı yaşamayı öğretir.",
    "Düzenli olarak sevdiğimiz bir aktiviteyle zaman geçirmek bizi motive eder.",
    "İnsanları anlamak için empati kurmak önemlidir.",
    "Kendimize olumlu afirmasyonlar söylemek özgüvenimizi artırır.",
    "Yaratıcılığımızı serbest bırakacak bir sanat faaliyetiyle uğraşmak bizi rahatlatır.",
    "Hayatın tadını çıkarmak için kendimize zaman ayırmak önemlidir.",
    "Olumlu insanlarla zaman geçirmek enerjimizi yükseltir.",
    "Dışarı çıkıp doğayla bağlantı kurmak ruh halimizi iyileştirir.",
    "Zihnimizi sakinleştirmek için derin nefes almak önemlidir.",
    "Günlük bir güzel söz veya motivasyonel mesaj okumak moralimizi yükseltir.",
    "Stresten uzaklaşmak için meditasyon veya yoga yapmak faydalıdır.",
    "Yeni bir şey öğrenmek bizi heyecanlandırır ve geliştirir.",
    "Sevdiğimiz bir müzik parçasıyla coşmak bizi mutlu eder.",
    "İş yerinde takdir edildiğimizde kendimize olan güvenimiz artar.",
    "Bir gün içinde birkaç kez kısa bir mola vermek enerji seviyemizi dengelemeye yardımcı olur.",
    "Hayatta küçük başarıları kutlamak motivasyon sağlar.",
    "Kendimize iyi bakmak için düzenli olarak egzersiz yapmak önemlidir.",
    "Sevdiğimiz birine anlamlı bir hediye vermek sevgimizi gösterir.",
    "Olumlu bir günlük afilli bir not almak günümüzü aydınlatır.",
    "Kendimize olan saygımızı korumak için sınırlarımızı belirlemek önemlidir.",
    "Sağlıklı bir akşam yemeği yemek vücudumuza iyi gelir ve uyku kalitemizi artırır.",
    "Gönüllü çalışmalara katılmak topluma katkı sağlar ve bizi mutlu eder.",
    "Hedeflerimize ulaşmak için kendimize günlük adımlar belirlemek önemlidir.",
    "Sevdiklerimizle keyifli sohbetler etmek ilişkilerimizi güçlendirir.",
    "Zaman zaman telefon ve sosyal medya kullanımını kısıtlamak zihinsel dinginlik sağlar.",
    "Minnettarlık günlüğü tutmak bizi pozitif düşünmeye yönlendirir.",
    "Kendimize olan değerimizi bilmek ve takdir etmek önemlidir.",
    "Geçmişteki hatalardan ders çıkarmak ve ileriye odaklanmak kişisel büyümeyi destekler."
]

def guncelle_json(bilgiler):
    kullanici_adi = "HESAP_KULLANICIADI"
    parola = "HESAP_SIFRESI"
    erisim_belirtici = "HESAP_TOKENI"

    repository = "DailyInfoApi"
    dosya_yolu = "informations.json"

    data = random.choices(bilgiler, k=20)

    url = f"https://api.github.com/repos/{kullanici_adi}/{repository}/contents/{dosya_yolu}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"token {erisim_belirtici}"
    }
    auth = (kullanici_adi, parola)
    payload = {
        "message": "Bilgileri güncelle",
        "content": str(base64.b64encode(json.dumps(data).encode("utf-8")), "utf-8")
    }
    response = requests.put(url, headers=headers, auth=auth, json=payload)
    if response.status_code == 200:
        print("Bilgiler başarıyla güncellendi.")
    else:
        print("Bir hata oluştu. Bilgiler güncellenemedi.")

guncelle_json(bilgiler)
