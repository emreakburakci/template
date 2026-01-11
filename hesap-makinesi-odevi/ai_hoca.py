# Dosya adı: ai_hoca.py
import os
import google.generativeai as genai

# GitHub'dan gelen API anahtarını al
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("API Key bulunamadı, AI yorumu yapılamıyor.")
    exit()

# Gemini Ayarları
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash') # Hızlı ve ücretsiz model

# Öğrencinin kodunu oku
try:
    with open("main.py", "r", encoding="utf-8") as file:
        ogrenci_kodu = file.read()
except FileNotFoundError:
    print("Kod dosyası bulunamadı.")
    exit()

# Yapay Zekaya Gönderilecek Emir (Prompt)
prompt = f"""
Sen deneyimli bir Senior Software Developer'sın. Aşağıdaki Python kodunu bir Junior Developer yazdı.
Kodu incele ve sadece şunları yap:
1. Kodun okunabilirliği ve değişken isimlendirmeleri hakkında kısa bir yorum yap.
2. Varsa daha iyi/modern bir yazım şekli öner (Pythonic way).
3. Çok sert olma, motive edici ve öğretici ol.
4. Yanıtın Türkçe olsun ve maksimum 3-4 cümle olsun.

İşte Kod:
{ogrenci_kodu}
"""

# Cevabı al ve yazdır
response = model.generate_content(prompt)
print(response.text)