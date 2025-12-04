import re

input_file = "1salmonella_final copy.jsonl"            # file jsonl gốc
output_file = "cleaned_paths.jsonl"   # file xuất ra với path đã rút gọn

# regex để cắt phần path trước dataset_chicken
pattern = re.compile(r'"img_path":\s*"[^"]*dataset_chicken')

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:

    for line in infile:
        # tìm và thay bằng phần rút gọn
        new_line = pattern.sub('"img_path": "dataset_chicken', line)
        outfile.write(new_line)

print("✔ Done! All img_path have been shortened.")
