# RAML Demo: Server & UI Documentation

Thư mục này trình bày cách sử dụng **RAML 1.0** để thiết kế API, sinh giao diện tài liệu (UI) và chạy server thử nghiệm.

## 📁 Cấu trúc thư mục

- `api.raml`: File thiết kế API theo chuẩn RAML 1.0.
- `server.py`: Server Flask tối giản để phục vụ việc kiểm thử các endpoint.
- `api_docs.html`: Tài liệu API định dạng HTML (được sinh từ RAML).

---

## 🎨 1. Sinh giao diện tài liệu (UI)

Chúng ta sử dụng công cụ `raml2html` để chuyển đổi file RAML sang giao diện web.

### Cài đặt:

```powershell
npm install -g raml2html
```

### Thực hiện sinh UI:

```powershell
raml2html api.raml > api_docs.html
```

_Sau khi chạy, bạn có thể mở file `api_docs.html` bằng trình duyệt để xem tài liệu._

---

## 🚀 2. Chạy Server thử nghiệm

Server được viết bằng Python Flask, tuân thủ đúng cấu trúc dữ liệu mô tả trong RAML.

### Cài đặt thư viện:

```powershell
pip install Flask
```

### Chạy Server:

```powershell
python server.py
```

_Server sẽ lắng nghe tại: `http://localhost:5000`_

---

## 🧪 3. Kiểm tra API

Bạn có thể dùng Postman hoặc `curl` để gọi các endpoint:

- **Lấy danh sách sách**: `GET http://localhost:5000/books`
- **Thêm sách mới**: `POST http://localhost:5000/books` (với body JSON)
- **Cập nhật sách**: `PUT http://localhost:5000/books/1`
- **Xóa sách**: `DELETE http://localhost:5000/books/1`
