from PIL import Image
import os
import sys

if len(sys.argv) < 2:
    print("Usage: python imgsize.py <folder_path>")
    sys.exit(1)

folder = sys.argv[1]

max_width = 1200
jpeg_quality = 85
png_optimize = True
MIN_SIZE_BYTES = 1 * 1024 * 1024  # 1 MB

for filename in os.listdir(folder):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    path = os.path.join(folder, filename)

    if os.path.getsize(path) < MIN_SIZE_BYTES:
        print(f"Skipped (too small): {filename}")
        continue

    ext = os.path.splitext(filename)[1].lower()

    with Image.open(path) as img:
        w, h = img.size
        if w > max_width:
            new_h = int(h * max_width / w)
            img = img.resize((max_width, new_h), Image.LANCZOS)

        if ext in (".jpg", ".jpeg"):
            if img.mode in ("RGBA", "LA", "P"):
                img = img.convert("RGBA")
                bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
                img = Image.alpha_composite(bg, img).convert("RGB")
            else:
                img = img.convert("RGB")

            img.save(path, format="JPEG", optimize=True, quality=jpeg_quality)

        elif ext == ".png":
            img.save(path, format="PNG", optimize=png_optimize)

    print(f"Processed: {filename}")

print("All done.")

