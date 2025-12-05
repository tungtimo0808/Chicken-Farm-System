import json

input_file = "1Avian_influenza.jsonl"
output_file = "1AI_not_influenza_2.txt"

# Tập chứa ảnh không phải AI
not_ai_images = set()

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        try:
            item = json.loads(line)
        except:
            continue
        
        # Điều kiện: tìm QUESTION STAGE 1 - câu số 3
        if item["question"].strip().startswith("Based on the visible lesions"):
            if item["answer"].strip().lower() == "another disease":
                not_ai_images.add(item["img_path"])

# Lưu danh sách vào file
with open(output_file, "w", encoding="utf-8") as f:
    for img in sorted(not_ai_images):
        f.write(img + "\n")

print("🎯 Số ảnh không phải Avian Influenza:", len(not_ai_images))
print("📁 Lưu danh sách tại:", output_file)
