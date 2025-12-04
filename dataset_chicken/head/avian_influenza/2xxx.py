import os
import hashlib

# ======================= CONFIG =======================
DATASET_FOLDER = r"D:\Dự đoán bệnh ở gà\Chicken-Farm-System\dataset_chicken\head\avian_influenza"
# =======================================================

def get_file_hash(path):
    """Tính MD5 hash của file."""
    hasher = hashlib.md5()
    with open(path, "rb") as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

duplicates = {}     # hash → [list các ảnh trùng]
hash_map = {}        # hash → ảnh đầu tiên

print("🔍 Đang quét dataset, vui lòng đợi...")

for root, _, files in os.walk(DATASET_FOLDER):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.webp')):
            img_path = os.path.join(root, file)
            file_hash = get_file_hash(img_path)

            if file_hash in hash_map:
                # đã thấy hash này trước đó → trùng
                if file_hash not in duplicates:
                    duplicates[file_hash] = [hash_map[file_hash]]
                duplicates[file_hash].append(img_path)
            else:
                hash_map[file_hash] = img_path

# ======================= OUTPUT =======================

if duplicates:
    print("\n⚠️ CÓ ẢNH TRÙNG LẶP TRONG DATASET:\n")
    for h, paths in duplicates.items():
        print(f"🔑 Hash: {h}")
        for p in paths:
            print("   →", p)
        print("-" * 50)
else:
    print("\n✅ Dataset sạch — KHÔNG có ảnh trùng!")
