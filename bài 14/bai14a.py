from itertools import product

# Tạo tất cả các trường hợp có thể cho Smoke
possible_values = [True, False]

true_cases = []
false_cases = []

print(" - Sử dụng bảng chân lý: ")

for smoke in possible_values:
    # Kiểm tra giá trị của mệnh đề "Smoke -> Smoke"
    stmt = not smoke or smoke  # ¬ Smoke hoặc Smoke
    
    if stmt:
        true_cases.append(f"+ Smoke = {smoke}: Đúng đắn")
    else:
        false_cases.append(f"+ Smoke= {smoke}: Không đúng")

if false_cases:
    print("Những trường hợp không đúng:")
    for case in false_cases:
        print(case)
else:
    print("Tất cả trường hợp đều đúng => Đúng đắn")

if true_cases:
    print("Những trường hợp đúng:")
    for case in true_cases:
        print(case)
else:
    print("Không có trường hợp đúng => Không thỏa mãn")
