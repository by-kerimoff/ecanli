import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Kanalların URL-lərini daxil edirik
channels = [
    {"name": "Xezer TV", "url": "https://www.ecanlitvizle.app/xezer-tv-canli-izle/", "slug": "xezer-tv"}
]

M3U_FILE = "playlist.m3u"

# Saytdan yeni tokeni əldə etmək üçün funksiyanı yazırıq
def get_new_m3u8_link(channel_url):
    # ChromeOptions obyektini yaradın
    options = Options()
    options.add_argument("--headless")  # Başsız modda çalışsın

    # WebDriver servisi yaradın
    service = Service(ChromeDriverManager().install())

    # WebDriver obyektini yalnız `options` və `service` ilə yaradın
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(channel_url)
    
    # Sayfanın tam yüklənməsini gözləyirik
    time.sleep(5)  # Saytın yüklənməsi üçün gözləmə (bunu saytın yüklənmə sürətinə görə tənzimləyə bilərsiniz)
    
    # JavaScript ilə tokeni əldə edirik
    try:
        # Saytdakı canlı yayının URL-lərini alırıq
        video_url = driver.find_element_by_xpath('//*[@id="embed_player"]/iframe').get_attribute("src")
        if video_url:
            return video_url
        else:
            print(f"❌ Xezer TV üçün link tapılmadı.")
            return None
    except Exception as e:
        print(f"❌ Xəta: {e} | Kanal: {channel_url}")
        return None
    finally:
        driver.quit()

# Playlist faylını yeniləyirik
with open(M3U_FILE, "w", encoding="utf-8") as m3u:
    m3u.write("#EXTM3U\n")
    
    for channel in channels:
        new_m3u8_link = get_new_m3u8_link(channel["url"])
        
        if new_m3u8_link:
            m3u.write(f"#EXTINF:-1, {channel['name']}\n")
            m3u.write(f"{new_m3u8_link}\n")
        else:
            print(f"❌ Kanal linki yenilənmədi: {channel['name']}")

print(f"✅ M3U playlist yeniləndi: {M3U_FILE}")
