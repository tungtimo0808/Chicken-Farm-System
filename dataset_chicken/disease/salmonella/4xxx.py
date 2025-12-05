import os
import shutil

# File chứa danh sách ID cần move
id_file = "non_salmonella_ids.txt"

# Folder chứa ảnh gốc
source_folder = r"D:\Dự đoán bệnh ở gà\Chicken-Farm-System\dataset_chicken\disease\salmonella"

# Folder backup để lưu ảnh bị loại
backup_folder = r"D:\Dự đoán bệnh ở gà\Chicken-Farm-System\dataset_chicken\disease\salmonella\not_salmonella"
os.makedirs(backup_folder, exist_ok=True)

moved = 0

# Đọc từng ID và move ảnh tương ứng
with open(id_file, "r", encoding="utf-8") as f:
    for line in f:
        img_id = line.strip()
        if not img_id:
            continue

        # Tạo tên file ảnh
        file_name = f"salmonella_{img_id}.jpg"

        # Đường dẫn gốc → backup
        src = os.path.join(source_folder, file_name)
        dst = os.path.join(backup_folder, file_name)

        # Kiểm tra và move
        if os.path.exists(src):
            shutil.move(src, dst)
            moved += 1
            print(f"📦 Moved: {src}  →  {dst}")
        else:
            print(f"⚠️ Not found: {src}")

print("\nDONE. Moved", moved, "files into", backup_folder)
