import qrcode
import os

# Create qrcodes directory if it doesn't exist
os.makedirs('qrcodes', exist_ok=True)

# Chapter data for Rene 3.14 - Tome 1
chapters = [
    (1, "Bruit Omega"),
    (2, "Barèmes inviolables"),
    (3, "Dette Géné-René"),
    (4, "Mécanismes d'avant-garde"),
    (5, "Calendrier Polaris"),
    (6, "Polyphonie des Cercles"),
    (7, "Année du Dénombrement"),
    (8, "Seconde Marée (Profonds)"),
    (9, "Chasse aux Profonds"),
    (10, "Pari Post-Ego")
]

# Generate QR codes
for chapter_num, chapter_title in chapters:
    # Create QR code
    url = f"https://renereviens-hue.github.io/rene314-book/chapitres/resume-ch{chapter_num}.pdf"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save image
    filename = f'qrcodes/qr_ch{chapter_num:02d}_{chapter_title.replace(" ", "_").replace("(", "").replace(")", "")}.png'
    img.save(filename)
    print(f"✓ Generated: {filename} → {url}")

print("\n✓ All 10 QR codes generated successfully!")
print("Location: /qrcodes/")