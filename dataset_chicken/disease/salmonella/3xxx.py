import re

input_path = "1non_salmonella_predictions.txt"
output_path = "1non_salmonella_ids.txt"

ids = []

with open(input_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        # Tìm số sau salmonella_
        match = re.search(r"salmonella_(\d+)\.jpg", line)
        if match:
            ids.append(match.group(1))

# Xuất ra file (mỗi số 1 dòng)
with open(output_path, "w", encoding="utf-8") as f:
    for img_id in ids:
        f.write(img_id + "\n")

print("DONE. Extracted", ids, "IDs.")
