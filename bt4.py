# (1) Phân tích và thiết kế giải pháp
# Phân tích Input/Output
# Input: Mã sản phẩm, số lượng (mua/nhập), lựa chọn menu (số nguyên).

# Output: Thông tin sản phẩm chi tiết, cảnh báo tồn kho, báo cáo doanh thu tổng và chi tiết.

# Đề xuất giải pháp
# Cấu trúc dữ liệu: Duy trì danh sách product_list gồm các từ điển (dict).

# Logic tồn kho: Sử dụng hàm get_status(quantity) để trả về nhãn trạng thái dựa trên các ngưỡng 0 và 5.

# Xử lý doanh thu: Duyệt qua danh sách, tính toán tích số price * sold, cộng dồn vào biến total_revenue, đồng thời theo dõi max_sold để xác định sản phẩm bán chạy.

# Đảm bảo tính nhất quán: Luôn sử dụng .strip().upper() để xử lý mã sản phẩm. Sử dụng try-except để kiểm tra kiểu dữ liệu số.

# Thiết kế thuật toán (Pseudocode)
# Khởi tạo danh sách product_list.

# Tạo vòng lặp vô hạn while True để hiển thị menu.

# Chức năng 1: Duyệt danh sách, áp dụng quy tắc trạng thái (nếu qty == 0 -> "Hết hàng", qty <= 5 -> "Sắp hết hàng", ngược lại -> "Còn hàng").

# Chức năng 2 (Bán): Tìm sản phẩm theo mã, kiểm tra điều kiện tồn kho, trừ quantity, cộng sold, hiển thị tổng thanh toán.

# Chức năng 3 (Nhập): Tìm sản phẩm theo mã, cộng thêm vào quantity.

# Chức năng 4 (Báo cáo): Duyệt danh sách, nếu sold > 0 thì tính doanh thu. Tìm max dựa trên giá trị sold.

# Chức năng 5: break vòng lặp.

# (2) Triển khai code

# Danh sách sản phẩm ban đầu
product_list = [
    {"product_id": "SP001", "product_name": "Áo polo nam", "price": 299000, "quantity": 20, "sold": 5},
    {"product_id": "SP002", "product_name": "Quần kaki nam", "price": 399000, "quantity": 8, "sold": 3},
    {"product_id": "SP003", "product_name": "Váy công sở nữ", "price": 459000, "quantity": 3, "sold": 7}
]

def get_status(quantity):
    if quantity == 0: return "Hết hàng"
    if quantity <= 5: return "Sắp hết hàng"
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
    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách và cảnh báo tồn kho\n2. Bán sản phẩm\n3. Nhập thêm hàng\n4. Xem báo cáo doanh thu\n5. Thoát")
    choice = input("Lựa chọn: ")

    if choice == '1':
        if not product_list: print("Danh sách hiện đang trống.")
        else:
            for i, p in enumerate(product_list, 1):
                status = get_status(p['quantity'])
                print(f"{i}. Mã SP: {p['product_id']} | Tên: {p['product_name']} | Giá: {p['price']} | Tồn kho: {p['quantity']} | Đã bán: {p['sold']} | Trạng thái: {status}")

    elif choice == '2':
        pid = input("Nhập mã sản phẩm: ").strip().upper()
        p = next((item for item in product_list if item['product_id'] == pid), None)
        if not p: print("Không tìm thấy sản phẩm cần bán!")
        else:
            qty = get_valid_positive_int("Số lượng khách mua: ")
            if qty > p['quantity']: print("Số lượng trong kho không đủ để bán!")
            else:
                p['quantity'] -= qty
                p['sold'] += qty
                print(f"Thành công! Tổng tiền: {qty * p['price']}")

    elif choice == '3':
        pid = input("Nhập mã sản phẩm: ").strip().upper()
        p = next((item for item in product_list if item['product_id'] == pid), None)
        if not p: print("Không tìm thấy sản phẩm cần nhập kho!")
        else:
            qty = get_valid_positive_int("Số lượng nhập thêm: ")
            p['quantity'] += qty
            print("Nhập hàng thành công!")

    elif choice == '4':
        total_revenue = 0
        best_seller = None
        print("\n===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")
        for i, p in enumerate(product_list, 1):
            if p['sold'] > 0:
                rev = p['price'] * p['sold']
                total_revenue += rev
                print(f"{i}. {p['product_name']} | Đã bán: {p['sold']} | Doanh thu: {rev}")
                if best_seller is None or p['sold'] > best_seller['sold']: best_seller = p
        
        if total_revenue == 0: print("Chưa có doanh thu phát sinh.")
        else:
            print(f"\nTổng doanh thu: {total_revenue}")
            print(f"Sản phẩm bán chạy nhất: {best_seller['product_name']}")

    elif choice == '5':
        print("Thoát chương trình."); break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")