import pillow_avif  # bắt buộc import dòng này để bật AVIF support
from PIL import Image
import os

folder = r"D:\Dự đoán bệnh ở gà\Chicken-Farm-System\dataset_chicken\head\avian_influenza"

files_to_convert = [
    "ai_head_154.jpg",
    "ai_head_157.jpg",
    "ai_head_162.jpg",
    "ai_head_166.jpg",
    "ai_head_169.jpg",
    "ai_head_177.jpg",
    "ai_head_182.jpg"
]

bad_files = []

for filename in files_to_convert:
    path = os.path.join(folder, filename)

    if not os.path.exists(path):
        bad_files.append((filename, "File does not exist"))
        continue

    try:
        img = Image.open(path)
        img = img.convert("RGB")
        img.save(path, "JPEG", quality=95)
        print(f"Đã convert: {filename}")

    except Exception as e:
        bad_files.append((filename, str(e)))

print("\n❌ Những file không convert được:")
for f, err in bad_files:
    print(f"- {f}  --> {err}")
