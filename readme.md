## API bilgisi

- informations.json Dosyası her 6 saatte bir güncellenen 20 tane rastgele bilgi içeren bir JSON dosyasıdır.
- Günlük bilgileri göstermek istediğiniz projelerinizde kullanabileceğiniz bir kaynak.

## Kurulum

- UpdateInformation.py dosyasını kendinize uygun şekilde düzenleyin ve informations.json dosyasını kendi GitHub hesabınıza yükleyin.
- Herhangi bir sanal sunucu veya heroku gibi bulut tabanlı platform sitelerinden UpdateInformations.py dosyasını her 6 saatte bir çalışacak şekilde ayarlayın. 

## Kullanım

- Projenizde ApiKey kısmına https://raw.githubusercontent.com/{kullanici_adi}/{repository_adi}/main/informations.json yazmanız yeterli olacaktır.

Örnek ApiKey çıktısı:
```json
{
  "Birinci rastgele bilgi...",
  "İkinci rastgele bilgi...",
  "Üçüncü rastgele bilgi...",
  // Diğer 17 bilgi...
}
```

### Başarılar!
