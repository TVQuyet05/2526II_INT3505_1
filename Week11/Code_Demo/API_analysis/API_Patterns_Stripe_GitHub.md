# Phân tích API & Webhook Patterns: Stripe & GitHub

Tóm tắt các mẫu thiết kế (Design Patterns) nổi bật của Stripe và GitHub.

## 1. Stripe API Patterns

- **(VD: `POST /v1/charges`) Idempotency (Tính luỹ đẳng):** Dùng header `Idempotency-Key` để không bị trừ tiền 2 lần nếu gọi lại request do rớt mạng.
- **(VD: `GET /v1/payment_intents/pi_123?expand[]=customer`) Expandable Objects:** Tránh "N+1 query" bằng cách trả về ID, nhưng cho phép client mở rộng chi tiết data (VD: `expand[]=customer`).
- **(VD: `GET /v1/customers?limit=3&starting_after=cus_abc`) Cursor-based Pagination:** Dùng con trỏ `starting_after=[id]` thay vì `page=2` để phân trang không bị lệch khi dữ liệu thay đổi liên tục.
- **(VD: `POST <Your_Webhook_URL>`) Webhook Security:** Ký HMAC-SHA256 payload qua header `Stripe-Signature` kèm timestamp để chống giả mạo và Replay Attacks.

## 2. GitHub API Patterns

- **(VD: `POST /graphql` vs `GET /users/:username`) Dual Approach (REST + GraphQL):** Cung cấp GraphQL (v4) để client lấy đúng dữ liệu cần thiết, chống rác data (Over-fetching).
- **(VD: `GET /users/octocat`) HATEOAS (Hypermedia):** Trả về kèm các link điều hướng (VD: `"followers_url": "https://api.github.com/users/octocat/followers"`), giúp client không cần hard-code URL.
- **(VD: `GET /rate_limit`) Rate Limit Headers:** Trả về các Header minh bạch báo cáo dung lượng API còn lại (`X-RateLimit-Limit`, `Remaining`, `Reset`).
- **(VD: `POST <Your_Webhook_URL>`) Webhook Event Headers:** Phân loại sự kiện ngay ở Header (`X-GitHub-Event: pull_request`) để server định tuyến nhanh mà không cần đọc hết Body.

## 3. Best Practices Chung

1. **Versioning rõ ràng:** Quản lý phiên bản API qua Header (VD: `Accept: application/vnd.github.v3+json`).
2. **Delivery Retries:** Tự động gửi lại Webhook (Exponential backoff) nếu server client bị lỗi (HTTP 5xx).
3. **Mã lỗi (Error Model):** Trả về HTTP status đúng chuẩn kèm mã lỗi `code` và `message` rõ ràng.
4. **Webhook Dashboard:** Cung cấp UI để Developer dễ dàng kiểm tra lịch sử và log gửi/nhận webhook.
