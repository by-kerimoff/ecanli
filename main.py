import re

# URL və token dəyişdirmə funksiyası
def get_new_token(url):
    # URL-dəki tokeni tapmaq üçün reg-ex istifadə edirik
    token_pattern = r'token=([a-zA-Z0-9\-]+)'
    match = re.search(token_pattern, url)
    
    if match:
        token = match.group(1)
        # Burada yeni tokeni təyin edirik
        new_token = "yeni_token"  # Yeni tokeni buraya daxil edin
        new_url = url.replace(token, new_token)
        return new_url
    else:
        return None

# Yeni URL və m3u faylı yaratmaq
def create_m3u(new_url):
    with open("new_channel.m3u", "w") as f:
        f.write("#EXTM3U\n")
        f.write("#EXTINF:-1, Yeni Kanal\n")
        f.write(new_url + "\n")

# Başlanğıc URL
old_url = "https://str.yodacdn.net/ictimai/tracks-v1a1/mono.ts.m3u8?token=104ca719e0399569043c15302ab129afb1d7e370-264b3bed0324abbee29655f6101cf29b-1740642099-1740631299"
new_url = get_new_token(old_url)

if new_url:
    create_m3u(new_url)
    print("Yeni kanal m3u faylı yaradıldı!")
else:
    print("Token tapılmadı!")
