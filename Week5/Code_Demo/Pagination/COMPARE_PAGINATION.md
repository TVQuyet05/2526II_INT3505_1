# API Pagination Demo

Dự án này minh họa 3 kỹ thuật phân trang (Pagination) phổ biến nhất trong thiết kế RESTful API.

## So sánh chi tiết các kỹ thuật Pagination

Dưới đây là bảng so sánh sâu hơn về 3 phương pháp phân trang phổ biến:

### 1. Offset/Limit Pagination

Đây là phương pháp cơ bản nhất, sử dụng hai tham số là vị trí bắt đầu (`offset`) và số lượng cần lấy (`limit`).

- **Cơ chế:** Dựa trên tập kết quả được đánh chỉ số (index-based).
- **Ưu điểm:**
  - Cực kỳ dễ cài đặt phía Backend (tương ứng trực tiếp với `LIMIT offset, limit` trong SQL).
  - Client có thể nhảy đến bất kỳ vị trí dữ liệu nào.
- **Nhược điểm:**
  - **Hiệu năng kém:** Khi `offset` quá lớn (ví dụ trang thứ 10,000), cơ sở dữ liệu vẫn phải quét qua tất cả các bản ghi trước đó rồi mới lấy dữ liệu.
  - **Dữ liệu không nhất quán:** Nếu có một bản ghi mới được chèn vào trang 1 trong khi người dùng đang ở trang 2, họ sẽ thấy một bản ghi bị lặp lại ở đầu trang 2.

### 2. Page-based Pagination

Là một biến thể của Offset/Limit nhưng được thiết kế thân thiện hơn với giao diện người dùng (UI).

- **Cơ chế:** Chuyển đổi công thức `offset = (page - 1) * per_page`.
- **Ưu điểm:**
  - Phù hợp nhất cho các trang web có tính năng **Pagination Bar** (hiển thị danh sách số trang 1, 2, 3... để người dùng click).
  - Người dùng biết được tổng số trang và vị trí hiện tại của mình.
- **Nhược điểm:**
  - Gặp tất cả các vấn đề về hiệu năng và trùng lặp dữ liệu giống như Offset/Limit.

### 3. Cursor-based Pagination (Seek Method)

Phương pháp hiện đại nhất, sử dụng một "con trỏ" đại diện cho bản ghi cuối cùng của trang trước đó.

- **Cơ chế:** Thay vì đếm vị trí, nó sử dụng mệnh đề `WHERE id > last_seen_id ORDER BY id LIMIT n`.
- **Ưu điểm:**
  - **Hiệu năng cực cao:** Luôn là O(1) hoặc dựa trên Index, không phụ thuộc vào độ sâu của trang.
  - **Nhất quán 100%:** Ngay cả khi dữ liệu mới được chèn vào, các trang tiếp theo dựa trên cursor vẫn trả về đúng các bản ghi cũ mà không bị lặp lại.
  - **Lý tưởng cho Infinite Scroll:** Được các nền tảng như Facebook, Instagram, Twitter sử dụng cho dòng thời gian.
- **Nhược điểm:**
  - **Không thể nhảy trang:** Bạn không thể từ trang 1 nhảy ngay sang trang 50 vì bạn cần cursor của trang 49.
  - **Cài đặt phức tạp:** Cần xử lý mã hóa/giải mã cursor (thường dùng Base64) để ẩn giấu logic nội bộ phía server.


