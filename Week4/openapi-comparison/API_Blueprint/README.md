# API Blueprint Demo: Server & Testing with Dredd

Thư mục này demo cách sử dụng **API Blueprint** để thiết kế API, viết mã nguồn server Flask tương ứng và thực hiện kiểm thử tự động (Contract Testing) bằng **Dredd**.

## 🚀 1. Khởi chạy Server

Server được viết bằng Flask, cung cấp 5 endpoints CRUD quản lý sách khớp hoàn toàn với thiết kế trong `api_blueprint.apib`.

### Cài đặt thư viện:

```powershell
pip install Flask
```

### Chạy Server:

```powershell
python server.py
```

_Server sẽ chạy tại: `http://localhost:5000`_

---

## 🧪 2. Kiểm thử với Dredd

**Dredd** là công cụ HTTP API Testing dùng để kiểm tra xem server thực tế có chạy đúng như những gì đã mô tả trong file thiết kế hay không.

### Cài đặt Dredd:

```powershell
npm install -g dredd
```

### Thực hiện Test:

Đảm bảo server Flask đang chạy, sau đó mở một terminal mới và chạy lệnh:

```powershell
dredd api_blueprint.apib http://localhost:5000
```

### Kết quả mong đợi:

Dredd sẽ tự động gửi các request (GET, POST, PUT, DELETE) lên server và so sánh:

- **Status Code**: Phải khớp (ví dụ: 200, 201, 204, 404).
- **Body Content-Type**: Phải là `application/json`.
- **JSON Structure**: Dữ liệu trả về phải có đầy đủ các trường (id, title, author...) như đã định nghĩa trong phần `Data Structures`.

### Kết quả thực tế (Dredd Output):

Khi chạy thành công, Dredd sẽ báo cáo các lượt pass qua từng endpoint:

```text
pass: GET (200) /books duration: 68s
pass: POST (201) /books duration: 17ms
pass: GET (200) /books/1 duration: 10ms
pass: PUT (200) /books/1 duration: 8ms
pass: DELETE (204) /books/1 duration: 7ms

complete: 5 passing, 0 failing, 0 errors, 0 skipped, 5 total
complete: Tests took 113ms
```

---

## 🎨 3. Sinh giao diện tài liệu (UI)

Bạn có thể dùng **Aglio** để biến file Blueprint thành trang HTML đẹp mắt:

```powershell
npm install -g aglio
aglio -i api_blueprint.apib -o docs.html
```

Sau đó mở file `docs.html` bằng trình duyệt để xem tài liệu.
