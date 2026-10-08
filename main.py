# ============================================================
# HTML SCANNER
# Digunakan untuk memeriksa struktur HTML sebuah website
# ============================================================

import requests
from bs4 import BeautifulSoup
from collections import Counter


# ============================================================
# 1. INPUT URL
# ============================================================

URL = input("Masukkan URL website: ")

print("\nMengakses website...")
print("URL:", URL)


# ============================================================
# 2. MENGAMBIL HTML
# ============================================================

try:

    response = requests.get(
        URL,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=10
    )

    print("Status code:", response.status_code)

except requests.RequestException as e:

    print("Gagal mengakses website.")
    print("Error:", e)

    exit()


# ============================================================
# 3. MEMBUAT SOUP
# ============================================================

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

print("HTML berhasil dibaca.")


# ============================================================
# 4. MENGHITUNG SEMUA TAG
# ============================================================

tags = [
    tag.name
    for tag in soup.find_all()
]

tag_counts = Counter(tags)


print("\n")
print("=" * 60)
print("DAFTAR TAG HTML")
print("=" * 60)

for tag, jumlah in tag_counts.most_common():

    print(f"{tag:<20} {jumlah}")


# ============================================================
# 5. MENCARI SEMUA CLASS
# ============================================================

class_counts = Counter()

for tag in soup.find_all():

    classes = tag.get("class")

    if classes:

        for class_name in classes:

            class_counts[class_name] += 1


print("\n")
print("=" * 60)
print("DAFTAR CLASS HTML")
print("=" * 60)

if class_counts:

    for class_name, jumlah in class_counts.most_common():

        print(f"{class_name:<30} {jumlah}")

else:

    print("Tidak ditemukan class.")


# ============================================================
# 6. MENCARI SEMUA ID
# ============================================================

id_counts = Counter()

for tag in soup.find_all():

    tag_id = tag.get("id")

    if tag_id:

        id_counts[tag_id] += 1


print("\n")
print("=" * 60)
print("DAFTAR ID HTML")
print("=" * 60)

if id_counts:

    for id_name, jumlah in id_counts.most_common():

        print(f"{id_name:<30} {jumlah}")

else:

    print("Tidak ditemukan ID.")


# ============================================================
# 7. MENCARI SEMUA ATRIBUT
# ============================================================

attribute_counts = Counter()

for tag in soup.find_all():

    for attribute in tag.attrs:

        attribute_counts[attribute] += 1


print("\n")
print("=" * 60)
print("DAFTAR ATRIBUT HTML")
print("=" * 60)

for attribute, jumlah in attribute_counts.most_common():

    print(f"{attribute:<30} {jumlah}")


# ============================================================
# 8. MENCARI SEMUA LINK
# ============================================================

links = soup.find_all("a")

print("\n")
print("=" * 60)
print("LINK / <a>")
print("=" * 60)

print("Jumlah link:", len(links))

for i, link in enumerate(links[:20], start=1):

    text = link.get_text(" ", strip=True)

    href = link.get("href")

    print(f"\n{i}. Text : {text}")
    print(f"   Href : {href}")


# ============================================================
# 9. MENCARI SEMUA GAMBAR
# ============================================================

images = soup.find_all("img")

print("\n")
print("=" * 60)
print("GAMBAR / <img>")
print("=" * 60)

print("Jumlah gambar:", len(images))

for i, image in enumerate(images[:20], start=1):

    src = image.get("src")

    alt = image.get("alt")

    print(f"\n{i}. SRC : {src}")
    print(f"   ALT : {alt}")


# ============================================================
# 10. MENCARI SEMUA TABEL
# ============================================================

tables = soup.find_all("table")

print("\n")
print("=" * 60)
print("TABEL / <table>")
print("=" * 60)

print("Jumlah tabel:", len(tables))

for i, table in enumerate(tables, start=1):

    table_class = table.get("class")

    table_id = table.get("id")

    rows = table.find_all("tr")

    print(f"\nTabel {i}")
    print("Class :", table_class)
    print("ID    :", table_id)
    print("Baris :", len(rows))


# ============================================================
# 11. MENCARI FORM
# ============================================================

forms = soup.find_all("form")

print("\n")
print("=" * 60)
print("FORM / <form>")
print("=" * 60)

print("Jumlah form:", len(forms))

for i, form in enumerate(forms, start=1):

    action = form.get("action")

    method = form.get("method")

    print(f"\nForm {i}")
    print("Action :", action)
    print("Method :", method)


# ============================================================
# 12. CONTOH STRUKTUR HTML
# ============================================================

print("\n")
print("=" * 60)
print("CONTOH STRUKTUR HTML")
print("=" * 60)


def tampilkan_struktur(element, level=0, maksimal=3):

    if level > maksimal:
        return

    if not hasattr(element, "name") or element.name is None:
        return

    indent = "  " * level

    class_name = element.get("class")

    tag_id = element.get("id")

    informasi = element.name

    if class_name:

        informasi += f" class={class_name}"

    if tag_id:

        informasi += f" id={tag_id}"

    print(indent + informasi)

    for child in element.find_all(recursive=False):

        tampilkan_struktur(
            child,
            level + 1,
            maksimal
        )


tampilkan_struktur(
    soup.html,
    maksimal=3
)


# ============================================================
# 13. RINGKASAN
# ============================================================

print("\n")
print("=" * 60)
print("RINGKASAN HTML")
print("=" * 60)

print("URL              :", URL)
print("Status code      :", response.status_code)
print("Ukuran HTML      :", len(response.text), "karakter")
print("Jumlah tag       :", len(tags))
print("Jenis tag        :", len(tag_counts))
print("Jumlah class     :", len(class_counts))
print("Jumlah ID        :", len(id_counts))
print("Jumlah atribut   :", len(attribute_counts))
print("Jumlah link      :", len(links))
print("Jumlah gambar    :", len(images))
print("Jumlah tabel     :", len(tables))
print("Jumlah form      :", len(forms))

print("=" * 60)
print("Scanning selesai.")
print("=" * 60)
