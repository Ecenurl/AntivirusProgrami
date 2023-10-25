from bs4 import BeautifulSoup, element #web sayfalarını çözümlemek ve verileri çekmek için kullanılan bir Python kütüphanesidir.Elements belirli bir etiketi temsil eden bir nesnedir
from selenium import webdriver #WebDriver modülünü içe aktarmak ve Web sitelerinden veri çekmek gibi amaçlarla kullanılır
from selenium.webdriver.chrome.options import Options #Selenium kütüphanesinin WebDriver'ı ile Chrome tarayıcısını kullanırken, Chrome tarayıcısının seçeneklerini yapılandırmak için kullanılır
import requests #HTTP istemcisi olarak kullanılarak web siteleri ile iletişim kurmayı ve web üzerinde veri alışverişi yapmayı sağlar.
import json #verileri insanlar tarafından okunabilir ve yazılabilir bir formatta temsil eden bir metin tabanlı veri değişim biçimidir.
import time # belirli zaman dilimlerini ölçmek, zaman damgaları eklemek, beklemek veya programınızın belirli bir hızda çalışmasını sağlamak gibi birçok uygulamada faydalıdır.
import os #işletim sistemi işlemleriyle ilgili işlevler sağlar. Bu modülü içe aktardığınızda, dosya ve dizin işlemleri, dosya yol işlemleri, çevre değişkenleri ve diğer işletim sistemi ile ilgili işlemleri gerçekleştirmek için kullanabilirsiniz.



#api kısmı
url = ('https://www.virustotal.com/vtapi/v2/file/scan') #Virustotal API'sini kullanarak dosya tarayıcı hizmetine bir dosya tarama isteği göndermek için kullanılır. 
os.system("cls") #Bu komut, komut istemini veya terminal penceresini temizlemek için kullanılır ve mevcut ekranın içeriğini temizler, yeni bir sayfa başlatır.
print("="*15+ "\n" + "Emrovsky Antivirus" + "\n" + "="*15 ) #"=" karakterini 15 kez Emrovsky Antivirus 15 adet = işareti yazdırarak bir çizgi çeker.
print("Taratacağınız dosyayı programın olduğu klasöre sürükleyin") #ekrana yazdırma
fileqwe = input("Lütfen taratılacak dosyanın adını giriniz : ")  #Kullanıcı metin girdisini yazdıktan sonra, bu girdi fileqwe adlı değişkene atanır. 
 
dosya = open("apikey.txt","r",encoding="utf-8") #"apikey.txt" adlı bir dosya açmak istendiğini gösterir."r" modu, dosyanın sadece okuma amaçlı açılacağını belirti.encoding="utf-8": Bu ifade, dosyanın karakter kodlamasını belirtir.
apikey = (dosya.readline()) #dosya.readline(): Bu ifade, açılmış olan dosya adlı dosyadan bir satırı okur.işleminin sonucunu apikey adlı bir değişkene atar. 

params = {'apikey': apikey}  #Bu kod, bir Python sözlüğü (params) oluşturur ve bu sözlüğün içine, daha önce bir dosyadan okunmuş olan bir API anahtarını (apikey) ekler.
 
files = {'file': (fileqwe, open(fileqwe, 'rb'))} #rb' modu, dosyanın ikili okuma modunda açılacağını belirtir. Bu, dosyanın metin veya ikili veriler içerebileceği anlamına gelir.veriyi düzenlemek ve iletmek amacıyla kullanılır.

