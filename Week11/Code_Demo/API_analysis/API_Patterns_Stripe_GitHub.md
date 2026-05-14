# Phân tích API & Webhook Patterns: Stripe & GitHub

Stripe và GitHub sở hữu hai trong số những hệ thống API và Webhook được thiết kế tốt nhất trên thế giới. Dưới đây là các "Design Patterns" (Mẫu thiết kế) nổi bật mà họ áp dụng để đảm bảo hiệu suất, bảo mật và trải nghiệm cho lập trình viên (Developer Experience - DX).

## 1. Stripe API Patterns

Stripe là chuẩn mực "vàng" về thiết kế REST API, đặc biệt cho mảng tài chính.

### A. Idempotency (Tính luỹ đẳng)

- **Vấn đề:** Khi gọi API thanh toán bị rớt mạng, client gọi lại lần nữa có thể dẫn đến việc khách hàng bị trừ tiền 2 lần.
- **Pattern:** Stripe sử dụng Header `Idempotency-Key`. Cùng một key gọi nhiều lần, hệ thống chỉ thực thi giao dịch đúng 1 lần duy nhất, các lần sau sẽ tự động trả về kết quả của lần gọi đầu.

### B. Expandable Objects (Đối tượng mở rộng)

- **Vấn đề:** Tránh bài toán "N+1 query" hoặc "Under-fetching" (lấy thiếu dữ liệu).
- **Pattern:** Theo mặc định, object chỉ chứa ID của object liên quan (VD: `customer: "cus_123"`). Nhưng nếu client truyền param `expand[]=customer`, Stripe sẽ trả về nguyên object Customer chi tiết lồng bên trong.

### C. Webhook Signatures (Chữ ký Webhook)

- **Pattern:** Để đảm bảo Webhook thực sự đến từ Stripe (không phải hacker giả mạo), Stripe gửi kèm Header `Stripe-Signature`.
- **Cơ chế:** Ký Payload bằng HMAC-SHA256 với một "Secret key" mà chỉ bạn và Stripe biết, kèm theo timestamp để chống lại Replay Attacks (kẻ gian lấy payload cũ gửi lại).

### D. Cursor-based Pagination (Phân trang dựa trên con trỏ)

- **Pattern:** Stripe không dùng `page=2&size=10` vì dữ liệu tài chính thay đổi liên tục dẫn đến lệch trang.
- **Cơ chế:** Dùng `starting_after` hoặc `ending_before` kết hợp với ID của phần tử cuối cùng (VD: `?limit=10&starting_after=obj_987`).

---

## 2. GitHub API Patterns

API của GitHub được thiết kế tối ưu cho nền tảng mạng lưới phức tạp của code, user và repository.

### A. Dual Approach (Cung cấp cả REST và GraphQL)

- **Pattern:** GitHub v3 sử dụng REST truyền thống, nhưng với GitHub v4, họ cung cấp **GraphQL**.
- **Ý nghĩa:** GraphQL cho phép client (nhất là mobile app của GitHub) lấy chính xác những trường dữ liệu cần thiết mà không bị rác (Over-fetching), giảm tải băng thông.

### B. HATEOAS (Hypermedia / Links)

- **Pattern:** Trong mọi kết quả trả về, GitHub luôn kèm theo các URL dẫn đến tài nguyên tiếp theo.
- **Ví dụ:** Trả về User nhưng kèm sẵn link `followers_url`, `repos_url`. Điều này giúp client không cần tự ghép nối URL cứng nhắc (hardcode URL).

### C. Rate Limiting Headers minh bạch

- **Pattern:** Mọi Response đều có các Header báo cáo giới hạn rõ ràng:
  - `X-RateLimit-Limit`: Tổng số request cho phép trong 1 giờ (VD: 5000).
  - `X-RateLimit-Remaining`: Số lượng còn lại.
  - `X-RateLimit-Reset`: Timestamp lúc nào bộ đếm quay lại mức tối đa.

### D. Webhook Event Headers

- **Pattern:** Khi bắn Webhook, GitHub dùng Request Header để phân loại ngay từ vòng gửi xe (routing) mà không cần parse Body:
  - `X-GitHub-Event`: Tên sự kiện (VD: `push`, `pull_request`, `issues`).
  - `X-GitHub-Delivery`: ID định danh (UUID) của lần bắn webhook (hữu ích cho truy vết log).
  - `X-Hub-Signature-256`: Bảo mật HMAC-SHA256 tương tự Stripe.

---

## 3. Các Best Practices chung từ cả hai hệ thống

Nếu bạn xây dựng hệ thống API / Webhook, hãy học tập các mẫu thiết kế chung này từ họ:

1. **Versioning rõ ràng:**
   - GitHub dùng Accept header (`Accept: application/vnd.github.v3+json`).
   - Stripe dùng Header (`Stripe-Version: 2023-10-16`) và cho phép cấu hình mặc định version trong Dashboard.
2. **Cơ chế Retry cho Webhook (Delivery Retries):** Nếu server của bạn sập trả về 500, cả Stripe và GitHub sẽ tự động "lùi lại" và gửi lại webhook theo hàm số mũ (Exponential backoff) trong nhiều giờ hoặc vài ngày tới.
3. **Mã lỗi (Error Model) dễ hiểu:** Không chỉ trả http status code (400, 404), trong body luôn có trường `code` (VD: `insufficient_funds`, `missing_field`) và `message` ghi rõ lý do.
4. **Dashboard cho Webhook:** Cung cấp UI cho nhà phát triển xem lại lịch sử các Webhook đã được bắn lúc mấy giờ, payload là gì và server của user phản hồi HTTP status nào (rất tốt để debug).
