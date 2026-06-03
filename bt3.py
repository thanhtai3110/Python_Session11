# (1) Phân tích và thiết kế giải pháp
# Phân tích Input/Output
# Input: Mã sản phẩm (chuỗi), Tên (chuỗi), Giá (số nguyên), Số lượng (số nguyên), Lựa chọn menu (số).

# Output: Hiển thị danh sách sản phẩm, thông báo trạng thái thao tác, hoặc thoát chương trình.

# Đề xuất giải pháp
# Cấu trúc dữ liệu: Sử dụng list chứa các dictionary (mỗi phần tử là một sản phẩm).

# Chuẩn hóa: Luôn dùng .strip().upper() cho mã sản phẩm để tránh lỗi trùng lặp do khoảng trắng hoặc định dạng hoa/thường.

# Kiểm tra dữ liệu (Validation): Sử dụng khối try-except để bắt lỗi khi người dùng nhập sai kiểu dữ liệu (nhập chữ vào ô số) và kiểm tra if để chặn số âm/bằng 0.

# Tìm kiếm: Sử dụng vòng lặp for để duyệt qua danh sách và so sánh product_id.

# Thiết kế thuật toán (Pseudocode)
# Khởi tạo danh sách product_list.

# Tạo vòng lặp while True để hiển thị menu.

# Lấy lựa chọn từ người dùng:

# Nếu là 1: Duyệt danh sách và in định dạng.

# Nếu là 2: Nhập thông tin, kiểm tra trùng mã, kiểm tra số dương, thêm vào list.

# Nếu là 3: Tìm mã, nếu thấy thì nhập thông tin mới để cập nhật.

# Nếu là 4: Tìm mã, nếu thấy thì xóa phần tử.

# Nếu là 5: Break vòng lặp.

# Khác: Thông báo lỗi.

# (2) Triển khai code

# Danh sách sản phẩm khởi tạo
product_list = [
    {"product_id": "SP001", "product_name": "Áo polo nam", "price": 299000, "quantity": 20},
    {"product_id": "SP002", "product_name": "Quần kaki nam", "price": 399000, "quantity": 15},
    {"product_id": "SP003", "product_name": "Váy công sở nữ", "price": 459000, "quantity": 10}
]

def display_menu():
    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Giá trị phải là số nguyên dương!")
        except ValueError:
            print("Giá/Số lượng không hợp lệ!")

while True:
    display_menu()
    choice = input("Chọn chức năng (1-5): ")

    if choice == '1':
        if not product_list:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("Danh sách sản phẩm hiện tại:")
            for i, p in enumerate(product_list, 1):
                print(f"{i}. Mã SP: {p['product_id']} | Tên: {p['product_name']} | Giá: {p['price']} | Số lượng: {p['quantity']}")

    elif choice == '2':
        p_id = input("Nhập mã sản phẩm: ").strip().upper()
        if any(p['product_id'] == p_id for p in product_list):
            print("Mã sản phẩm bị trùng!")
        else:
            name = input("Nhập tên sản phẩm: ")
            price = get_positive_int("Nhập giá sản phẩm: ")
            qty = get_positive_int("Nhập số lượng sản phẩm: ")
            product_list.append({"product_id": p_id, "product_name": name, "price": price, "quantity": qty})
            print("Thêm sản phẩm thành công")

    elif choice == '3':
        p_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
        found = False
        for p in product_list:
            if p['product_id'] == p_id:
                p['product_name'] = input("Nhập tên mới: ")
                p['price'] = get_positive_int("Nhập giá mới: ")
                p['quantity'] = get_positive_int("Nhập số lượng mới: ")
                found = True
                print("Cập nhật thành công!")
                break
        if not found:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")

    elif choice == '4':
        p_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
        initial_len = len(product_list)
        product_list = [p for p in product_list if p['product_id'] != p_id]
        if len(product_list) < initial_len:
            print("Xóa sản phẩm thành công!")
        else:
            print("Không tìm thấy mã sản phẩm cần xoá!")

    elif choice == '5':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")