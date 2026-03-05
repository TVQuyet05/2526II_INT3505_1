# Nội dung Tuần 2: Kiến trúc REST & HTTP

## 1. Kiến thức cần đạt

### 6 Nguyên tắc của kiến trúc REST
1.  **Client-Server**: Tách biệt giữa client và server.
2.  **Stateless**: Server không lưu trạng thái của client giữa các request.
3.  **Cacheable**: Response có thể được cache để cải thiện hiệu năng.
4.  **Uniform Interface**: Giao diện thống nhất giữa các thành phần.
5.  **Layered System**: Hệ thống phân lớp, client không cần biết server cụ thể nào xử lý.
6.  **Code on Demand**: (Tùy chọn) Server có thể gửi code (vd: JS) để thực thi ở client.

### Giao thức HTTP
*   **HTTP Methods**:
    *   `GET`: Lấy dữ liệu.
    *   `POST`: Tạo mới dữ liệu.
    *   `PUT`: Cập nhật toàn bộ dữ liệu.
    *   `PATCH`: Cập nhật một phần dữ liệu.
    *   `DELETE`: Xóa dữ liệu.
*   **Status Codes**:
    *   2xx: Thành công (200 OK, 201 Created)
    *   3xx: Điều hướng
    *   4xx: Lỗi Client (400 Bad Request, 401 Unauthorized, 404 Not Found)
    *   5xx: Lỗi Server (500 Internal Server Error)
*   **Headers**: Metadata (Content-Type, Authorization, Accept...)
