# PhishingDetect

## Giới thiệu

**PhishingDetect** là một ứng dụng web giúp phát hiện và ngăn chặn các cuộc tấn công email lừa đảo (phishing). Dự án sử dụng các mô hình học máy tiên tiến và kỹ thuật phân tích hiện đại để tự động quét, đánh giá mức độ rủi ro của email, bảo vệ người dùng khỏi các mối đe dọa trực tuyến.

---

## Tính Năng Nổi Bật

- **Phân tích URL Phishing**  
  So sánh các URL trong email với cơ sở dữ liệu lừa đảo đã biết. Nhận diện URL đáng ngờ dựa trên cấu trúc, lỗi chính tả, và tên miền giả mạo.

- **Phát hiện URL Malware**  
  Kiểm tra các liên kết có khả năng dẫn đến việc tải xuống phần mềm độc hại.

- **Phân tích Kỹ thuật Xã hội (Social Engineering)**  
  Ứng dụng NLP để nhận diện dấu hiệu lừa đảo trong nội dung email như:  
  - Yêu cầu khẩn cấp  
  - Mạo danh tổ chức  
  - Hứa hẹn hấp dẫn

- **Quét Tệp Đính Kèm**  
  Tự động quét các tệp đính kèm bằng công cụ diệt virus, phát hiện và cảnh báo về các tệp chứa mã độc trước khi người dùng mở.

- **Phân tích trong Sandbox**  
  Các tệp đính kèm và liên kết đáng ngờ sẽ được thực thi trong môi trường sandbox an toàn để quan sát hành vi, phát hiện các mối nguy hiểm tiềm ẩn mà không gây ảnh hưởng đến hệ thống thật.

---
## Chạy ứng dụng (Django)

Để chạy các lệnh `manage.py` (ví dụ `runserver`, `migrate`, `createsuperuser`), bạn cần di chuyển vào thư mục chứa file `manage.py`. Trong dự án này file `manage.py` nằm trong:

`src/Web_Python_AI_NCKH`

Hướng dẫn nhanh (PowerShell trên Windows) — chạy từ thư mục gốc của repository:

```powershell
# 1) Chuyển vào thư mục chứa manage.py
Set-Location -Path .\src\Web_Python_AI_NCKH
# hoặc: cd .\src\Web_Python_AI_NCKH

# 2) Tạo và kích hoạt virtual environment (khuyến nghị)
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1

# Nếu PowerShell chặn chạy script do ExecutionPolicy, dùng tạm:
# powershell -ExecutionPolicy Bypass -Command ".\.venv\Scripts\Activate.ps1"

# 3) Cài dependencies (nếu có file requirements.txt trong cùng thư mục)
pip install -r requirements.txt

# 4) Chạy migrate và (tuỳ chọn) tạo superuser
python manage.py migrate
python manage.py createsuperuser

# 5) Chạy development server
python manage.py runserver 
``` 

Ghi chú:
- Nếu bạn dùng `python` thay vì `py`, thay `py -3` bằng `python` theo môi trường của bạn.
- Nếu dự án có hướng dẫn riêng (Docker, compose, hoặc README bên trong `src/Web_Python_AI_NCKH`), kiểm tra các hướng dẫn đó trước khi chạy.
- Nếu gặp lỗi liên quan tới biến môi trường (ví dụ `DJANGO_SETTINGS_MODULE` hoặc file `.env`), kiểm tra `src/Web_Python_AI_NCKH/config/settings.py` hoặc các file cấu hình trong thư mục đó.