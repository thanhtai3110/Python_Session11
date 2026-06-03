# 1. Phân tích lỗi
# Dictionary employee gồm những key nào?
# Gồm: "employee_id", "full_name", "department", và "status".

# Vì sao employee[0] gây lỗi?
# Vì dictionary không phải là kiểu dữ liệu có thứ tự dựa trên index (như list). Bạn không thể dùng số thứ tự để truy cập giá trị.

# Dictionary có truy cập phần tử bằng index giống list không?
# Không. dictionary truy cập dựa trên cặp key: value.

# Muốn lấy mã nhân viên "NV001", cần viết lệnh như thế nào?
# Dùng key: employee["employee_id"].

# Vì sao full_name = employee["name"] gây lỗi?
# Vì key "name" không tồn tại trong dictionary (KeyError).

# Key đúng để lấy họ tên nhân viên là gì?
# Key đúng là "full_name".

# Vì sao employee["employee_status"] = "official" chưa cập nhật đúng?
# Vì bạn đang tạo ra một key mới là "employee_status" thay vì cập nhật giá trị cho key cũ là "status".

# Muốn cập nhật trạng thái nhân viên, cần dùng key nào?
# Dùng key "status".

# Vì sao employee.append(...) gây lỗi?
# Vì dictionary không có phương thức append(). append() là phương thức của list.

# Muốn thêm lương cơ bản, cần viết lệnh thế nào?
# Dùng cú pháp gán trực tiếp: employee["base_salary"] = 15000000.

# Vì sao del employee["team"] gây lỗi?
# Vì key "team" không tồn tại trong dictionary.

# Muốn xóa thông tin phòng ban, cần dùng key nào?
# Dùng key "department".

# 2. Sửa lỗi (Source Code chuẩn hóa)
# Dưới đây là mã nguồn đã được sửa lỗi để đảm bảo hệ thống vận hành đúng theo yêu cầu nghiệp vụ:


# Thông tin nhân viên ban đầu
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

# 1. Lấy mã nhân viên (Truy cập bằng key)
employee_id = employee["employee_id"]

# 2. Lấy họ tên nhân viên (Sử dụng key đúng)
full_name = employee["full_name"]

# 3. Cập nhật trạng thái nhân viên (Gán lại giá trị cho key hiện có)
employee["status"] = "official"

# 4. Thêm lương cơ bản (Gán key mới)
employee["base_salary"] = 15000000

# 5. Xóa thông tin phòng ban (Xóa key hiện có)
del employee["department"]

# Hiển thị kết quả
print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)