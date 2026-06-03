# 1. Phân tích lỗi
# Tuple product_info ban đầu có bao nhiêu phần tử?
# Có 4 phần tử: "SP001", "Áo polo nam", "Size L", 299000.

# Phần tử "SP001" đang nằm ở index nào?
# Ở index 0 (Trong Python, index bắt đầu từ 0).

# Vì sao dòng product_code = product_info[1] lấy sai mã sản phẩm?
# Vì index 1 trỏ đến phần tử thứ hai là "Áo polo nam". Để lấy mã sản phẩm ("SP001"), bạn phải dùng index 0.

# Phần tử "Áo polo nam" đang nằm ở index nào?
# Ở index 1.

# Vì sao dòng product_name = product_info[2] lấy sai tên sản phẩm?
# Vì index 2 trỏ đến phần tử thứ ba là "Size L". Để lấy tên sản phẩm, bạn phải dùng index 1.

# Vì sao dòng product_length = product_info.length() gây lỗi?
# Vì tuple không có phương thức length(). Python sử dụng hàm có sẵn (built-in function) để thực hiện việc này.

# Muốn đếm số phần tử trong tuple, cần dùng hàm nào?
# Cần dùng hàm len(product_info).

# Vì sao dòng product_info[3] = 279000 không hợp lệ?
# Vì tuple là kiểu dữ liệu bất biến (immutable). Bạn không thể thay đổi, thêm hoặc xóa bất kỳ phần tử nào sau khi đã khởi tạo.

# Tuple có cho phép sửa trực tiếp không?
# Không.

# Muốn cập nhật giá bán, cần xử lý như thế nào?
# Bạn cần tạo ra một tuple mới bằng cách kết hợp các phần tử cũ (cắt lát - slicing) với giá trị mới.

# 2. Sửa lỗi (Source Code hoàn chỉnh)
# Dưới đây là mã nguồn đã được tối ưu và sửa lỗi để hệ thống vận hành đúng yêu cầu:


# Thông tin sản phẩm ban đầu
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

# 1. Lấy mã sản phẩm (Index 0)
product_code = product_info[0]

# 2. Lấy tên sản phẩm (Index 1)
product_name = product_info[1]

# 3. Đếm số lượng thông tin sản phẩm (Dùng len())
product_length = len(product_info)

# 4. Cập nhật giá bán: Vì tuple không thể sửa trực tiếp, 
# ta tạo tuple mới bằng cách lấy từ đầu đến phần tử trước giá (index 0, 1, 2) 
# và nối thêm giá trị mới
product_info_updated = product_info[:3] + (279000,)

# Hiển thị kết quả
print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info_updated)