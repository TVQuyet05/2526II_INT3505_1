# Các Mô hình Thiết kế API (API Design Patterns)

Dưới đây là mô tả ngắn gọn về 5 mẫu thiết kế API phổ biến, từ quản lý dữ liệu cơ bản đến kiến trúc tương tác thời gian thực.

## 1. CRUD (Create, Read, Update, Delete)

- **Mô tả:** Mẫu thiết kế nền tảng xoay quanh các thao tác trực tiếp trên một tập dữ liệu hoặc tài nguyên (Resources).
- **Cơ chế:** Ánh xạ trực tiếp 4 thao tác Database cơ bản vào các phương thức HTTP:
  - `POST` để tạo mới (Create).
  - `GET` để truy xuất (Read).
  - `PUT` / `PATCH` để cập nhật (Update).
  - `DELETE` để xóa (Delete).
- **Trường hợp sử dụng:** Thích hợp cho các hệ thống API quản lý dữ liệu đơn giản như CMS, quản lý sản phẩm, tài khoản.

## 2. Query (Truy vấn)

- **Mô tả:** Mở rộng từ `Read` trong CRUD, tối ưu cho việc tìm kiếm, lọc, sắp xếp (sorting) và phân trang (pagination) trên các tập dữ liệu lớn.
- **Cơ chế:** Sử dụng Query Parameters trên URL (VD: `GET /users?age=20&sort=name&limit=10`) hoặc sử dụng chung kiến trúc như GraphQL (chỉ định chính xác các trường cần lấy).
- **Trường hợp sử dụng:** Search engine, bộ lọc sản phẩm trên e-commerce, Dashboard cần tổng hợp nhiều tiêu chí.

## 3. HATEOAS (Hypermedia As The Engine Of Application State)

- **Mô tả:** Một nguyên tắc cấp cao của RESTful API. Thay vì Client phải tự biết quy tắc ghép nối URL, Server trả về dữ liệu kèm theo các "đường link" (như click chuột trên web) chỉ rõ các hành động tiếp theo có thể làm.
- **Cơ chế:** Trong Payload JSON trả về có mảng `links`.
  Vd: Khi xem 1 đơn hàng, trả về kèm link `pay_url` hoặc `cancel_url`.
- **Trường hợp sử dụng:** Các hệ thống có state machine (máy trạng thái) phức tạp (VD: Hủy đơn, thanh toán, duyệt bài), giúp Client dễ dàng tự động hóa mà không cần hard-code (gắn cứng) logic URL.

## 4. Event-Driven (Hướng Sự Kiện)

- **Mô tả:** Kiến trúc mà các thành phần của hệ thống giao tiếp bằng cách phát ra hoặc lắng nghe các "Sự kiện" (Events).
- **Cơ chế:** Hệ thống A tạo ra sự kiện đưa vào hàng đợi/Broker (như Kafka, RabbitMQ). Hệ thống B (và C, D) đang lắng nghe (subscribe) sẽ tự động tiêu thụ sự kiện đó để xử lý một cách độc lập (Asynchronous).
- **Trường hợp sử dụng:** Hệ thống Microservices, ứng dụng thời gian thực, xử lý ảnh/video, IoT băng thông lớn. Đảm bảo tính lỏng lẻo (decoupled) giữa các hệ thống.

## 5. Webhook (Reverse API / HTTP Callback)

- **Mô tả:** Là một dạng biểu hiện mạnh mẽ của Event-Driven nhưng hoạt động trên nền tảng HTTP public (giữa 2 mạng lưới khác nhau).
- **Cơ chế:** Thay vì Client liên tục gọi API để hỏi (Pull), Client đăng ký một URL. Khi có thay đổi, Server sẽ gửi một `POST` request chứa dữ liệu sự kiện thẳng vào URL của Client (Push).
- **Trường hợp sử dụng:** Tích hợp với dịch vụ của bên thứ 3 (Thanh toán Stripe, Tin nhắn Slack, Cảnh báo GitHub / CI-CD), thông báo trạng thái của quy trình chạy ngầm.
