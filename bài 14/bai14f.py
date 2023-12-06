from itertools import product

# Tạo tất cả các trường hợp có thể cho Smoke, Fire và Heat
possible_values = [True, False]

cases = []
print(" - Sử dụng bảng chân lý: ")

for smoke, fire, heat in product(possible_values, repeat=3):
    # Kiểm tra giá trị của mệnh đề "(Smoke -> Fire) -> ((Smoke ∧ Heat) -> Fire)"
    # stmt = ((not smoke or fire) <= fire) <= ((smoke and heat) <= fire)
    stmt = not(not(not smoke or fire) or fire) or (not(smoke and heat) or fire)
    
    if stmt:
        cases.append(f"+ Smoke={smoke}, Fire={fire}, Heat={heat}: Đúng đắn")
    else:
        cases.append(f"+ Smoke={smoke}, Fire={fire}, Heat={heat}: Không đúng")

print("Kết quả từng trường hợp:")
for case in cases:
    print(case)

if all("Đúng đắn" in case for case in cases):
    print("=> Đúng đắn")
else:
    print("=> Không thỏa mãn")
