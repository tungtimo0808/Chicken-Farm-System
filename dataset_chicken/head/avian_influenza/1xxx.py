import os

def count_images(folder_path, recursive=False):
    # Các định dạng ảnh cần đếm
    valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.webp', '.avif', '.tiff', '.gif', '.heic'}

    count = 0

    if recursive:
        # Đếm cả trong thư mục con
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if os.path.splitext(file)[1].lower() in valid_extensions:
                    count += 1
    else:
        # Chỉ đếm trong thư mục chính
        for file in os.listdir(folder_path):
            if os.path.splitext(file)[1].lower() in valid_extensions:
                count += 1

    return count


# ---- Ví dụ sử dụng ----
folder = r"D:\Dự đoán bệnh ở gà\Chicken-Farm-System\dataset_chicken\head\avian_influenza"

print("Ảnh trong folder (không tính folder con):", count_images(folder, recursive=False))
print("Ảnh trong folder (bao gồm tất cả thư mục con):", count_images(folder, recursive=True))
