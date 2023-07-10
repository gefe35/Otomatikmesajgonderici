from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# WhatsApp Web sayfasını aç
from selenium import webdriver

# WebDriver dosyasının konumunu belirtin
driver_path = "path/to/chromedriver.exe"

# WebDriver'ı başlatın
driver = webdriver.Chrome(executable_path=driver_path)

# Kodunuzun geri kalanını buraya ekleyin
# ...

# WebDriver'ı kapatın
driver.quit()

driver.get('https://web.whatsapp.com')

# Kullanıcıya WhatsApp QR kodunu taraması için zaman ver
time.sleep(15)

# Mesaj göndermek istediğiniz kişinin adını veya grubun adını burada belirtin
receiver_name = "Alıcı İsmi"

# Mesaj içeriğini burada belirtin
message_content = "Merhaba! Bu bir otomatik mesajdır."

# Alıcının veya grubun bulunduğu elementi bulmak için XPATH kullanarak arama yapın
search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
search_box.send_keys(receiver_name)
search_box.send_keys(Keys.ENTER)

# Mesaj kutusunu bul ve mesajı gönder
message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
message_box.send_keys(message_content)
message_box.send_keys(Keys.ENTER)

# İşlem tamamlandıktan sonra tarayıcıyı kapat
time.sleep(5)
driver.quit()
