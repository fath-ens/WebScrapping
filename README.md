# WebScrapping
Scrapy kütüphanesi ile web scrapping işlemi gerçekleştirilmiştir. Bu uygulama için scrapy ve pymongo kütüphaneleri kullanılmıştır.
Öncelikle projeye scrapy kütüphanesi dahil edilmelidir. Bunun için terminalden scrapy kütüphanesinin dosyalarını indirmemiz gerekmektedir. Bu işlem için aşağıdaki kod bloğu çalıştırılmıştır:

![image](https://github.com/fath-ens/WebScrapping/assets/56679812/0d7c6d5b-d219-4b50-91fd-24da6020f1de)

Sonraki aşamada bir scrapy projesi oluşturulmuştur. Terminal üzerinde aşağıdaki kod bloğu çalıştırılarak bir scrapy projesi oluşturulabilir:

![image](https://github.com/fath-ens/WebScrapping/assets/56679812/efeefafc-332d-436d-bb59-928a07776fa7)

Daha sonrasında oluşturmuş olduğumuz projede scraping işlemi gerçekleştirilecektir. Bunun için öncelikle örnek web siteleri kullanılması gerekmektedir. Biz bu projede "www.kitapsepeti.com" ve "www.kitapyurdu.com" adresleri üzerinden kitap listleme işlemi yapılacaktır.
Bu işlem için üç farklı nesne türü kullanılmıştır.
  1) start_url: Bu nesne içerisinde kitapların listediğinde adres belirtilmiştir.
  2) book: Adreste belirtilen html dosyasında kitapların yerini bildiren alandır. İki şekilde belirtilebilir. Bunlar css ve xpath metodlarıdır. Projede xpath kullanılmıştır.
  3) data: Kitapların listelenecek özellikleri seçimi ve JSON formatında dönüştürülmüştür halidir.

 Son işlem olarak JSON nesnelerimiz mongodb veritabanına işlenmiştir. Bu işlem üç adımda gerçekleştirilmiştir.
   1) Pymongo kütüphenesinin kurulması: Terminalde çalıştırılan aşağıdaki kod bloğu ile işlem gerçekleşmiştir.

      ![image](https://github.com/fath-ens/WebScrapping/assets/56679812/de93a06e-a622-4b2c-affd-f153005a81bc)

  2) Veritabanı bağlantılarının oluşturulması: Bu aşamada veritabanı adresi ve collection ismi verilmiştir.
  3) Verilerin veritabanına eklenmesi: insert_one() metodunun içerisinde JSON nesnesini belirterek bu adım gerçekleştirilmiştir.

Bu projenin çalıştırılması için terminalde şu kod bloğu takip edilmelidir:

![image](https://github.com/fath-ens/WebScrapping/assets/56679812/6fd999b8-966e-40ce-8bd9-fc82d8060f90)






