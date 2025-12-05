import json
from collections import defaultdict

CLASSES = ["salmonella", "healthy", "coccidiosis", "new_castle_disease"]

input_path = "1salmonella_class1+2.jsonl"
output_path = "1non_salmonella_predictions.txt"

# 1. Gom các Q&A theo từng ảnh
qa_by_image = defaultdict(list)

with open(input_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        obj = json.loads(line)
        img = obj["img_path"]
        qa_by_image[img].append(obj)


def extract_label_for_image(qa_list):
    """
    Trả về 1 trong 4 class hoặc None
    """

    # Tách riêng câu hỏi nhận dạng (identity) và câu khác
    identity_qas = []
    other_qas = []

    for qa in qa_list:
        q = qa["question"].lower()
        if "which class" in q or "which disease class" in q:
            identity_qas.append(qa)
        else:
            other_qas.append(qa)

    def collect_positive_classes(qas):
        positives = set()
        for qa in qas:
            q = qa["question"].lower()
            a = qa["answer"].lower()

            for cls in CLASSES:
                # BỎ Q&A loại: "Why is this not X?"
                if f"not {cls}" in q:
                    continue

                # Nếu câu trả lời có chứa tên class → coi là signal dương
                if cls in a:
                    positives.add(cls)
        return positives

    # 2. Ưu tiên lấy class từ các câu identity trước
    positives = collect_positive_classes(identity_qas)

    # 3. Nếu chưa ra gì, mới nhìn sang các câu khác
    if not positives:
        positives = collect_positive_classes(other_qas)

    # 4. Quy tắc chọn nhãn cuối cùng
    if "salmonella" in positives:
        return "salmonella"
    else:
        # Nếu có class khác → lấy 1 class bất kỳ trong đó
        for cls in CLASSES:
            if cls in positives:
                return cls

    # Không tìm thấy class nào
    return None


# 5. Áp dụng cho toàn bộ ảnh
labels = {}
for img, qa_list in qa_by_image.items():
    labels[img] = extract_label_for_image(qa_list)

# 6. Ghi ra các ảnh KHÔNG phải salmonella
with open(output_path, "w", encoding="utf-8") as f:
    for img, cls in labels.items():
        if cls is not None and cls != "salmonella":
            f.write(f"{img}\t{cls}\n")

print("DONE.")
print("Total images:", len(labels))
print("Non-salmonella images:", sum(1 for c in labels.values() if c not in (None, "salmonella")))



