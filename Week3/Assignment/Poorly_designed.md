# Case Study: Phân tích lỗi thiết kế API (Legacy Bookstore System)

Tài liệu này phân tích các lỗi thiết kế phổ biến (**Anti-patterns**) trong một hệ thống API giả định và đưa ra giải pháp khắc phục theo tiêu chuẩn **RESTful** hiện đại.

---

## 1. Hiện trạng hệ thống (Poorly Designed API)

Dưới đây là danh sách các Endpoint hiện tại của hệ thống được đánh giá là thiết kế kém:

| Endpoint | Method | Chức năng | Vấn đề chính |
| :--- | :--- | :--- | :--- |
| `/get-all-books` | `GET` | Lấy danh sách sách | Vi phạm Resource-based, thiếu phân trang. |
| `/addBook` | `POST` | Thêm sách mới | Đặt tên theo động từ, không nhất quán. |
| `/update-book?id=123` | `POST` | Cập nhật thông tin | Sai Method (`POST` thay vì `PUT/PATCH`). |
| `/delete_book_final` | `GET` | Xóa sách | **Nghiêm trọng:** Dùng `GET` để thay đổi dữ liệu. |

---

## 2. Chi tiết các lỗi thiết kế & Giải pháp

### 2.1. Vi phạm nguyên tắc Resource-based (Danh từ vs Động từ)
* **Mô tả:** API sử dụng các động từ như `get`, `add`, `update` trực tiếp trên URL.
* **Hệ quả:** Gây khó khăn cho việc mở rộng. URL trở nên hỗn loạn khi hệ thống lớn dần (ví dụ: `/fetch-book-v2`, `/remove-book-now`).
* **Giải pháp:** Sử dụng **Danh từ** cho tài nguyên và tận dụng **HTTP Methods** để chỉ hành động.
    * `GET /books` (Lấy danh sách)
    * `POST /books` (Tạo mới)

### 2.2. Sử dụng sai HTTP Methods
* **Mô tả:** Sử dụng `GET` cho hành động xóa dữ liệu hoặc dùng `POST` cho mọi thao tác.
* **Hệ quả:** * **Bảo mật:** Trình duyệt hoặc Bot tìm kiếm có thể tự động truy cập link `GET`, vô tình thực thi lệnh xóa.
    * **Caching:** Không tận dụng được cơ chế lưu đệm của hạ tầng mạng.
* **Giải pháp:** * Dùng `DELETE` để xóa tài nguyên.
    * Dùng `PUT` (thay thế) hoặc `PATCH` (cập nhật một phần).

### 2.3. Thiếu cơ chế phân trang (Pagination)
* **Mô tả:** Endpoint `/get-all-books` trả về toàn bộ bản ghi trong một lần gọi.
* **Hệ quả:** * **Hiệu suất:** Phản hồi cực chậm khi dữ liệu lên đến hàng nghìn bản ghi.
    * **Độ tin cậy:** Dễ gây lỗi tràn bộ nhớ (Out of Memory) cho Server hoặc treo trình duyệt Client.
* **Giải pháp:** Sử dụng Query Parameters:
    * `GET /books?page=1&limit=20`


---

## 3. Thiết kế lại (Redesign) theo chuẩn RESTful

Bảng dưới đây là cấu trúc API sau khi đã được chuẩn hóa:

| Hành động | Method | Endpoint (Clean) | HTTP Status |
| :--- | :--- | :--- | :--- |
| **Lấy danh sách** | `GET` | `/books?page=1&limit=10` | `200 OK` |
| **Lấy chi tiết** | `GET` | `/books/{id}` | `200 OK` / `404` |
| **Thêm mới** | `POST` | `/books` | `201 Created` |
| **Cập nhật** | `PATCH` | `/books/{id}` | `200 OK` |
| **Xóa** | `DELETE` | `/books/{id}` | `204 No Content` |

---