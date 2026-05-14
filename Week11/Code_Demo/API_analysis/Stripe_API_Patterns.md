# Phân tích API & Webhook Patterns: Stripe

## 1. Idempotency (Tính luỹ đẳng)

**API Tương ứng chi tiết:**

```http
POST /v1/charges
Host: api.stripe.com
Authorization: Bearer sk_test_123
Idempotency-Key: req_abc123
Content-Type: application/x-www-form-urlencoded

amount=2000&currency=usd&source=tok_visa
```

**Phân tích:**
Stripe cung cấp cơ chế chống lỗi mạng tuyệt vời. Khi truyền một chuỗi định danh duy nhất vào Header `Idempotency-Key`, nếu request thành công nhưng mạng bị đứt, client gọi lại chính request trên với cùng một key đó, Stripe sẽ không thực thi việc trừ tiền lần 2 mà chỉ trả lại đúng kết quả JSON của lần đầu tiên.

---

## 2. Expandable Objects (Đối tượng mở rộng)

**API Tương ứng chi tiết:**

```http
GET /v1/payment_intents/pi_123?expand[]=customer
Host: api.stripe.com
Authorization: Bearer sk_test_123
```

**Phân tích:**
Thay vì trả về `customer: "cus_abc"` bắt client phải gọi thêm 1 API nữa để lấy thông tin user (tình trạng N+1 Query), Stripe cho phép client chỉ định trực tiếp các field muốn lấy chi tiết để nhúng toàn bộ thông tin nguyên một Object Customer vào bên trong kết quả trả về của Payment Intent ngay từ đầu.

---

## 3. Cursor-based Pagination (Phân trang bằng con trỏ)

**API Tương ứng chi tiết:**

```http
GET /v1/customers?limit=3&starting_after=cus_abc
Host: api.stripe.com
Authorization: Bearer sk_test_123
```

**Phân tích:**
Sử dụng ID của phần tử cuối cùng hiện tại (`cus_abc`) làm mốc để lấy danh sách tiếp theo thay vì dùng số trang (`page=2`). Đối với data thay đổi và chèn vào liên tục (thanh toán realtime), dùng số trang truyền thống sẽ bị sai lệch mốc dẫn đến sót hoặc trùng lặp dữ liệu. Cursor giúp việc cuộn danh sách chính xác tuyệt đối.

---

## 4. Webhook Security (Chữ ký điện tử)

**API Tương ứng chi tiết:**

```http
POST <Your_Webhook_URL>
Host: your-server.com
Stripe-Signature: t=1614838612,v1=a3b2c...
Content-Type: application/json

{
  "type": "payment_intent.succeeded",
  "data": { ... }
}
```

**Phân tích:**
Dựa vào Request Header `Stripe-Signature`, ứng dụng của bạn sẽ trích xuất ra phần Timestamp (`t=...`) và phần băm HMAC (`v1=...`). Máy chủ tự tạo lại đoạn mã băm bằng Secret Key cấu hình riêng và so sánh. Việc này đảm bảo body JSON không bị sửa đổi trên đường truyền và webhook này thực sự được Stripe bắn ra chứ không phải hacker gọi giả mạo.

---

## 5. Metadata và Error Handling (Quản trị Lỗi & Dữ liệu chìm)

**API Tương ứng chi tiết:**

```json
{
  "error": {
    "code": "insufficient_funds",
    "message": "Your card has insufficient funds.",
    "type": "card_error"
  }
}
```

**Phân tích:**
Mã lỗi (Error Model) của Stripe không chỉ nằm ở HTTP Status (như 402 Payment Required). Body json luôn trả ra thuộc tính `code` có thể lập trình xử lý tự động (machine-readable) được chuẩn hóa và `message` rõ ràng cho con người (human-readable). Họ cũng cho phép đính kèm object tự do `metadata` đi dọc cùng tài nguyên hỗ trợ đối soát log cho developer sau này.
