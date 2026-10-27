# ============================================================
# HTML SCANNER
# Digunakan untuk memeriksa struktur HTML sebuah website
# ============================================================

import requests
import sys
from bs4 import BeautifulSoup
from collections import Counter


URL = input("Masukkan URL website: ")

print("\nMengakses website...")
print("URL:", URL)


# Mengambil HTML dari website

try:
    response = requests.get(
        URL,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    print("Status code:", response.status_code)
    response.raise_for_status()

except requests.RequestException as error:
    print("Gagal mengakses website.")
    print("Error:", error)
    sys.exit()


soup = BeautifulSoup(response.text, "html.parser")

print("HTML berhasil dibaca.")


# Menghitung semua tag HTML

tags = [tag.name for tag in soup.find_all()]
tag_counts = Counter(tags)

print("\n" + "=" * 60)
print("DAFTAR TAG HTML")
print("=" * 60)

for tag_name, jumlah in tag_counts.most_common():
    print(f"{tag_name:<20} {jumlah}")


# Menghitung semua class HTML

class_counts = Counter()

for tag in soup.find_all():
    classes = tag.get("class", [])

    for class_name in classes:
        class_counts[class_name] += 1

print("\n" + "=" * 60)
print("DAFTAR CLASS HTML")
print("=" * 60)

if class_counts:
    for class_name, jumlah in class_counts.most_common():
        print(f"{class_name:<30} {jumlah}")
else:
    print("Tidak ditemukan class.")


# Menghitung semua ID HTML

id_counts = Counter()

for tag in soup.find_all():
    tag_id = tag.get("id")

    if tag_id:
        id_counts[tag_id] += 1

print("\n" + "=" * 60)
print("DAFTAR ID HTML")
print("=" * 60)

if id_counts:
    for id_name, jumlah in id_counts.most_common():
        print(f"{id_name:<30} {jumlah}")
else:
    print("Tidak ditemukan ID.")


# Menghitung penggunaan atribut HTML

attribute_counts = Counter()

for tag in soup.find_all():
    for attribute_name in tag.attrs:
        attribute_counts[attribute_name] += 1

print("\n" + "=" * 60)
print("DAFTAR ATRIBUT HTML")
print("=" * 60)

for attribute_name, jumlah in attribute_counts.most_common():
    print(f"{attribute_name:<30} {jumlah}")


# Menampilkan link HTML

links = soup.find_all("a")

print("\n" + "=" * 60)
print("LINK / <a>")
print("=" * 60)
print("Jumlah link:", len(links))

for nomor, link in enumerate(links[:20], start=1):
    text_link = link.get_text(" ", strip=True)
    alamat_link = link.get("href")

    print(f"\n{nomor}. Text : {text_link}")
    print(f"   Href : {alamat_link}")


# Menampilkan gambar HTML

images = soup.find_all("img")

print("\n" + "=" * 60)
print("GAMBAR / <img>")
print("=" * 60)
print("Jumlah gambar:", len(images))

for nomor, image in enumerate(images[:20], start=1):
    sumber_gambar = image.get("src")
    teks_alt = image.get("alt")

    print(f"\n{nomor}. SRC : {sumber_gambar}")
    print(f"   ALT : {teks_alt}")


# Menampilkan informasi tabel HTML

tables = soup.find_all("table")

print("\n" + "=" * 60)
print("TABEL / <table>")
print("=" * 60)
print("Jumlah tabel:", len(tables))

for nomor, table in enumerate(tables, start=1):
    table_class = table.get("class")
    table_id = table.get("id")
    jumlah_baris = len(table.find_all("tr"))

    print(f"\nTabel {nomor}")
    print("Class :", table_class)
    print("ID    :", table_id)
    print("Baris :", jumlah_baris)


# Menampilkan informasi form HTML

forms = soup.find_all("form")

print("\n" + "=" * 60)
print("FORM / <form>")
print("=" * 60)
print("Jumlah form:", len(forms))

for nomor, form in enumerate(forms, start=1):
    action = form.get("action")
    method = form.get("method")

    print(f"\nForm {nomor}")
    print("Action :", action)
    print("Method :", method)


# Menampilkan struktur HTML secara bertingkat

def tampilkan_struktur(element, level=0, batas_level=3):
    if element is None or level > batas_level:
        return

    if element.name is None:
        return

    indentasi = "  " * level
    informasi = element.name

    classes = element.get("class")
    tag_id = element.get("id")

    if classes:
        informasi += f" class={classes}"

    if tag_id:
        informasi += f" id={tag_id}"

    print(indentasi + informasi)

    for child in element.find_all(recursive=False):
        tampilkan_struktur(
            child,
            level + 1,
            batas_level
        )


print("\n" + "=" * 60)
print("CONTOH STRUKTUR HTML")
print("=" * 60)

tampilkan_struktur(soup.html)


# Menampilkan ringkasan hasil scanning

print("\n" + "=" * 60)
print("RINGKASAN HTML")
print("=" * 60)

print("URL              :", URL)
print("Status code      :", response.status_code)
print("Ukuran HTML      :", len(response.text), "karakter")
print("Jumlah tag       :", len(tags))
print("Jenis tag        :", len(tag_counts))
print("Jumlah class     :", len(class_counts))
print("Jumlah ID        :", len(id_counts))
print("Jenis atribut    :", len(attribute_counts))
print("Jumlah link      :", len(links))
print("Jumlah gambar    :", len(images))
print("Jumlah tabel     :", len(tables))
print("Jumlah form      :", len(forms))

print("=" * 60)
print("Scanning selesai.")
print("=" * 60)
