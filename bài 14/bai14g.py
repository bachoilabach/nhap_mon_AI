from itertools import product

# Tạo tất cả các trường hợp có thể cho Big và Dumb
possible_values = [True, False]

cases = []
print(" - Sử dụng bảng chân lý: ")

for big, dumb in product(possible_values, repeat=2):
    # Kiểm tra giá trị của mệnh đề "Big ∨ Dumb ∨ (Big -> Dumb)"
    stmt = big or dumb or (not big or dumb)
    
    if stmt:
        cases.append(f"Big={big}, Dumb={dumb}: Đúng đắn")
    else:
        cases.append(f"Big={big}, Dumb={dumb}: Không đúng")

print("Kết quả từng trường hợp:")
for case in cases:
    print(case)

if all("Đúng đắn" in case for case in cases):
    print("=> Đúng đắn")
else:
    print("=> Không thỏa mãn")
