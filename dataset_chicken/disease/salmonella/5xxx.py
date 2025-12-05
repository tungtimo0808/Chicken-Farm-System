import json

id_file = "non_salmonella_ids.txt"
input_jsonl = "1salmonella_class1+2.jsonl"
output_jsonl = "2salmonella_class1+2.jsonl"

# Đọc danh sách ID cần loại
remove_ids = set()
with open(id_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            remove_ids.add(line)

# Tạo prefix ảnh
# VD: ID 56 → salmonella_56.jpg
remove_files = {f"salmonella_{img_id}.jpg" for img_id in remove_ids}

kept = 0
removed = 0

with open(input_jsonl, "r", encoding="utf-8") as fin, \
     open(output_jsonl, "w", encoding="utf-8") as fout:
    
    for line in fin:
        line = line.strip()
        if not line:
            continue
        
        obj = json.loads(line)
        img_path = obj["img_path"]           # ví dụ: dataset_chicken/.../salmonella_56.jpg
        file_name = img_path.split("/")[-1]  # lấy tên ảnh
        
        # Nếu ảnh nằm trong danh sách cần xoá → bỏ qua
        if file_name in remove_files:
            removed += 1
            continue
        
        # Ngược lại → ghi giữ lại
        fout.write(line + "\n")
        kept += 1

print("DONE.")
print("JSON kept:", kept)
print("JSON removed:", removed)
