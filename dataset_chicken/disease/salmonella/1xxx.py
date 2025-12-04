input_file = "1salmonella_tier3.jsonl"           # file gốc
output_file = "cleaned_output.jsonl" # file sạch không có dòng trống

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:

    for line in infile:
        if line.strip():  # chỉ ghi nếu dòng KHÔNG trống
            outfile.write(line)

print("Done! All blank lines removed.")
