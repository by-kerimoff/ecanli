import requests
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Kanalların linklərini daxil edirik
channels = [
    {"name": "Xazartv", "url": "https://ecanlitv3.etvserver.com/xazartv.m3u8?tkn=9ctUTj5jLCkNmWD_OxakCg&tms=1740634051", "slug": "xazartv"}
]

M3U_FILE = "playlist.m3u"

# Tokenin yenilənməsi üçün saytı açırıq
def get_new_m3u8_link(channel_url):
    # ChromeOptions obyektini yaradın
    options = Options()
    options.add_argument("--headless")  # Başsız modda çalışsın

    # Chrome WebDriver yaradın
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(channel_url)
    
    # Bəzi saytlarda tokeni əldə etmək üçün sayfada müəyyən bir müddət gözləmək lazım ola bilər
    time.sleep(5)  # 5 saniyəlik gözləmə (bunu saytın yüklənmə sürətinə görə tənzimləyə bilərsiniz)

    try:
        # URL-dəki yeni tokeni əldə edirik
        token_link = driver.current_url
        return token_link
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
