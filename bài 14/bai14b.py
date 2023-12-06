from itertools import product

# Tạo tất cả các trường hợp có thể cho Smoke và Fire
possible_values = [True, False]

cases = []

print(" - Sử dụng bảng chân lý: ")

for smoke, fire in product(possible_values, repeat=2):
    # Kiểm tra giá trị của mệnh đề "Smoke -> Fire"
    stmt = not smoke or fire  # ¬ Smoke hoặc Fire
    
    if stmt:
        cases.append(f"+ Smoke={smoke}, Fire={fire}: Đúng đắn")
    else:
        cases.append(f"+ Smoke={smoke}, Fire={fire}: Không đúng")

print("Kết quả từng trường hợp:")
for case in cases:
    print(case)

if all("Đúng đắn" in case for case in cases):
    print("=> Đúng đắn")
else:
    print("=> Không thỏa mãn")
