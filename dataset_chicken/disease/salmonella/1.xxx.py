output_file = "D:\Dự đoán bệnh ở gà\Chicken-Farm-System\dataset_chicken\disease\salmonella\1.annotations_salmonella1.jsonl"

with open(output_file, "w", encoding="utf-8") as f:
    for i in range(1, 10):  # từ 1 đến 1000
        image_path = f"salmonella_{i}.jpg"

        # Tạo 6 dòng Q&A rỗng cho mỗi ảnh
        for _ in range(6):
            entry = {
                "image": image_path,
                "question": "",
                "answer": ""
            }
            f.write(str(entry).replace("'", '"') + "\n")

        # Thêm một dòng trống giữa các ảnh
        f.write("\n")

print("Done! File annotations_salmonella.jsonl đã được tạo.")
