# (1) Phân tích và thiết kế giải pháp
# Phân tích Input/Output
# Input: Mã sản phẩm (string), Số lượng (int), Phần trăm giảm giá (int), Lựa chọn menu (string/int).

# Output: Hiển thị danh sách, thông báo lỗi (nếu có), tính toán số tiền thanh toán/hoàn lại.

# Đề xuất giải pháp
# Xử lý Logic: Tạo các hàm riêng biệt cho việc kiểm tra đầu vào (như get_positive_int) để tránh lặp code.

# Tính toán: Sử dụng công thức: giá_sau_giảm = giá * (100 - discount) / 100.

# Chuẩn hóa: Sử dụng .strip().upper() cho mọi thao tác liên quan đến product_id.

# Cấu trúc dữ liệu: Duy trì danh sách list các dict để dễ dàng truy xuất và cập nhật thuộc tính.

# Thiết kế thuật toán (Pseudocode)
# Vòng lặp chính: Hiển thị menu và nhận lựa chọn.

# Bán hàng: Kiểm tra tồn kho qty <= p['quantity'] -> Trừ tồn kho, cộng sold, tính price * (1 - discount/100).

# Đổi trả: Kiểm tra qty <= p['sold'] -> Cộng tồn kho, trừ sold, cộng returned, tính tiền hoàn lại.

# Giảm giá: Kiểm tra 0 <= discount <= 70 -> Gán vào p['discount'].

# (2) Triển khai code

# Danh sách sản phẩm khởi tạo
product_list = [
    {"product_id": "SP001", "product_name": "Áo polo nam", "price": 299000, "quantity": 20, "sold": 5, "returned": 1, "discount": 0},
    {"product_id": "SP002", "product_name": "Quần kaki nam", "price": 399000, "quantity": 8, "sold": 3, "returned": 0, "discount": 10},
    {"product_id": "SP003", "product_name": "Váy công sở nữ", "price": 459000, "quantity": 3, "sold": 7, "returned": 1, "discount": 15}
]

def get_status(qty):
    if qty == 0: return "Hết hàng"
    if qty <= 5: return "Sắp hết hàng"
    return "Còn hàng"

def get_valid_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val > 0: return val
            print("Số lượng phải là số nguyên dương!")
        except ValueError:
            print("Dữ liệu không hợp lệ!")

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách | 2. Bán hàng | 3. Đổi trả | 4. Giảm giá | 5. Nhập kho | 6. Thoát")
    choice = input("Lựa chọn: ")

    if choice == '1':
        for p in product_list:
            print(f"Mã: {p['product_id']} | Tên: {p['product_name']} | Giá: {p['price']} | Tồn: {p['quantity']} | Bán: {p['sold']} | Đổi trả: {p['returned']} | Giảm giá: {p['discount']}% | Trạng thái: {get_status(p['quantity'])}")

    elif choice == '2': # Bán hàng
        pid = input("Nhập mã SP: ").strip().upper()
        p = next((x for x in product_list if x['product_id'] == pid), None)
        if not p: print("Không tìm thấy sản phẩm cần bán!")
        else:
            qty = get_valid_positive_int("Số lượng mua: ")
            if qty > p['quantity']: print("Số lượng trong kho không đủ để bán!")
            else:
                price_after = p['price'] * (100 - p['discount']) / 100
                p['quantity'] -= qty
                p['sold'] += qty
                print(f"Thanh toán: {int(price_after * qty)}")

    elif choice == '3': # Đổi trả
        pid = input("Nhập mã SP: ").strip().upper()
        p = next((x for x in product_list if x['product_id'] == pid), None)
        if not p: print("Không tìm thấy sản phẩm cần đổi trả!")
        else:
            qty = get_valid_positive_int("Số lượng đổi/trả: ")
            if qty > p['sold']: print("Số lượng đổi/trả không được vượt quá số lượng đã bán!")
            else:
                p['quantity'] += qty
                p['sold'] -= qty
                p['returned'] += qty
                print(f"Số tiền hoàn lại: {int((p['price'] * (100 - p['discount']) / 100) * qty)}")

    elif choice == '4': # Giảm giá
        pid = input("Nhập mã SP: ").strip().upper()
        p = next((x for x in product_list if x['product_id'] == pid), None)
        if not p: print("Không tìm thấy sản phẩm!")
        else:
            try:
                d = int(input("Nhập % giảm giá (0-70): "))
                if 0 <= d <= 70: p['discount'] = d
                else: print("Phần trăm giảm giá không hợp lệ!")
            except: print("Phần trăm giảm giá không hợp lệ!")

    elif choice == '5': # Nhập hàng
        pid = input("Nhập mã SP: ").strip().upper()
        p = next((x for x in product_list if x['product_id'] == pid), None)
        if not p: print("Không tìm thấy sản phẩm!")
        else:
            p['quantity'] += get_valid_positive_int("Số lượng nhập: ")

    elif choice == '6':
        print("Thoát chương trình."); break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")