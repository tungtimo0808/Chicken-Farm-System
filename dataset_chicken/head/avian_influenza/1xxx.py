import os
import hashlib

def file_hash(path):
    hasher = hashlib.md5()    # hoặc dùng hashlib.sha256()
    with open(path, "rb") as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def check_duplicate(new_image_path, folder_path):
    new_hash = file_hash(new_image_path)

    for root, _, files in os.walk(folder_path):
        for file in files:
            existing_path = os.path.join(root, file)
            if file_hash(existing_path) == new_hash:
                return True, existing_path

    return False, None

# ==============================
# Example
new_img = r"D:\Dự đoán bệnh ở gà\Chicken-Farm-System\dataset_chicken\head\avian_influenza\ai_head_142.jpg"
dataset_folder = r"D:\Dự đoán bệnh ở gà\Chicken-Farm-System\dataset_chicken\head\avian_influenza"

is_dup, dup_path = check_duplicate(new_img, dataset_folder)

if is_dup:
    print("⚠️ Ảnh trùng:", dup_path)
else:
    print("✅ Không trùng!")