response = requests.post(url, files=files, params=params) #"requests" kütüphanesini kullanarak bir HTTP POST isteği yapar.
data = json.loads(response.text) #HTTP isteği sonucu metin verisi içerirHTTP yanıtının içindeki JSON verisini Python veri yapısına dönüştürür ve bu dönüştürülmüş veriyi "data" adlı bir değişkene atar. Bu, JSON verisi içeren yanıtları işlemek ve bu verilere Python programı içinde erişmek için yaygın olarak kullanılır.
linkkk = data['permalink'] #JSON verileri veya başka bir sözlük yapısından özgün verilere erişmek ve bu verileri daha fazla işlem yapmak veya görüntülemek için kullanılır
print("Virus taraması sonuçları 2 dakika içerisinde bu linkte olacaktır " +linkkk) #Örneğin, eğer "linkkk" değeri "https://www.example.com/results" ise, mesaj şu şekilde görünecektir:
time.sleep(5) #time.sleep kullanarak işlem aralarına zaman geciktirmesi ekleyebilirsiniz.

#api kısmı

#indiriliyor animasyon ok işareti (>) eklenir. Bu, kullanıcıya dosyanın yüklenmekte olduğu izlenimi verir.
a = 1
b = "="
c = ">"
dosya = "Dosya yükleniyor... "


while True:
    a += 1
    print(dosya+b*a+c)
    time.sleep(1)
    os.system("cls")
    if a == 150:
        os.system("ping " + linkkk)
        os.system("cls")
        os.system("ping " + linkkk)
        os.system("cls")
        os.system("ping " + linkkk)
        os.system("cls")
        os.system("ping " + linkkk)
        os.system("cls")
        os.system("ping " + linkkk)
        os.system("cls")
        break
#indiriliyor animasyonu


weblink = linkkk


if weblink.endswith("/details"):
    weblink = weblink.replace("/details", "/summary")  #dizesindeki "/details" alt dizesini "/summary" ile değiştirir. Yani, eğer URL "/details" ile bitiyorsa, bu kod URL'yi "/summary" ile değiştir

option = Options()
option.headless = True
driver = webdriver.Chrome(executable_path='C:/Users/yilma/OneDrive/Masaüstü/project/python/chrome.exe',options=option) #Chrome tarayıcısını başlatır ve kullanıcı arayüzü olmadan web otomasyon işlemleri gerçekleştirmenize olanak tanır. Headless mod, web sayfalarını açmak, veri kazımı (scrapping), test otomasyonu ve diğer otomasyon işlemleri için kullanışlıdır.

driver.get(weblink) #Bu kod, Selenium WebDriver kullanarak bir web tarayıcısının belirtilen URL'ye gitmesini sağlar.

def expand_shadow_element(element):
  shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root  #Bu fonksiyon, shadow DOM içeriği ile etkileşimde bulunmak istediğinizde veya shadow DOM içeriğine erişmek istediğinizde kullanılır. Shadow DOM içeriği, web uygulamalarının daha iyi bileşenleştirilmesi ve izole edilmesi gereken durumlarda sıkça kullanılır.

#the above becomes 
shadow_section = expand_shadow_element(driver.find_element_by_tag_name("file-view"))
shadow_section2 = expand_shadow_element(shadow_section.find_element_by_css_selector('vt-ui-main-generic-report'))
shadow_section3 = expand_shadow_element(shadow_section2.find_element_by_css_selector('vt-ui-detections-widget'))
html = shadow_section3.get_attribute('innerHTML')
driver.close()
soup = BeautifulSoup(html, "lxml")
div = soup.find('div', {'class':"engines"})

informations = str(div.text)
informations = informations.replace(" ", "")
os.system("cls")
print("Sonuçlar Aşağıdaki Gibidir" + "\n")
print("="*15+f"\n Virüs bulunan/Antivirüs programı: {informations}\n"+"="*15)
print("Hangi antivirüs programları virüs algılaşmış daha detaylı bakmak için : " + linkkk) #Bu kod, bir web sayfasının içeriğini shadow DOM kullanarak çekmek ve bu içeriği işlemek için kullanılır. Bu tür işlemler özellikle web otomasyonu ve veri çekimi için önemlidir.Shadow DOM (Gölge DOM), HTML ve CSS içeriğinin daha iyi izole edilmesini ve yönetilmesini sağlayan bir web teknolojisi türüdür. 